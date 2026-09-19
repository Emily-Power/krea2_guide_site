// 开发期调试脚本：单独验证 CDP 点击命中与页面初始化状态
import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

const PORT = 9334;
const BASE = "http://127.0.0.1:8766";
const EDGE = ["C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe", "C:/Program Files/Microsoft/Edge/Application/msedge.exe"].find(existsSync);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const edge = spawn(EDGE, ["--headless=new", "--disable-gpu", "--disable-extensions", `--remote-debugging-port=${PORT}`, `--user-data-dir=${path.join(tmpdir(), "ui-dbg-" + Date.now())}`, "--no-first-run", "--no-default-browser-check", "--hide-scrollbars", "about:blank"], { stdio: "ignore" });

let ws, idSeq = 0;
const pending = new Map();
let events = [];
const send = (method, params = {}) => new Promise((res, rej) => {
  const id = ++idSeq; pending.set(id, { res, rej });
  ws.send(JSON.stringify({ id, method, params }));
  setTimeout(() => { if (pending.delete(id)) rej(new Error("timeout " + method)); }, 15000);
});
const evalJs = async (expression) => {
  const r = await send("Runtime.evaluate", { expression, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) return { __exception: String(r.exceptionDetails.text) };
  return r.result.value;
};

async function main() {
  for (let i = 0; i < 60; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
      const page = list.find((t) => t.type === "page");
      if (page?.webSocketDebuggerUrl) {
        ws = new WebSocket(page.webSocketDebuggerUrl);
        await new Promise((res, rej) => { ws.onopen = res; ws.onerror = () => rej(new Error("ws")); });
        ws.onmessage = (e) => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { const p = pending.get(m.id); pending.delete(m.id); m.error ? p.rej(new Error(JSON.stringify(m.error))) : p.res(m.result); } else if (m.method) events.push(m); };
        break;
      }
    } catch {}
    await sleep(200);
  }
  await send("Page.enable"); await send("Runtime.enable"); await send("Log.enable");
  await send("Emulation.setDeviceMetricsOverride", { width: 1440, height: 2000, deviceScaleFactor: 1, mobile: false });
  await send("Page.navigate", { url: `${BASE}/#intro` });
  await sleep(1200);

  const info = await evalJs(`(() => {
    const b = document.getElementById('btnVaryShots');
    if (!b) return { missing: true };
    b.scrollIntoView({ behavior: 'instant', block: 'center' });
    const r = b.getBoundingClientRect();
    const cx = Math.round(r.x + r.width / 2), cy = Math.round(r.y + r.height / 2);
    const at = document.elementFromPoint(cx, cy);
    window.__hitTest = 0;
    b.addEventListener('click', () => window.__hitTest++);
    return {
      href: location.href, scrollY: window.scrollY,
      shotCount: document.querySelectorAll('#shotStrip > *').length,
      shotsHtml: document.getElementById('shotStrip')?.innerHTML.slice(0, 300),
      rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }, cx, cy,
      atPoint: at ? at.tagName + '#' + (at.id || '') + '.' + String(at.className).slice(0, 26) : 'none',
    };
  })()`);
  console.log(JSON.stringify(info, null, 1));

  // 真实 CDP 点击（逐事件诊断，单发 5s 超时）
  const centerOf = async (sel) => {
    const r = await evalJs(`(() => { const b = document.querySelector('${sel}'); if (!b) return null;
      b.scrollIntoView({ behavior: 'instant', block: 'center' }); const r = b.getBoundingClientRect();
      return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) }; })()`);
    await sleep(200);
    return r;
  };
  const clickAt = async (name, pos) => {
    try { await Promise.race([send("Input.dispatchMouseEvent", { type: "mouseMoved", x: pos.x, y: pos.y }), sleep(4000).then(() => { throw new Error("t"); })]); console.log(name, "moved OK"); } catch (e) { console.log(name, "moved FAILED:", e.message); }
    try { await Promise.race([send("Input.dispatchMouseEvent", { type: "mousePressed", x: pos.x, y: pos.y, button: "left", clickCount: 1 }), sleep(4000).then(() => { throw new Error("t"); })]); console.log(name, "pressed OK, events:", events.length); } catch (e) { console.log(name, "pressed FAILED:", e.message); }
    const dlg = events.find((e) => e.method === "Page.javascriptDialogOpening");
    if (dlg) { console.log(name, "DIALOG:", dlg.params.message); await send("Page.handleJavaScriptDialog", { accept: false }); }
    try { await Promise.race([send("Input.dispatchMouseEvent", { type: "mouseReleased", x: pos.x, y: pos.y, button: "left", clickCount: 1 }), sleep(4000).then(() => { throw new Error("t"); })]); console.log(name, "released OK"); } catch (e) { console.log(name, "released FAILED:", e.message); }
  };
  const cpuProbe = async () => {
    try {
      const { execSync } = await import("node:child_process");
      const out = execSync('powershell -NoProfile -Command "Get-Process msedge -ErrorAction SilentlyContinue | Where-Object {$_.MainWindowTitle -eq \\"\\"} | Sort-Object CPU -Descending | Select-Object -First 3 Id,CPU | Format-Table -HideTableHeaders"', { encoding: "utf8", timeout: 8000 });
      console.log("edge cpu:", out.trim().split(/\s+/).filter(Boolean).join(" "));
    } catch (e) { console.log("cpu probe failed", e.message); }
  };
  // 1) 已知正常按钮
  const addPos = await centerOf("#btnAddShot");
  if (addPos) { await clickAt("addShot", addPos); await sleep(500); console.log("after addShot:", JSON.stringify(await evalJs(`({ shotCount: document.querySelectorAll('#shotStrip > *').length })`))); }
  // 2) varyShots（press 后盲试 handleJavaScriptDialog）
  const v2 = await centerOf("#btnVaryShots");
  if (v2) {
    await clickAt("varyShots", v2);
    await cpuProbe();
    for (let i = 0; i < 3; i++) {
      try {
        await Promise.race([send("Page.handleJavaScriptDialog", { accept: false }), sleep(4000).then(() => { throw new Error("t"); })]);
        console.log("blind handleJavaScriptDialog OK");
        break;
      } catch (e) { console.log("blind handleJavaScriptDialog FAILED:", e.message); }
    }
    try { await Promise.race([send("Input.dispatchMouseEvent", { type: "mouseReleased", x: v2.x, y: v2.y, button: "left", clickCount: 1 }), sleep(4000).then(() => { throw new Error("t"); })]); console.log("late release OK"); } catch (e) { console.log("late release FAILED:", e.message); }
    try { const r = await Promise.race([evalJs(`({ shotCount: document.querySelectorAll('#shotStrip > *').length })`), sleep(5000).then(() => { throw new Error("eval timeout"); })]); console.log("after varyShots:", JSON.stringify(r)); } catch (e) { console.log("after varyShots eval FAILED:", e.message); }
  }
  // --- 对照实验：Tab 走查 + 输入框聚焦后，reload 是否导致 evaluate 挂起 ---
  console.log("== tab-then-reload test ==");
  for (let i = 0; i < 40; i++) {
    await send("Input.dispatchKeyEvent", { type: "keyDown", key: "Tab", code: "Tab", windowsVirtualKeyCode: 9 });
    await send("Input.dispatchKeyEvent", { type: "keyUp", key: "Tab", code: "Tab", windowsVirtualKeyCode: 9 });
  }
  const focusInfo = await evalJs(`({ tag: document.activeElement.tagName, id: document.activeElement.id || '' })`);
  console.log("after 40 tabs focus:", JSON.stringify(focusInfo));
  await send("Page.reload", {});
  await sleep(1500);
  try {
    const r = await Promise.race([evalJs(`1 + 1`), sleep(5000).then(() => { throw new Error("eval timeout"); })]);
    console.log("eval after tab-reload:", r);
  } catch (e) { console.log("eval after tab-reload FAILED:", e.message); }
  console.log("== reload test ==");
  await evalJs(`window.__m = 'A'`);
  const t = Date.now();
  try {
    await Promise.race([send("Page.reload", {}), sleep(5000).then(() => { throw new Error("reload cmd timeout"); })]);
    console.log("reload cmd OK", Date.now() - t);
  } catch (e) { console.log("reload cmd FAILED:", e.message); }
  await sleep(1500);
  try {
    const r = await Promise.race([evalJs(`window.__m`), sleep(5000).then(() => { throw new Error("eval timeout"); })]);
    console.log("eval after reload:", r, "(undefined = 页面已重载，上下文新)");
  } catch (e) { console.log("eval after reload FAILED:", e.message); }
  // --- query 参数强制导航测试 ---
  console.log("== query-nav test ==");
  try {
    await Promise.race([send("Page.navigate", { url: `${BASE}/#intro?reset=${Date.now()}` }), sleep(5000).then(() => { throw new Error("nav timeout"); })]);
    console.log("nav cmd OK");
  } catch (e) { console.log("nav cmd FAILED:", e.message); }
  await sleep(1500);
  try {
    const r = await Promise.race([evalJs(`({ shots: document.querySelectorAll('#shotStrip > *').length, href: location.href })`), sleep(5000).then(() => { throw new Error("eval timeout"); })]);
    console.log("eval after query-nav:", JSON.stringify(r));
  } catch (e) { console.log("eval after query-nav FAILED:", e.message); }
  process.exit(0);
}
main().catch((e) => { console.error("FATAL", e); process.exit(1); });
