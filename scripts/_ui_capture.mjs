// scripts/_ui_capture.mjs — 开发期 CDP 截图/诊断驱动（不入站点加载链，UI/UX 重构回归用）
// 用法：node scripts/_ui_capture.mjs [输出目录]  （默认 docs/_ui-baseline）
// 依赖：本机 Edge（headless=new + 远程调试端口）+ Node ≥22（原生 WebSocket）
// 产出：<out>/baseline-report.json + 各截图。滚动等待真实完成，规避 headless 截图不等待平滑滚动的问题。
import { spawn } from "node:child_process";
import { existsSync, mkdirSync, writeFileSync, readdirSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

const PORT = 9300 + Math.floor(Math.random() * 200);
const OUT = process.argv[2] || "docs/_ui-baseline";
const BASE = "http://127.0.0.1:8766";
const SHOTS = [
  { file: "01-director-1440x2000.png", url: `${BASE}/#directorRoot`, w: 1440, h: 2000 },
  { file: "02-figure-1440x1400.png", url: `${BASE}/#skill-figure?tab=figure`, w: 1440, h: 1400 },
  { file: "03-youth-1440x1400.png", url: `${BASE}/#skill-youth?tab=youth`, w: 1440, h: 1400 },
  { file: "04-erotic-1440x1400.png", url: `${BASE}/#skill-erotic?tab=erotic`, w: 1440, h: 1400 },
  { file: "05-figure-menu-1440x1600.png", url: `${BASE}/#skill-figure?tab=figure-menu`, w: 1440, h: 1600 },
  { file: "06-combo-gallery-1440x1600.png", url: `${BASE}/#combo-gallery`, w: 1440, h: 1600 },
  { file: "07-intro-640x1600.png", url: `${BASE}/#intro`, w: 640, h: 1600 },
  { file: "08-erotic-400x1600.png", url: `${BASE}/#skill-erotic?tab=erotic`, w: 400, h: 1600 },
  { file: "09-figure-1100x1200.png", url: `${BASE}/#skill-figure?tab=figure`, w: 1100, h: 1200 },
  {
    file: "10-gallery-lightbox-1440x1200.png", url: `${BASE}/#combo-gallery`, w: 1440, h: 1200,
    pre: `(() => { const card = document.querySelector('#combo-gallery .cg-card'); if (!card) return false; card.click(); return true; })()`,
  },
  {
    file: "11-director-lightbox-1440x1200.png", url: `${BASE}/#directorRoot`, w: 1440, h: 1200,
    pre: `(() => { const b = document.querySelector('#comboGrid .combo-thumb-btn'); if (!b) return false; b.click(); return true; })()`,
  },
  {
    file: "12-director-combo-link-1440x1200.png", url: `${BASE}/#directorRoot`, w: 1440, h: 1200,
    pre: `(async () => {
      const modeBtn = document.querySelector('[data-mode="erotic"]');
      if (modeBtn) modeBtn.click();
      await new Promise(r => setTimeout(r, 350));
      const search = document.querySelector('#comboPicker input[type="search"]');
      if (search) {
        const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(search, '雪女');
        search.dispatchEvent(new Event('input', { bubbles: true }));
        await new Promise(r => setTimeout(r, 350));
      }
      const pick = [...document.querySelectorAll('.combo-select-btn')].find(b => (b.dataset.combo || '').includes('yuki-onsen'));
      if (!pick) return false;
      pick.click();
      await new Promise(r => setTimeout(r, 350));
      return true;
    })()`,
  },
];
const EDGE_CANDIDATES = [
  "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
  "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
];
const EDGE = EDGE_CANDIDATES.find(existsSync);
if (!EDGE) { console.error("Edge not found"); process.exit(1); }
mkdirSync(OUT, { recursive: true });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
async function fetchJson(url, init) {
  const res = await fetch(url, init);
  if (!res.ok) throw new Error(`${res.status} ${url}`);
  return res.json();
}

// ---- 启动 Edge + CDP 连接 ----
const profile = path.join(tmpdir(), "ui-cap-" + Date.now());
const edge = spawn(EDGE, [
  "--headless=new", "--disable-gpu", "--disable-extensions",
  `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  "--no-first-run", "--no-default-browser-check", "--hide-scrollbars", "about:blank",
], { stdio: "ignore" });

let ws;
let idSeq = 0;
const pending = new Map();
let events = [];

async function connect() {
  for (let i = 0; i < 60; i++) {
    try {
      const list = await fetchJson(`http://127.0.0.1:${PORT}/json/list`);
      const page = list.find((t) => t.type === "page");
      if (page?.webSocketDebuggerUrl) {
        ws = new WebSocket(page.webSocketDebuggerUrl);
        await new Promise((res, rej) => { ws.onopen = res; ws.onerror = () => rej(new Error("ws error")); });
        ws.onmessage = (e) => {
          const m = JSON.parse(e.data);
          if (m.id && pending.has(m.id)) {
            const p = pending.get(m.id); pending.delete(m.id);
            m.error ? p.rej(new Error(JSON.stringify(m.error))) : p.res(m.result);
          } else if (m.method) events.push(m);
        };
        return;
      }
    } catch {}
    await sleep(200);
  }
  throw new Error("CDP connect timeout");
}
const send = (method, params = {}) =>
  new Promise((res, rej) => {
    const id = ++idSeq;
    pending.set(id, { res, rej });
    ws.send(JSON.stringify({ id, method, params }));
    setTimeout(() => { if (pending.delete(id)) rej(new Error(`timeout: ${method}`)); }, 15000);
  });
const evalJs = async (expression) => {
  const r = await send("Runtime.evaluate", { expression, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error("evaluate failed: " + JSON.stringify(r.exceptionDetails).slice(0, 300));
  return r.result.value === undefined ? null : r.result.value;
};

async function goto(url, w = 1440, h = 2000) {
  events = [];
  // 先设视口再导航：避免导航后 resize 触发媒体查询重排的截图竞态
  await send("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: 1, mobile: false });
  await send("Page.navigate", { url });
  await sleep(700); // 站点脚本同步执行
  // 等平滑滚动（hash scrollIntoView）真实完成
  let last = -1, stable = 0;
  for (let i = 0; i < 60; i++) {
    const y = await evalJs("window.scrollY");
    if (y === last) { if (++stable >= 3) break; } else { stable = 0; last = y; }
    await sleep(100);
  }
  await sleep(150); // 让重排/过渡余量落地
}

function collectErrors() {
  const errs = [];
  for (const m of events) {
    if (m.method === "Runtime.exceptionThrown") errs.push("exception: " + (m.params.exceptionDetails?.text || "").slice(0, 200));
    if (m.method === "Log.entryAdded" && m.params.entry.level === "error") errs.push("log.error: " + (m.params.entry.url || "") + " :: " + m.params.entry.text.slice(0, 160));
    if (m.method === "Runtime.consoleAPICalled" && ["error", "assert"].includes(m.params.type))
      errs.push("console." + m.params.type + ": " + (m.params.args || []).map((a) => a.value ?? a.description ?? "").join(" ").slice(0, 200));
  }
  return errs;
}

// browser 级剪贴板授权（页面 ws 无法调用 Browser 域；失败不致命）
async function grantClipboard() {
  try {
    const ver = await fetchJson(`http://127.0.0.1:${PORT}/json/version`);
    const bws = new WebSocket(ver.webSocketDebuggerUrl);
    await new Promise((res, rej) => { bws.onopen = res; bws.onerror = () => rej(new Error("bws")); });
    let bid = 0;
    const bsend = (method, params = {}) => new Promise((res) => {
      const id = ++bid;
      const onm = (e) => { const m = JSON.parse(e.data); if (m.id === id) { bws.removeEventListener("message", onm); res(m.result); } };
      bws.addEventListener("message", onm);
      bws.send(JSON.stringify({ id, method, params }));
      setTimeout(() => { bws.removeEventListener("message", onm); res(null); }, 5000);
    });
    await bsend("Browser.grantPermissions", { permissions: ["clipboardReadWrite", "clipboardSanitizedWrite"], origin: BASE });
    bws.close();
  } catch {}
}

async function main() {
  await connect();
  await send("Page.enable");
  await send("Runtime.enable");
  await send("Log.enable");
  await grantClipboard();
  const report = { shots: [], measurements: {} };

  // ---- 截图 ----
  for (const s of SHOTS) {
    await goto(s.url, s.w, s.h);
    if (s.pre) {
      const opened = await evalJs(s.pre).catch(() => false);
      if (opened) await sleep(300); // lightbox 动画落地
    }
    const shot = await send("Page.captureScreenshot", { format: "png" });
    writeFileSync(path.join(OUT, s.file), Buffer.from(shot.data, "base64"));
    const errs = collectErrors();
    report.shots.push({ file: s.file, w: s.w, h: s.h, errors: errs, scrollY: await evalJs("window.scrollY") });
    console.log(`shot ${s.file}  scrollY=${report.shots.at(-1).scrollY}  errors=${errs.length}`);
  }

  // ---- DOM 测量（导演台/介绍页）----
  await goto(`${BASE}/#intro`, 1440, 2000);
  report.measurements = await evalJs(`(() => {
    const rect = (e) => { const r = e.getBoundingClientRect(); return { tag: e.tagName, cls: String(e.className).slice(0, 45), w: Math.round(r.width), h: Math.round(r.height) }; };
    const interactive = [...document.querySelectorAll('button, a[href], select, input, textarea, [role="button"], details, .pill, .chip, .copy-btn, .skill-tab')];
    const smallControls = interactive.map(rect).filter((r) => r.h > 0 && (r.h < 24 || r.w < 24));
    const fontCounts = {};
    let smallFontEls = 0;
    document.querySelectorAll('*').forEach((e) => {
      const fs = parseFloat(getComputedStyle(e).fontSize);
      if (fs > 0 && fs < 12) { smallFontEls++; const k = fs.toFixed(1) + 'px'; fontCounts[k] = (fontCounts[k] || 0) + 1; }
    });
    const overflow = [...document.querySelectorAll('*')].filter((e) => {
      if (e.tagName === 'SVG' || e.closest('.sr-only')) return false;
      return e.scrollWidth > e.clientWidth + 2 && !['auto','scroll'].includes(getComputedStyle(e).overflowX);
    }).slice(0, 15).map((e) => ({ tag: e.tagName, id: e.id || '', cls: String(typeof e.className === 'string' ? e.className : e.className.baseVal).slice(0, 50), parent: String(e.parentElement?.className || '').slice(0, 40), sw: e.scrollWidth, cw: e.clientWidth }));
    const dc = typeof DIRECTOR_CATALOG !== 'undefined' ? DIRECTOR_CATALOG : window.DIRECTOR_CATALOG;
    const cg = typeof COMBO_GALLERY !== 'undefined' ? COMBO_GALLERY : window.COMBO_GALLERY;
    const catalogs = {
      DIRECTOR_CATALOG: typeof DIRECTOR_CATALOG !== 'undefined' ? 'object' : typeof window.DIRECTOR_CATALOG,
      COMBO_GALLERY: typeof COMBO_GALLERY !== 'undefined' ? 'object' : typeof window.COMBO_GALLERY,
      DIM_RECOMMEND: typeof DIM_RECOMMEND !== 'undefined' ? 'object' : typeof window.DIM_RECOMMEND,
      dcKeys: dc ? Object.keys(dc) : null,
      dcSizes: dc ? Object.fromEntries(Object.keys(dc).map((k) => [k, Array.isArray(dc[k]) ? dc[k].length : (dc[k] && typeof dc[k] === 'object' ? 'obj' : typeof dc[k])])) : null,
      cgKeys: cg ? (Array.isArray(cg) ? ['(array)'] : Object.keys(cg).slice(0, 10)) : null,
      cgCount: cg ? (Array.isArray(cg) ? cg.length : Object.keys(cg).length) : -1,
      galleryImgs: document.querySelectorAll('#combo-gallery img').length,
      galleryCards: document.querySelectorAll('#combo-gallery .cg-card').length,
    };
    const scripts = [...document.querySelectorAll('script[src]')].map((s) => s.getAttribute('src'));
    const textDump = {
      comboCurrent: (document.querySelector('.combo-current')?.innerText || '').slice(0, 120),
      recipeBar: (document.querySelector('.recipe-bar')?.innerText || '').slice(0, 200),
      recPanel: (document.querySelector('.rec-panel:not([hidden])')?.innerText || '').slice(0, 120),
      formulaEls: [...document.querySelectorAll('*')].filter((e) => e.children.length === 0 && /配方/.test(e.textContent || '')).slice(0, 6).map((e) => ({ tag: e.tagName, cls: String(e.className).slice(0, 40), text: (e.textContent || '').slice(0, 60), w: Math.round(e.getBoundingClientRect().width), x: Math.round(e.getBoundingClientRect().x) })),
    };
    return { smallControls, fontCounts, smallFontEls, overflow, catalogs, scripts, textDump };
  })()`);

  // ---- 轻量功能冒烟：三壳 Tab 逐个点击 + hash 往返 ----
  report.functionalSmoke = await evalJs(`(async () => {
    const out = { tabs: [], hashRoundtrip: [] };
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    for (const shell of document.querySelectorAll('[data-skill-shell]')) {
      for (const btn of shell.querySelectorAll('.skill-tab')) {
        btn.click();
        await sleep(30);
        const active = shell.querySelector('.skill-panel.active');
        out.tabs.push(btn.dataset.skillTab + ' -> ' + (active?.dataset.skillPanel === btn.dataset.skillTab ? 'OK' : 'MISMATCH:' + (active?.dataset.skillPanel || 'none')));
      }
    }
    for (const h of ['#skill-figure?tab=figure-menu', '#skill-youth?tab=youth-gallery', '#skill-erotic?tab=nsfw-gallery']) {
      location.hash = h; await sleep(250);
      const id = location.hash.replace(/^#/, '').split('?')[0];
      const tab = new URLSearchParams(location.hash.split('?')[1] || '').get('tab');
      const shell = document.getElementById(id);
      const active = shell?.querySelector('.skill-panel.active');
      out.hashRoundtrip.push(h + ' -> ' + (active?.dataset.skillPanel === tab ? 'OK' : 'MISMATCH:' + (active?.dataset.skillPanel || 'none')));
    }
    return out;
  })()`);

  // ---- 640px 侧栏状态探针 + 触控目标测量 ----
  await goto(`${BASE}/#intro`, 640, 1600);
  report.sidebar640 = await evalJs(`(() => {
    const sb = document.querySelector('.sidebar');
    const mb = document.querySelector('.mobile-bar');
    const r = sb.getBoundingClientRect();
    const rect = (e) => { const r = e.getBoundingClientRect(); return { tag: e.tagName, id: e.id || '', cls: String(e.className).slice(0, 36), text: (e.textContent || '').slice(0, 16), w: Math.round(r.width), h: Math.round(r.height) }; };
    const mainOps = [...document.querySelectorAll('.form-actions button, .shot-strip-actions button, .recipe-bar button, .out-head button, .copy-btn, .skill-tab, .cg-skill-btn, .mobile-bar button')].map(rect).filter((r) => r.h > 0 && r.h < 44);
    const undersized = [...document.querySelectorAll('button, a[href], select, input, textarea, [role="button"]')].map(rect).filter((r) => r.h > 0 && r.h < 24);
    return { sidebarX: Math.round(r.x), sidebarRight: Math.round(r.right), sidebarW: Math.round(r.width),
      mobileBarDisplay: mb ? getComputedStyle(mb).display : 'none',
      navOpen: document.body.classList.contains('nav-open'),
      mainOpUnder44: mainOps, undersizedUnder24: undersized.slice(0, 12) };
  })()`);

  // ---- F 键盘基线：Tab 走查 intro 页，记录 activeElement 与焦点环可见性 ----
  await goto(`${BASE}/#intro`, 1440, 2000);
  const kb = [];
  for (let i = 0; i < 40; i++) {
    await send("Input.dispatchKeyEvent", { type: "keyDown", key: "Tab", code: "Tab", windowsVirtualKeyCode: 9 });
    await send("Input.dispatchKeyEvent", { type: "keyUp", key: "Tab", code: "Tab", windowsVirtualKeyCode: 9 });
    const r = await evalJs(`(() => { const e = document.activeElement; if (!e || e === document.body || e === document.documentElement) return null;
      const cs = getComputedStyle(e); const r = e.getBoundingClientRect();
      return { tag: e.tagName, id: e.id || '', cls: String(e.className).slice(0, 40), text: (e.textContent || '').slice(0, 24),
        focusRing: cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0, outline: cs.outlineStyle + ' ' + cs.outlineWidth, outlineColor: cs.outlineColor,
        vis: r.width > 0 && r.height > 0, x: Math.round(r.x), y: Math.round(r.y) }; })()`);
    if (r === null) break;
    kb.push(r);
  }
  report.keyboard = { walked: kb.length, focusRingVisible: kb.filter((k) => k.focusRing).length, items: kb };
  // ---- I 交互状态探针（三态截图）与阶段8共用：按钮中心坐标 ----
  const btnCenter = async (sel) => {
    const r = await evalJs(`(() => { const e = document.querySelector(${JSON.stringify(sel)}); if (!e) return null;
      e.scrollIntoView({ behavior: 'instant', block: 'center' }); const r = e.getBoundingClientRect();
      return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) }; })()`);
    if (r) await sleep(300); // 等布局稳定
    return r;
  };
  const shotTo = async (file) => {
    const s = await send("Page.captureScreenshot", { format: "png" });
    writeFileSync(path.join(OUT, file), Buffer.from(s.data, "base64"));
  };
  // headless=new 下 Input 事件触发的 confirm 不推 javascriptDialogOpening 事件，
  // 且 click 在 release 时才触发 → 必须先 release，再盲试 handleJavaScriptDialog
  const clickWithDialog = async (pos, accept) => {
    events.length = 0;
    await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: pos.x, y: pos.y }).catch(() => {});
    const p = send("Input.dispatchMouseEvent", { type: "mousePressed", x: pos.x, y: pos.y, button: "left", clickCount: 1 }).catch(() => {});
    await sleep(150);
    await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: pos.x, y: pos.y, button: "left", clickCount: 1 }).catch(() => {});
    await p.catch(() => {});
    await sleep(400); // click 已触发，对话框（若有）此时已打开
    const ev = events.find((e) => e.method === "Page.javascriptDialogOpening");
    const msg = ev ? ev.params.message : null;
    let lastErr = null;
    await Promise.race([
      send("Page.handleJavaScriptDialog", { accept }).catch((e) => { lastErr = e.message; }),
      sleep(3000),
    ]);
    await sleep(400);
    return { msg, handled: lastErr === null };
  };

  // ---- 阶段8 confirm 对话框回归：B19 取消无副作用 / B20 空态不弹窗 / B21 导入覆盖确认 / B22 toast aria-live ----
  const s8 = {};
  const step = (n) => console.log("  [s8]", n);
  try {
  await step("marker");
  await evalJs(`window.__reloadMarker = 1`);
  await send("Emulation.setDeviceMetricsOverride", { width: 1440, height: 2000, deviceScaleFactor: 1, mobile: false });
  // 路径差异 URL 保证真实整页加载（hash/query 差异可能被当作同文档导航）
  await send("Page.navigate", { url: `${BASE}/index.html?reset=${Date.now()}#intro` });
  await sleep(1200);
  await step("reloadVerified");
  s8.reloadVerified = await evalJs(`({ marker: typeof window.__reloadMarker, shots: document.querySelectorAll('#shotStrip > *').length, href: location.href })`);
  await step("toastAttrs");
  s8.toastAttrs = await evalJs(`(() => { const t = document.getElementById('dirToast');
    return { role: t?.getAttribute('role'), ariaLive: t?.getAttribute('aria-live') }; })()`);
  const readShots = () => evalJs(`(() => { const els = [...document.querySelectorAll('#shotStrip > *')];
    return { count: els.length, titles: els.map((e) => (e.querySelector('.shot-title')?.textContent || '').trim()).join('|') }; })()`);
  const readToastText = () => evalJs(`document.getElementById('dirToast')?.textContent || ''`);
  // B20 空态：单 Shot 默认态点击不弹窗，直接生成 4 镜
  await step("btnCenter");
  const vPos = await btnCenter("#btnVaryShots");
  await step("click-empty");
  if (vPos) {
    const before = await readShots();
    const r0 = await clickWithDialog(vPos, false);
    s8.emptyState = { dialog: r0.handled, before, after: await readShots(), toast: (await readToastText()).trim().slice(0, 30) };
  }
  await step("cancel");
  // B19 取消路径：有内容时弹窗，取消后分镜不变
  if (vPos) {
    const before = await readShots();
    s8.cancelDialog = await clickWithDialog(vPos, false);
    const after = await readShots();
    s8.cancelNoSideEffect = { after, unchanged: JSON.stringify(before) === JSON.stringify(after) };
  }
  await step("accept");
  // B19 接受路径：确认后重新生成
  if (vPos) {
    s8.acceptDialog = await clickWithDialog(vPos, true);
    s8.acceptApplied = { toast: (await readToastText()).trim().slice(0, 30), after: await readShots() };
  }
  await step("import");
  // B21 导入覆盖确认：合法 JSON 弹确认，取消不改状态（confirm 在 FileReader.onload 异步触发，同样盲处理）
  const beforeImport = await readShots();
  const importEval = evalJs(`(() => {
    const input = document.getElementById('recipeFile');
    const dt = new DataTransfer();
    dt.items.add(new File(['{"mode":"youth","shots":[{"title":"导入测试","picks":{},"extra":""}]}'], 't.json', { type: 'application/json' }));
    input.files = dt.files;
    input.dispatchEvent(new Event('change', { bubbles: true }));
    return true;
  })()`).catch(() => true);
  await sleep(600); // 等 FileReader onload → confirm 打开
  const impEv = events.find((e) => e.method === "Page.javascriptDialogOpening");
  s8.importDialogMsg = impEv ? impEv.params.message : null;
  let impErr = null;
  await Promise.race([
    send("Page.handleJavaScriptDialog", { accept: false }).catch((e) => { impErr = e.message; }),
    sleep(3000),
  ]);
  s8.importDialogHandled = impErr === null;
  await importEval;
  await sleep(500);
  const afterImport = await readShots();
  s8.importCancelNoSideEffect = { after: afterImport, unchanged: JSON.stringify(beforeImport) === JSON.stringify(afterImport) };
  await step("save");
  // B13 删除确认：先存配方 → 点删除弹确认 → 取消后配方仍在；再点删除 → 确认后消失
  await evalJs(`(() => { const i = document.getElementById('recipeName'); i.value = '回归测试配方'; return true; })()`);
  const sPos = await btnCenter("#btnSaveRecipe");
  if (sPos) {
    events.length = 0;
    s8.saveDialog = await clickWithDialog(sPos, false);
    await sleep(300);
  }
  const optionsBefore = () => evalJs(`[...document.querySelectorAll('#recipeSelect option')].map((o) => o.value + ':' + o.textContent).join('|')`);
  s8.deleteOptsBefore = await optionsBefore();
  const dPos = await btnCenter("#btnDelRecipe");
  await step("del-cancel");
  if (dPos) {
    s8.deleteCancelDialog = await clickWithDialog(dPos, false);
    s8.deleteCancelKept = await optionsBefore();
  }
  await step("del-accept");
  if (dPos) {
    s8.deleteAcceptDialog = await clickWithDialog(dPos, true);
    await sleep(300);
    s8.deleteAcceptRemoved = await optionsBefore();
  }
  } catch (e) {
    s8.failedAt = e.message;
    console.log("  [s8] FAILED:", e.message);
  }
  report.stage8 = s8;

  // ---- I 交互状态探针：hover / 按压 / 焦点三态截图 ----
  await goto(`${BASE}/#intro`, 1440, 2000);
  const hoverPos = await btnCenter("#btnVaryShots");
  if (hoverPos) {
    await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: hoverPos.x, y: hoverPos.y });
    await sleep(300);
    await shotTo("12-state-hover.png");
  }
  const pressPos = await btnCenter("#btnAddShot");
  if (pressPos) {
    await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: pressPos.x, y: pressPos.y });
    await send("Input.dispatchMouseEvent", { type: "mousePressed", x: pressPos.x, y: pressPos.y, button: "left", clickCount: 1 });
    await sleep(300);
    await shotTo("13-state-active.png");
    await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: pressPos.x, y: pressPos.y, button: "left", clickCount: 1 });
  }
  const focusPos = await btnCenter(".combo-search-wrap input, #dirComboSearch");
  if (focusPos) {
    await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: focusPos.x, y: focusPos.y });
    await send("Input.dispatchMouseEvent", { type: "mousePressed", x: focusPos.x, y: focusPos.y, button: "left", clickCount: 1 });
    await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: focusPos.x, y: focusPos.y, button: "left", clickCount: 1 });
    await sleep(300);
    await shotTo("14-state-inputfocus.png");
  }
  report.stateShots = { hover: "12-state-hover.png", active: "13-state-active.png", inputFocus: "14-state-inputfocus.png" };
  // ---- B 全量功能回归（B2-B18 自动化）----
  report.functional = {};
  const f = async (name, fn) => { try { report.functional[name] = await fn(); } catch (e) { report.functional[name] = { error: e.message }; } };
  const plainClick = async (pos) => {
    if (!pos) return;
    await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: pos.x, y: pos.y }).catch(() => {});
    await send("Input.dispatchMouseEvent", { type: "mousePressed", x: pos.x, y: pos.y, button: "left", clickCount: 1 }).catch(() => {});
    await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: pos.x, y: pos.y, button: "left", clickCount: 1 }).catch(() => {});
    await sleep(300);
  };
  const clickSel = async (sel) => { const p = await btnCenter(sel); await plainClick(p); return p; };
  const probe = (js) => evalJs(js);
  const readToast = async () => (await probe(`document.getElementById('dirToast')?.textContent || ''`)).trim().slice(0, 40);
  const resetPage = async () => { await send("Page.navigate", { url: `${BASE}/index.html?reset=${Date.now()}#intro` }); await sleep(1200); };
  const resetTo = async (hash) => { await send("Page.navigate", { url: `${BASE}/index.html?reset=${Date.now()}${hash}` }); await sleep(1200); };
  // 剪贴板/下载权限（失败不致命）
  try { await send("Browser.grantPermissions", { permissions: ["clipboardReadWrite", "clipboardSanitizedWrite"], origin: BASE }); } catch {}
  try { await send("Page.setDownloadBehavior", { behavior: "allow", downloadPath: OUT }); } catch {}

  // B2 刷新保持：hash+tab 在刷新后保持
  await f("B2-refresh-keeps-hash", async () => {
    await goto(`${BASE}/#skill-figure?tab=figure-menu`, 1440, 1400);
    const before = await probe(`document.querySelector('[data-skill-shell="figure"] .skill-panel.active')?.dataset.skillPanel`);
    await send("Page.navigate", { url: `${BASE}/index.html?reset=${Date.now()}#skill-figure?tab=figure-menu` });
    await sleep(1200);
    const after = await probe(`document.querySelector('[data-skill-shell="figure"] .skill-panel.active')?.dataset.skillPanel`);
    return { before, after, ok: before === after && after === "figure-menu" };
  });

  // B3 前进/后退
  await f("B3-back-forward", async () => {
    await goto(`${BASE}/#skill-figure?tab=figure`, 1440, 1400);
    await probe(`location.hash = '#skill-youth?tab=youth'`);
    await sleep(500);
    const mid = await probe(`location.hash`);
    await probe(`history.back()`);
    await sleep(500);
    const back = await probe(`location.hash`);
    await probe(`history.forward()`);
    await sleep(500);
    const fwd = await probe(`location.hash`);
    return { mid, back, fwd, ok: back.includes("skill-figure") && fwd.includes("skill-youth") };
  });

  // B5 一键预设 ×3 mode
  await f("B5-presets-x3", async () => {
    await resetPage();
    const out = {};
    for (const mode of ["figure", "youth", "erotic"]) {
      await clickSel(`.skill-switch button[data-mode="${mode}"]`);
      await sleep(400);
      const before = await probe(`document.getElementById('dirPreview')?.textContent?.length || 0`);
      await clickSel(".preset-card");
      await sleep(400);
      const after = await probe(`document.getElementById('dirPreview')?.textContent?.length || 0`);
      out[mode] = { toast: await readToast(), previewChanged: after > 0 && after !== before };
    }
    return { ...out, ok: Object.values(out).every((v) => v.previewChanged) };
  });

  // B6 组合包搜索点选
  await f("B6-combo-search-pick", async () => {
    await resetPage();
    await probe(`(() => { const i = document.querySelector('.combo-search-wrap input'); i.value = '街拍'; i.dispatchEvent(new Event('input', { bubbles: true })); return true; })()`);
    await sleep(500);
    const cardCount = await probe(`document.querySelectorAll('.combo-card').length`);
    await clickSel(".combo-card");
    await sleep(400);
    const name = await probe(`document.querySelector('.combo-current-name')?.textContent || ''`);
    return { cardCount, picked: name, ok: cardCount > 0 && name.length > 0 };
  });

  // B7 分组点选（单选互斥 + 多选累积）
  await f("B7-group-picks", async () => {
    await resetPage();
    const opened = await probe(`[...document.querySelectorAll('.field-group[open]')].map((g) => g.querySelector('summary')?.textContent?.trim().slice(0, 10))`);
    const setOf = `[...document.querySelectorAll('.field-group[open] .chip-opt.is-on')].map((c) => c.textContent.trim().slice(0, 8)).join('|')`;
    const beforeSet = await probe(setOf);
    await clickSel(".field-group[open] .chip-opt:nth-of-type(2)");
    await sleep(300);
    const afterSet = await probe(setOf);
    const cur1 = await probe(`(document.querySelector('.field-group[open] .field-cur')?.textContent || '')`);
    const multiInfo = await probe(`(() => { const g = document.querySelector('.field-block.is-multi'); return g ? (g.querySelector('.field-cur')?.textContent || '') : 'no-multi-visible'; })()`);
    return { opened, beforeSet, afterSet, cur1, multiInfo, ok: beforeSet !== afterSet };
  });

  // B8 复制英文/命令 + toast（成功信号可能是 toast 或按钮文字变化）
  await f("B8-copy-toast", async () => {
    await resetPage();
    await clickSel("#btnDirCopy");
    const t1 = await readToast();
    await sleep(150);
    const btnTxt = await probe(`document.getElementById('btnDirCopy')?.textContent`);
    await clickSel("#btnDirCopyCmd");
    const t2 = await readToast();
    await sleep(150);
    const cmdBtn = await probe(`document.getElementById('btnDirCopyCmd')?.textContent`);
    const copyOk = t1.includes("已复制") || btnTxt.includes("已复制");
    const cmdOk = t2.includes("已复制") || String(cmdBtn).includes("已复制");
    return { copyToast: t1, copyBtn: btnTxt, cmdToast: t2, cmdBtn, ok: copyOk && cmdOk };
  });

  // B9 词数条与实际词数一致
  await f("B9-wordcount", async () => {
    await resetPage();
    const wc = await probe(`document.getElementById('dirWordCount')?.textContent || ''`);
    const text = await probe(`document.getElementById('dirPreview')?.textContent || ''`);
    const actual = text.trim().split(/\s+/).filter(Boolean).length;
    const shown = parseInt((wc.match(/约 (\d+)/) || [])[1] || "-1", 10);
    return { shownText: wc, actual, shown, ok: actual > 0 && Math.abs(actual - shown) <= Math.max(5, actual * 0.1) };
  });

  // B10 推荐面板（出现与否依赖状态，如实记录）
  await f("B10-rec-panel", async () => {
    await resetPage();
    const visible = await probe(`(() => { const p = document.querySelector('.rec-panel'); return p && !p.hidden ? { shown: true, text: p.textContent.slice(0, 60) } : { shown: false }; })()`);
    if (!visible.shown) return { ...visible, note: "推荐面板未出现（状态相关，非缺陷）", ok: true };
    const before = await probe(`document.getElementById('dirPreview')?.textContent?.length || 0`);
    await clickSel("#btnRecApply");
    await sleep(300);
    const after = await probe(`document.getElementById('dirPreview')?.textContent?.length || 0`);
    return { ...visible, appliedChanged: after !== before, ok: true };
  });

  // B11 Shot 操作
  await f("B11-shots", async () => {
    await resetPage();
    const c0 = await probe(`document.querySelectorAll('#shotStrip > *').length`);
    await clickSel("#btnAddShot");
    const c1 = await probe(`document.querySelectorAll('#shotStrip > *').length`);
    await clickSel("#btnDupShot");
    const c2 = await probe(`document.querySelectorAll('#shotStrip > *').length`);
    await clickSel(".shot-card[data-si='1']");
    await sleep(200);
    const activeSi = await probe(`document.querySelector('.shot-card.active')?.dataset.si`);
    await clickSel("#btnDirCopySeries");
    const t = await readToast();
    return { c0, c1, c2, activeSi, copySeriesToast: t, ok: c1 === c0 + 1 && c2 === c1 + 1 && activeSi === "1" };
  });

  // B12 随机 / 恢复默认
  await f("B12-random-reset", async () => {
    await resetPage();
    const before = await probe(`document.getElementById('dirPreview')?.textContent || ''`);
    await clickSel("#btnDirRandom");
    await sleep(300);
    const after = await probe(`document.getElementById('dirPreview')?.textContent || ''`);
    await clickSel("#btnResetDefaults");
    const t = await readToast();
    return { changed: before !== after, resetToast: t, ok: before !== after && t.includes("已恢复默认") };
  });

  // B13 配方往返（保存→刷新→加载）+ 导出文件落盘
  await f("B13-recipe-roundtrip", async () => {
    await resetPage();
    await probe(`(() => { const i = document.getElementById('recipeName'); i.value = '往返配方'; return true; })()`);
    await clickSel("#btnSaveRecipe");
    await sleep(300);
    await resetPage();
    const opts = await probe(`[...document.querySelectorAll('#recipeSelect option')].map((o) => o.textContent).join('|')`);
    const has = opts.includes("往返配方");
    // 选中该配方再加载
    await probe(`(() => { const s = document.getElementById('recipeSelect'); const o = [...s.options].find((x) => x.textContent === '往返配方'); if (o) { s.value = o.value; s.dispatchEvent(new Event('change', { bubbles: true })); } return true; })()`);
    await clickSel("#btnLoadRecipe");
    const t = await readToast();
    // 导出：文件应写入下载目录
    const before = new Set(readdirSync(OUT));
    await clickSel("#btnExportRecipe");
    await sleep(1200);
    const afterFiles = readdirSync(OUT);
    const exported = afterFiles.filter((x) => !before.has(x) && x.includes("director-"));
    return { optsHas: has, loadToast: t, exported, ok: has && t.includes("已加载") };
  });

  // B14 图库搜索/筛选/计数/点卡
  await f("B14-gallery", async () => {
    await goto(`${BASE}/#combo-gallery`, 1440, 1600);
    const cAll = await probe(`document.querySelectorAll('.cg-card').length`);
    const btns = await probe(`[...document.querySelectorAll('.cg-skill-btn')].map((b) => b.textContent.trim()).join('|')`);
    await clickSel(".cg-skill-btn:nth-of-type(2)");
    await sleep(500);
    const cFiltered = await probe(`document.querySelectorAll('.cg-card').length`);
    await probe(`(() => { const i = document.querySelector('.cg-search'); if (i) { i.value = '白'; i.dispatchEvent(new Event('input', { bubbles: true })); } return true; })()`);
    await sleep(500);
    const cSearched = await probe(`document.querySelectorAll('.cg-card').length`);
    await probe(`(() => { const c = [...document.querySelectorAll('.cg-card')].find((x) => x.getBoundingClientRect().width > 0); if (!c) return null; c.scrollIntoView({ behavior: 'instant', block: 'center' }); const r = c.getBoundingClientRect(); return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) }; })()`).then(async (pos) => { if (pos) await plainClick(pos); });
    await sleep(250);
    const copied = await probe(`(document.querySelector('.cg-card.copied')?.dataset?.comboId || '')`);
    return { cAll, btns, cFiltered, cSearched, copied, ok: cAll > 0 && cFiltered !== cAll && copied !== "" };
  });

  // B15 router 决策器
  await f("B15-router", async () => {
    await goto(`${BASE}/#intro`, 1440, 2000);
    await probe(`(() => { const el = document.querySelector('.router'); el?.scrollIntoView({ behavior: 'instant', block: 'center' }); return true; })()`);
    await sleep(300);
    await clickSel(".router-options button");
    await sleep(400);
    const result = await probe(`(() => { const r = document.querySelector('.router-result'); return r && r.classList.contains('show') ? r.textContent.slice(0, 80) : 'not-shown'; })()`);
    return { result, ok: result !== "not-shown" };
  });

  // B16 details 折叠 + copy-btn
  await f("B16-details-copy", async () => {
    await goto(`${BASE}/#intro`, 1440, 2000);
    await probe(`(() => { const el = document.querySelector('details.more'); el?.scrollIntoView({ behavior: 'instant', block: 'center' }); return true; })()`);
    await sleep(300);
    return probe(`(() => { const d = [...document.querySelectorAll('details.more')].find((x) => x.getBoundingClientRect().width > 0); if (!d) return null; const s = d.querySelector('summary'); s.scrollIntoView({ behavior: 'instant', block: 'center' }); const r = s.getBoundingClientRect(); return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2), wasOpen: d.open }; })()`).then(async (info) => {
      if (!info) return { error: "no visible details" };
      await plainClick({ x: info.x, y: info.y });
      await sleep(300);
      const isOpen = await probe(`(() => { const d = [...document.querySelectorAll('details.more')].find((x) => x.getBoundingClientRect().width > 0); return d ? d.open : null; })()`);
      let t = "";
      if (isOpen) { const cp = await probe(`(() => { const d = [...document.querySelectorAll('details.more')].find((x) => x.getBoundingClientRect().width > 0); if (!d) return null; const b = d.querySelector('.copy-btn'); if (!b) return null; b.scrollIntoView({ behavior: 'instant', block: 'center' }); const r = b.getBoundingClientRect(); return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) }; })()`); if (cp) { await plainClick(cp); await sleep(200); t = await readToast(); } }
      return { wasOpen: info.wasOpen, isOpen, toast: t, ok: isOpen === true };
    });
  });

  // B18 localStorage 清空后不崩
  await f("B18-localstorage-clear", async () => {
    await resetPage();
    await probe(`localStorage.clear()`);
    await resetPage();
    const ok = await probe(`({ catalog: typeof DIRECTOR_CATALOG === 'object', shots: document.querySelectorAll('#shotStrip > *').length, hasRoot: !!document.getElementById('directorRoot') })`);
    return { ...ok, ok: ok.catalog && ok.hasRoot && ok.shots >= 1 };
  });

  // 全站键盘走查（三壳/图库/首页，各 40 步）
  await f("B-keyboard-all-pages", async () => {
    const pages = [
      ["intro", `${BASE}/index.html?reset=${Date.now()}#intro`],
      ["figure", `${BASE}/index.html?reset=${Date.now()}#skill-figure?tab=figure`],
      ["youth", `${BASE}/index.html?reset=${Date.now()}#skill-youth?tab=youth`],
      ["erotic", `${BASE}/index.html?reset=${Date.now()}#skill-erotic?tab=erotic`],
      ["gallery", `${BASE}/index.html?reset=${Date.now()}#combo-gallery`],
    ];
    const results = {};
    for (const [name, url] of pages) {
      await send("Emulation.setDeviceMetricsOverride", { width: 1440, height: 2000, deviceScaleFactor: 1, mobile: false });
      await send("Page.navigate", { url });
      await sleep(1200);
      await send("Input.dispatchMouseEvent", { type: "mousePressed", x: 8, y: 200, button: "left", clickCount: 1 }).catch(() => {});
      await send("Input.dispatchMouseEvent", { type: "mouseReleased", x: 8, y: 200, button: "left", clickCount: 1 }).catch(() => {});
      await sleep(200);
      let walked = 0, ringVisible = 0, noRing = [];
      for (let i = 0; i < 40; i++) {
        await send("Input.dispatchKeyEvent", { type: "keyDown", key: "Tab", code: "Tab", windowsVirtualKeyCode: 9 });
        await send("Input.dispatchKeyEvent", { type: "keyUp", key: "Tab", code: "Tab", windowsVirtualKeyCode: 9 });
        const r = await probe(`(() => { const e = document.activeElement; if (!e || e === document.body || e === document.documentElement) return null;
          const cs = getComputedStyle(e); const r = e.getBoundingClientRect();
          return { ring: cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0, cls: String(e.className).slice(0, 30), text: (e.textContent || '').trim().slice(0, 14) }; })()`);
        if (r === null) break;
        walked++;
        if (r.ring) ringVisible++; else noRing.push(r.cls + ':' + r.text);
      }
      results[name] = { walked, ringVisible, noRing: noRing.slice(0, 4), ok: walked > 5 && ringVisible === walked };
    }
    return results;
  });

  // ---- E 缩放回归（真实浏览器 Ctrl+ 缩放 = CSS 视口收缩触发响应式重排；dsf 恒 1，
  //      实测 headless 下 dsf 切换会挂起后续真实导航）----
  // 定向导演台顶部，覆盖验收口径（按钮组/预览/预设卡列）
  await goto(`${BASE}/#directorRoot`, 960, 1300);
  const z15 = await send("Page.captureScreenshot", { format: "png" });
  writeFileSync(path.join(OUT, "10-zoom150-director.png"), Buffer.from(z15.data, "base64"));
  // 补拍预览面板区（窄视口单列下预览在表单下方）——960 档，锚定 out-head 按钮组（center 避开 sticky 顶栏遮挡）
  await evalJs(`(() => { const el = document.querySelector('.out-head'); el?.scrollIntoView({ behavior: 'instant', block: 'center' }); return true; })()`);
  await sleep(400);
  const z15p = await send("Page.captureScreenshot", { format: "png" });
  writeFileSync(path.join(OUT, "12-zoom150-preview.png"), Buffer.from(z15p.data, "base64"));
  await goto(`${BASE}/#directorRoot`, 720, 1200);
  const z2 = await send("Page.captureScreenshot", { format: "png" });
  writeFileSync(path.join(OUT, "11-zoom200-director.png"), Buffer.from(z2.data, "base64"));
  // 720 档预览面板，锚定 out-head（center 避开 sticky 顶栏遮挡）
  await evalJs(`(() => { const el = document.querySelector('.out-head'); el?.scrollIntoView({ behavior: 'instant', block: 'center' }); return true; })()`);
  await sleep(400);
  const z2p = await send("Page.captureScreenshot", { format: "png" });
  writeFileSync(path.join(OUT, "13-zoom200-preview.png"), Buffer.from(z2p.data, "base64"));
  report.zoom720 = await evalJs(`(() => {
    const cw = document.documentElement.clientWidth;
    const offenders = [...document.querySelectorAll('*')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 0 && r.right > cw + 2 && !e.closest('.shot-strip');
    }).slice(0, 10).map((e) => { const r = e.getBoundingClientRect();
      return { tag: e.tagName, id: e.id || '', cls: String(typeof e.className === 'string' ? e.className : '').slice(0, 40), right: Math.round(r.right), w: Math.round(r.width) }; });
    return { cw, pageScrollWidth: document.documentElement.scrollWidth, offenders };
  })()`);
  await send("Emulation.setDeviceMetricsOverride", { width: 1440, height: 2000, deviceScaleFactor: 1, mobile: false });
  report.zoom = { captured: ["10-zoom150-director.png", "11-zoom200-director.png"], note: "960/720 CSS 视口（dsf 恒 1），等价真实缩放的重排行为，定向导演台" };

  // ---- G 动效回归：reduced-motion 下动画/过渡必须被全局禁用 ----
  const motionProbe = `(() => {
    const el = document.querySelector('.preset-card, .cg-card, .skill-panel') || document.body;
    const cs = getComputedStyle(el);
    return { sampleCls: String(el.className).slice(0, 40), animationName: cs.animationName, transitionDuration: cs.transitionDuration };
  })()`;
  await send("Emulation.setEmulatedMedia", { features: [{ name: "prefers-reduced-motion", value: "reduce" }] });
  const reduced = await evalJs(motionProbe);
  await send("Emulation.setEmulatedMedia", { features: [] });
  const normal = await evalJs(motionProbe);
  report.reducedMotion = { reduced, normal };

  report.meta = { at: new Date().toISOString(), port: PORT };
  writeFileSync(path.join(OUT, "baseline-report.json"), JSON.stringify(report, null, 2));
  console.log("REPORT saved. console errors total:", report.shots.reduce((n, s) => n + s.errors.length, 0));
  console.log("smallControls(<24px):", report.measurements.smallControls.length, " smallFontEls(<12px):", report.measurements.smallFontEls, " overflow:", report.measurements.overflow.length);
  ws.close();
  edge.kill();
  process.exit(0);
}

main().catch((e) => { console.error("FATAL:", e.message); try { edge.kill(); } catch {} process.exit(1); });
