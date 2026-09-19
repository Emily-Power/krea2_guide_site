(() => {
  const body = document.body;
  const menuBtn = document.getElementById("menuBtn");
  const backdrop = document.getElementById("backdrop");

  function closeNav() {
    body.classList.remove("nav-open");
  }
  function toggleNav() {
    body.classList.toggle("nav-open");
  }
  if (menuBtn) menuBtn.addEventListener("click", toggleNav);
  if (backdrop) backdrop.addEventListener("click", closeNav);

  /* ---------- 图片兜底：assets/images/ 不随仓库分发，缺图时用占位图顶住版式 ---------- */
  // 占位图是内联 SVG（3:4，与站内人像比例一致，配色取自 :root 的 --card/--elev/--dim）。
  // 自己画满整张画布，因此不需要配套 CSS；有图时本段完全不介入，视觉零变化。
  const IMG_PLACEHOLDER = (() => {
    const svg =
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1600">' +
      '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">' +
      '<stop offset="0" stop-color="#181e2a"/><stop offset="1" stop-color="#12161f"/>' +
      "</linearGradient></defs>" +
      '<rect width="1200" height="1600" fill="url(#g)"/>' +
      '<rect x="400" y="650" width="400" height="300" rx="28" fill="none" stroke="#7c879c" stroke-width="14"/>' +
      '<circle cx="490" cy="730" r="30" fill="#7c879c"/>' +
      '<path d="M430 900 L560 780 L650 860 L720 790 L770 900 Z" fill="#7c879c"/>' +
      "</svg>";
    return "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
  })();

  let imgMissingCount = 0;
  function fallbackImage(img) {
    if (!img.dataset.imgFallback) {
      img.dataset.imgFallback = "1";
      imgMissingCount += 1;
    }
    // 元素自带 width/height 属性时沿用它声明的比例（如首页头图 1200×400），
    // 避免统一 3:4 占位把这类横幅撑高；没有属性则吃占位图自身的 3:4。
    const w = Number(img.getAttribute("width"));
    const h = Number(img.getAttribute("height"));
    if (w > 0 && h > 0) img.style.aspectRatio = `${w} / ${h}`;
    img.src = IMG_PLACEHOLDER;
  }
  // error 事件不冒泡，但捕获阶段能听到；覆盖 index.html 静态图与 JS 动态插入的图
  document.addEventListener(
    "error",
    (e) => {
      if (e.target instanceof HTMLImageElement) fallbackImage(e.target);
    },
    true
  );
  // app.js 执行前就已失败的图不会重放 error，这里补扫一次（含后续 lightbox 换图）
  function sweepMissingImages() {
    document.querySelectorAll("img").forEach((img) => {
      if (img.complete && img.naturalWidth === 0) fallbackImage(img);
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", sweepMissingImages);
  } else {
    sweepMissingImages();
  }
  window.addEventListener("load", () => {
    sweepMissingImages();
    if (imgMissingCount) {
      console.info(
        `[krea2-guide] ${imgMissingCount} 张示例图缺失：assets/images/ 不随仓库分发，` +
          "生成或替换方式见 README「图片资源」一节。"
      );
    }
  });

  /* ---------- Skill shell: 栏内 Tab 切换（同一栏目，不竖向平铺） ---------- */
  function activateSkillTab(shell, panelId, pushHash) {
    if (!shell) return;
    const tabs = shell.querySelectorAll(".skill-tab");
    const panels = shell.querySelectorAll(".skill-panel");
    tabs.forEach((t) => t.classList.toggle("active", t.dataset.skillTab === panelId));
    panels.forEach((p) => p.classList.toggle("active", p.dataset.skillPanel === panelId));
    if (pushHash) {
      const skill = shell.dataset.skillShell;
      history.replaceState(null, "", `#${shell.id}?tab=${panelId}`);
    }
    // lazy render combo galleries inside newly shown panel
    shell.querySelectorAll(".combo-gallery-embed").forEach(initComboGallery);
  }

  document.querySelectorAll("[data-skill-shell]").forEach((shell) => {
    shell.querySelectorAll(".skill-tab").forEach((btn) => {
      btn.addEventListener("click", () => {
        activateSkillTab(shell, btn.dataset.skillTab, true);
      });
    });
  });

  /* ---------- Sidebar / hash navigation ---------- */
  function showPageFromHash() {
    const raw = location.hash.replace(/^#/, "") || "intro";
    const [id, qs] = raw.split("?");
    const params = new URLSearchParams(qs || "");
    const tab = params.get("tab");

    // skill shell
    const shell = document.getElementById(id);
    if (shell?.classList.contains("skill-shell")) {
      shell.scrollIntoView({ behavior: "smooth", block: "start" });
      const firstTab = shell.querySelector(".skill-tab")?.dataset.skillTab;
      activateSkillTab(shell, tab || firstTab, false);
    } else {
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    // nav active
    document.querySelectorAll(".sidebar a[href^='#']").forEach((link) => {
      const href = (link.getAttribute("href") || "").replace(/^#/, "").split("?")[0];
      link.classList.toggle("active", href === id);
    });
  }

  document.querySelectorAll(".sidebar a").forEach((a) => {
    a.addEventListener("click", (e) => {
      closeNav();
      const href = a.getAttribute("href") || "";
      if (href.startsWith("#")) {
        // allow default hash then handle
        setTimeout(showPageFromHash, 0);
      }
    });
  });

  window.addEventListener("hashchange", showPageFromHash);

  // scroll spy only for top-level non-shell sections when no skill hash
  const pageSections = [
    ...document.querySelectorAll(
      "main > section[id]:not(.skill-shell), main > header.hero[id], #combo-gallery"
    ),
  ];
  const navLinks = [...document.querySelectorAll(".sidebar a[href^='#']")];

  function setActiveScroll() {
    if (location.hash && location.hash.includes("skill-")) return;
    let current = pageSections[0]?.id;
    const y = window.scrollY + 120;
    for (const s of pageSections) {
      if (s.offsetTop <= y) current = s.id;
    }
    navLinks.forEach((link) => {
      const href = (link.getAttribute("href") || "").replace(/^#/, "").split("?")[0];
      if (href.startsWith("skill-")) return;
      link.classList.toggle("active", href === current);
    });
  }
  window.addEventListener("scroll", setActiveScroll, { passive: true });

  /* ---------- Generic data-tabs (legacy) ---------- */
  document.querySelectorAll("[data-tabs]").forEach((root) => {
    const buttons = root.querySelectorAll(".tab-btn");
    const panels = root.querySelectorAll(".tab-panel");
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const id = btn.dataset.tab;
        buttons.forEach((b) => b.classList.toggle("active", b === btn));
        panels.forEach((p) => p.classList.toggle("active", p.id === id));
      });
    });
  });

  /* ---------- Copy buttons ---------- */
  document.querySelectorAll(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const pre = btn.closest(".example")?.querySelector("pre");
      if (!pre) return;
      try {
        await navigator.clipboard.writeText(pre.textContent || "");
        const old = btn.textContent;
        btn.textContent = "已复制";
        setTimeout(() => {
          btn.textContent = old;
        }, 1200);
      } catch {
        btn.textContent = "失败";
      }
    });
  });

  /* ---------- Router demo ---------- */
  const result = document.getElementById("routerResult");
  document.querySelectorAll("[data-route]").forEach((btn) => {
    btn.addEventListener("click", () => {
      if (!result) return;
      const type = btn.dataset.route;
      const title = btn.dataset.title || "";
      const detail = btn.dataset.detail || "";
      result.className = "router-result show " + type;
      result.innerHTML = `<strong>${title}</strong><p style="margin:0.4rem 0 0;color:inherit;opacity:0.9">${detail}</p>`;
    });
  });

  /* ---------- Combo gallery (全量组合实例图) ---------- */
  const GALLERY = window.COMBO_GALLERY;
  const galleryInited = new WeakSet();

  function escapeHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function itemsForSkill(skill) {
    if (!GALLERY?.items) return [];
    if (!skill || skill === "all") return GALLERY.items;
    return GALLERY.items.filter((x) => x.skill === skill);
  }

  function initComboGallery(root) {
    if (!root || galleryInited.has(root) || !GALLERY?.items) return;
    // allow re-init when skill changes on main gallery
    if (root.dataset.cgBound === "1" && root.dataset.cgReady) {
      // only re-filter
    } else {
      galleryInited.add(root);
      root.dataset.cgReady = "1";
    }

    const skill = root.dataset.comboGallery || "figure";
    const search = root.querySelector(".cg-search");
    const groupSel = root.querySelector(".cg-group");
    const grid = root.querySelector(".cg-grid");
    const countEl = root.querySelector(".cg-count");
    if (!grid) return;

    function currentSkill() {
      return root.dataset.comboGallery || skill;
    }

    function rebuildGroups() {
      if (!groupSel) return;
      const items = itemsForSkill(currentSkill());
      const groups = [...new Set(items.map((i) => i.group).filter(Boolean))].sort();
      const cur = groupSel.value || "all";
      groupSel.innerHTML =
        `<option value="all">全部分组</option>` +
        groups.map((g) => `<option value="${escapeHtml(g)}">${escapeHtml(g)}</option>`).join("");
      if ([...groupSel.options].some((o) => o.value === cur)) groupSel.value = cur;
    }

    function render() {
      const sk = currentSkill();
      let list = itemsForSkill(sk);
      const q = (search?.value || "").trim().toLowerCase();
      const g = groupSel?.value || "all";
      if (g !== "all") list = list.filter((i) => i.group === g);
      if (q) {
        list = list.filter(
          (i) =>
            i.id.toLowerCase().includes(q) ||
            (i.label || "").toLowerCase().includes(q) ||
            (i.look || "").toLowerCase().includes(q) ||
            (i.group || "").toLowerCase().includes(q)
        );
      }
      if (countEl) countEl.textContent = `${list.length} / ${itemsForSkill(sk).length} 个组合`;
      grid._lbList = list;
      grid.innerHTML = list
        .map(
          (i, idx) => `
        <button type="button" class="cg-card" data-idx="${idx}" data-combo-id="${escapeHtml(i.id)}" title="查看大图与提示词">
          <span class="cg-thumb"><img src="${escapeHtml(i.img)}" alt="" loading="lazy" /></span>
          <span class="cg-meta">
            <span class="cg-label">${escapeHtml(i.label)}</span>
            <span class="cg-id">${escapeHtml(i.id)}</span>
            <span class="cg-group-tag">${escapeHtml(i.group || "")}</span>
          </span>
        </button>`
        )
        .join("");
    }

    // 事件委托：点击卡片 → lightbox（大图 + 复制提示词/命令/ID）
    grid.addEventListener("click", (e) => {
      const card = e.target.closest(".cg-card");
      if (!card || !grid._lbList) return;
      const idx = Number(card.dataset.idx) || 0;
      const list = grid._lbList.map((i) => ({
        img: i.img,
        label: i.label,
        id: i.id,
        group: i.group,
        skill: i.skill,
        look: i.look || "",
        prompt: i.prompt || "",
      }));
      window.Lightbox?.open(list, idx);
    });

    rebuildGroups();
    render();
    search?.addEventListener("input", render);
    groupSel?.addEventListener("change", render);

    // expose refresh when skill changes
    root._cgRefresh = () => {
      rebuildGroups();
      render();
    };
  }

  // Main combo gallery skill switch
  document.querySelectorAll(".cg-skill-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".cg-skill-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const sk = btn.dataset.cgSkill;
      const main = document.querySelector("[data-cg-main]");
      if (main) {
        main.dataset.comboGallery = sk;
        if (main._cgRefresh) main._cgRefresh();
        else initComboGallery(main);
      }
    });
  });

  // Init all embeds on load
  document.querySelectorAll(".combo-gallery-embed").forEach(initComboGallery);

  // Initial hash
  if (location.hash) showPageFromHash();
  else setActiveScroll();
})();
