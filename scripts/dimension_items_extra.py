# -*- coding: utf-8 -*-
"""v3 扩库：所有 L1 下 L2/L3（+L4/L5）继续加厚 · 联网补全 2026-08-12。
外搭夹克分类、上装细分、场景/调色/姿/道具/专属再扩。
"""
from __future__ import annotations

# reuse I from parent - define local to avoid circular import
def I(id: str, label: str, en: str, group: str = "") -> dict:
    d = {"id": id, "label": label, "en": en}
    if group:
        d["group"] = group
    return d


# ── SUBJECT 扩 ───────────────────────────────────────────────
ETH_X = [
    I("e_asian_se_mix", "东亚东南亚混", "East-Southeast Asian mixed adult", "L2人种"),
    I("e_pacific", "太平洋岛民", "Pacific Islander adult", "L2人种"),
    I("e_indigenous", "原住民点名", "indigenous adult as specified", "L2人种"),
]
AGE_X = [
    I("y18_22", "年龄带Y18-22美学", "adult early twenties youthful adult lock", "L3年龄带"),
    I("y23_26", "年龄带Y23-26", "adult mid-twenties", "L3年龄带"),
    I("y27_30", "年龄带Y27-30奔三", "adult late twenties approaching thirty", "L3年龄带"),
]
BODY_X = [
    I("body_lean_muscle", "精瘦肌", "lean muscle definition soft adult", "L2体型"),
    I("body_pear", "梨型", "pear shape fuller hips adult", "L2体型"),
    I("body_apple", "苹果型", "softer midsection adult natural", "L2体型"),
    I("body_long_torso", "长躯干", "long torso proportion adult", "L3体型读"),
    I("body_long_leg", "长腿读", "long-leg visual read adult", "L3体型读"),
]
CAST_X = [
    I("cast_trio", "三人三角", "three adults triangle composition", "L2人数"),
    I("cast_mmf", "二男一女焦点", "MMF group heroine focus", "L2人数"),
    I("cast_ffm", "二女一男焦点", "FFM group focus", "L2人数"),
    I("cast_mirror_duo_true", "真双人+镜", "two adults plus mirror", "L3人数"),
    I("cast_pet", "女主+宠物", "heroine with pet soft", "L2关系"),
    I("cast_faceless_him", "男配无脸", "male partner face out of frame", "L2关系"),
]

# ── HAIR 扩 L2/L3 ───────────────────────────────────────────
HAIR_X = [
    I("hair_hug_curl", "韩Hug卷/空气卷", "hug curls soft face frame kr", "L2造型"),
    I("hair_inner_curl", "内扣卷", "inward curl ends polished", "L2造型"),
    I("hair_outer_curl", "外翘卷", "outward flip ends playful adult", "L2造型"),
    I("hair_s_curl", "S卷大波浪", "S-wave glam waves", "L2造型"),
    I("hair_perm_digital", "数字烫感", "digital perm soft bounce", "L2造型"),
    I("hair_mullet_soft", "软鲻鱼/狼鲻", "soft mullet wolf hybrid adult", "L2造型"),
    I("hair_french_bob", "法式短bob", "french bob chin soft", "L2造型"),
    I("hair_pageboy", "蘑菇头成人", "pageboy soft adult not child", "L2造型"),
    I("hair_undercut_soft", "侧铲软", "soft undercut longer top adult", "L2造型"),
    I("hair_twin_low", "双低马尾成人", "twin low tails adult not loli", "L2造型"),
    I("hair_space_bun", "双丸子成人", "space buns adult fashion", "L2造型"),
    I("hair_topknot", "高丸/半丸", "high top knot soft", "L2造型"),
    I("hair_braid_crown", "皇冠编", "crown braid elegant", "L2造型"),
    I("hair_fishtail", "鱼骨辫", "fishtail braid soft", "L2造型"),
    I("hair_bubble_pony", "泡泡马尾", "bubble ponytail segments", "L2造型"),
    I("hair_pigtail_soft", "双麻花软成人", "soft pigtails adult proportions", "L2造型"),
    I("bang_baby", "空气碎盖眉", "baby wispy bangs adult soft", "L3刘海"),
    I("bang_choppy", "碎齐刘", "choppy textured bangs", "L3刘海"),
    I("bang_growout", "刘海过渡", "grown-out bangs side sweep", "L3刘海"),
    I("state_half_wet", "半干发", "half-dry towel hair texture", "L3发态"),
    I("state_clip_all", "全抓夹盘", "full claw up casual", "L3发态"),
    I("state_behind_both", "双耳后", "both sides tucked behind ears", "L3发态"),
    I("state_mouth_strand", "唇边发丝", "strand near lips soft", "L3发态"),
    I("col_burgundy", "发色红酒", "soft burgundy dark roots", "L3发色"),
    I("col_copper", "发色铜棕", "copper brown soft", "L3发色"),
    I("col_blue_black", "发色蓝黑", "blue-black cool sheen", "L3发色"),
    I("col_gray_fashion", "发色灰白时尚点名", "fashion gray adult not elderly caricature", "L3发色"),
    I("tex_oily_soft", "微油光真实", "slight natural oil sheen lived-in", "L4发质"),
    I("tex_product_hold", "定型感", "product hold textured pieces", "L4发质"),
]

# ── MAKEUP 扩 ────────────────────────────────────────────────
MAKEUP_X = [
    I("mk_idol_soft", "偶像淡舞台", "idol soft stage still readable", "L2妆壳"),
    I("mk_office", "职场干净妆", "office clean soft contour", "L2妆壳"),
    I("mk_bride_soft", "婚礼宾客淡", "wedding guest soft glam", "L2妆壳"),
    I("mk_gothic_soft", "软哥特", "soft gothic muted dark lip", "L2妆壳"),
    I("mk_y2k_gloss", "Y2K亮唇", "y2k gloss lip thin liner", "L2妆壳"),
    I("mk_sun_kissed", "日晒亲肤", "sun-kissed freckle soft bronze", "L2妆壳"),
    I("mk_freckle", "雀斑点缀", "soft freckles natural", "L2妆壳"),
    I("mk_no_brow", "淡眉近无", "very soft barely-there brows", "L2妆壳"),
    I("mk_bold_brow", "浓眉编辑", "bold editorial brows", "L2妆壳"),
    I("mk_graphic_liner", "图形眼线点名", "graphic liner fashion still", "L2妆壳"),
    I("mk_monolid_soft", "内双/单眼皮强调", "soft monolid friendly makeup", "L2妆壳"),
    I("mk_aegyo_heavy", "卧蚕强调", "stronger aegyo-sal still adult", "L2妆壳"),
    I("mk_nose_cont", "鼻影轻", "soft nose contour", "L3妆件"),
    I("mk_lip_tint_only", "只唇釉", "lip tint only bare rest", "L3妆件"),
    I("mk_cream_blush", "膏状腮红", "cream blush melt skin", "L3妆件"),
    I("mk_highlighter_wet", "湿高光", "wet-look highlighter controlled", "L3妆件"),
    I("mk_mascara_clump_soft", "睫毛分离", "separated natural lashes", "L3妆件"),
    I("mk_tear_bag", "泪沟轻提", "soft under-eye brighten", "L3妆件"),
    I("mk_ear_flush", "耳尖红", "ear tip soft flush", "L3妆件"),
]

# ── EXPR 扩 ──────────────────────────────────────────────────
EXPR_X = [
    I("expr_smirk_side", "单侧嘴角", "asymmetric half-smirk", "L2表情"),
    I("expr_pout_soft", "轻嘟嘴", "soft pout not childish", "L2表情"),
    I("expr_open_mouth_soft", "微张口", "soft parted lips breath", "L2表情"),
    I("expr_bite_finger", "轻咬指尖", "soft bite fingertip careful anatomy", "L2表情"),
    I("expr_laugh_eyes", "眼笑", "smiling eyes mouth soft", "L2表情"),
    I("expr_angry_sexy", "嗔怒欲", "annoyed-aroused adult play", "L2分轨"),
    I("expr_shy_glance", "羞涩斜视", "shy side glance", "L2表情"),
    I("expr_intense_stare", "强烈直视", "intense unbroken stare", "L2表情"),
    I("expr_melancholy", "淡淡忧郁", "soft melancholy eyes", "L2表情"),
    I("expr_euphoria", "恍惚欢愉", "euphoric unfocused bliss", "L2分轨"),
    I("expr_pain_pleasure", "快感蹙眉", "pleasure knit brows not horror", "L2分轨"),
    I("expr_command", "命令眼神", "commanding dominant gaze", "L2分轨"),
    I("expr_submissive", "仰视服从", "upward submissive soft eyes", "L2分轨"),
    I("gaze_over_glasses", "视线·眼镜上方", "gaze over glasses frames", "L3视线"),
    I("gaze_through_bangs", "视线·刘海间", "eyes through bangs", "L3视线"),
    I("gaze_closed_soft", "视线·轻闭眼", "softly closed eyes peaceful", "L3视线"),
]

# ── CLOTH 扩 L2/L3/L4/L5 ─────────────────────────────────────
CLOTH_X = [
    # 外搭细分
    I("outer_bomber", "外套·飞行夹克", "bomber jacket clean", "L2外搭"),
    I("outer_field", "外套·战地/工装夹克", "field or chore jacket", "L2外搭"),
    I("outer_moto", "外套·机车皮衣", "moto leather jacket", "L2外搭"),
    I("outer_parka", "外套·派克", "parka hood soft", "L2外搭"),
    I("outer_cape", "外套·斗篷披肩", "cape or capelet elegant", "L2外搭"),
    I("outer_overcoat", "外套·长大衣经典", "classic long overcoat", "L2外搭"),
    I("outer_pea", "外套·海军短大衣", "pea coat structured", "L2外搭"),
    I("outer_raincoat", "外套·雨衣透明点名", "raincoat clear or colored", "L2外搭"),
    I("outer_shirting", "外套·衬衫式夹克", "shirt jacket shacket", "L2外搭"),
    I("outer_fur_soft", "外套·毛绒仿", "soft faux fur coat adult", "L2外搭"),
    I("outer_kimono", "外套·和风羽织点名", "kimono-inspired haori respectful", "L2外搭"),
    # 上装细分
    I("top_oxford", "上·牛津纺衬衫", "crisp oxford shirt", "L2上装"),
    I("top_silk_blouse", "上·真丝衫", "silk blouse soft drape", "L2上装"),
    I("top_polo", "上·Polo", "polo shirt clean", "L2上装"),
    I("top_turtleneck", "上·高领", "turtleneck fine knit", "L2上装"),
    I("top_off_shoulder", "上·一字肩", "off-shoulder top adult", "L2上装"),
    I("top_halter", "上·挂脖", "halter top adult", "L2上装"),
    I("top_corset_soft", "上·软胸衣外穿", "soft corset top outerwear", "L2上装"),
    I("top_crop", "上·短款露腰", "crop top midriff adult", "L2上装"),
    I("top_hoodie_oversize", "上·oversize卫衣", "oversized hoodie soft", "L2上装"),
    I("top_vest_knit", "上·针织马甲", "knit vest layering", "L2上装"),
    I("top_vest_tailor", "上·西装马甲", "tailored waistcoat", "L2上装"),
    I("top_tube", "上·抹胸点名", "tube top adult covered tasteful", "L2上装"),
    I("top_mesh_layer", "上·网纱层", "mesh layer over solid", "L2上装"),
    # 连衣更多
    I("dress_cheongsam_soft", "连衣·旗袍雅", "qipao-inspired respectful adult", "L3连衣"),
    I("dress_blazer", "连衣·西装裙", "blazer dress tailored", "L3连衣"),
    I("dress_slip_lace", "连衣·蕾丝slip", "lace trim slip dress", "L3连衣"),
    I("dress_smock", "连衣·罩衫式", "smock dress soft volume", "L3连衣"),
    I("dress_halter", "连衣·挂脖", "halter dress adult", "L3连衣"),
    I("dress_backless", "连衣·露背点名", "open-back dress tasteful", "L3连衣"),
    I("dress_cutout", "连衣·挖空点名", "tasteful cutout dress adult", "L3连衣"),
    I("dress_two_piece", "连衣感·分体套", "matching two-piece set dressy", "L3连衣"),
    I("dress_ballgown", "连衣·蓬裙礼服", "ballgown volume formal", "L3连衣"),
    I("dress_column_satin", "连衣·直筒缎", "column satin gown-dress", "L3连衣"),
    # 半裙更多
    I("skirt_mermaid", "半裙·鱼尾", "mermaid skirt flare hem", "L3半裙"),
    I("skirt_trumpet", "半裙·喇叭", "trumpet skirt soft flare", "L3半裙"),
    I("skirt_column", "半裙·直筒长", "column long skirt", "L3半裙"),
    I("skirt_handkerchief", "半裙·手帕摆", "handkerchief hem", "L3半裙"),
    I("skirt_sarong", "半裙·纱笼感", "sarong wrap beach soft", "L3半裙"),
    I("skirt_kilt_soft", "半裙·格纹百褶", "plaid pleated soft", "L3半裙"),
    I("skirt_prairie", "半裙·田园层层", "prairie tiered soft", "L3半裙"),
    I("skirt_utility", "半裙·机能多袋", "utility multi-pocket skirt", "L3半裙"),
    I("skirt_velvet", "半裙·丝绒", "velvet skirt soft pile", "L3半裙"),
    I("skirt_tulle", "半裙·纱裙", "tulle volume skirt adult", "L3半裙"),
    # 裤更多
    I("pants_palazzo", "裤·帕拉佐", "palazzo wide fluid", "L3裤"),
    I("pants_cigarette", "裤·烟管", "cigarette slim ankle", "L3裤"),
    I("pants_paperbag", "裤·纸袋腰", "paperbag waist trousers", "L3裤"),
    I("pants_leather", "裤·皮裤", "leather pants soft", "L3裤"),
    I("pants_track", "裤·运动裤", "track pants clean", "L3裤"),
    I("pants_leggings", "裤·紧身裤", "leggings opaque adult", "L3裤"),
    I("shorts_bermuda", "裤·百慕大", "bermuda shorts tailored", "L3裤"),
    I("shorts_denim", "裤·牛仔短裤", "denim shorts mid-thigh adult", "L3裤"),
    # 状态更多
    I("st_sleeve_roll", "状态·挽袖", "sleeves rolled forearms", "L3状态"),
    I("st_untucked", "状态·下摆不塞", "shirt untucked relaxed", "L3状态"),
    I("st_tucked_front", "状态·前塞后放", "front-tuck shirt", "L3状态"),
    I("st_belted", "状态·腰带收", "belt cinched waist", "L3状态"),
    I("st_open_fly", "状态·门襟开点名", "open fly controlled erotic", "L3状态"),
    I("st_bra_out", "状态·内衣外露", "bra visible under open shirt", "L3状态"),
    I("st_no_bra_line", "状态·无内衣线", "no bra line soft drape", "L3状态"),
    I("st_stocking_tear", "状态·丝袜破点名", "sheer hosiery small tear", "L3状态"),
    I("st_garter", "状态·吊袜带", "garter straps visible", "L3状态"),
    I("st_glove_on", "状态·手套", "gloves on elegant", "L3状态"),
    # 鞋配更多
    I("foot_platform", "鞋·厚底", "platform shoes", "L4鞋"),
    I("foot_oxford", "鞋·牛津", "oxford shoes polished", "L4鞋"),
    I("foot_combat", "鞋·马丁/工装靴", "combat or work boots", "L4鞋"),
    I("foot_slides", "鞋·拖鞋外穿", "slides outdoor soft", "L4鞋"),
    I("foot_socks_legwarmer", "鞋·袜套/护腿", "leg warmers balletcore", "L4鞋"),
    I("acc_brooch", "配·胸针", "brooch lapel", "L4配"),
    I("acc_bag_charm", "配·包挂件", "bag charm plush soft", "L4配"),
    I("acc_rings", "配·多戒", "multiple thin rings", "L4配"),
    I("acc_anklet", "配·脚链", "anklet delicate", "L4配"),
    I("acc_hair_clip_vis", "配·发夹可见", "visible hair clip accent", "L4配"),
    # 面料更多
    I("fab_tweed", "料·花呢", "tweed texture", "L5面料"),
    I("fab_linen", "料·亚麻", "linen weave breathable", "L5面料"),
    I("fab_velvet", "料·丝绒", "velvet soft pile", "L5面料"),
    I("fab_sequin", "料·亮片点名", "sequin sparkle controlled", "L5面料"),
    I("fab_organza", "料·欧根纱", "organza sheer structured", "L5面料"),
    I("fab_jersey", "料·针织汗布", "jersey stretch soft", "L5面料"),
    I("fab_tulle", "料·薄纱", "tulle layers soft", "L5面料"),
    I("pat_stripe", "纹·条纹", "stripe pattern clean", "L5图案"),
    I("pat_check", "纹·格纹", "check or plaid soft", "L5图案"),
    I("pat_floral", "纹·碎花", "small floral print", "L5图案"),
    I("pat_solid", "纹·纯色", "solid color clean", "L5图案"),
    I("col_black_cloth", "衣色·黑", "black clothing", "L5衣色"),
    I("col_white_cloth", "衣色·白", "white clothing", "L5衣色"),
    I("col_cream", "衣色·米白奶油", "cream ivory clothing", "L5衣色"),
    I("col_navy", "衣色·海军蓝", "navy clothing", "L5衣色"),
    I("col_red", "衣色·红", "red clothing accent", "L5衣色"),
    I("col_pastel", "衣色·粉彩", "pastel clothing soft", "L5衣色"),
]

# ── POSE 扩 ──────────────────────────────────────────────────
POSE_X = [
    I("pose_contrapposto_hard", "站·强对立", "strong contrapposto hip pop", "L2站"),
    I("pose_t_pose_soft", "站·开臂柔", "soft open arms T not stiff", "L2站"),
    I("pose_arms_cross", "站·抱臂", "arms crossed soft not closed-off", "L2站"),
    I("pose_hand_neck", "站·手触颈", "hand light on neck collarbone", "L2站"),
    I("pose_fix_adjust", "站·整理发", "both hands adjust hair mid", "L2站"),
    I("pose_jacket_hook", "站·挂外套肩", "jacket hooked finger over shoulder", "L2站"),
    I("pose_stride_long", "走·大步", "long stride confident", "L2走"),
    I("pose_twirl_walk", "走·旋步", "walking twirl freeze", "L2走"),
    I("pose_lean_rail_back", "靠·后仰栏杆", "lean back on rail arms", "L2靠"),
    I("pose_lean_elbow_high", "靠·高肘", "elbow high on wall head soft", "L2靠"),
    I("pose_sit_lotus_soft", "坐·软盘腿", "soft cross-leg floor adult", "L2坐"),
    I("pose_sit_side_saddle", "坐·侧坐", "side-saddle sit elegant", "L2坐"),
    I("pose_sit_straddle_chair", "坐·跨坐椅", "straddle chair back face cam", "L2坐"),
    I("pose_sit_knees_chest", "坐·抱膝", "knees to chest arms wrap", "L2坐"),
    I("pose_lie_stomach_chin", "卧·趴撑下巴", "prone chin on hands", "L2镜床"),
    I("pose_lie_arch_bridge", "卧·轻桥", "soft back arch bridge careful", "L2镜床"),
    I("pose_kneel_upright", "跪·直身", "upright kneeling formal", "L2其它"),
    I("pose_kneel_sit_heels", "跪·坐踵", "seiza-like sit on heels adult", "L2其它"),
    I("pose_all_fours", "跪爬姿", "all fours skill-dependent", "L2其它"),
    I("pose_lunge_photo", "弓步造型", "photo lunge not sport", "L2其它"),
    I("pose_jump_freeze", "跳跃定格", "jump freeze hair cloth motion", "L3细姿"),
    I("pose_hair_flip", "甩发定格", "hair flip freeze", "L3细姿"),
    I("pose_look_down_eyes_up", "低头抬眼", "chin down eyes up beauty", "L3细姿"),
    I("pose_profile_look_cam", "侧脸转眼", "profile body eyes to cam", "L3细姿"),
    I("pose_hands_pocket_one", "单手插袋", "one hand pocket one free", "L3细姿"),
    I("pose_point_soft", "轻指远方", "soft point off-frame", "L3细姿"),
    I("pose_hold_hat", "持帽", "hat in hand hip", "L3细姿"),
    I("pose_umbrella_shoulder", "伞靠肩", "umbrella on shoulder", "L3细姿"),
]

# ── PROP 扩 ──────────────────────────────────────────────────
PROP_X = [
    I("prop_wine", "酒杯", "wine glass stem soft", "L2道具"),
    I("prop_cigarette_soft", "烟氛围点名", "cigarette or vapor aesthetic adult", "L2道具"),
    I("prop_lollipop", "棒棒糖成人", "lollipop adult playful not child", "L2道具"),
    I("prop_shopping_bags", "购物袋", "shopping bags both hands", "L2道具"),
    I("prop_balloon", "气球庆生成人", "balloon string adult celebration", "L2道具"),
    I("prop_vinyl", "黑胶", "vinyl sleeve under arm", "L2道具"),
    I("prop_guitar", "吉他", "guitar strap or held", "L2道具"),
    I("prop_mic", "麦克风", "handheld mic stage", "L2道具"),
    I("prop_tablet", "平板手绘", "tablet stylus mid-draw", "L2道具"),
    I("prop_passport", "护照登机牌", "passport boarding pass chest", "L2道具"),
    I("prop_map_phone", "导航手机", "phone as map citywalk", "L2道具"),
    I("prop_skewer", "烤串", "street skewer night market", "L2道具"),
    I("prop_cake_fork", "甜品叉", "dessert fork mid-bite", "L2道具"),
    I("prop_perfume", "香水瓶", "perfume bottle vanity", "L2道具"),
    I("prop_lipstick", "口红管", "lipstick tube mid-apply freeze", "L2道具"),
    I("prop_towel_hand", "手持毛巾", "towel in hand damp", "L2道具"),
    I("prop_pillow", "抱枕", "hug pillow soft", "L2道具"),
    I("prop_blanket", "裹毯", "blanket wrap shoulders", "L2道具"),
    I("prop_leash_fashion", "牵引绳时尚", "fashion leash aesthetic adult", "L2道具"),
    I("prop_handcuffs_soft", "铐装饰点名", "decorative cuffs soft metal", "L2道具"),
    I("prop_candle", "蜡烛", "candle flame soft", "L2道具"),
    I("prop_fan", "扇", "hand fan elegant", "L2道具"),
    I("prop_lantern", "灯笼/提灯", "lantern soft glow", "L2道具"),
]

# ── SET 扩 ───────────────────────────────────────────────────
SET_X = [
    I("set_bridge", "桥面/桥洞", "bridge walkway or underpass", "L2城"),
    I("set_subway_tunnel", "地铁通道", "subway corridor tiles", "L2城"),
    I("set_bus_stop", "公交站", "bus stop night light", "L2城"),
    I("set_phone_booth", "电话亭感", "phone booth or glass kiosk", "L2城"),
    I("set_graffiti_wall", "涂鸦墙", "graffiti wall street art", "L2城"),
    I("set_stairwell", "楼梯间", "stairwell concrete railing", "L2城"),
    I("set_fire_escape", "消防梯", "fire escape metal stairs", "L2城"),
    I("set_construction", "工地边缘安全", "construction edge safety gear if needed", "L2城"),
    I("set_museum", "美术馆", "museum white wall artwork", "L2城"),
    I("set_gallery_opening", "画廊开幕", "gallery opening crowd soft", "L2城"),
    I("set_record_shop", "黑胶店", "record shop crates posters", "L2城"),
    I("set_arcade", "夹娃娃/街机", "arcade claw machines glow", "L2城"),
    I("set_bakery", "面包店", "bakery warm case light", "L2城"),
    I("set_bar_night", "酒吧吧台", "bar counter bottles bokeh", "L2城"),
    I("set_club_soft", "夜店柔化", "club soft gel not chaos", "L2城"),
    I("set_hotel_corridor", "酒店长廊", "hotel long corridor doors", "L2室内"),
    I("set_hotel_bath", "酒店浴室大理石", "hotel marble bath", "L2室内"),
    I("set_penthouse", "顶层公寓", "penthouse glass city night", "L2室内"),
    I("set_loft", "阁楼loft", "loft brick high ceiling", "L2室内"),
    I("set_conservatory", "玻璃房/花房", "glass conservatory plants", "L2室内"),
    I("set_attic", "阁楼斜顶", "attic sloped ceiling soft", "L2室内"),
    I("set_garage", "车库", "garage concrete car soft", "L2室内"),
    I("set_warehouse", "仓库巨构", "warehouse industrial scale", "L2室内"),
    I("set_greenhouse", "温室", "greenhouse glass plants humid", "L2户外"),
    I("set_flower_field", "花海", "flower field horizon", "L2户外"),
    I("set_bamboo", "竹林", "bamboo forest path", "L2户外"),
    I("set_snow", "雪地", "snow field soft cold light", "L2户外"),
    I("set_desert", "沙漠戈壁", "desert dune scale", "L2户外"),
    I("set_cliff", "悬崖山脊", "cliff ridge tiny figure option", "L2户外"),
    I("set_pier", "码头栈桥", "wooden pier water", "L2户外"),
    I("set_ferry", "轮渡甲板", "ferry deck rail wind", "L2户外"),
    I("set_temple", "寺社旅拍尊重", "temple gate respectful pose", "L2户外"),
    I("set_hutong", "胡同", "hutong gray brick wires", "L2户外"),
    I("set_jiangnan", "江南水巷", "jiangnan canal white walls", "L2户外"),
    I("set_onsen_outdoor", "露天温泉", "outdoor onsen steam night", "L2特殊"),
    I("set_yacht", "游艇甲板", "yacht deck sea luxury", "L2特殊"),
    I("set_private_jet", "私人飞机舱点名", "private jet cabin interior", "L2特殊"),
    I("set_classroom_adult", "教室成人RP", "classroom adult roleplay empty", "L2特殊"),
    I("set_office_desk", "办公桌夜", "office desk after hours", "L2特殊"),
    I("set_server_room", "机房冷光", "server room cold LED", "L2特殊"),
]

# ── LIGHT 扩 ─────────────────────────────────────────────────
LIGHT_X = [
    I("lt_window_north", "北窗柔", "north window soft even", "L2自然"),
    I("lt_sunset_rim", "日落缘光", "sunset strong rim warm", "L2自然"),
    I("lt_moon_soft", "月光感", "moonlight cool soft dim", "L2自然"),
    I("lt_streetlamp", "路灯顶", "streetlamp overhead night", "L2实用"),
    I("lt_shop_window", "橱窗光", "shop window spill warm", "L2实用"),
    I("lt_vending", "贩卖机光", "vending machine glow night", "L2实用"),
    I("lt_fridge", "冰箱冷光", "open fridge cool spill", "L2实用"),
    I("lt_tv_flicker", "电视闪烁", "TV flicker cool room", "L2实用"),
    I("lt_fairy", "灯串氛围", "fairy string lights bokeh", "L2实用"),
    I("lt_paper_lantern", "纸灯笼", "paper lantern warm diffuse", "L2实用"),
    I("lt_three_point", "三点布光", "three-point key fill back", "L2棚"),
    I("lt_butterfly_no_fill", "蝶形无补", "butterfly no fill drama", "L2棚"),
    I("lt_loop_left", "环形左主", "loop key camera-left", "L3方位"),
    I("lt_loop_right", "环形右主", "loop key camera-right", "L3方位"),
    I("lt_rembrandt_left", "伦勃朗左", "Rembrandt camera-left", "L3方位"),
    I("lt_rembrandt_right", "伦勃朗右", "Rembrandt camera-right", "L3方位"),
    I("lt_split_left", "分割左亮", "split light left bright", "L3方位"),
    I("lt_kicker", "勾边灯", "kicker edge light hair", "L2棚"),
    I("lt_hair_light", "发灯", "dedicated hair light separation", "L2棚"),
    I("lt_background_light", "背景灯", "background light gradient", "L2棚"),
    I("lt_ring", "环形灯自拍", "ring light catchlight circles", "L2棚"),
    I("lt_led_panel", "LED平板", "LED panel soft continuous", "L2棚"),
    I("lt_strobe_hard", "频闪硬", "hard strobe specular", "L2棚"),
    I("lt_proj_gobo", "投影gobos", "gobo projected pattern", "L3光效"),
    I("lt_prism", "棱镜光斑", "prism flare color spots", "L3光效"),
    I("lt_lens_flare", "镜头眩光", "controlled lens flare", "L3光效"),
    I("lt_rain_reflect", "雨地反光", "rain ground reflections", "L3光效"),
]

# ── CAM 扩 ───────────────────────────────────────────────────
CAM_X = [
    I("cam_wide_full", "广角全身略畸变控", "wide full body controlled distortion", "L2景别"),
    I("cam_detail_hands", "手部特写", "detail close-up hands", "L2景别"),
    I("cam_detail_eyes", "眼部特写", "extreme close-up eyes", "L2景别"),
    I("cam_detail_lips", "唇部特写", "extreme close-up lips", "L2景别"),
    I("cam_detail_fabric", "面料特写", "fabric texture macro-ish", "L2景别"),
    I("cam_pov_partner", "POV对方视角", "POV from partner eyes", "L2角度"),
    I("cam_worm", "虫视极仰", "worm's-eye extreme low", "L2角度"),
    I("cam_bird", "鸟瞰", "bird's-eye high down", "L2角度"),
    I("cam_dutch_soft", "微荷兰角", "slight dutch imbalance", "L2角度"),
    I("ar_45", "画幅4:5", "vertical 4:5 instagram", "L2画幅"),
    I("ar_67", "画幅6:7中画幅感", "6:7 medium format feel", "L2画幅"),
    I("lens_28", "焦感28", "28mm documentary wide", "L3焦段"),
    I("lens_40", "焦感40", "40mm natural mild", "L3焦段"),
    I("lens_70", "焦感70", "70mm short tele", "L3焦段"),
    I("lens_100_macro", "焦感100微距", "100mm macro beauty detail", "L3焦段"),
    I("lens_200", "焦感200压缩", "200mm heavy compression", "L3焦段"),
    I("dof_f14", "光圈感f1.4极浅", "f1.4 extreme shallow", "L3光学"),
    I("dof_f28", "光圈感f2.8", "f2.8 moderate shallow", "L3光学"),
    I("dof_f8", "光圈感f8深", "f8 deeper scene", "L3光学"),
    I("comp_golden", "构图黄金分割", "golden ratio placement", "L3构图"),
    I("comp_sym", "构图对称", "symmetry centered formal", "L3构图"),
    I("comp_diagonal", "构图对角", "diagonal dynamic line", "L3构图"),
    I("comp_layer_fg", "构图前景遮挡", "foreground occluder soft", "L3构图"),
    I("comp_reflection", "构图倒影", "reflection double read", "L3构图"),
]

# ── GRADE 扩 ─────────────────────────────────────────────────
GRADE_X = [
    I("grade_teal_orange_hard", "青橙电影重", "strong teal-orange cinematic", "L2调色"),
    I("grade_matrix_green", "矩阵绿感", "matrix green tint controlled", "L2调色"),
    I("grade_bleach_bypass", "漂白旁路", "bleach bypass contrast desat", "L2调色"),
    I("grade_cross_process", "交叉冲印感", "cross-process color shift", "L2调色"),
    I("grade_kodachrome", "柯达色正感", "kodachrome-like vivid warm", "L2调色"),
    I("grade_fuji_green", "富士绿偏", "fuji green-cool bias", "L2调色"),
    I("grade_cinestill", "CineStill夜红", "cinestill night red halo soft", "L2调色"),
    I("grade_gold_luxe", "金色奢华", "gold luxe warm highlights", "L2调色"),
    I("grade_silver", "银色冷金属", "silver cool metallic", "L2调色"),
    I("grade_sepia", "棕褐怀旧", "sepia warm nostalgia", "L2调色"),
    I("grade_duo_blue", "双色调蓝", "blue duotone", "L2调色"),
    I("grade_duo_red", "双色调红", "red duotone soft", "L2调色"),
    I("grade_low_sat_skin", "低饱和保肤", "low sat keep skin hue", "L2调色"),
    I("grade_hdr_soft", "软HDR", "soft HDR balanced", "L2调色"),
    I("grade_log_flat", "Log平调感", "log-flat low contrast base", "L2调色"),
    I("grade_vintage_fade", "复古褪色", "vintage fade lifted blacks", "L2调色"),
    I("grade_night_blue", "夜蓝调", "night blue cast", "L2调色"),
    I("grade_candle_warm", "烛暖调", "candle extreme warm", "L2调色"),
    I("grain_heavy", "重颗粒", "heavy film grain", "L3质感"),
    I("grain_16mm", "16mm颗粒", "16mm grain texture", "L3质感"),
    I("vignette_soft", "柔暗角", "soft vignette", "L3质感"),
    I("chromatic_soft", "轻色差", "soft chromatic aberration edge", "L3质感"),
]

# ── Youth 专属扩 ─────────────────────────────────────────────
YOUTH_ACT_X = [
    I("act_change_clothes", "换装中", "mid clothing change freeze covered", "专属行为"),
    I("act_skincare", "护肤步骤", "skincare dropper freeze", "专属行为"),
    I("act_read_bed", "床上阅读", "reading in bed soft", "专属行为"),
    I("act_cook_morning", "晨厨", "morning kitchen light task", "专属行为"),
    I("act_return_night", "夜归进门", "night return doorway", "专属行为"),
    I("act_bath_edge", "浴缸沿坐", "tub edge sit covered", "专属行为"),
    I("act_balcony_smoke_soft", "阳台夜风", "balcony night wind soft", "专属行为"),
]
YOUTH_FOCUS_X = [
    I("focus_ear", "耳廓", "ear helix light soft", "专属暗示"),
    I("focus_wrist", "腕骨", "wrist bone bracelet", "专属暗示"),
    I("focus_ankle", "踝", "ankle line soft", "专属暗示"),
    I("focus_back_line", "背沟线", "soft back midline covered", "专属暗示"),
    I("focus_hip_bone", "胯骨", "hip bone edge fabric", "专属暗示"),
]
YOUTH_AES_X = [
    I("aes_tomato", "番茄女孩", "tomato girl warm summer", "专属美学"),
    I("aes_mob_wife", "Mob Wife软", "mob wife soft glam SFW", "专属美学"),
    I("aes_dopamine", "多巴胺色", "dopamine bright color joy", "专属美学"),
    I("aes_old_money_soft", "老钱软欲", "old money soft desire", "专属美学"),
    I("aes_acubi", "Acubi冷", "acubi cool dark soft", "专属美学"),
    I("aes_douyin_pure", "抖音纯欲标签", "douyin pure-desire tag shell", "专属美学"),
    I("aes_weishuyan", "伪素颜", "fake bare-face polished", "专属美学"),
    I("aes_yanxi", "盐系", "yanxi salt cool low smile", "专属美学"),
    I("aes_tangxi", "糖系", "tangxi sweet soft blush", "专属美学"),
    I("aes_lengbaipi", "冷白皮", "cool fair skin read", "专属美学"),
]

# ── Erotic 专属扩 ────────────────────────────────────────────
EROTIC_ACT_X = [
    I("act_69", "六九", "sixty-nine mutual oral freeze", "专属行为"),
    I("act_facesitting", "颜面骑乘", "facesitting hips over face", "专属行为"),
    I("act_spitroast", "两头", "spitroast oral and rear", "专属行为"),
    I("act_dp", "双插入点名", "double penetration two junctions", "专属行为"),
    I("act_amazon", "亚马逊体位", "amazon woman-on-top control", "专属体位"),
    I("act_pretzel", "麻花体位", "pretzel entangled limbs", "专属体位"),
    I("act_butterfly_hips", "蝶式抬髋", "butterfly hips edge bed", "专属体位"),
    I("act_standing_carry", "抱起站立", "standing carry hold", "专属体位"),
    I("act_table_edge", "桌沿", "table edge support", "专属体位"),
    I("act_shower_wall", "淋浴墙", "shower wall standing", "专属体位"),
    I("act_car_seat", "车座折叠", "car seat cramped fold", "专属体位"),
    I("act_mirror_sex", "镜前做", "mirror sex reflection match", "专属行为"),
    I("act_phone_record", "自拍录像感", "phone record performative", "专属行为"),
    I("act_toy_insert", "玩具在位", "toy inserted visible base", "专属行为"),
    I("act_fingering", "手指进入", "fingers entering wet", "专属行为"),
    I("act_grinding", "隔衣磨", "grinding clothed friction", "专属行为"),
]
EROTIC_FANTASY_X = [
    I("fan_lamia", "蛇女", "lamia coils adult", "专属幻想"),
    I("fan_mermaid", "人鱼", "mermaid wet scales adult", "专属幻想"),
    I("fan_vampire", "吸血鬼", "vampire soft bite mark", "专属幻想"),
    I("fan_demoness", "女恶魔", "demoness horns tail adult", "专属幻想"),
    I("fan_angel_fallen", "堕天使", "fallen angel torn wings", "专属幻想"),
    I("fan_witch", "魔女", "witch circle candles", "专属幻想"),
    I("fan_possession", "附身", "possession eyes glow self hands", "专属幻想"),
    I("fan_hypno", "催眠螺旋", "hypno spiral eyes service", "专属幻想"),
    I("fan_tentacle_altar", "触手祭坛", "tentacle altar binding circle", "专属幻想"),
    I("fan_slime_pink", "粉史莱姆", "pink slime translucent", "专属幻想"),
    I("fan_plant_vine", "藤缚", "living vine bind forest", "专属幻想"),
    I("fan_shadow_hands", "影手", "shadow hands spread", "专属幻想"),
]
EROTIC_DYNAMIC_X = [
    I("dyn_blindfold", "蒙眼", "blindfold heighten touch", "专属权力"),
    I("dyn_gag_soft", "口塞点名", "soft gag adult play", "专属权力"),
    I("dyn_hair_pull", "抓发", "hair pull scalp", "专属权力"),
    I("dyn_choke_soft", "轻扼颈点名", "soft hand on throat careful", "专属权力"),
    I("dyn_praise", "夸奖服从", "praise kink soft eyes", "专属权力"),
    I("dyn_orgasm_control", "高潮控制", "edged denied peak freeze", "专属权力"),
]
FIGURE_ZONE_X = [
    # zone stays A-I; add intensity-like tags as figure specialty extras via makeup already
    I("zone_tag_editorial", "标签·编辑时尚", "editorial fashion tag within zone", "专属标签"),
    I("zone_tag_lookbook", "标签·lookbook", "lookbook clean catalog", "专属标签"),
    I("zone_tag_campaign", "标签·大片广告", "campaign hero poster", "专属标签"),
    I("zone_tag_candid", "标签·抓拍纪实", "candid documentary tag", "专属标签"),
    I("zone_tag_sport_ad", "标签·运动广告", "sport brand ad tag", "专属标签"),
]


def merge(base: list, extra: list) -> list:
    seen = {x["id"] for x in base}
    out = list(base)
    for x in extra:
        if x["id"] not in seen:
            out.append(x)
            seen.add(x["id"])
    return out
