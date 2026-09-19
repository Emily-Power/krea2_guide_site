/**
 * 软推荐搭配（先验 Soft Prior）
 * - 来源：常见穿搭公式 / 人像摄影习惯（联网内化，非唯一真理）
 * - 用法：用户点到 trigger 时提示「推荐叠层」；一键应用可改，绝不锁死
 * - Skill 同构规则见 references/soft-recommend-priors-2026.md
 */
window.DIM_RECOMMEND = (() => {
  const r = (title, source, merge, alts) => ({
    title,
    source,
    weight: "high",
    merge,
    alts: alts || [],
  });

  /** key = `${field}:${id}` 当用户选中该 id 时弹出 */
  const byTrigger = {
    // ── cloth 品类 · 穿搭公式 ──
    "cloth:skirt": r(
      "半身裙 · 通勤/街拍高频",
      "2026：midi 百褶/缎面 + 尖头芭蕾鞋或薄底乐福 + fitted 针织/白衬衫塞衣角（锚生态 2026-Q3）",
      {
        cloth: ["skirt", "skirt_pleat", "len_midi", "st_full", "knit_cardigan", "foot_ballet", "foot_loafer"],
        pose: ["walk_midstride"],
        set: ["street_city", "cafe"],
        light: ["window_soft", "overcast"],
        hair: ["long_straight", "bang_curtain"],
        makeup: ["commute"],
        cam: ["full", "ar_34", "lens_35"],
        grade: ["natural", "jp_cream"],
        expr: ["soft_smile", "away"],
      },
      [
        {
          title: "西装铅笔裙",
          merge: {
            cloth: ["skirt", "skirt_pencil", "len_knee", "blazer_suit", "shirt_blouse", "st_full", "foot_loafer"],
            set: ["office", "street_city"],
            pose: ["stand_power", "walk_midstride"],
            makeup: ["commute", "id_neutral"],
          },
        },
        {
          title: "牛仔半裙休闲",
          merge: {
            cloth: ["skirt", "skirt_denim", "len_mini", "tee_hoodie", "st_full", "foot_sneaker"],
            set: ["street_city", "crosswalk_night"],
            pose: ["walk_midstride", "pocket"],
            grade: ["ccd", "natural"],
          },
        },
      ]
    ),
    "cloth:dress": r(
      "连衣裙 · 一体简洁",
      "穿搭：一条连衣裙 + 简鞋，少叠；外加薄开衫/风衣看季节",
      {
        cloth: ["dress", "dress_aline_midi", "len_midi", "st_full", "foot_maryjane"],
        pose: ["walk_midstride", "over_shoulder"],
        set: ["street_city", "cafe", "garden_cn"],
        light: ["window_soft", "golden"],
        hair: ["long_waves", "waves", "long_straight"],
        makeup: ["bare", "jp_bite"],
        cam: ["full", "ar_34"],
        grade: ["jp_cream", "natural"],
      },
      [
        {
          title: "丝质 slip 约会",
          merge: {
            cloth: ["dress", "dress_slip_bias", "slip", "st_full", "foot_heel_kit", "outer_coat"],
            set: ["hotel", "street_city"],
            light: ["tungsten", "neon_mix"],
            makeup: ["soft_glam", "warm_date"],
          },
        },
      ]
    ),
    "cloth:blazer_suit": r(
      "西装通勤 · 办公室公式",
      "穿搭：西装 + 衬衫/针织 + 西裤或裙 + 乐福（business casual 共识）",
      {
        cloth: ["blazer_suit", "shirt_blouse", "pants", "pants_wide", "st_full", "foot_loafer", "acc_none"],
        pose: ["stand_power", "walk_midstride", "task_work"],
        set: ["office", "street_city", "metro_transit"],
        light: ["window_soft", "softbox_studio"],
        hair: ["low_pony", "long_straight"],
        makeup: ["commute", "id_neutral"],
        cam: ["full", "medium", "ar_34"],
        grade: ["natural", "old_money"],
        prop: ["bag_tote", "none"],
        expr: ["neutral", "focus_task", "soft_smile"],
      },
      [
        {
          title: "西装 + 牛仔裤休闲",
          merge: {
            cloth: ["blazer_suit", "jeans_straight", "tee_hoodie", "st_full", "foot_loafer"],
            pose: ["walk_midstride", "pocket"],
            set: ["street_city", "cafe"],
            makeup: ["commute", "bare"],
            grade: ["natural", "ccd"],
          },
        },
        {
          title: "西装裙套",
          merge: {
            cloth: ["blazer_suit", "skirt_pencil", "shirt_blouse", "len_knee", "st_full", "foot_loafer"],
            set: ["office", "street_city"],
            pose: ["stand_power", "walk_midstride"],
            makeup: ["commute", "id_neutral"],
          },
        },
      ]
    ),
    "cloth:outer_coat": r(
      "大衣/风衣 · 层叠街拍",
      "穿搭：长外套敞开压腰线 + 内搭简 + 靴/乐福（冬装靠开压常见）",
      {
        cloth: ["outer_coat", "outer_trench", "st_layer_open", "st_full", "pants", "jeans_straight", "foot_boot_ankle"],
        pose: ["walk_midstride", "over_shoulder"],
        set: ["street_city", "metro_transit"],
        light: ["overcast", "open_shade", "golden"],
        hair: ["long_straight", "state_wind"],
        makeup: ["commute", "qingleng"],
        cam: ["full", "lens_35", "ar_34"],
        grade: ["qingleng", "natural"],
      }
    ),
    "cloth:outer_trench": r(
      "风衣 · 经典层叠",
      "穿搭：风衣 + 直筒裤/裙 + 简鞋",
      {
        cloth: ["outer_trench", "st_layer_open", "pants_straight", "shirt_blouse", "foot_loafer"],
        pose: ["walk_midstride", "lean"],
        set: ["street_city", "set_wukang"],
        light: ["overcast", "window_soft"],
        grade: ["jp_cream", "natural"],
      }
    ),
    "cloth:shirt_only": r(
      "男友衫/仅衬衫 · 居家纯欲向",
      "2026：大一码落肩衬衫当睡衣 + 袖口挽起 + 前摆半塞；上宽下窄配修身短裤；45° 窗侧光塑锁骨（锚生态 2026-Q3）",
      {
        cloth: ["shirt_only", "st_one_button", "st_few_buttons", "st_relaxed", "st_untucked", "foot_bare"],
        pose: ["mirror_self", "bed_edge", "sit_edge", "sit_cross"],
        set: ["indoor_home", "bedroom", "window_sill"],
        light: ["window_soft", "window_back", "tungsten"],
        hair: ["messy", "long_straight", "state_one_shoulder"],
        makeup: ["home_soft", "bare"],
        expr: ["half_lidded", "knowing_lens", "soft_bite"],
        cam: ["mcu", "medium", "ar_34"],
        grade: ["jp_cream", "natural"],
        prop: ["none", "phone"],
      }
    ),
    "cloth:shirt_blouse": r(
      "衬衫 · 通勤或禁欲",
      "穿搭：白衬衫 + 高腰下装；少扣则偏情绪向",
      {
        cloth: ["shirt_blouse", "pants", "st_full", "foot_loafer"],
        pose: ["stand_weight", "sit_edge"],
        set: ["office", "cafe", "window_sill"],
        light: ["window_soft", "blind_stripe"],
        hair: ["low_pony", "state_tucked_ear"],
        makeup: ["commute", "qingleng"],
      }
    ),
    "cloth:denim": r(
      "牛仔 · 休闲公式",
      "穿搭：牛仔 + tee/卫衣 + 运动鞋（基础休闲）",
      {
        cloth: ["denim", "jeans_straight", "tee_hoodie", "st_full", "foot_sneaker"],
        pose: ["walk_midstride", "pocket", "lean"],
        set: ["street_city", "cafe"],
        light: ["overcast", "flash_on"],
        grade: ["ccd", "natural"],
        cam: ["full", "lens_35"],
      }
    ),
    "cloth:sport": r(
      "运动套 · 体能可读",
      "摄影：功能姿 + 健身房/晨跑场 + 硬侧或顶光",
      {
        cloth: ["sport", "sport_yoga_set", "st_full", "foot_sneaker"],
        pose: ["athletic", "yoga_asana", "stretch"],
        set: ["gym_sport", "nature_outdoor", "street_city"],
        light: ["hard_side", "softbox_studio", "window_soft"],
        makeup: ["sport_sheer", "bare"],
        hair: ["high_pony", "messy_bun"],
        cam: ["full", "low"],
        grade: ["natural"],
      }
    ),
    "cloth:sleep": r(
      "睡衣 · 居家柔",
      "居家窗光 + 松弛姿 + 近素妆（SFW/纯欲常见）",
      {
        cloth: ["sleep", "st_relaxed", "st_full", "foot_bare"],
        pose: ["sit_cross", "lie_side", "bed_edge"],
        set: ["bedroom", "window_sill", "indoor_home"],
        light: ["window_soft", "tungsten"],
        makeup: ["home_soft", "bare"],
        hair: ["messy", "half_up"],
        expr: ["sleepy", "soft_smile"],
        cam: ["medium", "mcu", "ar_34"],
      }
    ),
    "cloth:lingerie": r(
      "内衣轮廓 · 需点名",
      "2026：半杯/网纱三件套 + 半脱状态（st_half_off）+ 钨丝低光 + 烛光补（moody cinematic）；尺度随 skill（Figure 慎）（锚生态 2026-Q3）",
      {
        cloth: ["lingerie", "lin_lace_set", "st_full", "st_half_off"],
        pose: ["bed_edge", "lie_side", "mirror_self"],
        set: ["bedroom", "hotel"],
        light: ["tungsten", "practical_lamp", "low_key"],
        makeup: ["soft_glam", "ruined"],
        expr: ["bedroom_eyes", "half_lidded"],
        cam: ["mcu", "medium"],
        grade: ["grade_candle_warm", "natural"],
      }
    ),
    "cloth:knit_cardigan": r(
      "针织开衫 · 日系层叠",
      "穿搭：开衫 + midi 裙/阔腿 + 乐福（日系空气常见）",
      {
        cloth: ["knit_cardigan", "skirt", "len_midi", "st_full", "foot_loafer"],
        set: ["cafe", "bookstore", "street_city"],
        light: ["window_soft"],
        hair: ["long_straight", "bang_wispy"],
        makeup: ["jp_bite", "bare"],
        grade: ["jp_cream"],
      }
    ),
    "cloth:old_money": r(
      "静奢名媛",
      "中性色层叠 + 克制妆 + 干净场景",
      {
        cloth: ["old_money", "outer_coat", "st_full", "foot_loafer", "acc_chain"],
        set: ["hotel", "set_hotel_corridor", "library"],
        light: ["window_soft", "softbox_studio"],
        makeup: ["id_neutral", "qianjin"],
        grade: ["old_money", "natural"],
        pose: ["stand_power", "walk_midstride"],
        expr: ["neutral", "cool"],
      }
    ),
    "cloth:pants": r(
      "西裤/阔腿 · 胶囊公式",
      "穿搭：白 T 或衬衫 + 高腰西裤/阔腿 + 乐福（Who What Wear 类经典公式）",
      {
        cloth: ["pants", "pants_wide", "tee_hoodie", "shirt_blouse", "st_full", "foot_loafer"],
        pose: ["walk_midstride", "stand_weight", "pocket"],
        set: ["street_city", "office", "cafe"],
        light: ["window_soft", "overcast"],
        makeup: ["commute", "bare"],
        cam: ["full", "ar_34", "lens_35"],
        grade: ["natural", "old_money"],
      },
      [
        {
          title: "西装叠裤气场",
          merge: {
            cloth: ["pants", "pants_wide", "blazer_suit", "shirt_blouse", "st_full", "foot_loafer"],
            pose: ["stand_power", "walk_midstride"],
            set: ["office", "street_city"],
            makeup: ["commute", "id_neutral"],
          },
        },
      ]
    ),
    "cloth:pants_wide": r(
      "阔腿裤 · 淡人公式",
      "2026 上海街拍爆火公式：米白亚麻/咖蓝 + 短一截 fitted 上装 + 旧牛津鞋/薄底乐福；细腰带强调腰线（锚生态 2026-Q3）",
      {
        cloth: ["pants_wide", "shirt_blouse", "st_full", "st_belted", "foot_oxford", "foot_loafer"],
        pose: ["walk_midstride", "stand_weight"],
        cam: ["full", "comp_foot", "ar_34"],
        set: ["street_city", "office", "cafe"],
        light: ["overcast", "window_soft"],
        grade: ["natural"],
      }
    ),
    "cloth:jeans_straight": r(
      "直筒牛仔 · polished casual",
      "穿搭：直筒牛仔 + 西装或白 T + 乐福/运动鞋（西装+牛仔裤经典公式）",
      {
        cloth: ["jeans_straight", "denim", "tee_hoodie", "st_full", "foot_sneaker"],
        pose: ["walk_midstride", "pocket", "lean"],
        set: ["street_city", "cafe"],
        light: ["overcast", "open_shade"],
        grade: ["natural", "ccd"],
      },
      [
        {
          title: "西装+牛仔裤",
          merge: {
            cloth: ["jeans_straight", "blazer_suit", "tee_hoodie", "st_full", "foot_loafer"],
            pose: ["walk_midstride", "stand_power"],
            set: ["street_city", "office"],
            makeup: ["commute"],
            grade: ["natural", "old_money"],
          },
        },
      ]
    ),
    "cloth:tee_hoodie": r(
      "白 T / 卫衣 · 2026 薄底街装",
      "2026：oversize 卫衣 + baggy/直筒牛仔 + 薄底复古跑鞋/白球鞋；前摆半扎露腰线（锚生态 2026-Q3）",
      {
        cloth: ["tee_hoodie", "jeans_straight", "st_tucked_front", "st_untucked", "foot_sneaker"],
        pose: ["walk_midstride", "pocket", "sit_edge"],
        set: ["street_city"],
        light: ["overcast", "golden", "flash_on"],
        makeup: ["bare", "commute"],
        cam: ["full", "lens_35", "ar_34"],
        grade: ["ccd", "natural"],
      },
      [
        {
          title: "卫衣 + 阔腿 + 乐福（polished casual）",
          merge: {
            cloth: ["tee_hoodie", "pants_wide", "st_full", "foot_loafer", "acc_chain"],
            set: ["street_city", "cafe"],
            pose: ["walk_midstride", "stand_weight"],
            grade: ["old_money", "natural"],
          },
        },
      ]
    ),
    "cloth:skirt_pleat": r(
      "百褶裙 · 日系通勤",
      "穿搭：百褶 midi + 针织/衬衫 + 乐福（胶囊穿搭高频）",
      {
        cloth: ["skirt_pleat", "skirt", "len_midi", "knit_cardigan", "shirt_blouse", "st_full", "foot_loafer"],
        pose: ["walk_midstride", "over_shoulder"],
        set: ["street_city", "cafe", "bookstore"],
        light: ["window_soft", "overcast"],
        makeup: ["jp_bite", "commute"],
        grade: ["jp_cream", "natural"],
        hair: ["long_straight", "bang_wispy"],
      }
    ),
    "cloth:dress_aline_midi": r(
      "A字 midi 裙 · 一键公式",
      "穿搭：midi 裙 + 乐福/平底（Who What Wear 类 failsafe）",
      {
        cloth: ["dress_aline_midi", "dress", "len_midi", "st_full", "foot_loafer", "foot_maryjane"],
        pose: ["walk_midstride", "over_shoulder"],
        set: ["street_city", "garden_cn", "cafe"],
        light: ["golden", "window_soft"],
        makeup: ["bare", "warm_date"],
        cam: ["full", "ar_34"],
        grade: ["jp_cream", "natural"],
      },
      [
        {
          title: "毛衣+midi+大衣+靴",
          merge: {
            cloth: ["dress_aline_midi", "knit_cardigan", "outer_coat", "len_midi", "st_layer_open", "foot_boot_ankle"],
            set: ["street_city", "metro_transit"],
            light: ["overcast", "golden"],
            pose: ["walk_midstride"],
          },
        },
      ]
    ),

    // ── 场景触发 · 摄影习惯 ──
    "set:cafe": r(
      "咖啡场景 · 坐窗",
      "人像：窗侧光 + 坐沿/托腮 + 杯道具",
      {
        set: ["cafe"],
        light: ["window_soft"],
        pose: ["sit_edge", "chin_hand_table", "perch"],
        prop: ["cup_drink", "book"],
        cam: ["medium", "mcu", "ar_34"],
        cloth: ["knit_cardigan", "st_full"],
      }
    ),
    "set:street_city": r(
      "街拍 · 中步全身",
      "2026：梧桐法式街配 blazer/风衣 · 地铁口配阔腿淡人 · 咖啡外摆配 midi/缎面 · 红墙斑马线配牛仔混搭 · 雨夜霓虹配深色+直闪（锚生态 2026-Q3）",
      {
        set: ["street_city"],
        pose: ["walk_midstride", "over_shoulder"],
        light: ["overcast", "open_shade", "golden", "flash_on"],
        cam: ["full", "lens_35", "ar_34", "comp_foot"],
        grade: ["natural", "ccd", "grade_fuji400h"],
      }
    ),
    "set:hotel": r(
      "酒店 · 钨丝情绪",
      "2026：晨光穿纱帘金色高光 vs 冷蓝阴影（cinematic）或墙灯暖 vs 窗光冷双色温；unmade bed 微乱被窝可选（锚生态 2026-Q3）",
      {
        set: ["hotel"],
        light: ["tungsten", "practical_lamp", "window_soft", "window_back"],
        pose: ["bed_edge", "sit_edge", "mirror_self"],
        cam: ["mcu", "medium", "ar_34"],
        grade: ["natural", "cine_soft"],
      }
    ),
    "set:bedroom": r(
      "卧室 · 茧居暖灯",
      "2026 cocooning：层叠床品 + 床头多盏暖光入镜 + 2700K 钨丝主光 + 烛光点缀（锚生态 2026-Q3）",
      {
        set: ["bedroom", "window_sill"],
        light: ["tungsten", "practical_lamp", "window_soft"],
        pose: ["bed_edge", "lie_side", "sit_cross"],
        cam: ["medium", "mcu"],
        prop: ["prop_candle", "prop_pillow"],
        grade: ["grade_candle_warm", "natural"],
      }
    ),
    "set:gym_sport": r(
      "健身房",
      "硬侧光/顶光 + 功能姿 + 运动装",
      {
        set: ["gym_sport"],
        light: ["hard_side", "softbox_studio"],
        pose: ["athletic", "yoga_asana"],
        cloth: ["sport", "st_full", "foot_sneaker"],
        makeup: ["sport_sheer"],
        hair: ["high_pony"],
      }
    ),
    "set:bookstore": r(
      "书店 · 安静人像",
      "摄影：窗柔 + 站靠/坐读 + 书 + 开衫层叠",
      {
        set: ["bookstore"],
        light: ["window_soft", "open_shade"],
        pose: ["lean", "sit_edge", "stand_weight"],
        prop: ["book"],
        cloth: ["knit_cardigan", "shirt_blouse", "st_full"],
        cam: ["medium", "full", "ar_34"],
        makeup: ["bare", "commute"],
        grade: ["jp_cream", "natural"],
      }
    ),
    "set:office": r(
      "办公室 · 通勤人像",
      "窗侧/棚柔 + 气场站或任务姿 + 西装或衬衫",
      {
        set: ["office"],
        light: ["window_soft", "softbox_studio"],
        pose: ["stand_power", "task_work", "sit_edge"],
        cloth: ["blazer_suit", "shirt_blouse", "pants", "st_full", "foot_loafer"],
        makeup: ["commute", "id_neutral"],
        cam: ["full", "medium", "ar_34"],
        expr: ["neutral", "focus_task"],
      }
    ),
    "set:studio": r(
      "棚拍 · 光型主导",
      "棚：蚌式/伦勃朗等主光写死 + 景别匹配（美妆 MCU / 全身 lookbook）",
      {
        set: ["studio"],
        light: ["clamshell", "softbox_studio", "rembrandt"],
        cam: ["mcu", "full", "lens_85", "ar_34"],
        pose: ["stand_weight", "stand_power"],
        grade: ["natural", "kr_clean"],
      }
    ),

    // ── 光 · 经典搭配 ──
    "light:clamshell": r(
      "蚌式光 · 美妆半身",
      "人像九光位：蚌式 → 头肩/MCU + 85 感 + 水光妆",
      {
        light: ["clamshell"],
        cam: ["mcu", "cu", "lens_85", "ar_34"],
        pose: ["stand_weight", "hand_face"],
        makeup: ["kr_glass", "soft_glam"],
        hair: ["slick_back", "wet", "long_straight"],
        set: ["studio"],
        grade: ["kr_clean", "natural"],
      }
    ),
    "light:rembrandt": r(
      "伦勃朗 · 戏剧肖像",
      "侧 45° 主光 + 中近景 + 少笑表情",
      {
        light: ["rembrandt", "lt_key_45_left"],
        cam: ["mcu", "medium", "lens_85"],
        expr: ["neutral", "cool", "qingleng"],
        set: ["studio", "indoor_home"],
        grade: ["bw", "natural"],
      }
    ),
    "light:window_soft": r(
      "窗光软 · 万金油",
      "窗 45° + 中景/全身 + 自然妆（最常用现场光）",
      {
        light: ["window_soft"],
        cam: ["medium", "full", "ar_34"],
        pose: ["sit_edge", "stand_weight", "lean"],
        makeup: ["bare", "commute"],
        grade: ["natural", "jp_cream"],
      }
    ),
    "light:flash_on": r(
      "直闪 · 夜/CCD",
      "硬闪 + 夜街 + 略重妆 + 颗粒感",
      {
        light: ["flash_on"],
        set: ["street_city", "night_neon"],
        makeup: ["flash_ready", "soft_glam"],
        grade: ["flash_pop", "ccd"],
        cam: ["full", "medium"],
        pose: ["walk_midstride", "stand_power"],
      }
    ),
    "light:tungsten": r(
      "钨丝 · 夜室内",
      "床头/酒店灯 + 暖肤 + 中近景",
      {
        light: ["tungsten", "practical_lamp"],
        set: ["hotel", "bedroom"],
        cam: ["mcu", "medium"],
        grade: ["natural", "grade_candle_warm"],
        pose: ["bed_edge", "sit_edge"],
      }
    ),

    // ── 姿势 ──
    "pose:walk_midstride": r(
      "中步 · 街拍默认",
      "行走定格常配全身 + 街 + 阴天/开敞阴影",
      {
        pose: ["walk_midstride"],
        cam: ["full", "comp_foot", "lens_35"],
        set: ["street_city"],
        light: ["overcast", "open_shade"],
      }
    ),
    "pose:mirror_self": r(
      "镜前 · 自赏/OOTD",
      "镜前全身或中景 + 室内 + 可叠手机",
      {
        pose: ["mirror_self"],
        cam: ["full", "medium", "ar_34"],
        set: ["indoor_home", "hotel", "set_hair_salon"],
        prop: ["phone", "none"],
        light: ["window_soft", "softbox_studio"],
      }
    ),

    // ── 妆发 ──
    "makeup:kr_glass": r(
      "韩水光 · 美妆棚",
      "水光妆常配蚌式/高键 + MCU + 湿发或丝滑直",
      {
        makeup: ["kr_glass", "part_aegyo", "part_gradient_lip"],
        light: ["clamshell", "high_key"],
        cam: ["mcu", "lens_85"],
        hair: ["wet", "slick_back", "long_straight"],
        set: ["studio"],
        grade: ["kr_clean"],
      }
    ),
    "hair:wolf": r(
      "狼尾 · 酷感街拍",
      "层次狼尾 + 盐系/酷妆 + 街 + 风动可选",
      {
        hair: ["wolf", "bang_curtain", "state_wind"],
        makeup: ["qingleng", "fox_soft"],
        set: ["street_city", "rooftop"],
        pose: ["over_shoulder", "walk_midstride"],
        grade: ["qingleng", "ccd"],
        cloth: ["layer_ootd", "denim", "st_full"],
      }
    ),

    // ── 专属触发（Youth / Erotic 用同一表，应用时只 merge 存在的键）──
    "aes:jinyu": r(
      "禁欲衬衫壳",
      "白衬衫 + 少扣/整齐 + 百叶或窗 + 低马尾",
      {
        aes: ["jinyu"],
        cloth: ["shirt_blouse", "st_few_buttons", "st_full"],
        hair: ["low_pony", "state_tucked_ear"],
        set: ["window_sill", "office"],
        light: ["blind_stripe", "window_soft"],
        makeup: ["qingleng", "dan_gan"],
        expr: ["cool", "qingleng"],
      }
    ),
    "aes:chunyu": r(
      "纯欲默认壳",
      "2026 低饱和原生向：居家或窗 + 半眯 + 近素 + 松弛衣；避开深 V 蕾丝堆砌（锚生态 2026-Q3）",
      {
        aes: ["chunyu"],
        cloth: ["shirt_only", "sleep", "st_relaxed", "st_untucked"],
        expr: ["half_lidded", "soft_bite"],
        makeup: ["home_soft", "douyin_soft"],
        set: ["bedroom", "window_sill"],
        light: ["window_soft", "tungsten"],
        grade: ["jp_cream", "natural"],
        prop: ["none", "phone"],
      }
    ),
    "act:cowgirl": r(
      "骑乘静帧",
      "体位常配低仰/MCU + 连接可读 + 床/酒店",
      {
        act: ["cowgirl", "intercourse"],
        pose: ["kneel"],
        set: ["bedroom", "hotel"],
        cam: ["mcu", "low", "ar_34"],
        light: ["tungsten", "softbox_studio"],
        expr: ["bedroom_eyes", "orgasm"],
      }
    ),
    "act:doggy": r(
      "后入静帧",
      "ass up 可读 + 侧光/钨丝 + 床",
      {
        act: ["doggy", "intercourse"],
        pose: ["kneel", "pose_all_fours"],
        set: ["bedroom", "hotel"],
        cam: ["medium", "mcu", "low"],
        light: ["tungsten", "hard_side"],
        bodyfocus: ["ass", "junction"],
      }
    ),

    // ── 锚定成套生态 2026-Q3（与 skill references/anchor-ecosystem-fill-2026.md 同构）──
    "set:window_sill": r(
      "飘窗/窗边日景",
      "2026 窗光共识：离窗 1 米 + 纱帘/百叶柔光 + 45° 侧光塑面部 + 浅色衣逆光镶金边（锚生态 2026-Q3）",
      {
        set: ["window_sill"],
        light: ["window_soft", "window_back"],
        pose: ["sit_edge", "chin_hand_table", "sit_cross"],
        cam: ["medium", "mcu", "ar_34"],
        cloth: ["sleep", "knit_cardigan", "st_full"],
        makeup: ["home_soft", "bare"],
        grade: ["jp_cream", "natural"],
        prop: ["book", "none"],
      }
    ),
    "set:hotel_bath": r(
      "浴室蒸汽/浴后",
      "湿发贴脸 + 水汽遮 + 玻璃水珠前景；冷调（关暖灯）或暖背光磨砂玻璃剪影两路（锚生态 2026-Q3）",
      {
        set: ["hotel_bath"],
        light: ["window_back", "flash_on"],
        pose: ["sit_edge", "mirror_self"],
        cam: ["medium", "mcu"],
        cloth: ["st_sheer_wet", "shirt_only"],
        hair: ["wet", "messy"],
        grade: ["natural"],
      }
    ),
    "set:office_desk": r(
      "办公桌夜景 · office siren",
      "corporate sleaze：衬衫只系下两粒 + 铅笔裙 + 冷白顶光 × 窗外夜景霓虹青紫（锚生态 2026-Q3）",
      {
        set: ["office_desk"],
        light: ["low_key", "practical_lamp"],
        pose: ["task_work", "sit_edge"],
        cam: ["mcu", "medium"],
        cloth: ["shirt_blouse", "st_few_buttons", "lin_lace_set"],
        makeup: ["soft_glam", "qianjin"],
        grade: ["grade_night_blue", "natural"],
      }
    ),
    "cloth:slip": r(
      "缎面吊带裙 · Old Hollywood",
      "charmeuse slip + 吊带滑落一肩 + 下摆堆在髋；晨窗柔光侧逆勾缎面高光或烛光（锚生态 2026-Q3）",
      {
        cloth: ["slip", "st_strap_slip", "st_hem_up"],
        pose: ["bed_edge", "mirror_self"],
        set: ["bedroom", "hotel"],
        light: ["window_soft", "tungsten"],
        cam: ["mcu", "medium"],
        grade: ["grade_candle_warm", "natural"],
      }
    ),
    "light:neon_mix": r(
      "霓虹 LED · 情趣/夜店",
      "品红/青撞色 LED + 镜面 + 皮肤反光；magenta+amber 落日窗光可叠（锚生态 2026-Q3）",
      {
        light: ["neon_mix"],
        set: ["hotel"],
        cam: ["mcu", "low"],
        grade: ["grade_night_blue", "natural"],
        pose: ["mirror_self", "bed_edge"],
      }
    ),
  };

  // 兼容 hair long_waves 笔误：waves
  if (byTrigger["cloth:dress"]?.merge?.hair) {
    byTrigger["cloth:dress"].merge.hair = byTrigger["cloth:dress"].merge.hair.map((h) =>
      h === "long_waves" ? "waves" : h
    );
  }

  return {
    version: "2026-09-08-soft-prior-v3",
    maxStack: 8,
    byTrigger,
    /** 查找：field + id */
    lookup(field, id) {
      if (!field || !id) return null;
      return byTrigger[`${field}:${id}`] || null;
    },
    /** 从当前 picks 里找「最后点到的」或任意已选 trigger */
    findFromPicks(picks, preferredField, preferredId) {
      if (preferredField && preferredId) {
        const hit = this.lookup(preferredField, preferredId);
        if (hit) return { key: `${preferredField}:${preferredId}`, rec: hit };
      }
      // 扫描常见主 trigger 字段
      const order = ["cloth", "set", "light", "pose", "makeup", "hair", "aes", "act"];
      for (const f of order) {
        const ids = Array.isArray(picks[f]) ? picks[f] : picks[f] ? [picks[f]] : [];
        for (let i = ids.length - 1; i >= 0; i--) {
          const hit = this.lookup(f, ids[i]);
          if (hit) return { key: `${f}:${ids[i]}`, rec: hit };
        }
      }
      return null;
    },
  };
})();
