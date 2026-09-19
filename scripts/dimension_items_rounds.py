# -*- coding: utf-8 -*-
"""至少 5 轮全网加厚：R1 内衣/衣着细 · R2 中式/城市场 · R3 姿手光 · R4 发妆表调色 · R5 专属+主体+道具。
全部挂 L2/L3/L4/L5 分组标签。仅成人 18+。
"""
from __future__ import annotations


def I(id: str, label: str, en: str, group: str = "") -> dict:
    d = {"id": id, "label": label, "en": en}
    if group:
        d["group"] = group
    return d


# ════════════════════════════════════════════════════════════
# ROUND 1 · 衣着 L2/L3/L4/L5 内衣·礼服·运动·鞋配再厚
# ════════════════════════════════════════════════════════════
R1_CLOTH = [
    # 内衣品类（联网 lingerie taxonomy）
    I("lin_bra_balconette", "内衣·半杯/阳台杯", "balconette bra lift adult", "L3内衣"),
    I("lin_bra_pushup", "内衣·聚拢", "push-up bra full", "L3内衣"),
    I("lin_bra_softcup", "内衣·软杯无钢圈", "soft-cup wireless bra", "L3内衣"),
    I("lin_bralette", "内衣·bralette", "bralette soft unlined", "L3内衣"),
    I("lin_bustier", "内衣·bustier束衣", "bustier structured torso", "L3内衣"),
    I("lin_corset", "内衣·胸衣corset", "corset laced waist adult", "L3内衣"),
    I("lin_teddy", "内衣·teddy连体", "lace teddy one-piece", "L3内衣"),
    I("lin_bodysuit", "内衣·bodysuit", "lingerie bodysuit snap", "L3内衣"),
    I("lin_chemise", "内衣·chemise衬裙", "silk chemise slip night", "L3内衣"),
    I("lin_babydoll", "内衣·babydoll", "babydoll sheer overlay adult", "L3内衣"),
    I("lin_garter_belt", "内衣·吊袜带", "garter belt straps stockings", "L3内衣"),
    I("lin_stockings", "内衣·长筒丝袜", "thigh-high sheer stockings", "L3内衣"),
    I("lin_pantyhose", "内衣·连裤丝袜", "pantyhose sheer or opaque", "L3内衣"),
    I("lin_panty_brief", "内衣·三角/高腰", "briefs or high-waist panty", "L3内衣"),
    I("lin_thong", "内衣·丁字", "thong minimal", "L3内衣"),
    I("lin_open_cup", "内衣·开杯点名", "open-cup bra still strapped", "L3内衣"),
    I("lin_mesh_set", "内衣·网纱套", "mesh lingerie set", "L3内衣"),
    I("lin_satin_set", "内衣·缎面套", "satin lingerie set", "L3内衣"),
    I("lin_lace_set", "内衣·蕾丝套", "full lace lingerie set", "L3内衣"),
    I("lin_harness_soft", "内衣·软束带", "soft harness straps fashion", "L3内衣"),
    # 礼服/正装
    I("form_cocktail", "礼服·鸡尾酒短", "cocktail dress knee", "L3礼服"),
    I("form_evening", "礼服·晚宴长", "evening gown floor", "L3礼服"),
    I("form_slit_gown", "礼服·高开衩", "high-slit evening gown", "L3礼服"),
    I("form_suit_dress", "礼服·西装裙套", "formal skirt suit", "L3礼服"),
    I("form_tuxedo_soft", "礼服·女烟装配", "soft tuxedo look woman", "L3礼服"),
    I("form_wedding_guest", "礼服·婚礼宾客", "wedding guest formal soft", "L3礼服"),
    # 运动细
    I("sport_yoga_set", "运动·瑜伽套", "yoga set matching soft", "L3运动"),
    I("sport_run_kit", "运动·跑步套", "running kit shorts tank", "L3运动"),
    I("sport_tennis_set", "运动·网球套", "tennis skirt polo set", "L3运动"),
    I("sport_swim_one", "泳装·连体", "one-piece swimsuit", "L3泳装"),
    I("sport_swim_bi", "泳装·分体", "bikini two-piece adult", "L3泳装"),
    I("sport_swim_cover", "泳装·罩衫", "swim cover-up sheer", "L3泳装"),
    I("sport_ski", "运动·滑雪时尚", "ski fashion layers", "L3运动"),
    I("sport_cycle", "运动·骑行套", "cycling kit jersey", "L3运动"),
    # 鞋 L4 再扩
    I("foot_espadrille", "鞋·草编", "espadrilles summer", "L4鞋"),
    I("foot_kitten", "鞋·猫跟", "kitten heels low", "L4鞋"),
    I("foot_wedge", "鞋·坡跟", "wedge heels", "L4鞋"),
    I("foot_thigh_boot", "鞋·过膝高跟靴", "thigh-high boots", "L4鞋"),
    I("foot_sock_boots", "鞋·袜靴", "sock boots stretch", "L4鞋"),
    I("foot_croc_soft", "鞋·洞洞/休闲点名", "casual clog soft adult", "L4鞋"),
    # 衣色图案 L5
    I("col_beige", "衣色·卡其杏", "beige khaki clothing", "L5衣色"),
    I("col_gray", "衣色·灰", "gray clothing", "L5衣色"),
    I("col_pink", "衣色·粉", "soft pink clothing", "L5衣色"),
    I("col_green", "衣色·绿", "green clothing", "L5衣色"),
    I("col_purple", "衣色·紫", "purple clothing soft", "L5衣色"),
    I("col_gold", "衣色·金色点缀", "gold accent clothing", "L5衣色"),
    I("pat_polka", "纹·波点", "polka dot print", "L5图案"),
    I("pat_animal", "纹·动物纹点名", "animal print controlled", "L5图案"),
    I("pat_abstract", "纹·抽象", "abstract print fashion", "L5图案"),
    I("fab_cashmere", "料·羊绒", "cashmere soft knit", "L5面料"),
    I("fab_tweed_check", "料·格子花呢", "checked tweed", "L5面料"),
    I("fab_pvc_soft", "料·软PVC点名", "soft PVC shine fashion", "L5面料"),
]

# ════════════════════════════════════════════════════════════
# ROUND 2 · 场景 L2/L3 中式城市+自然+室内
# ════════════════════════════════════════════════════════════
R2_SET = [
    I("set_bund", "场·上海外滩", "Shanghai Bund skyline night or day", "L3地标"),
    I("set_lujiazui", "场·陆家嘴", "Lujiazui towers glass", "L3地标"),
    I("set_wukang", "场·武康路", "Wukang road plane tree street", "L3地标"),
    I("set_yu_garden", "场·豫园城隍", "Yu Garden traditional roofs", "L3地标"),
    I("set_westlake", "场·西湖", "West Lake willow causeway", "L3地标"),
    I("set_hongya", "场·洪崖洞", "Hongyadong night stilt lights", "L3地标"),
    I("set_kuanzhai", "场·宽窄巷子", "Kuanzhai alleys Chengdu", "L3地标"),
    I("set_hutong_nanluo", "场·南锣鼓巷感", "hutong tourist street soft", "L3地标"),
    I("set_gugong_out", "场·故宫外景尊重", "Forbidden City exterior respectful tourist adult", "L3地标"),
    I("set_greatwall", "场·长城点景", "Great Wall ridge scale figure", "L3地标"),
    I("set_galaxy_soho", "场·Galaxy Soho感", "curved modern mall architecture", "L3地标"),
    I("set_chongqing_cyber", "场·重庆赛博感", "Chongqing multi-level cyberpunk city", "L3地标"),
    I("set_liziba", "场·李子坝穿楼", "train through building viewpoint", "L3地标"),
    I("set_suzhou_garden", "场·苏州园林", "Suzhou classical garden corridor", "L3地标"),
    I("set_xiamen_gulang", "场·鼓浪屿", "Gulangyu colonial street sea", "L3地标"),
    I("set_shenzhen_bay", "场·深圳湾", "Shenzhen bay tech skyline", "L3地标"),
    I("set_guangzhou_tower", "场·广州塔远", "Canton Tower distant skyline", "L3地标"),
    I("set_nanjing_confu", "场·夫子庙秦淮", "Confucius temple Qinhuai lanterns", "L3地标"),
    I("set_xi_an_wall", "场·西安城墙", "Xi'an city wall bike path", "L3地标"),
    I("set_qingdao_sea", "场·青岛海边", "Qingdao sea promenade red roofs", "L3地标"),
    I("set_bookstore_chain", "场·大型书店中庭", "multi-floor bookstore atrium", "L3室内"),
    I("set_capsule_hotel", "场·胶囊旅馆", "capsule hotel corridor LED", "L3室内"),
    I("set_manga_cafe", "场·漫画咖", "manga cafe booth soft", "L3室内"),
    I("set_sauna", "场·桑拿休息区", "sauna lounge towel adult", "L3室内"),
    I("set_spa", "场·水疗", "spa treatment room soft", "L3室内"),
    I("set_nail_salon", "场·美甲店", "nail salon pink chairs", "L3室内"),
    I("set_hair_salon", "场·理发店镜", "hair salon mirror cape", "L3室内"),
    I("set_tattoo_shop", "场·纹身店", "tattoo shop chairs art walls", "L3室内"),
    I("set_photo_booth", "场·拍贴机", "purikura photo booth interior", "L3室内"),
    I("set_vr_arcade", "场·VR厅", "VR arcade neon soft", "L3室内"),
    I("set_rooftop_bar", "场·天台酒吧", "rooftop bar skyline drinks", "L3城"),
    I("set_underground_mall", "场·地下街", "underground mall corridor", "L3城"),
    I("set_bike_share", "场·共享单车点", "bike share dock street", "L3城"),
    I("set_charging_station", "场·充电站夜", "EV charging night LED", "L3城"),
    I("set_rain_alley", "场·雨巷", "rain alley umbrellas wet", "L3城"),
    I("set_sakura_path", "场·樱花道", "sakura path petals adult", "L3户外"),
    I("set_ginkgo", "场·银杏道", "ginkgo yellow path", "L3户外"),
    I("set_maple", "场·红叶", "maple red autumn", "L3户外"),
    I("set_lavender", "场·薰衣草", "lavender field purple", "L3户外"),
    I("set_rice_terrace", "场·梯田", "rice terrace scale", "L3户外"),
    I("set_hot_spring_town", "场·温泉小镇", "onsen town wooden streets", "L3户外"),
    I("set_ski_resort", "场·雪场酒店", "ski resort lodge snow", "L3户外"),
    I("set_camp_glamp", "场·露营/轻奢露营", "glamping tent fairy lights", "L3户外"),
    I("set_observatory", "场·天文台感", "observatory dome night", "L3户外"),
    I("set_aquarium", "场·水族馆", "aquarium blue tank glow", "L3特殊"),
    I("set_zoo_soft", "场·动物园外围", "zoo soft path adult casual", "L3特殊"),
    I("set_theme_park", "场·乐园广场", "theme park plaza soft crowd", "L3特殊"),
    I("set_stadium", "场·体育场空场", "empty stadium seats scale", "L3特殊"),
    I("set_church_exterior", "场·教堂外景", "church exterior soft tourist", "L3特殊"),
    I("set_castle_soft", "场·城堡旅拍", "castle tourist soft adult", "L3特殊"),
]

# ════════════════════════════════════════════════════════════
# ROUND 3 · 姿势 L2/L3 + 光 L3 + 镜头 L3
# ════════════════════════════════════════════════════════════
R3_POSE = [
    I("pose_power_hip", "站·手叉腰强", "both hands hips power soft", "L2站"),
    I("pose_model_angle", "站·模特45收下巴", "model 45 chin soft forward", "L2站"),
    I("pose_weight_front", "站·前脚重心", "weight front foot soft", "L2站"),
    I("pose_crossed_ankle", "站·交踝", "ankles crossed standing", "L2站"),
    I("pose_kick_heel", "站·轻踢脚跟", "soft heel kick back", "L3细姿"),
    I("pose_step_up", "站·一脚台阶", "one foot higher step", "L3细姿"),
    I("pose_walk_look_down", "走·低头中步", "midstride gaze down phone", "L2走"),
    I("pose_walk_bag", "走·提袋中步", "midstride shopping bags", "L2走"),
    I("pose_lean_forehead_wall", "靠·额贴墙", "forehead near wall soft", "L2靠"),
    I("pose_lean_back_hands", "靠·双手后撑", "hands behind on wall lean", "L2靠"),
    I("pose_sit_table_chin_two", "坐·双手托腮", "both hands under chin table", "L2坐"),
    I("pose_sit_legs_extend", "坐·伸腿", "legs extended seated soft", "L2坐"),
    I("pose_sit_side_lean", "坐·侧倾", "side lean on sofa arm", "L2坐"),
    I("pose_floor_sprawl", "地·舒展躺", "floor soft sprawl modest", "L2坐"),
    I("pose_bed_crawl", "床·膝行前倾", "kneel-crawl on bed forward", "L2镜床"),
    I("pose_bed_roll", "床·侧滚定格", "mid roll on bed freeze", "L2镜床"),
    I("pose_mirror_squat", "镜·半蹲自拍", "mirror squat selfie pose", "L2镜床"),
    I("pose_yoga_down_dog", "瑜伽·下犬", "downward dog asana", "L2运动"),
    I("pose_yoga_warrior", "瑜伽·战士", "warrior pose lunge", "L2运动"),
    I("pose_stretch_quad", "拉伸·股四", "standing quad stretch", "L2运动"),
    I("pose_boxing_guard", "拳击·戒备", "boxing guard stance", "L2运动"),
    I("pose_ballet_releve", "芭蕾·半脚尖", "ballet relevé soft adult", "L2表演"),
    I("pose_ballet_arabesque", "芭蕾·阿拉贝斯克", "arabesque line adult", "L2表演"),
    I("pose_hiphop_freeze", "街舞·定格", "hip-hop freeze power", "L2表演"),
    I("pose_instrument_violin", "乐器·提琴", "violin under chin bow", "L3任务"),
    I("pose_instrument_piano", "乐器·钢琴", "piano hands keys freeze", "L3任务"),
    I("pose_chef_toss", "职业·颠锅", "chef pan toss freeze", "L3任务"),
    I("pose_lab_pipette", "职业·移液", "lab pipette mid-task PPE", "L3任务"),
    I("pose_teacher_board", "职业·讲台", "teacher gesture board adult", "L3任务"),
]
R3_LIGHT = [
    I("lt_key_45_left", "主光45左", "key 45 degrees camera-left", "L3方位"),
    I("lt_key_45_right", "主光45右", "key 45 degrees camera-right", "L3方位"),
    I("lt_key_above", "主光正上", "key directly above slight front", "L3方位"),
    I("lt_fill_weak", "弱补光", "weak fill ratio 4:1 drama", "L3光比"),
    I("lt_fill_strong", "强补光", "strong fill ratio 2:1 soft", "L3光比"),
    I("lt_no_fill", "无补光", "no fill deep shadow", "L3光比"),
    I("lt_reflector_silver", "银反光板", "silver reflector kick", "L3辅光"),
    I("lt_reflector_gold", "金反光板", "gold reflector warm kick", "L3辅光"),
    I("lt_reflector_white", "白反光板", "white reflector soft fill", "L3辅光"),
    I("lt_black_flag", "黑旗减光", "black flag negative fill", "L3辅光"),
    I("lt_soft_1x1", "1x1柔光", "1x1 soft LED panel", "L3器材感"),
    I("lt_octa", "八角柔光箱", "octabox large soft", "L3器材感"),
    I("lt_strip", "长条柔光", "strip softbox edge", "L3器材感"),
    I("lt_snoot", "束光筒", "snoot spot accent", "L3器材感"),
    I("lt_grid", "蜂巢", "grid control spill", "L3器材感"),
    I("lt_ctb", "CTB冷校", "CTB cool gel", "L3色温"),
    I("lt_cto", "CTO暖校", "CTO warm gel", "L3色温"),
    I("lt_magenta_gel", "品红凝胶", "magenta gel accent", "L3色温"),
    I("lt_cyan_gel", "青色凝胶", "cyan gel accent", "L3色温"),
]
R3_CAM = [
    I("cam_slider_feel", "轨道横移感", "slider lateral still frame feel", "L3运动感"),
    I("cam_handheld_breath", "手持呼吸感", "handheld slight imperfect frame", "L3运动感"),
    I("cam_tripod_lock", "三脚架锁定", "locked tripod perfect level", "L3运动感"),
    I("cam_drone_feel", "航拍感", "drone high angle tiny figure", "L2角度"),
    I("cam_cctv_feel", "监控俯视感", "CCTV high corner angle", "L2角度"),
    I("cam_security_soft", "门禁镜头感", "door cam slight wide", "L2角度"),
    I("comp_rule_space", "构图动向留白", "lead room in gaze direction", "L3构图"),
    I("comp_headroom", "构图头顶空间", "correct headroom", "L3构图"),
    I("comp_crop_waist", "构图腰裁", "intentional waist crop", "L3构图"),
    I("comp_crop_tight_face", "构图紧脸", "tight face crop beauty", "L3构图"),
    I("comp_dutch_env", "构图环境荷兰", "dutch with strong environment line", "L3构图"),
]

# ════════════════════════════════════════════════════════════
# ROUND 4 · 发·妆·表·调色 L2/L3 再厚
# ════════════════════════════════════════════════════════════
R4_HAIR = [
    I("hair_silk_press", "直发丝熨感", "silk press ultra sleek", "L2造型"),
    I("hair_blowout_volume", "大吹塑", "salon blowout volume crown", "L2造型"),
    I("hair_flat_iron_wave", "夹板波浪", "flat-iron soft bends", "L2造型"),
    I("hair_roller_set", "发卷定型", "roller set soft curls", "L2造型"),
    I("hair_braid_box_soft", "软脏辫成人", "soft box braids adult fashion", "L2造型"),
    I("hair_cornrow_soft", "软玉米辫", "soft cornrows adult", "L2造型"),
    I("hair_afro_soft", "软爆炸头", "soft afro volume adult", "L2造型"),
    I("hair_loc_soft", "软脏辫loc", "soft locs adult", "L2造型"),
    I("hair_buzz_fashion", "寸头时尚点名", "fashion buzz adult", "L2造型"),
    I("hair_undercut_design", "侧铲图案点名", "undercut design adult", "L2造型"),
    I("state_towel_wrap", "毛巾包发", "towel wrap turban damp", "L3发态"),
    I("state_shower_cap", "浴帽点名", "shower cap humorous adult", "L3发态"),
    I("state_headphones_over", "头戴耳机压发", "over-ear headphones on hair", "L3发态"),
    I("col_highlight_face", "脸周高光发", "face-framing highlights", "L3发色"),
    I("col_peekaboo", "内层挑染", "peekaboo underlights", "L3发色"),
    I("col_ombre", "渐变染", "ombre dark to light", "L3发色"),
    I("col_reverse_ombre", "反向渐变", "reverse ombre light roots", "L3发色"),
]
R4_MAKEUP = [
    I("mk_glass_body", "水光身体高光", "body glass sheen shoulders", "L2妆壳"),
    I("mk_tan_soft", "轻仿晒", "soft faux tan even", "L2妆壳"),
    I("mk_editorial_color", "编辑彩妆", "editorial color eye soft", "L2妆壳"),
    I("mk_runway_clean", "走秀干净", "runway clean strong brow", "L2妆壳"),
    I("mk_period_soft", "年代妆软", "period makeup soft adult", "L2妆壳"),
    I("mk_cyber_soft", "赛博淡彩", "soft cyber liner accent", "L2妆壳"),
    I("part_lip_liner", "件·唇线", "defined lip liner soft fill", "L3妆件"),
    I("part_overlip", "件·外扩唇", "soft overlined lip adult", "L3妆件"),
    I("part_bottom_lash", "件·下睫毛", "bottom lash emphasis", "L3妆件"),
    I("part_white_liner", "件·白色眼线", "white waterline brighten", "L3妆件"),
    I("part_stamp_freckle", "件·点斑", "stamped freckles soft", "L3妆件"),
    I("part_highlight_inner", "件·内眼角高光", "inner corner highlight", "L3妆件"),
]
R4_EXPR = [
    I("expr_think", "思考托腮", "thinking chin hand soft", "L2表情"),
    I("expr_surprise_soft", "轻惊喜", "soft surprise brows up", "L2表情"),
    I("expr_skeptical", "怀疑挑眉", "skeptical one brow", "L2表情"),
    I("expr_flirty_wink", "轻眨眼", "soft wink adult", "L2表情"),
    I("expr_cry_soft", "含泪不哭", "glassy almost-tears soft", "L2表情"),
    I("expr_after_kiss", "吻后失神", "post-kiss dazed lips", "L2分轨"),
    I("expr_mid_moan", "轻吟定格", "soft open mouth mid-breath", "L2分轨"),
    I("expr_eye_roll_soft", "轻翻白眼欲", "soft eye roll pleasure not ahegao", "L2分轨"),
]
R4_GRADE = [
    I("grade_portra160", "Portra160暖肤", "Portra 160 warm soft skin", "L2胶片"),
    I("grade_portra400", "Portra400平衡", "Portra 400 balanced versatile", "L2胶片"),
    I("grade_portra800", "Portra800夜暖", "Portra 800 low light warm", "L2胶片"),
    I("grade_ektar", "Ektar高饱和", "Ektar vivid contrast", "L2胶片"),
    I("grade_gold200", "Gold200怀旧暖", "Kodak Gold 200 nostalgic warm", "L2胶片"),
    I("grade_fuji400h", "Fuji400H绿冷肤", "Fuji 400H cool green skin soft", "L2胶片"),
    I("grade_fuji_c200", "FujiC200", "Fuji C200 everyday", "L2胶片"),
    I("grade_cinestill800t", "CineStill800T红晕", "CineStill 800T tungsten red halo", "L2胶片"),
    I("grade_cinestill50d", "CineStill50D日光", "CineStill 50D daylight rich", "L2胶片"),
    I("grade_cinestill400d", "CineStill400D", "CineStill 400D portrait soft", "L2胶片"),
    I("grade_tri_x", "Tri-X黑白", "Tri-X grainy bw", "L2胶片"),
    I("grade_hp5", "HP5黑白", "HP5 classic bw", "L2胶片"),
    I("grade_superia", "Superia绿偏", "Superia consumer green bias", "L2胶片"),
    I("grade_velvia", "Velvia高饱和风光", "Velvia vivid landscape", "L2胶片"),
    I("grade_provia", "Provia中性", "Provia neutral slide", "L2胶片"),
    I("grade_instagram_early", "早期IG滤镜感", "early Instagram filter soft", "L2数码"),
    I("grade_vsco_a6", "VSCO感", "VSCO soft film recipe feel", "L2数码"),
    I("grade_rec709", "Rec709视频静帧", "Rec709 video still clean", "L2数码"),
    I("grade_log_to_709", "Log转709感", "log converted contrast", "L2数码"),
    I("grade_aces_soft", "ACES电影软", "ACES soft cinematic", "L2数码"),
]

# ════════════════════════════════════════════════════════════
# ROUND 5 · 主体/道具/专属 Youth+Erotic+Figure 再厚
# ════════════════════════════════════════════════════════════
R5_SUBJECT = [
    I("eth_hapa", "混血Hapa感", "hapa mixed East Asian white adult", "L2人种"),
    I("body_soft_athletic", "运动微肉", "soft athletic not shredded", "L2体型"),
    I("cast_twins_soft", "双胞胎感双人", "twin-like duo same clothes soft", "L2人数"),
    I("cast_crowd_bokeh", "人群焦外", "dense crowd bokeh only", "L3人数"),
]
R5_PROP = [
    I("prop_switch", "游戏手柄", "game controller both hands", "L2道具"),
    I("prop_keyboard", "机械键盘", "mechanical keyboard mid-type", "L2道具"),
    I("prop_drone_remote", "无人机遥控", "drone controller outdoor", "L2道具"),
    I("prop_telescope", "望远镜", "telescope balcony night", "L2道具"),
    I("prop_binoculars", "双筒望远", "binoculars tourist", "L2道具"),
    I("prop_skateboard", "滑板", "skateboard vertical beside", "L2道具"),
    I("prop_scooter", "滑板车", "scooter handle adult", "L2道具"),
    I("prop_ebike", "电动车旁", "e-bike standing beside", "L2道具"),
    I("prop_coffee_machine", "咖啡机旁", "espresso machine soft bg", "L2道具"),
    I("prop_record_player", "黑胶机", "turntable hands soft", "L2道具"),
    I("prop_projector", "投影光", "projector beam dust soft", "L2道具"),
    I("prop_polaroid_stack", "拍立得堆", "stack of polaroids hands", "L2道具"),
    I("prop_journal", "手帐笔", "journal pen mid-write", "L2道具"),
    I("prop_tarot", "塔罗牌", "tarot cards table soft", "L2道具"),
    I("prop_crystal", "水晶", "crystal in palm soft", "L2道具"),
    I("prop_sword_prop", "道具剑点名", "prop sword costume adult", "L2道具"),
    I("prop_wand_magic", "魔杖幻想", "magic wand fantasy soft", "L2道具"),
]
R5_YOUTH = [
    I("aes_clean_rich", "干净有钱感", "clean rich quiet aesthetic", "专属美学"),
    I("aes_dark_feminine", "暗黑女性", "dark feminine soft power", "专属美学"),
    I("aes_soft_girl", "soft girl", "soft girl pastel adult", "专属美学"),
    I("aes_e_girl_soft", "e-girl软", "soft e-girl liner adult", "专属美学"),
    I("aes_cottage", "村姑core", "cottagecore meadow soft", "专属美学"),
    I("aes_coastal", "海岸孙女", "coastal granddaughter clean", "专属美学"),
    I("aes_office_minimal", "极简通勤", "minimal commute shell", "专属美学"),
    I("act_video_call", "视频通话脸", "video call screen face soft", "专属行为"),
    I("act_voice_msg", "语音条嘴型", "voice message mouth soft", "专属行为"),
    I("focus_shoulder_blade", "肩胛骨", "shoulder blade light line", "专属暗示"),
]
R5_EROTIC = [
    I("act_edge_orgasm", "边缘高潮", "edged peak freeze wet", "专属行为"),
    I("act_creampie_overflow", "中出溢流定格", "creampie overflow still", "专属行为"),
    I("act_impregnation_rp", "受孕RP合意", "breeding rp adult consensual fiction", "专属行为"),
    I("act_public_risk_hard", "强公开风险", "public risk sex half-hidden", "专属行为"),
    I("act_elevator_risk", "电梯风险", "elevator mirror risk freeze", "专属体位"),
    I("act_balcony_risk", "阳台风险", "balcony night risk soft", "专属体位"),
    I("fan_futa", "扶她点名", "futa adult anatomy clear", "专属幻想"),
    I("fan_monster_gentle", "温柔非人", "gentle monster sensual not horror", "专属幻想"),
    I("fan_giantess_soft", "巨大娘软点名", "soft giantess scale adult", "专属幻想"),
    I("dyn_cnc_play", "合意强迫play", "CNC play adult fiction soft", "专属权力"),
    I("dyn_pet_play_soft", "宠物play软", "pet play soft collar adult", "专属权力"),
    I("exp_e1_skirt_up", "E1细·裙掀", "skirt hiked half-undress", "专属E细"),
    I("exp_e1_pants_knee", "E1细·裤褪膝", "pants at knees", "专属E细"),
    I("exp_e2_garter_only", "E2细·仅吊带袜", "garter stockings only set", "专属E细"),
    I("exp_e3_aside_panty", "E3细·拨开内裤", "panties pulled aside still on", "专属E细"),
]
R5_FIGURE = [
    I("zone_tag_beauty", "标签·美妆广告", "beauty campaign tag", "专属标签"),
    I("zone_tag_jewelry", "标签·珠宝", "jewelry neck focus tag", "专属标签"),
    I("zone_tag_watch", "标签·腕表", "watch wrist hero tag", "专属标签"),
    I("zone_tag_auto", "标签·汽车", "automotive lifestyle tag", "专属标签"),
    I("zone_tag_real_estate", "标签·地产样板", "real estate lifestyle tag", "专属标签"),
    I("zone_tag_food", "标签·美食探店", "food lifestyle tag", "专属标签"),
    I("zone_tag_travel_brand", "标签·旅行品牌", "travel brand campaign", "专属标签"),
    I("zone_tag_sportswear", "标签·运动品牌", "sportswear campaign", "专属标签"),
]
R5_POSE = [
    I("pose_hand_glass", "手扶玻璃", "hand on glass window city", "L3细姿"),
    I("pose_hand_mirror", "手扶镜框", "hand on mirror frame", "L3细姿"),
    I("pose_adjust_earring", "整理耳环", "adjust earring soft", "L3细姿"),
    I("pose_adjust_strap", "整理肩带", "adjust strap freeze", "L3细姿"),
    I("pose_zip_back", "背后拉链", "hand on back zipper", "L3细姿"),
]
R5_LIGHT = [
    I("lt_golden_rim_only", "仅金缘光", "golden rim only silhouette face fill soft", "L3光效"),
    I("lt_neon_pink_blue", "粉蓝霓虹", "pink blue neon dual rim", "L3光效"),
    I("lt_candle_only", "仅烛光", "candle only warm dark", "L3光效"),
]
R5_CAM = [
    I("comp_mirror_split", "构图镜面分割", "mirror splits frame two", "L3构图"),
    I("comp_window_frame", "构图窗框", "subject in window frame", "L3构图"),
    I("comp_door_frame", "构图门框", "subject in door frame", "L3构图"),
]
R5_EXPR = [
    I("gaze_through_wine", "视线·酒杯后", "eyes over wine glass rim", "L3视线"),
    I("gaze_phone_screen", "视线·看手机屏", "eyes on phone screen glow", "L3视线"),
]
R5_MAKEUP = [
    I("mk_no_makeup_filter", "伪素滤镜感", "no-makeup filter polished still", "L2妆壳"),
]
R5_HAIR = [
    I("state_swim_cap_off", "泳帽刚摘乱发", "post swim cap messy wet", "L3发态"),
]
R5_GRADE = [
    I("grade_iphone_portrait", "手机人像模式感", "phone portrait mode soft bokeh grade", "L2数码"),
    I("grade_android_natural", "安卓自然", "android natural HDR soft", "L2数码"),
]
R5_CLOTH = [
    I("st_one_sleeve_off", "状态·单袖褪", "one sleeve off shoulder", "L3状态"),
    I("st_both_straps_down", "状态·双肩带落", "both straps down arms", "L3状态"),
    I("st_shirt_tied", "状态·衣下摆打结", "shirt hem tied waist", "L3状态"),
]


def all_round_extras() -> dict:
    """返回 {list_name: [items]} 供 merge 到 public / subject / specialty。"""
    return {
        "cloth": R1_CLOTH + R5_CLOTH,
        "set": R2_SET,
        "pose": R3_POSE + R5_POSE,
        "light": R3_LIGHT + R5_LIGHT,
        "cam": R3_CAM + R5_CAM,
        "hair": R4_HAIR + R5_HAIR,
        "makeup": R4_MAKEUP + R5_MAKEUP,
        "expr": R4_EXPR + R5_EXPR,
        "grade": R4_GRADE + R5_GRADE,
        "prop": R5_PROP,
        "eth": R5_SUBJECT,  # only eth-like in list - filter below
    }
