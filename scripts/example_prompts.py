# -*- coding: utf-8 -*-
"""
教学站 index.html 硬编码示例图/卡片图/头图的重出提示词（2026-09-08 对齐锚生态铁律）。

- 文件名不变（index.html 硬编码引用），图直接写 assets/images/<filename>
- 出图走 scripts/templates/krea2-image-api.json（Moody-Krea-Mix 蒸馏，不挂 LoRA）
- 四段式与 combo_prompts.py 同版式；figure=SFW 完整着装、youth=暗示非露骨、
  erotic=氛围记忆（非露骨连接示范，最多半褪/剪影/静物）
- 用法：python scripts/example_prompts.py [--limit N] [--only 文件名...]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "images"
TEMPLATE = ROOT / "scripts" / "templates" / "krea2-image-api.json"

SKILL_DIR = Path(
    os.environ.get("DIRECTOR_PRODUCE_PATH")
    or (Path.home() / ".claude" / "skills" / "director-produce")
)
sys.path.insert(0, str(SKILL_DIR / "scripts"))
import comfy_api as C  # noqa: E402

from PIL import Image  # noqa: E402

LOCK = {
    "figure": ("An adult East Asian woman of twenty-two, one hundred fifty-eight centimeters, "
               "petite adult frame, slim waist, dancer hips under clothing, warm-neutral East Asian undertone, "
               "no glasses. Dark brown center-part hair. Soft natural lip. Adult face fully readable. "
               "Same heroine identity. She is fully dressed."),
    "youth": ("An adult East Asian woman of twenty-two, petite adult frame, warm-neutral East Asian undertone, "
              "no glasses. Dark brown center-part hair. Soft lip. Adult face fully readable. "
              "Implied sensual only; body covered; no nudity; no sex."),
    "erotic": ("An adult East Asian woman of twenty-two, petite adult frame with B-cup breasts, slim waist, "
               "dancer hips, warm-neutral East Asian undertone, no glasses. Dark brown center-part hair. "
               "True crimson lipstick. Adult face fully readable. One heroine only."),
}
BAN = {
    "figure": "SFW, fully non-explicit.",
    "youth": "Soft-sensual implied only; no genitals, no penetration, no explicit sex; adult 18+ solo.",
    "erotic": "Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most.",
}

# filename -> {skill, aspect, prompt}
EXAMPLES: dict[str, dict] = {}


def E(fname: str, skill: str, aspect: str, prompt: str) -> None:
    EXAMPLES[fname] = {"skill": skill, "aspect": aspect, "prompt": prompt}


# ---------------- hero / 卡片 / 默认与用法 ----------------
E("hero-banner.jpg", "figure", "16:9 (Widescreen)",
  """This is a wide cinematic still, photoreal adult East Asian woman in a golden-hour city street: a horizontal composition built for a site banner, one heroine as the visual anchor.
Main subject: An adult East Asian woman of twenty-two, petite adult frame, warm-neutral East Asian undertone, dark brown center-part hair, fully dressed in a camel long coat over a cream knit and straight jeans with retro sneakers, walking candid mid-stride, face turned softly toward the lens. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a tree-lined city sidewalk at dusk, storefront glass and warm streetlamps fading into the wide horizontal frame, two to four readable anchors, depth falls away left and right.
Composition and atmosphere: horizontal wide framing with the heroine right of center, negative space to the left for site text; golden sunset rim on her hair; muted low-saturation dan-ren palette; masterpiece, best quality.""")

E("street-ootd.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 street candid with photoreal street photography: a photoreal adult East Asian woman frozen mid-stride, garment lines readable toward the lens.
Main subject: An adult East Asian woman of twenty-two, fully dressed in an oversized hoodie with a pleated midi skirt and white sneakers, one hand tucked in the hoodie pocket, mid-walk stride, face in soft daylight. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a crosswalk corner with storefront glass, a streetlamp and one parked bicycle; two to four readable anchors; depth falls away softly behind her.
Composition and atmosphere: she fills most of the vertical frame with a thin margin; overcast soft daylight, even and muted; muted low-saturation dan-ren palette; masterpiece, best quality.""")

E("beauty-glass.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a medium close-up vertical 3:4 beauty still with Korean-style dewy editorial: a photoreal adult East Asian woman, glass skin with a soft highlight, centered half-body.
Main subject: An adult East Asian woman of twenty-two, dark brown center-part hair, soft natural lip, dewy glass skin with a subtle highlighter on the cheekbones, one hand raised near the jaw, serene gaze to lens. Fully dressed in a simple knit top. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a pale seamless paper studio with a faint floor seam, one softbox stand off-frame; two to four readable anchors only.
Composition and atmosphere: clam-shell beauty light, even fill, soft falloff; gentle fill, thin hair rim; natural true-color restrained grade; masterpiece, best quality.""")

E("yoga-sport.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 sport still with athletic editorial photography: a photoreal adult East Asian woman in a balanced yoga pose, muscle lines readable.
Main subject: An adult East Asian woman of twenty-two, fully dressed in a sports bra layered under a loose tank with high-waist leggings and training sneakers, standing in a warrior pose, arms extended, focused-athletic expression. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a gym floor with wall mirrors, one barbell rack and a hanging rope; two to four readable anchors; no clutter competing with the figure.
Composition and atmosphere: cool overhead panels with a soft window fill; clean bright midtones fresh skin grade; masterpiece, best quality.""")

E("home-soft.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 lifestyle still with soft boudoir-SFW photography: a photoreal adult East Asian woman relaxed at home, warm evening light.
Main subject: An adult East Asian woman of twenty-two, fully dressed in a relaxed cardigan over a tank top and soft lounge trousers, sitting on a linen sofa with one knee up, gentle smile off-frame. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a bright apartment living room with a linen sofa, one floor lamp and a rug; two to four readable anchors; depth falls away softly.
Composition and atmosphere: evening lamp light with a warm wrap; warm neutral home tone; masterpiece, best quality.""")

# ---------------- figure 示例图 6 ----------------
E("fg-street-midstride.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 street candid with photoreal street photography: an adult East Asian woman frozen mid-stride on a sidewalk, motion readable in one beat.
Main subject: An adult East Asian woman of twenty-two, fully dressed in a denim jacket over a striped tee with cargo pants and clean trainers, mid-walk stride, one hand brushing hair back, face in soft daylight. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a quiet sidewalk lined with plane trees, a low railing and window reflections; two to four readable anchors; depth falls away softly behind her.
Composition and atmosphere: overcast soft daylight, even and muted; jp cream low-saturation airy grade; masterpiece, best quality.""")

E("fg-metro-commute.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 commuter candid with photoreal urban photography: an adult East Asian woman holding a subway strap, commute moment frozen.
Main subject: An adult East Asian woman of twenty-two, fully dressed in a cropped knit with high-waist wide jeans and low-top canvas shoes, one hand holding an overhead strap, weight on one hip, calm expression to lens. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a metro carriage with a window, handrails and one seated commuter blurred beyond; two to four readable anchors; depth falls away softly.
Composition and atmosphere: daylight through the window with a cool ambient base; muted low-saturation dan-ren palette; masterpiece, best quality.""")

E("fg-editorial.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 fashion editorial still with high-fashion photography: an adult East Asian woman in a sculptural s-curve pose, studio minimal.
Main subject: An adult East Asian woman of twenty-two, fully dressed in an oversized blazer dress with sheer tights and square-toe boots, one leg crossed before the other, arms long at the sides, chin lifted, neutral-editorial expression. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a white cyclorama with a single gray v-flat leaning against the wall; two to four readable anchors only.
Composition and atmosphere: softbox key from front-left, gentle fill, thin hair rim; polished catalog neutral grade; masterpiece, best quality.""")

E("fg-yoga.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 athletic still with yoga editorial photography: an adult East Asian woman in a seated cross-leg stretch, controlled lines.
Main subject: An adult East Asian woman of twenty-two, fully dressed in a zip-up track jacket with matching tapered joggers and running shoes, seated in a cross-legged forward fold, spine long, eyes closed, focused-task expression. Adult face fully readable. SFW, fully non-explicit.
Environmental background: an indoor track lane with painted lines and a foam roller at the edge; two to four readable anchors; no clutter.
Composition and atmosphere: high windows with dust-beam light; clean bright midtones fresh skin grade; masterpiece, best quality.""")

E("fg-travel.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 travel still with photoreal travel photography: an adult East Asian woman before a landmark, scale readable.
Main subject: An adult East Asian woman of twenty-two, fully dressed in a quilted jacket with a plaid scarf, jeans and hiking boots, standing at a lakeside promenade railing, one hand resting on the rail, relaxed smile to lens. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a lakeside promenade with a railing, one bench and distant mountains; two to four readable anchors; depth falls away softly.
Composition and atmosphere: golden hour side light with long shadows; Portra-like warm skin soft grain grade; masterpiece, best quality.""")

E("fg-beauty.jpg", "figure", "3:4 (Portrait Standard)",
  """This is a medium close-up vertical 3:4 beauty still with Korean-style dewy makeup photography: an adult East Asian woman, half-body, water-gloss finish.
Main subject: An adult East Asian woman of twenty-two, dark brown center-part hair, dewy skin with glass-skin highlight, soft gradient lip, one hand near the collarbone, serene gaze slightly off lens. Fully dressed in a knit camisole under a thin cardigan. Adult face fully readable. SFW, fully non-explicit.
Environmental background: a pale seamless paper studio with a faint floor seam, one softbox stand off-frame; two to four readable anchors only.
Composition and atmosphere: top beauty dish with a low fill card; clean bright editorial grade; masterpiece, best quality.""")

# ---------------- youth 6 ----------------
E("ys-window-lace.jpg", "youth", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 window-light still with soft-sensual youth photography: an adult East Asian woman by a sheer-curtain window at dusk, backlit hair rim.
Main subject: An adult East Asian woman of twenty-two, wearing a soft white slip dress with spaghetti straps, sitting sideways on the window sill, one shoulder bare, glancing over her shoulder toward the lens, half-lidded gaze. Implied sensual only; body covered; no nudity; no sex. Adult face fully readable.
Environmental background: a bedroom window seat with sheer curtains, one plant and city lights beyond; two to four readable anchors; depth falls away softly.
Composition and atmosphere: window backlight with hair rim, face softly filled; cool white low-chroma restrained grade; masterpiece, best quality.""")

E("ys-mirror-shirt.jpg", "youth", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 mirror self-gaze still with soft-sensual youth photography: an adult East Asian woman in a closed oversized boyfriend shirt, seen through a full-length mirror.
Main subject: An adult East Asian woman of twenty-two, wearing an oversized white boyfriend shirt buttoned all the way up to the collar, the fabric fully covering her chest and body, hem falling to mid-thigh, one hand resting on the collar, standing before a full-length mirror, gaze meeting her own reflection, soft knowing eyes. Implied sensual only; body covered; no nudity; no sex. Adult face fully readable.
Environmental background: a full-length mirror against a bedroom wall, one jewelry tray below; two to four readable anchors; depth falls away softly.
Composition and atmosphere: window daylight bounced off the mirror; warm neutral dusk tone; masterpiece, best quality.""")

E("ys-bed-soft.jpg", "youth", "3:4 (Portrait Standard)",
  """This is a medium vertical 3:4 bed-core still with soft-sensual youth photography: an adult East Asian woman curled on rumpled bedding, warm bedside light.
Main subject: An adult East Asian woman of twenty-two, wearing an oversized light-blue shirt slipping off one shoulder, sitting on the bed edge with knees drawn up, arms wrapped around them, soft knowing gaze to lens. Implied sensual only; body covered; no nudity; no sex. Adult face fully readable.
Environmental background: a low bed with white sheets, a crumpled duvet and one bedside lamp; two to four readable anchors; depth falls away softly.
Composition and atmosphere: bedside lamp warm and low; cream-white with soft-pink blush, warm tungsten grade; masterpiece, best quality.""")

E("ys-sofa-phone.jpg", "youth", "3:4 (Portrait Standard)",
  """This is a medium vertical 3:4 lazy-sofa still with soft-sensual youth photography: an adult East Asian woman curled on a linen sofa scrolling her phone.
Main subject: An adult East Asian woman of twenty-two, wearing a cream knit two-piece with a camisole and an open cardigan, sleeves past the wrist, curled on the sofa with legs tucked under, phone in one hand, eyes on the screen, soft relaxed lips. Implied sensual only; body covered; no nudity; no sex. Adult face fully readable.
Environmental background: a soft linen sofa with two pillows, a knitted throw and one side lamp; two to four readable anchors; depth falls away softly.
Composition and atmosphere: one warm floor lamp as key, soft falloff; cozy amber evening tone; masterpiece, best quality.""")

E("ys-wet-hair.jpg", "youth", "3:4 (Portrait Standard)",
  """This is a medium vertical 3:4 after-shower still with soft-sensual youth photography: an adult East Asian woman in a thick white terry bathrobe with damp hair, steamy bathroom, cool mist light.
Main subject: An adult East Asian woman of twenty-two, wet hair clinging to her face and collarbones, wearing a thick white terry bathrobe loosely belted at the waist, opaque thick fabric fully covering her chest and body, collarbones hinted only, one hand pushing damp hair back, eyes toward the lens through soft steam. Implied sensual only; body covered; no nudity; no sex. Adult face fully readable.
Environmental background: a bathroom with a fogged mirror, one folded towel and steam light; two to four readable anchors; depth falls away softly.
Composition and atmosphere: steam-soft backlight with a warm wall lamp; steamy soft with lifted whites grade; masterpiece, best quality.""")

E("ys-softlife.jpg", "youth", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 soft-life still with golden-hour youth photography: an adult East Asian woman by a window in warm evening glow, soft living mood.
Main subject: An adult East Asian woman of twenty-two, wearing a v-neck cashmere sweater with sleeves pushed to the elbows, sitting cross-legged on a window-side sofa with a mug in both hands, gaze drifting off-frame, soft smile. Implied sensual only; body covered; no nudity; no sex. Adult face fully readable.
Environmental background: a window-side sofa with a mug on the armrest and evening glow; two to four readable anchors; depth falls away softly.
Composition and atmosphere: dusk window glow with a warm practical; warm neutral dusk tone; masterpiece, best quality.""")

# ---------------- erotic 氛围 11 ----------------
E("nsfw-robe-hotel.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 hotel mood still with cinematic boudoir photography: an adult East Asian woman in a satin robe by a hotel bed, tungsten amber light.
Main subject: An adult East Asian woman of twenty-two, wearing a deep-v silk robe loosely belted, one shoulder slipping bare, sitting on the hotel bed edge, one strap fallen, gaze to lens through low light. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Adult face fully readable.
Environmental background: a dim luxury hotel room with a king bed, one tungsten bedside lamp and drawn sheers; two to four readable anchors; depth falls away softly.
Composition and atmosphere: bedside tungsten warm and low; warm tungsten amber with burgundy accent notes grade; masterpiece, best quality.""")

E("nsfw-sheer-silhouette.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 silhouette still with soft boudoir photography: an adult East Asian woman as a backlit silhouette behind a sheer curtain, form hinted not shown.
Main subject: An adult East Asian woman of twenty-two, silhouette behind a sheer curtain, bare shoulders and waist curve suggested through the fabric, face turned in profile against the window light. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Face hinted, not fully detailed.
Environmental background: a bedroom window with sheer curtains glowing at night, one bedside lamp low; two to four readable anchors; depth falls away softly.
Composition and atmosphere: sheer window light with a floor lamp fill; low-key moody warm grade; masterpiece, best quality.""")

E("nsfw-stockings-shirt.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 half-undress still with boudoir narrative photography: an adult East Asian woman in a button shirt and stockings, undress paused mid-beat.
Main subject: An adult East Asian woman of twenty-two, a button shirt open to the navel, skirt hiked, nothing removed, sheer stockings catching the light, one hand on the last fastened button, gaze lowered to lens. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Adult face fully readable.
Environmental background: a bedroom with rumpled sheets, one warm lamp and soft shadows; two to four readable anchors; depth falls away softly.
Composition and atmosphere: one warm lamp as key, amber shadows; warm amber low-key grade; masterpiece, best quality.""")

E("nsfw-hands-sheet.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a close-up vertical 3:4 still-life detail with boudoir photography: hands only, fingers gripping white sheets, no face in frame.
Main subject: An adult woman's hands and wrists only, fingers curled into rumpled white cotton sheets, one wrist with a thin silver bracelet, skin lit by warm lamp light. Adult 18+ only. Atmosphere memory shot; no nudity shown; hands and fabric only.
Environmental background: a bed with rumpled white sheets, soft shadows around the hands; two to four readable anchors only; shallow depth of field.
Composition and atmosphere: bedside lamp warm and low; warm amber low-key grade; masterpiece, best quality.""")

E("nsfw-bed-stilllife.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a wide vertical 3:4 still-life of an unmade bed with boudoir mood: no person in frame, traces only.
Main subject: an unmade hotel bed with rumpled white sheets, a silk robe draped across the foot, one pillow dented, morning light across the folds. Adult 18+ only. Atmosphere memory shot; object still life, no figure.
Environmental background: a dim hotel room with a king bed, one tungsten bedside lamp and drawn sheers; two to four readable anchors only.
Composition and atmosphere: bedside tungsten warm and low with a slit of window light; warm tungsten amber with burgundy accent notes grade; masterpiece, best quality.""")

E("er-hotel-robe.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 hotel boudoir still with tungsten cinema photography: an adult East Asian woman in a hotel robe by the bathroom mirror.
Main subject: An adult East Asian woman of twenty-two, wearing a soft hotel robe with a loosely tied belt, collarbones visible, standing before a wide bathroom mirror, applying lipstick with one hand, reflected gaze to lens. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Adult face fully readable.
Environmental background: a hotel bathroom with a wide mirror, a towel rack and warm downlight; two to four readable anchors; depth falls away softly.
Composition and atmosphere: bathroom downlight with mirror bounce; warm tungsten amber with burgundy accent notes grade; masterpiece, best quality.""")

E("er-bed-edge.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a medium vertical 3:4 bed-edge still with half-undress narrative: an adult East Asian woman seated on the bed edge, dress pulled up to the waist, bra still worn.
Main subject: An adult East Asian woman of twenty-two, a slip dress pulled up to the waist, bra still worn, trousers at the knees not in frame, sitting on the bed edge with one leg crossed over the other, hand resting on the hem, gaze over the shoulder. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Adult face fully readable.
Environmental background: a bedroom with a vanity glow, silk bedding and a floor mirror; two to four readable anchors; depth falls away softly.
Composition and atmosphere: vanity glow mixed with cool moonlight; warm amber low-key grade; masterpiece, best quality.""")

E("er-window-sheer.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a full-body vertical 3:4 night-window still with moody boudoir photography: an adult East Asian woman by a sheer night window, city lights beyond.
Main subject: An adult East Asian woman of twenty-two, wearing a satin slip with lace edges, one strap fallen, standing beside a floor-to-ceiling window with sheer curtains, back to the lens, face in profile reflection on the glass. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Adult face readable in reflection.
Environmental background: a hotel suite window with a city view and a robe on the chair; two to four readable anchors; depth falls away softly.
Composition and atmosphere: sheer window light with a floor lamp fill; cinematic soft with teal shadows grade; masterpiece, best quality.""")

E("er-neon-night.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a medium vertical 3:4 neon-night still with cinematic boudoir photography: an adult East Asian woman by a hotel window as neon light bleeds through the blinds.
Main subject: An adult East Asian woman of twenty-two, wearing a sheer bodysuit with high-cut legs, leaning against the window frame, magenta and cyan neon stripes falling across her skin and face, eyes to lens. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Adult face fully readable.
Environmental background: a dim hotel room with drawn blinds, city neon glow outside; two to four readable anchors; depth falls away softly.
Composition and atmosphere: neon signage glow with a cool ambient base; neon contrast with deep blacks grade; masterpiece, best quality.""")

E("er-bath-steam.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 shower-steam still with cold-tone boudoir photography: a woman seen from behind as a dark silhouette against heavily fogged glass, cool blue-white backlight.
Main subject: An adult East Asian woman of twenty-two photographed from behind, back to the lens, a dark silhouette against heavily fogged shower glass, only the outline of her shoulders, damp hair and neckline readable as a black shape, no frontal view, no skin detail visible at all. Adult 18+ only. Atmosphere memory shot; pure back silhouette, no visible body detail.
Environmental background: a tiled shower with glass doors and one warm wall lamp; two to four readable anchors; depth falls away softly.
Composition and atmosphere: strong steam-soft backlight against the glass, high contrast dark silhouette; steamy soft with lifted whites grade; masterpiece, best quality.""")

E("er-slip-sofa.jpg", "erotic", "3:4 (Portrait Standard)",
  """This is a three-quarter vertical 3:4 sofa still with boudoir narrative: an adult East Asian woman in a satin slip on a leather sofa, low moody light.
Main subject: An adult East Asian woman of twenty-two, wearing a satin slip with lace edges, hem riding high on the thigh, reclining across a leather sofa with one arm above her head, gaze to lens. Adult 18+ only. Atmosphere memory shot; suggestive half-undress or silhouette at most. Adult face fully readable.
Environmental background: a dim luxury hotel room with a king bed, one tungsten bedside lamp and drawn sheers; two to four readable anchors; depth falls away softly.
Composition and atmosphere: warm cove lighting along the headboard; low-key moody warm grade; masterpiece, best quality.""")


def png_to_jpg(src: Path, dest: Path) -> None:
    Image.open(src).convert("RGB").save(dest, quality=92, optimize=True)


def run_one(base: dict, fname: str, spec: dict) -> None:
    wf = json.loads(json.dumps(base))
    wf["627"]["inputs"]["text"] = spec["prompt"]
    seed = int(hashlib.md5(fname.encode("utf-8")).hexdigest()[:10], 16)
    wf["851"]["inputs"]["seed"] = seed
    wf["732"]["inputs"]["filename_prefix"] = f"examples/{fname[:-4]}"
    wf["857"]["inputs"]["aspect_ratio"] = spec["aspect"]
    wf["857"]["inputs"]["megapixels"] = 2.5
    pid = C.submit_prompt(wf, f"example-{fname[:30]}")
    hist = C.wait_done(pid, timeout=300)
    imgs = C.history_images(hist)
    if not imgs:
        raise RuntimeError("no image")
    src = C.resolve_output(imgs[0][0], imgs[0][1])
    png_to_jpg(src, IMG / fname)


def main() -> int:
    ap = argparse.ArgumentParser(description="示例图重出（对齐锚生态铁律）")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", nargs="*", default=[])
    args = ap.parse_args()

    base = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    items = list(EXAMPLES.items())
    if args.only:
        items = [(k, v) for k, v in items if k in args.only]
    if args.limit > 0:
        items = items[: args.limit]
    for i, (fname, spec) in enumerate(items, 1):
        t0 = time.time()
        try:
            run_one(base, fname, spec)
            print(f"[{i}/{len(items)}] ok {fname} {time.time()-t0:.1f}s", flush=True)
        except Exception as e:
            print(f"[{i}/{len(items)}] FAIL {fname}: {str(e)[:200]}", flush=True)
            time.sleep(2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
