/**
 * 形态 A 散文模板（对齐三 skill 交付金样）
 * —— 四段纯英文完整句：This is a… / Main subject: / Environmental background: / Composition and atmosphere:
 * 数据全部来自 DIRECTOR_CATALOG 的 en 碎片；中文（label/look）永不进入输出。
 * director.js 与 scripts/combo_prompts.py（Python 离线批量）共享本文件的版式铁律。
 */
window.PROSE_TEMPLATES = (() => {
  "use strict";

  /* ---------- 小工具 ---------- */
  const j = (a) => a.filter(Boolean).join(", ");
  const cap = (s) => (s ? s[0].toUpperCase() + s.slice(1) : "");
  const enOf = (o) => (o && o.en ? o.en : "");
  const toArr = (x) => (Array.isArray(x) ? x : x ? [x] : []);
  const ens = (x) => toArr(x).map(enOf).filter(Boolean);
  const first = (x) => {
    const a = toArr(x);
    return a.length ? a[0] : null;
  };
  const has = (x) => {
    const a = toArr(x);
    return a.length > 0 && a[0].id !== "none";
  };
  const A = (x) => (/^[aeiou]/i.test(x || "") ? "an " : "a ") + x;
  const list = (a) =>
    a.length > 1 ? a.slice(0, -1).join(", ") + " and " + a[a.length - 1] : a[0] || "";
  const tidy = (s) => (s || "").replace(/\s+/g, " ").trim();
  const period = (s) => {
    const t = tidy(s);
    if (!t) return "";
    return /[.!?]$/.test(t) ? t : t + ".";
  };

  /* ---------- 主体（SUBJECT 共享维度） ---------- */
  const ETH_NOUN = {
    eastasian: "East Asian",
    chinese: "East Asian Chinese",
    japanese: "Japanese",
    korean: "Korean",
    seasian: "Southeast Asian",
    southasian: "South Asian",
    central_asian: "Central Asian",
    white: "white",
    black: "Black",
    latina: "Latina",
  };
  const UNDERTONE = ["eastasian", "chinese", "japanese", "korean"];
  const ethNoun = (eth) =>
    (eth && ETH_NOUN[eth.id]) || tidy(enOf(eth).replace(/\s+adult features.*$/i, "")) || "adult";
  const cleanBody = (body) => tidy(enOf(body).replace(/\badult\b/gi, " "));
  const undertone = (eth) =>
    eth && UNDERTONE.includes(eth.id) ? "warm-neutral East Asian undertone, " : "";

  function identity(ctx, skin) {
    const parts = ["adult face and proportions"];
    if (cleanBody(ctx.body)) parts.push(cleanBody(ctx.body));
    parts.push((undertone(ctx.eth) + skin).trim());
    return `An adult ${ethNoun(ctx.eth)} woman ${enOf(ctx.age)}—${j(parts)}.`;
  }

  function camShot(cam) {
    const frags = ens(cam);
    const joined = j(frags) || "full body";
    const hasAngle = /eye-level|low angle|high angle|aerial|overhead|dutch/i.test(joined);
    return `${hasAngle ? "" : "eye-level "}${joined} vertical 3:4`;
  }

  function poseLead(pose) {
    const p = first(pose);
    if (!p) return "mid-stride";
    return tidy(enOf(p).replace(/\bfreeze(s|d|ing)?\b/gi, "")) || "mid-stride";
  }

  /* ---------- 三段共用句子装饰器 ---------- */
  function hairS(hair) {
    const h = ens(hair);
    if (!h.length) return "";
    return `Her ${list(h)}.`;
  }
  function poseS(pose) {
    const lead = poseLead(pose);
    const rest = ens(pose).slice(1);
    const tail = rest.length ? ", then " + j(rest) : "";
    return `She is frozen in ${lead}${tail}, weight readable through the frame; spine long, chin softly lifted.`;
  }
  function clothS(cloth) {
    const c = ens(cloth);
    if (!c.length) return "";
    return `She wears ${A(j(c))}, fabric drape readable.`;
  }
  function propS(prop) {
    const p0 = first(prop);
    if (!p0) return "";
    if (p0.id === "none") {
      const p = tidy(enOf(p0).replace(/^hands\s+/i, ""));
      return p ? `Her hands read relaxed—${p}.` : "";
    }
    return `In her hands, ${j(ens(prop))}.`;
  }
  function makeupS(makeup, expr) {
    const m = ens(makeup);
    const e = ens(expr);
    if (!m.length && !e.length) return "";
    const a = m.length ? `Her makeup reads ${j(m)}` : "";
    const b = e.length ? `her expression reads ${j(e)} toward the lens` : "";
    return `${a}${a && b ? "; " : ""}${b}.`;
  }
  function castS(cast) {
    const c = ens(cast);
    return c.length ? `${cap(j(c))}.` : "";
  }
  function lightS(light) {
    const l = ens(light);
    if (!l.length) return "soft key, gentle fill";
    const joined = j(l);
    const tail = /hair rim/i.test(joined) ? "gentle fill" : "gentle fill, thin hair rim";
    return `${joined}; ${tail}`;
  }
  function gradeS(grade) {
    const g = ens(grade);
    return g.length ? `finished in ${A(j(g))} grade; ` : "";
  }

  /* ---------- figure 六层 ---------- */
  function FIG(ctx) {
    const genre = tidy(enOf(ctx.zone).replace(/\s+zone$/i, "")) || "commercial fashion editorial";
    const combo = enOf(ctx.combo);
    const skin = "soft product-clean skin";

    const p1 =
      `This is ${camShot(ctx.cam)} editorial still with ${genre} photography: ` +
      `a photoreal adult ${ethNoun(ctx.eth)} woman frozen ${poseLead(ctx.pose)}, ` +
      `${skin}, garment lines fully readable toward the lens` +
      (combo ? `, the shot built around ${A(combo)}` : "") +
      ".";

    const main = [
      identity(ctx, skin),
      hairS(ctx.hair),
      poseS(ctx.pose),
      clothS(ctx.cloth),
      propS(ctx.prop),
      makeupS(ctx.makeup, ctx.expr),
      castS(ctx.cast),
      ctx.ex ? period(ctx.ex) : "",
    ].filter(Boolean);

    const p2 = "Main subject: " + main.join(" ") + " SFW, fully non-explicit.";
    const p3 =
      "Environmental background: " +
      `A setting of ${j(ens(ctx.set))}, with two to four readable anchors; no clutter competing with the figure.`;
    const p4 =
      "Composition and atmosphere: " +
      `She fills most of the vertical frame with thin margin; visual center on the posture line; ` +
      `${lightS(ctx.light)}; ${gradeS(ctx.grade)}` +
      `masterpiece, best quality, photoreal ${genre} still.`;

    return [p1, p2, p3, p4];
  }

  /* ---------- youth 七层（暗示焦点优先，勿露骨） ---------- */
  function YOU(ctx) {
    const combo = enOf(ctx.combo);
    const aes = ens(ctx.aes);
    const skin = "soft natural skin";

    const p1 =
      `This is ${camShot(ctx.cam)} cinematic still with intimate lifestyle photography: ` +
      `a photoreal adult ${ethNoun(ctx.eth)} woman frozen ${poseLead(ctx.pose)}, ` +
      `${skin}, the ${j(aes) || "quiet pure-desire"} mood` +
      (combo ? `, the shot built around ${A(combo)}` : "") +
      ".";

    const implyFrag = ens(ctx.imply);
    const focusFrag = ens(ctx.focus);
    const actFrag = ens(ctx.act);
    const inten = enOf(ctx.intensity);
    const implication = [
      focusFrag.length ? `The implication centers on ${j(focusFrag)}` : "",
      actFrag.length ? `within a ${j(actFrag)} beat` : "",
      inten ? `intensity stays ${inten}` : "",
      implyFrag.length ? `wardrobe state ${j(implyFrag)}` : "",
    ]
      .filter(Boolean)
      .join(", ") + ".";

    const main = [
      identity(ctx, skin),
      hairS(ctx.hair),
      poseS(ctx.pose),
      implication,
      clothS(ctx.cloth),
      propS(ctx.prop),
      makeupS(ctx.makeup, ctx.expr),
      castS(ctx.cast),
      ctx.ex ? period(ctx.ex) : "",
    ].filter(Boolean);

    const p2 =
      "Main subject: " + main.join(" ") +
      " Soft-sensual implied only; no genitals, no penetration, no explicit sex; adult 18+ solo.";
    const p3 =
      "Environmental background: " +
      `A setting of ${j(ens(ctx.set))}, with two to four readable anchors; no second person body.`;
    const p4 =
      "Composition and atmosphere: " +
      `visual center on the implication focus; ${lightS(ctx.light)}; ${gradeS(ctx.grade)}` +
      `quiet self-seduction tension; ` +
      `masterpiece, best quality, photoreal cinematic still.`;

    return [p1, p2, p3, p4];
  }

  /* ---------- erotic 七层（连接优先） ---------- */
  function ERO(ctx) {
    const combo = enOf(ctx.combo);
    const inten = enOf(ctx.intensity);
    const skin = "soft skin with honest texture";

    const p1 =
      `This is ${camShot(ctx.cam)} cinematic still with cinematic erotic photography: ` +
      `a photoreal adult ${ethNoun(ctx.eth)} woman frozen ${poseLead(ctx.pose)}, ` +
      `${skin}, the shot built around ${A(combo || "erotic beat")}, ${inten || "sensual"}.`;

    const actFrag = ens(ctx.act);
    const expo = enOf(ctx.exposure);
    const dyn = ens(ctx.dynamic);
    const fin = ens(ctx.finish);
    const fan = ens(ctx.fantasy);
    const bf = ens(ctx.bodyfocus);

    const actSentence = [
      actFrag.length ? `The act reads ${j(actFrag)}` : "",
      expo ? `exposure at ${expo}` : "",
      dyn.length ? `dynamic ${j(dyn)}` : "",
    ]
      .filter(Boolean)
      .join("; ") + ".";
    const finSentence = has(ctx.finish) ? `A ${j(fin)} finish reads at the junction.` : "";
    const fanSentence = has(ctx.fantasy) ? `Fantasy assist: ${j(fan)}.` : "";
    const focusSentence = bf.length ? `Visual weight stays on ${j(bf)}.` : "";

    const main = [
      identity(ctx, skin),
      hairS(ctx.hair),
      poseS(ctx.pose),
      actSentence,
      finSentence,
      fanSentence,
      "Arousal reads honest—soft flush, damp skin.",
      clothS(ctx.cloth),
      propS(ctx.prop),
      makeupS(ctx.makeup, ctx.expr),
      focusSentence,
      castS(ctx.cast),
      ctx.ex ? period(ctx.ex) : "",
    ].filter(Boolean);

    const p2 = "Main subject: " + main.join(" ") + " Adult 18+ only.";
    const p3 =
      "Environmental background: " +
      `A setting of ${j(ens(ctx.set))}, with two to four readable anchors; no clutter competing with the act.`;
    const p4 =
      "Composition and atmosphere: " +
      `visual center on the act-readable anatomy; ${lightS(ctx.light)}; ${gradeS(ctx.grade)}` +
      `intimate still; masterpiece, best quality.`;

    return [p1, p2, p3, p4];
  }

  /* ---------- 对外 ---------- */
  function build(mode, ctx) {
    const paras = mode === "figure" ? FIG(ctx) : mode === "youth" ? YOU(ctx) : ERO(ctx);
    const en = paras.join("\n\n");
    return { en, words: en.trim().split(/\s+/).filter(Boolean).length };
  }

  return { build };
})();
