// scripts/_verify_combo_link.mjs — 一次性验证：导演台点选组合包后主题维度联动（读 DOM 值，不看图）
// 用法：node scripts/_verify_combo_link.mjs   （依赖 8766 端口 http server）
import { spawn } from "node:child_process";
import { writeFileSync, existsSync } from "node:fs";

const EDGE = ["C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe", "C:/Program Files/Microsoft/Edge/Application/msedge.exe"].find(existsSync);

const PORT = 9800 + Math.floor(Math.random() * 100);
const BASE = "http://127.0.0.1:8766";
let ws, idSeq = 0;
const pending = new Map();

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const fetchJson = async (url, init) => (await fetch(url, init)).json();

const edge = spawn(EDGE, [
  "--headless=new", `--remote-debugging-port=${PORT}`, "--disable-gpu", "--no-first-run",
  `--user-data-dir=${process.env.TEMP}/edge-ui-verify-${Date.now()}`, "about:blank",
], { stdio: "ignore" });

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
          }
        };
        return;
      }
    } catch {}
    await sleep(200);
  }
  throw new Error("CDP connect timeout");
}
const send = (method, params = {}) => new Promise((res, rej) => {
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

async function main() {
  await connect();
  await send("Page.enable");
  await send("Runtime.enable");
  const exceptions = [];
  ws.addEventListener("message", (e) => {
    const m = JSON.parse(e.data);
    if (m.method === "Runtime.exceptionThrown") {
      exceptions.push((m.params.exceptionDetails?.exception?.description || m.params.exceptionDetails?.text || "").slice(0, 300));
    }
  });
  await send("Emulation.setDeviceMetricsOverride", { width: 1440, height: 1600, deviceScaleFactor: 1, mobile: false });
  await send("Page.navigate", { url: `${BASE}/#directorRoot` });
  await sleep(1200);

  const result = await evalJs(`(async () => {
    const out = { steps: [] };
    // 1. 切 erotic 模式
    const modeBtn = document.querySelector('[data-mode="erotic"]');
    if (!modeBtn) return { error: "no erotic mode button" };
    modeBtn.click();
    await new Promise(r => setTimeout(r, 400));
    out.mode = document.querySelector('[data-mode="erotic"]')?.classList.contains('is-on') ? 'erotic' : '?';

    // 2. 组合包搜索框输入"雪女"
    const search = document.querySelector('#comboPicker input[type="search"], #comboPicker .combo-filter');
    if (search) {
      const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
      setter.call(search, '雪女');
      search.dispatchEvent(new Event('input', { bubbles: true }));
      await new Promise(r => setTimeout(r, 400));
      out.searchFound = search.value;
    } else {
      out.searchFound = 'no search box';
    }

    // 3. 点击雪女温泉组合包
    const pick = [...document.querySelectorAll('.combo-select-btn')].find(b => (b.dataset.combo || '').includes('yuki-onsen'));
    if (!pick) return { ...out, error: "no yuki-onsen button (分组未展开或搜索未过滤)", btns: document.querySelectorAll('.combo-select-btn').length };
    pick.click();
    await new Promise(r => setTimeout(r, 400));
    const onCard = document.querySelector('.combo-card.is-on');
    out.selectedCard = onCard ? onCard.dataset.combo : 'none';
    out.comboCurrent = document.querySelector('.combo-current-img, [class*="combo-cur"]')?.textContent?.slice(0, 60) || '';

    // 4. 读表单字段当前值
    const fields = {};
    document.querySelectorAll('.field-block').forEach(fb => {
      const key = fb.dataset.field;
      const cur = fb.querySelector('.field-cur');
      if (key && cur) fields[key] = cur.textContent.trim();
    });
    out.fields = fields;

    // 5. 读预览区文本前 500 字符
    const prev = document.querySelector('#previewEn, .preview-en, [data-role="preview-en"]');
    out.preview = prev ? prev.textContent.slice(0, 600) : 'no preview element';

    // 6. 读当前配方卡
    const recipe = document.querySelector('.recipe-title, [class*="recipe"]');
    out.recipe = recipe ? recipe.textContent.slice(0, 120) : '';

    return out;
  })()`);

  console.log(JSON.stringify(result, null, 2));
  console.log("JS exceptions:", JSON.stringify(exceptions, null, 2));
  writeFileSync("docs/_ui-baseline/combo-link-verify.json", JSON.stringify({ ...result, exceptions }, null, 2));
  edge.kill();
  process.exit(0);
}

main().catch((e) => { console.error("FAIL:", e.message); edge.kill(); process.exit(1); });
