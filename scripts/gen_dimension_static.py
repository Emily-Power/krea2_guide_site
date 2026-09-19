#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 director-catalog.static.json：L1–L5 公共维 + 三 skill 专属（数据在 dimension_items.py）。"""
from __future__ import annotations

import json
from pathlib import Path

from dimension_items import (
    EROTIC_ACT,
    EROTIC_BODYFOCUS,
    EROTIC_DYNAMIC,
    EROTIC_EXPOSURE,
    EROTIC_FANTASY,
    EROTIC_FINISH,
    EROTIC_INTENSITY,
    FIGURE_ZONE,
    YOUTH_ACT,
    YOUTH_AES,
    YOUTH_FOCUS,
    YOUTH_IMPLY,
    YOUTH_INTENSITY,
    public_lists,
    subject_dict,
)
from dimension_items_extra import (
    BODY_X,
    CAM_X,
    CAST_X,
    CLOTH_X,
    AGE_X,
    EROTIC_ACT_X,
    EROTIC_DYNAMIC_X,
    EROTIC_FANTASY_X,
    ETH_X,
    EXPR_X,
    FIGURE_ZONE_X,
    GRADE_X,
    HAIR_X,
    LIGHT_X,
    MAKEUP_X,
    POSE_X,
    PROP_X,
    SET_X,
    YOUTH_ACT_X,
    YOUTH_AES_X,
    YOUTH_FOCUS_X,
    merge,
)
from dimension_items_rounds import (
    R1_CLOTH,
    R2_SET,
    R3_CAM,
    R3_LIGHT,
    R3_POSE,
    R4_EXPR,
    R4_GRADE,
    R4_HAIR,
    R4_MAKEUP,
    R5_CAM,
    R5_CLOTH,
    R5_EROTIC,
    R5_EXPR,
    R5_FIGURE,
    R5_GRADE,
    R5_HAIR,
    R5_LIGHT,
    R5_MAKEUP,
    R5_POSE,
    R5_PROP,
    R5_SUBJECT,
    R5_YOUTH,
)

OUT = Path(__file__).resolve().parent / "director-catalog.static.json"


def count_items(d: dict) -> int:
    return sum(len(v) for v in d.values() if isinstance(v, list))


def thickened_public() -> dict:
    p = public_lists()
    p["pose"] = merge(merge(p["pose"], POSE_X), R3_POSE + R5_POSE)
    p["cloth"] = merge(merge(p["cloth"], CLOTH_X), R1_CLOTH + R5_CLOTH)
    p["prop"] = merge(merge(p["prop"], PROP_X), R5_PROP)
    p["set"] = merge(merge(p["set"], SET_X), R2_SET)
    p["light"] = merge(merge(p["light"], LIGHT_X), R3_LIGHT + R5_LIGHT)
    p["cam"] = merge(merge(p["cam"], CAM_X), R3_CAM + R5_CAM)
    p["makeup"] = merge(merge(p["makeup"], MAKEUP_X), R4_MAKEUP + R5_MAKEUP)
    p["expr"] = merge(merge(p["expr"], EXPR_X), R4_EXPR + R5_EXPR)
    p["grade"] = merge(merge(p["grade"], GRADE_X), R4_GRADE + R5_GRADE)
    p["hair"] = None  # hair lives in SUBJECT
    return {k: v for k, v in p.items() if v is not None}


def thickened_subject() -> dict:
    s = subject_dict()
    s["eth"] = merge(s["eth"], ETH_X)
    s["age"] = merge(s["age"], AGE_X)
    s["body"] = merge(s["body"], BODY_X)
    s["cast"] = merge(s["cast"], CAST_X)
    s["hair"] = merge(merge(s["hair"], HAIR_X), R4_HAIR + R5_HAIR)
    # R5_SUBJECT mixed ids
    eth_r5 = [x for x in R5_SUBJECT if x["id"].startswith("eth_")]
    body_r5 = [x for x in R5_SUBJECT if x["id"].startswith("body_")]
    cast_r5 = [x for x in R5_SUBJECT if x["id"].startswith("cast_")]
    s["eth"] = merge(s["eth"], eth_r5)
    s["body"] = merge(s["body"], body_r5)
    s["cast"] = merge(s["cast"], cast_r5)
    return s


def build() -> dict:
    public = thickened_public()
    sub = thickened_subject()
    # hair also available on skill catalogs for menus that read skill.hair? keep subject only; director uses SUBJECT
    zone = merge(merge(FIGURE_ZONE, FIGURE_ZONE_X), R5_FIGURE)
    y_act = merge(YOUTH_ACT, YOUTH_ACT_X)
    y_focus = merge(YOUTH_FOCUS, YOUTH_FOCUS_X)
    y_aes = merge(merge(YOUTH_AES, YOUTH_AES_X), [x for x in R5_YOUTH if x["id"].startswith("aes_")])
    y_act = merge(y_act, [x for x in R5_YOUTH if x["id"].startswith("act_")])
    y_focus = merge(y_focus, [x for x in R5_YOUTH if x["id"].startswith("focus_")])

    e_act = merge(EROTIC_ACT, EROTIC_ACT_X)
    e_fan = merge(EROTIC_FANTASY, EROTIC_FANTASY_X)
    e_dyn = merge(EROTIC_DYNAMIC, EROTIC_DYNAMIC_X)
    e_act = merge(e_act, [x for x in R5_EROTIC if x["id"].startswith("act_")])
    e_fan = merge(e_fan, [x for x in R5_EROTIC if x["id"].startswith("fan_")])
    e_dyn = merge(e_dyn, [x for x in R5_EROTIC if x["id"].startswith("dyn_")])
    e_exp = merge(EROTIC_EXPOSURE, [x for x in R5_EROTIC if x["id"].startswith("exp_")])

    figure = {"zone": zone, **public}
    youth = {
        "intensity": YOUTH_INTENSITY,
        "act": y_act,
        "imply": YOUTH_IMPLY,
        "focus": y_focus,
        "aes": y_aes,
        **public,
    }
    erotic = {
        "intensity": EROTIC_INTENSITY,
        "act": e_act,
        "exposure": e_exp,
        "finish": EROTIC_FINISH,
        "dynamic": e_dyn,
        "fantasy": e_fan,
        "bodyfocus": EROTIC_BODYFOCUS,
        **public,
    }
    return {
        "FIGURE": figure,
        "YOUTH": youth,
        "EROTIC": erotic,
        "SUBJECT": sub,
        "_meta": {
            "version": "2026-08-12-dim-v4-5rounds",
            "formula": "Skill = public L1-L5 + specialty",
            "rounds": "R1 cloth lingerie · R2 CN sets · R3 pose/light/cam · R4 hair/makeup/grade · R5 specialty",
            "generator": "dimension_items + extra + rounds",
        },
    }


def main() -> None:
    data = build()
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote", OUT)
    for k in ("FIGURE", "YOUTH", "EROTIC", "SUBJECT"):
        n = count_items(data[k])
        print(f"  {k}: {len(data[k])} lists, {n} items")
    pub_n = count_items(thickened_public())
    sub_n = count_items(thickened_subject())
    print(f"  public={pub_n} subject={sub_n}")


if __name__ == "__main__":
    main()
