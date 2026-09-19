/**
 * 站级 lightbox：组合实例大图 + 元信息 + 三个复制操作（英文提示词 / /skill 命令 / 组合 ID）。
 * 原生 <dialog>（无则退化为 div 覆盖层）：ESC/遮罩关闭、←/→ 切换、打开前焦点还原、复制按钮反馈。
 * 样式见 styles.css 的 .lb-* 段。
 */
window.Lightbox = (() => {
  "use strict";

  const CMD = {
    figure: "/figure-photo-prompt",
    youth: "/youth-seduction-prompt",
    erotic: "/erotic-prompt",
  };
  const BTN_LABEL = { prompt: "复制英文提示词", cmd: "复制 /skill 命令", id: "复制组合 ID" };

  let items = [];
  let cur = 0;
  let opener = null;
  let root = null;
  const els = {};
  let nativeDialog = typeof HTMLDialogElement !== "undefined";

  function buildRoot() {
    root = document.createElement(nativeDialog ? "dialog" : "div");
    root.className = "lb";
    root.setAttribute("role", nativeDialog ? undefined : "dialog");
    root.setAttribute("aria-modal", nativeDialog ? undefined : "true");
    root.setAttribute("aria-label", "组合实例大图");
    root.innerHTML =
      '<div class="lb-body">' +
      '<button type="button" class="lb-close" aria-label="关闭大图">×</button>' +
      '<button type="button" class="lb-nav lb-prev" aria-label="上一条">‹</button>' +
      '<div class="lb-media"><img class="lb-img" alt="" /></div>' +
      '<div class="lb-side">' +
      '<h3 class="lb-label"></h3>' +
      '<p class="lb-id"></p>' +
      '<p class="lb-group"></p>' +
      '<p class="lb-look"></p>' +
      '<div class="lb-actions">' +
      '<button type="button" class="lb-btn primary" data-lb="prompt">复制英文提示词</button>' +
      '<button type="button" class="lb-btn" data-lb="cmd">复制 /skill 命令</button>' +
      '<button type="button" class="lb-btn" data-lb="id">复制组合 ID</button>' +
      "</div>" +
      "</div>" +
      '<button type="button" class="lb-nav lb-next" aria-label="下一条">›</button>' +
      "</div>";
    document.body.appendChild(root);
    els.label = root.querySelector(".lb-label");
    els.id = root.querySelector(".lb-id");
    els.group = root.querySelector(".lb-group");
    els.look = root.querySelector(".lb-look");
    els.img = root.querySelector(".lb-img");
    els.prompt = root.querySelector('[data-lb="prompt"]');
    els.cmd = root.querySelector('[data-lb="cmd"]');
    els.idBtn = root.querySelector('[data-lb="id"]');
    els.prev = root.querySelector(".lb-prev");
    els.next = root.querySelector(".lb-next");

    root.addEventListener("cancel", (e) => {
      e.preventDefault();
      close();
    });
    root.addEventListener("click", (e) => {
      if (e.target === root) close();
      const btn = e.target.closest("[data-lb]");
      if (btn) copyBtn(btn.dataset.lb, btn);
    });
    root.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        prev();
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        next();
      }
    });
    root.querySelector(".lb-close").addEventListener("click", close);
    els.prev.addEventListener("click", prev);
    els.next.addEventListener("click", next);
  }

  function render() {
    const it = items[cur];
    if (!it) return;
    els.label.textContent = it.label || "";
    els.id.textContent = it.id || "";
    els.group.textContent = it.group || "";
    els.look.textContent = it.look || "";
    els.img.src = it.img || "";
    els.img.alt = it.label || "";
    els.prompt.hidden = !it.prompt;
    els.cmd.hidden = !it.prompt;
    els.prev.hidden = items.length <= 1;
    els.next.hidden = items.length <= 1;
  }

  function textOf(kind) {
    const it = items[cur] || {};
    if (kind === "prompt") return it.prompt || "";
    if (kind === "cmd") return `${CMD[it.skill] || ""}\n\n${it.prompt || ""}`.trim();
    return it.id || "";
  }

  async function copyBtn(kind, btn) {
    const text = textOf(kind);
    if (!text) return;
    const old = btn.textContent;
    try {
      await navigator.clipboard.writeText(text);
      btn.textContent = "已复制";
      btn.classList.add("ok");
    } catch {
      btn.textContent = "复制失败";
    }
    setTimeout(() => {
      btn.textContent = old;
      btn.classList.remove("ok");
    }, 1200);
  }

  function open(list, index) {
    if (!list || !list.length) return;
    if (!root) buildRoot();
    items = list;
    cur = Math.min(Math.max(index || 0, 0), items.length - 1);
    render();
    opener = document.activeElement;
    if (nativeDialog && root.showModal) {
      root.showModal();
    } else {
      root.classList.add("open");
    }
    const closeBtn = root.querySelector(".lb-close");
    if (closeBtn) closeBtn.focus();
  }

  function close() {
    if (!root) return;
    if (nativeDialog && root.close) root.close();
    else root.classList.remove("open");
    if (opener && opener.focus) opener.focus();
    opener = null;
  }

  function prev() {
    if (items.length <= 1) return;
    cur = (cur - 1 + items.length) % items.length;
    render();
  }

  function next() {
    if (items.length <= 1) return;
    cur = (cur + 1) % items.length;
    render();
  }

  function isOpen() {
    return !!root && (root.open || root.classList.contains("open"));
  }

  return { open, close, prev, next, isOpen };
})();
