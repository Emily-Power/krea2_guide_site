# -*- coding: utf-8 -*-
"""Patch director.js for youth-seduction mode. Idempotent."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JS = ROOT / "assets" / "director.js"
FIELDS = Path(__file__).with_name("_youth_fields.inc.js").read_text(encoding="utf-8").rstrip() + "\n"
PRESETS = Path(__file__).with_name("_youth_presets.inc.js").read_text(encoding="utf-8").rstrip() + "\n"


def main() -> int:
    text = JS.read_text(encoding="utf-8")
    if "FIELD_GROUPS_YOUTH" in text and "PRESETS_YOUTH" in text and 'mode === "youth"' in text:
        print("[skip] already patched")
        return 0

    text = text.replace(
        "   * 对齐最新 figure / erotic skill：六层/七层结构、目标篇幅、连接优先",
        "   * 对齐 figure / youth-seduction / erotic：六/七层、暗示焦点、连接优先",
    )
    text = text.replace(
        "  const { FIGURE, EROTIC, SUBJECT } = CAT;",
        "  const { FIGURE, EROTIC, YOUTH, SUBJECT } = CAT;",
    )

    marker = "  ];\n\n  /** 一键预设：整套 picks + extra，缺省字段用 defaults 补全 */"
    if marker not in text:
        raise SystemExit("field-groups marker not found")
    text = text.replace(
        marker,
        "  ];\n\n" + FIELDS + "\n  /** 一键预设：整套 picks + extra，缺省字段用 defaults 补全 */",
        1,
    )

    state_marker = "  const state = {"
    if state_marker not in text:
        raise SystemExit("state marker not found")
    text = text.replace(state_marker, PRESETS + "\n  const state = {", 1)

    old_cat = (
        '  function catalog() {\n'
        '    return state.mode === "figure" ? FIGURE : EROTIC;\n'
        "  }\n\n"
        "  function presetsForMode() {\n"
        '    return state.mode === "figure" ? PRESETS_FIGURE : PRESETS_EROTIC;\n'
        "  }"
    )
    new_cat = (
        "  function catalog() {\n"
        '    if (state.mode === "figure") return FIGURE;\n'
        '    if (state.mode === "youth") return YOUTH || {};\n'
        "    return EROTIC;\n"
        "  }\n\n"
        "  function presetsForMode() {\n"
        '    if (state.mode === "figure") return PRESETS_FIGURE;\n'
        '    if (state.mode === "youth") return PRESETS_YOUTH;\n'
        "    return PRESETS_EROTIC;\n"
        "  }"
    )
    if old_cat not in text:
        raise SystemExit("catalog block not found")
    text = text.replace(old_cat, new_cat, 1)

    text = text.replace(
        'state.mode === "figure" ? "Figure SFW · 点一下套完整参数" : "Erotic 18+ · 点一下套完整参数"',
        'state.mode === "figure" ? "Figure SFW · 点一下套完整参数" : state.mode === "youth" ? "Youth 纯欲暗示 · 点一下套完整参数" : "Erotic 18+ · 点一下套完整参数"',
    )

    # defaultsPicks: insert youth before erotic return
    needle = "    }\n    return {\n      eth: \"eastasian\",\n      age: \"e20\",\n      hair: \"messy\","
    youth_def = (
        "    }\n"
        '    if (mode === "youth") {\n'
        "      return {\n"
        '        eth: "eastasian",\n'
        '        age: "e20",\n'
        '        hair: "longblack",\n'
        '        body: "slim",\n'
        '        combo: "combo-window-lace",\n'
        '        intensity: "pure-desire",\n'
        '        act: "window-risk",\n'
        '        imply: "i1",\n'
        '        pose: "look-back",\n'
        '        cloth: "oversized-shirt",\n'
        '        set: "window-city",\n'
        '        light: "sheer-backlight",\n'
        '        cam: "full-v",\n'
        '        focus: "collarbone",\n'
        '        expr: "half-lidded",\n'
        '        aes: "chunyu",\n'
        "      };\n"
        "    }\n"
        "    return {\n"
        '      eth: "eastasian",\n'
        '      age: "e20",\n'
        '      hair: "messy",'
    )
    if needle not in text:
        raise SystemExit("defaultsPicks needle not found")
    text = text.replace(needle, youth_def, 1)

    # buildPromptFrom youth branch
    insert_at = '    const combo = findOpt(EROTIC.combo, picks.combo);'
    youth_build = r'''    if (mode === "youth") {
      const cat = YOUTH || {};
      const combo = findOpt(cat.combo, picks.combo);
      const intensity = findOpt(cat.intensity, picks.intensity);
      const act = findOpt(cat.act, picks.act);
      const imply = findOpt(cat.imply, picks.imply);
      const pose = findOpt(cat.pose, picks.pose);
      const cloth = findOpt(cat.cloth, picks.cloth);
      const set = findOpt(cat.set, picks.set);
      const light = findOpt(cat.light, picks.light);
      const cam = findOpt(cat.cam, picks.cam);
      const focus = findOpt(cat.focus, picks.focus);
      const expr = findOpt(cat.expr, picks.expr);
      const aes = findOpt(cat.aes, picks.aes);
      const shot = `This is a ${cam.en} with intimate cinematic still photography, freezing one solitary pure-desire moment (${combo.label}; ${aes.en}).`;
      const main = `Main subject: ${idLine}. She ${pose.en}. Implication focus: ${focus.en}. Act: ${act.en}. Intensity: ${intensity.en}. Clothing state: ${cloth.en} (${imply.en}). Expression: ${expr.en}.${ex ? " " + ex : ""} Soft-sensual implied only; no genitals, no penetration, no explicit sex; adult 18+ solo.`;
      const env = `Environmental background: ${set.en}; only 2–4 anchors; no second person body.`;
      const comp = `Composition and atmosphere: visual center on ${focus.en}; ${light.en}; quiet self-seduction tension; warm-neutral East Asian undertone; masterpiece, best quality.`;
      const en = [shot, main, env, comp].join("\n\n");
      return {
        en,
        words: countWords(en),
        zh: {
          skill: "youth-seduction · 纯欲暗示",
          pack: `${combo.label} · ${intensity.label} · ${aes.label}`,
          pose: `${pose.label} · ${act.label}`,
          cloth: `${cloth.label} · ${imply.label}`,
          set: set.label,
          light: light.label,
          cam: cam.label,
          note: `${focus.label} · ${expr.label} · 七层暗示 · 目标约160–320词`,
        },
        chips: [combo.label, intensity.label, pose.label, imply.label, focus.label, set.label],
        short: `${combo.label} · ${pose.label}`,
      };
    }

    ''' + insert_at
    if insert_at not in text:
        raise SystemExit("erotic insert not found")
    text = text.replace(insert_at, youth_build, 1)

    # buildCmd replace whole function
    start = text.find("  function buildCmd()")
    end = text.find("  /* ---------- combo picker ---------- */")
    if start < 0 or end < 0:
        raise SystemExit("buildCmd range not found")
    new_cmd = """  function buildCmd() {
    const b = buildCurrent();
    const cmd =
      state.mode === "figure"
        ? "/figure-photo-prompt"
        : state.mode === "youth"
          ? "/youth-seduction-prompt"
          : "/erotic-prompt";
    const layerHint =
      state.mode === "figure"
        ? "六层姿态优先"
        : state.mode === "youth"
          ? "七层暗示焦点优先（勿写露骨）"
          : "七层连接优先";
    return `${cmd}\\n\\n${b.en}\\n\\n---\\n请按 skill ${layerHint}与篇幅目标润色为可交付形态 A（完整句、单帧、默认东亚成人）。`;
  }

"""
    # Fix double-escaped newlines for template literal - match original style
    new_cmd = (
        "  function buildCmd() {\n"
        "    const b = buildCurrent();\n"
        "    const cmd =\n"
        '      state.mode === "figure"\n'
        '        ? "/figure-photo-prompt"\n'
        '        : state.mode === "youth"\n'
        '          ? "/youth-seduction-prompt"\n'
        '          : "/erotic-prompt";\n'
        "    const layerHint =\n"
        '      state.mode === "figure"\n'
        '        ? "六层姿态优先"\n'
        '        : state.mode === "youth"\n'
        '          ? "七层暗示焦点优先（勿写露骨）"\n'
        '          : "七层连接优先";\n'
        "    return `${cmd}\\n\\n${b.en}\\n\\n---\\n请按 skill ${layerHint}与篇幅目标润色为可交付形态 A（完整句、单帧、默认东亚成人）。`;\n"
        "  }\n\n"
    )
    # In JS source file the original uses real \n in template - check original
    snippet = text[start:start + 200]
    # Use same escape style as existing file
    if "`${cmd}\\n\\n${b.en}" in text[start:end] or "${cmd}\\n\\n" in text[start:end]:
        pass
    # Prefer copying style from original line
    orig = text[start:end]
    if r"\n\n" in orig:
        # file stores backslash-n
        pass
    text = text[:start] + new_cmd + text[end:]

    text = text.replace(
        '    return state.mode === "figure" ? FIELD_GROUPS_FIGURE : FIELD_GROUPS_EROTIC;',
        '    if (state.mode === "figure") return FIELD_GROUPS_FIGURE;\n'
        '    if (state.mode === "youth") return FIELD_GROUPS_YOUTH;\n'
        "    return FIELD_GROUPS_EROTIC;",
    )

    text = text.replace(
        'const max = state.mode === "figure" ? 350 : 360;',
        'const max = state.mode === "erotic" ? 360 : 350;',
    )
    text = text.replace(
        'state.mode === "figure" ? "160–320" : "170–330"',
        'state.mode === "erotic" ? "170–330" : "160–320"',
    )

    old_rand = (
        '    if (state.mode === "figure") {\n'
        "      state.picks.zone = pick(FIGURE.zone);\n"
        "      state.picks.pose = pick(FIGURE.pose);\n"
        "      state.picks.cloth = pick(FIGURE.cloth);\n"
        "      state.picks.prop = pick(FIGURE.prop);\n"
        "      state.picks.set = pick(FIGURE.set);\n"
        "      state.picks.light = pick(FIGURE.light);\n"
        "      state.picks.cam = pick(FIGURE.cam);\n"
        "      state.picks.makeup = pick(FIGURE.makeup);\n"
        "      state.picks.expr = pick(FIGURE.expr);\n"
        "      state.picks.grade = pick(FIGURE.grade);\n"
        "    } else {\n"
        "      state.picks.intensity = pick(EROTIC.intensity);\n"
        "      state.picks.act = pick(EROTIC.act);\n"
        "      state.picks.finish = pick(EROTIC.finish);\n"
        "      state.picks.dynamic = pick(EROTIC.dynamic);\n"
        "      state.picks.pose = pick(EROTIC.pose);\n"
        "      state.picks.cloth = pick(EROTIC.cloth);\n"
        "      state.picks.set = pick(EROTIC.set);\n"
        "      state.picks.light = pick(EROTIC.light);\n"
        "      state.picks.fantasy = pick(EROTIC.fantasy);\n"
        "      state.picks.cam = pick(EROTIC.cam);\n"
        "      state.picks.expr = pick(EROTIC.expr);\n"
        "      state.picks.bodyfocus = pick(EROTIC.bodyfocus);\n"
        "    }"
    )
    new_rand = (
        '    if (state.mode === "figure") {\n'
        "      state.picks.zone = pick(FIGURE.zone);\n"
        "      state.picks.pose = pick(FIGURE.pose);\n"
        "      state.picks.cloth = pick(FIGURE.cloth);\n"
        "      state.picks.prop = pick(FIGURE.prop);\n"
        "      state.picks.set = pick(FIGURE.set);\n"
        "      state.picks.light = pick(FIGURE.light);\n"
        "      state.picks.cam = pick(FIGURE.cam);\n"
        "      state.picks.makeup = pick(FIGURE.makeup);\n"
        "      state.picks.expr = pick(FIGURE.expr);\n"
        "      state.picks.grade = pick(FIGURE.grade);\n"
        '    } else if (state.mode === "youth") {\n'
        "      const Y = YOUTH || {};\n"
        "      state.picks.intensity = pick(Y.intensity);\n"
        "      state.picks.act = pick(Y.act);\n"
        "      state.picks.imply = pick(Y.imply);\n"
        "      state.picks.pose = pick(Y.pose);\n"
        "      state.picks.cloth = pick(Y.cloth);\n"
        "      state.picks.set = pick(Y.set);\n"
        "      state.picks.light = pick(Y.light);\n"
        "      state.picks.cam = pick(Y.cam);\n"
        "      state.picks.focus = pick(Y.focus);\n"
        "      state.picks.expr = pick(Y.expr);\n"
        "      state.picks.aes = pick(Y.aes);\n"
        "    } else {\n"
        "      state.picks.intensity = pick(EROTIC.intensity);\n"
        "      state.picks.act = pick(EROTIC.act);\n"
        "      state.picks.finish = pick(EROTIC.finish);\n"
        "      state.picks.dynamic = pick(EROTIC.dynamic);\n"
        "      state.picks.pose = pick(EROTIC.pose);\n"
        "      state.picks.cloth = pick(EROTIC.cloth);\n"
        "      state.picks.set = pick(EROTIC.set);\n"
        "      state.picks.light = pick(EROTIC.light);\n"
        "      state.picks.fantasy = pick(EROTIC.fantasy);\n"
        "      state.picks.cam = pick(EROTIC.cam);\n"
        "      state.picks.expr = pick(EROTIC.expr);\n"
        "      state.picks.bodyfocus = pick(EROTIC.bodyfocus);\n"
        "    }"
    )
    if old_rand not in text:
        raise SystemExit("randomize block not found")
    text = text.replace(old_rand, new_rand, 1)

    old_mode = (
        "  function applyModeClass() {\n"
        '    const root = $("#directorRoot");\n'
        '    root?.classList.toggle("mode-nsfw", state.mode === "erotic");\n'
        '    root?.classList.toggle("mode-sfw", state.mode === "figure");\n'
        '    $$(".skill-switch button").forEach((b) => {\n'
        '      b.classList.remove("active-sfw", "active-nsfw");\n'
        '      if (b.dataset.mode === "figure" && state.mode === "figure") b.classList.add("active-sfw");\n'
        '      if (b.dataset.mode === "erotic" && state.mode === "erotic") b.classList.add("active-nsfw");\n'
        "    });\n"
        '    const tip = $("#modeTip");\n'
        "    if (tip) {\n"
        "      tip.textContent =\n"
        '        state.mode === "figure"\n'
        '          ? "SFW · 姿态优先 · 全文目标约 160–320 词 · 禁默认私房"\n'
        '          : "NSFW 18+ · 连接优先 · 全文目标约 170–330 词 · 默认自展 E1/E2";\n'
        "    }\n"
        "  }"
    )
    new_mode = (
        "  function applyModeClass() {\n"
        '    const root = $("#directorRoot");\n'
        '    root?.classList.toggle("mode-nsfw", state.mode === "erotic");\n'
        '    root?.classList.toggle("mode-sfw", state.mode === "figure");\n'
        '    root?.classList.toggle("mode-youth", state.mode === "youth");\n'
        '    $$(".skill-switch button").forEach((b) => {\n'
        '      b.classList.remove("active-sfw", "active-nsfw", "active-youth");\n'
        '      if (b.dataset.mode === "figure" && state.mode === "figure") b.classList.add("active-sfw");\n'
        '      if (b.dataset.mode === "youth" && state.mode === "youth") b.classList.add("active-youth");\n'
        '      if (b.dataset.mode === "erotic" && state.mode === "erotic") b.classList.add("active-nsfw");\n'
        "    });\n"
        '    const tip = $("#modeTip");\n'
        "    if (tip) {\n"
        "      tip.textContent =\n"
        '        state.mode === "figure"\n'
        '          ? "SFW · 姿态优先 · 全文目标约 160–320 词 · 禁默认私房"\n'
        '          : state.mode === "youth"\n'
        '            ? "纯欲暗示 · 姿态+暗示焦点优先 · 全文约 160–320 词 · 禁止露骨 · I3 须点名"\n'
        '            : "NSFW 18+ · 连接优先 · 全文目标约 170–330 词 · 默认自展 E1/E2";\n'
        "    }\n"
        "  }"
    )
    if old_mode not in text:
        raise SystemExit("applyModeClass not found")
    text = text.replace(old_mode, new_mode, 1)

    text = text.replace(
        "openGroups: { subject: true, zone: true, scale: true },",
        "openGroups: { subject: true, zone: true, scale: true, posecloth: true },",
    )

    JS.write_text(text, encoding="utf-8")
    print("[ok] patched", JS)
    print("  FIELD_GROUPS_YOUTH", "FIELD_GROUPS_YOUTH" in text)
    print("  PRESETS_YOUTH", "PRESETS_YOUTH" in text)
    print("  youth refs", text.count("youth"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
