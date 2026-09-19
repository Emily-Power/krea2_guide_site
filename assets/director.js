(() => {
  /**
   * 导演台 v3 — 表单优先（组合包搜索 + 分组点选 + 实时预览）
   * 对齐 figure / youth-seduction / erotic：六/七层、暗示焦点、连接优先
   */
  const STORAGE_KEY = "skill-director-recipes-v4";
  const CAT = window.DIRECTOR_CATALOG;
  if (!CAT) {
    console.error("director-catalog.js missing");
    return;
  }
  const { FIGURE, EROTIC, YOUTH, SUBJECT } = CAT;

  /* 公共维度 L1–L4 + 专属分组（2026-08-12 schema） */
  const FIELD_GROUPS_FIGURE = [
    {
      id: "subject",
      title: "① 主体档案 · 人数 · 发型",
      hint: "L1:subject/cast/hair · 默认东亚成年女",
      fields: [
        { key: "eth", list: "eth", label: "人种" },
        { key: "age", list: "age", label: "年龄" },
        { key: "sex", list: "sex", label: "性别" },
        { key: "body", list: "body", label: "体型" },
        { key: "cast", list: "cast", label: "人数" },
        { key: "hair", list: "hair", label: "发型" },
      ],
    },
    {
      id: "zone",
      title: "② 专属·大区（A–I）",
      hint: "Figure 专属；未点名私房勿选 I",
      fields: [{ key: "zone", list: "zone", label: "大区" }],
    },
    {
      id: "posecloth",
      title: "③ 姿势 · 衣着 · 道具",
      hint: "cloth 含 L2 品类 + L3 裙型/状态 + L4 鞋配",
      fields: [
        { key: "pose", list: "pose", label: "姿势" },
        { key: "cloth", list: "cloth", label: "衣着" },
        { key: "prop", list: "prop", label: "道具" },
      ],
    },
    {
      id: "scene",
      title: "④ 场景 · 光 · 镜头",
      fields: [
        { key: "set", list: "set", label: "场景" },
        { key: "light", list: "light", label: "光线" },
        { key: "cam", list: "cam", label: "镜头画幅" },
      ],
    },
    {
      id: "polish",
      title: "⑤ 妆容 · 表情 · 调色",
      fields: [
        { key: "makeup", list: "makeup", label: "妆容" },
        { key: "expr", list: "expr", label: "表情视线" },
        { key: "grade", list: "grade", label: "调色媒介" },
      ],
    },
  ];

  const FIELD_GROUPS_EROTIC = [
    {
      id: "subject",
      title: "① 主体档案 · 人数 · 发型",
      hint: "18+ · 默认东亚年轻女",
      fields: [
        { key: "eth", list: "eth", label: "人种" },
        { key: "age", list: "age", label: "年龄" },
        { key: "sex", list: "sex", label: "性别" },
        { key: "body", list: "body", label: "体型" },
        { key: "cast", list: "cast", label: "人数" },
        { key: "hair", list: "hair", label: "发型" },
      ],
    },
    {
      id: "scale",
      title: "② 专属·尺度行为暴露",
      hint: "E0–E4 为专属暴露级，与衣着品类分离；默认大胆+自展",
      fields: [
        { key: "intensity", list: "intensity", label: "尺度" },
        { key: "act", list: "act", label: "行为/体位" },
        { key: "exposure", list: "exposure", label: "暴露 E" },
        { key: "finish", list: "finish", label: "体液结局" },
        { key: "dynamic", list: "dynamic", label: "权力" },
      ],
    },
    {
      id: "pose",
      title: "③ 姿势 · 衣着 · 焦点 · 表情",
      fields: [
        { key: "pose", list: "pose", label: "姿势" },
        { key: "cloth", list: "cloth", label: "衣着品类" },
        { key: "bodyfocus", list: "bodyfocus", label: "身体焦点" },
        { key: "expr", list: "expr", label: "表情" },
        { key: "makeup", list: "makeup", label: "妆容" },
      ],
    },
    {
      id: "scene",
      title: "④ 场景 · 光 · 镜头 · 幻想 · 调色",
      fields: [
        { key: "set", list: "set", label: "场景" },
        { key: "light", list: "light", label: "光线" },
        { key: "cam", list: "cam", label: "镜头" },
        { key: "fantasy", list: "fantasy", label: "幻想 F" },
        { key: "prop", list: "prop", label: "道具" },
        { key: "grade", list: "grade", label: "调色" },
      ],
    },
  ];

  const FIELD_GROUPS_YOUTH = [
    {
      id: "subject",
      title: "① 主体档案 · 人数 · 发型",
      hint: "18+ · 默认东亚 early twenties · 独处",
      fields: [
        { key: "eth", list: "eth", label: "人种" },
        { key: "age", list: "age", label: "年龄" },
        { key: "sex", list: "sex", label: "性别" },
        { key: "body", list: "body", label: "体型" },
        { key: "cast", list: "cast", label: "人数" },
        { key: "hair", list: "hair", label: "发型" },
      ],
    },
    {
      id: "scale",
      title: "② 专属·尺度 · 行为 · I 级",
      hint: "默认 pure-desire + I1；I3 须点名；禁露骨",
      fields: [
        { key: "intensity", list: "intensity", label: "尺度" },
        { key: "act", list: "act", label: "行为瞬间" },
        { key: "imply", list: "imply", label: "暴露 I" },
      ],
    },
    {
      id: "posecloth",
      title: "③ 姿势 · 暗示 · 衣着 · 妆表",
      fields: [
        { key: "pose", list: "pose", label: "姿势" },
        { key: "focus", list: "focus", label: "暗示焦点" },
        { key: "cloth", list: "cloth", label: "衣着" },
        { key: "prop", list: "prop", label: "道具" },
        { key: "makeup", list: "makeup", label: "妆容" },
        { key: "expr", list: "expr", label: "表情" },
      ],
    },
    {
      id: "scene",
      title: "④ 场景 · 光 · 镜头 · 美学壳 · 调色",
      fields: [
        { key: "set", list: "set", label: "场景" },
        { key: "light", list: "light", label: "光线" },
        { key: "cam", list: "cam", label: "镜头画幅" },
        { key: "aes", list: "aes", label: "美学壳" },
        { key: "grade", list: "grade", label: "调色" },
      ],
    },
  ];

  /** 一键预设：整套 picks + extra，缺省字段用 defaults 补全 */
  const PRESETS_FIGURE = [
    {
      id: "street",
      emoji: "🚶",
      title: "街拍中步",
      desc: "B 区 · OOTD 城市",
      extra: "feet in frame, candid not stiff",
      picks: {
        zone: "B",
        combo: "combo-street-midstride",
        pose: "walk_midstride",
        cloth: "outer_coat",
        prop: "boba",
        set: "street_city",
        light: "overcast",
        cam: "full",
        makeup: "commute",
        expr: "soft_smile",
        grade: "natural",
      },
    },
    {
      id: "krglass",
      emoji: "✨",
      title: "韩系水光",
      desc: "棚拍 · glass skin",
      extra: "glass-skin dewy finish, clean studio",
      picks: {
        zone: "A",
        combo: "combo-kr-glass-studio",
        pose: "stand_scurve",
        cloth: "blazer_suit",
        prop: "none",
        set: "studio",
        light: "highkey",
        cam: "mcu",
        makeup: "krglass",
        expr: "mute",
        grade: "krclean",
      },
    },
    {
      id: "jpwindow",
      emoji: "🪟",
      title: "日系窗光",
      desc: "空气感 · 逆光",
      extra: "soft backlight rim on hair, adult proportions",
      picks: {
        zone: "G",
        combo: "combo-jp-airy-window",
        pose: "window_pose",
        cloth: "knit_cardigan",
        prop: "none",
        set: "window_sill",
        light: "backlit",
        cam: "mcu",
        makeup: "jp",
        expr: "soft_smile",
        grade: "jpcream",
      },
    },
    {
      id: "xhs",
      emoji: "📱",
      title: "小红书封面",
      desc: "竖构图 · 显腿",
      extra: "3:4 cover crop, headroom, feet near bottom edge",
      picks: {
        zone: "B",
        combo: "combo-cover-xhs",
        pose: "walk_midstride",
        cloth: "layer_ootd",
        prop: "bag",
        set: "street_city",
        light: "overcast",
        cam: "xhs",
        makeup: "date",
        expr: "soft_smile",
        grade: "natural",
      },
    },
    {
      id: "idphoto",
      emoji: "🪪",
      title: "证件形象",
      desc: "干净头肩",
      extra: "neutral expression option, clean collar, no heavy filter",
      picks: {
        zone: "E",
        combo: "combo-id-photo-clean",
        pose: "stand_power",
        cloth: "blazer_suit",
        prop: "none",
        set: "studio",
        light: "loop",
        cam: "cu",
        makeup: "id",
        expr: "neutral",
        grade: "natural",
      },
    },
    {
      id: "travel",
      emoji: "🗺️",
      title: "中式旅拍",
      desc: "地标尺度",
      extra: "full body with landmark scale, feet in frame",
      picks: {
        zone: "G",
        combo: "combo-cn-travel-landmark",
        pose: "walk_midstride",
        cloth: "dress",
        prop: "none",
        set: "landmark",
        light: "golden",
        cam: "full",
        makeup: "date",
        expr: "soft_smile",
        grade: "portra",
      },
    },
    {
      id: "home",
      emoji: "🏡",
      title: "居家柔美",
      desc: "I 区 SFW · 点名",
      extra: "SFW soft home, fully clothed loungewear L0",
      picks: {
        zone: "I",
        combo: "combo-pb-window-side-l0",
        pose: "window_pose",
        cloth: "lounge",
        prop: "none",
        set: "bedroom",
        light: "window",
        cam: "mcu",
        makeup: "home",
        expr: "soft_smile",
        grade: "jpcream",
      },
    },
    {
      id: "sport",
      emoji: "🧘",
      title: "瑜伽运动",
      desc: "C 区 · 功能姿",
      extra: "support leg clear, athletic not pin-up",
      picks: {
        zone: "C",
        combo: "combo-sp-yoga",
        pose: "yoga_asana",
        cloth: "sport",
        prop: "none",
        set: "gym",
        light: "overcast",
        cam: "full",
        makeup: "sport",
        expr: "focus",
        grade: "natural",
      },
    },
    {
      id: "civitai-rgb",
      emoji: "🎮",
      title: "电竞房 RGB",
      desc: "Civitai · 词预算全身",
      extra: "room-first word budget optional; feet on carpet, RGB strips, adult East Asian",
      picks: {
        zone: "G",
        combo: "combo-cv-gaming-rgb",
        pose: "sit_edge",
        cloth: "tee_hoodie",
        prop: "none",
        set: "bedroom",
        light: "neon",
        cam: "full",
        makeup: "home",
        expr: "soft_smile",
        grade: "natural",
      },
    },
    {
      id: "civitai-ig",
      emoji: "📸",
      title: "IG 中步",
      desc: "Civitai 姿壳 · 街",
      extra: "instagram-style mid-stride, feet in frame, no score tags",
      picks: {
        zone: "B",
        combo: "combo-cv-ig-midstride",
        pose: "walk_midstride",
        cloth: "layer_ootd",
        prop: "bag",
        set: "street_city",
        light: "overcast",
        cam: "full",
        makeup: "commute",
        expr: "soft_smile",
        grade: "natural",
      },
    },
  ];

  const PRESETS_EROTIC = [
    {
      id: "jphotel",
      emoji: "🏨",
      title: "日系酒店",
      desc: "默认大胆 · 半褪",
      extra: "adult East Asian, tungsten hotel mood",
      picks: {
        combo: "combo-japanese-hotel",
        intensity: "explicit",
        act: "solo-display",
        finish: "none",
        dynamic: "equal",
        pose: "bed_edge",
        exposure: "e1",
        set: "hotel",
        light: "tungsten",
        fantasy: "none",
        cam: "mcu",
        expr: "bedroom_eyes",
        bodyfocus: "full",
      },
    },
    {
      id: "red-tungsten",
      emoji: "🔴",
      title: ".red 钨丝酒店",
      desc: "Civitai.red 壳 · 半褪",
      extra: "civitai.red shell: warm tungsten, adult East Asian, no score_9 tags",
      picks: {
        combo: "combo-red-hotel-tungsten",
        intensity: "explicit",
        act: "solo-display",
        finish: "none",
        dynamic: "equal",
        pose: "bed_edge",
        exposure: "e1",
        set: "hotel",
        light: "tungsten",
        fantasy: "none",
        cam: "mcu",
        expr: "bedroom_eyes",
        bodyfocus: "full",
      },
    },
    {
      id: "red-pov",
      emoji: "👀",
      title: ".red 床上 POV",
      desc: "POV · 连接可读",
      extra: "POV bed framing; write connection if act is intercourse; adult only",
      picks: {
        combo: "combo-red-pov-bed",
        intensity: "explicit",
        act: "solo-display",
        finish: "none",
        dynamic: "equal",
        pose: "kneel",
        exposure: "e2",
        set: "bedroom",
        light: "single",
        fantasy: "none",
        cam: "pov",
        expr: "eyecontact",
        bodyfocus: "full",
      },
    },
    {
      id: "maxsolo",
      emoji: "🔥",
      title: "最色自展",
      desc: "大开腿 · 无插入",
      extra: "knees far apart, hips to camera, not modest kneeling",
      picks: {
        combo: "combo-amateur-solo",
        intensity: "max",
        act: "solo-display",
        finish: "none",
        dynamic: "equal",
        pose: "kneel",
        exposure: "e4",
        set: "bedhome",
        light: "tungsten",
        fantasy: "none",
        cam: "mcu",
        expr: "bedroom_eyes",
        bodyfocus: "full",
      },
    },
    {
      id: "cowgirl",
      emoji: "💫",
      title: "骑乘中出",
      desc: "连接可见",
      extra: "buried to the hilt, wet junction visible",
      picks: {
        combo: "combo-creampie-cowgirl",
        intensity: "explicit",
        act: "cowgirl",
        finish: "creampie",
        dynamic: "equal",
        pose: "kneel",
        exposure: "e4",
        set: "hotel",
        light: "tungsten",
        fantasy: "none",
        cam: "mcu",
        expr: "bedroom_eyes",
        bodyfocus: "pussy",
      },
    },
    {
      id: "doggy",
      emoji: "🐕",
      title: "后入中出",
      desc: "ass up · 溢流",
      extra: "ass raised, junction overflow if creampie",
      picks: {
        combo: "combo-creampie-doggy",
        intensity: "explicit",
        act: "doggy",
        finish: "creampie",
        dynamic: "dommale",
        pose: "kneel",
        exposure: "e1",
        set: "hotel",
        light: "tungsten",
        fantasy: "none",
        cam: "mcu",
        expr: "bedroom_eyes",
        bodyfocus: "ass",
      },
    },
    {
      id: "povbj",
      emoji: "👀",
      title: "POV 口交",
      desc: "朝镜头侍奉",
      extra: "eye contact or watery eyes, lips on shaft",
      picks: {
        combo: "combo-pov-bj",
        intensity: "explicit",
        act: "bj",
        finish: "none",
        dynamic: "service",
        pose: "kneel",
        exposure: "e2",
        set: "hotel",
        light: "tungsten",
        fantasy: "none",
        cam: "mcu",
        expr: "tears",
        bodyfocus: "face",
      },
    },
    {
      id: "soft",
      emoji: "🌙",
      title: "软色窗边",
      desc: "sensual · 少露",
      extra: "suggestive not hardcore, fabric cling",
      picks: {
        combo: "combo-window-risk",
        intensity: "sensual",
        act: "solo-display",
        finish: "none",
        dynamic: "equal",
        pose: "window_pose",
        exposure: "e2",
        set: "window_sill",
        light: "coolwarm",
        fantasy: "none",
        cam: "mcu",
        expr: "bedroom_eyes",
        bodyfocus: "breasts",
      },
    },
    {
      id: "quickie",
      emoji: "⚡",
      title: "酒店速战",
      desc: "衣未脱完",
      extra: "half-undressed, door, hurried still",
      picks: {
        combo: "combo-hotel-quickie",
        intensity: "explicit",
        act: "standing",
        finish: "none",
        dynamic: "equal",
        pose: "lean",
        exposure: "e1",
        set: "hotel",
        light: "tungsten",
        fantasy: "none",
        cam: "mcu",
        expr: "shocked",
        bodyfocus: "full",
      },
    },
    {
      id: "tentacle",
      emoji: "🐙",
      title: "触手展示",
      desc: "爱抚撑开 · 无插入",
      extra: "elegant glossy sensual tentacles, spread only, no horror",
      picks: {
        combo: "combo-tentacle-display",
        intensity: "max",
        act: "solo-display",
        finish: "none",
        dynamic: "equal",
        pose: "lie_back",
        exposure: "e4",
        set: "fantasy",
        light: "tungsten",
        fantasy: "tentacle",
        cam: "mcu",
        expr: "ahegao",
        bodyfocus: "pussy",
      },
    },
  ];

  const PRESETS_YOUTH = [
    {
      id: "sunset-lace",
      emoji: "🌇",
      title: "日落蕾丝回眸",
      desc: "窗边 · 强逆光 · I3",
      extra: "strong window rim light, body in soft shadow, plain sheer white curtains no print, half-lidded knowing gaze",
      picks: {
        combo: "combo-window-lace",
        intensity: "edge",
        act: "window-risk",
        imply: "i3",
        pose: "over_shoulder",
        cloth: "lingerie",
        set: "window_sill",
        light: "golden-hour",
        cam: "full",
        focus: "spine",
        expr: "knowing-lens",
        aes: "chunyu",
        hair: "long_straight",
      },
    },
    {
      id: "mirror-shirt",
      emoji: "🪞",
      title: "镜前男友衫",
      desc: "自赏 · I2 单扣",
      extra: "mirror reflection matches pose exactly, one lower button only",
      picks: {
        combo: "combo-mirror-stretch",
        intensity: "pure-desire",
        act: "self-gaze",
        imply: "i2",
        pose: "mirror_self",
        cloth: "shirt_only",
        set: "bedroom-night",
        light: "bedside-tungsten",
        cam: "mirror-full",
        focus: "midriff",
        expr: "self-absorbed",
        aes: "chunyu",
      },
    },
    {
      id: "bed-soft",
      emoji: "🛏️",
      title: "床沿纯欲",
      desc: "侧坐 · 居家 I1",
      extra: "soft weight on one hip, feet or knees in frame",
      picks: {
        combo: "combo-bed-side-lie",
        intensity: "pure-desire",
        act: "solo-display",
        imply: "i1",
        pose: "bed_edge",
        cloth: "sleep",
        set: "bedroom-morning",
        light: "window-45",
        cam: "ms-v",
        focus: "collarbone",
        expr: "half_lidded",
        aes: "chunyu",
      },
    },
    {
      id: "sofa-phone",
      emoji: "📱",
      title: "沙发手机",
      desc: "懒刷 · 屏光",
      extra: "phone glow as key, casual not stiff",
      picks: {
        combo: "combo-sofa-phone",
        intensity: "pure-desire",
        act: "lazy-scroll",
        imply: "i1",
        pose: "sit_cross",
        cloth: "cami_set",
        set: "sofa-day",
        light: "phone-screen",
        cam: "ms-v",
        focus: "thighs",
        expr: "sleepy",
        aes: "songchi",
      },
    },
    {
      id: "wet-bath",
      emoji: "🚿",
      title: "浴后湿发",
      desc: "蒸汽 · 锁骨",
      extra: "damp hair on neck, coverage locked",
      picks: {
        combo: "combo-bath-fog-mirror",
        intensity: "sensual-implied",
        act: "after-bath",
        imply: "i3",
        pose: "mirror-strap",
        cloth: "towel-wrap",
        set: "bath-steam",
        light: "steam-bath",
        cam: "mcu-collar",
        focus: "wet-hair",
        expr: "half_lidded",
        aes: "chunyu",
      },
    },
    {
      id: "jinyu-blind",
      emoji: "👔",
      title: "禁欲百叶",
      desc: "白衬衫 · 条纹光",
      extra: "mostly buttoned white shirt, cool restrained desire",
      picks: {
        combo: "combo-v-jinyu-blind",
        intensity: "pure-desire",
        act: "window-risk",
        imply: "i1",
        pose: "window-lean",
        cloth: "white-shirt",
        set: "sparse-window",
        light: "blind-stripes",
        cam: "ms-v",
        focus: "collarbone",
        expr: "qingleng",
        aes: "jinyu",
      },
    },
    {
      id: "bai-window",
      emoji: "🌙",
      title: "白月光窗",
      desc: "清冷可望",
      extra: "almost no smile, sparse pale room",
      picks: {
        combo: "combo-v-bai-window",
        intensity: "fresh",
        act: "window-risk",
        imply: "i0",
        pose: "window-lean",
        cloth: "white-shirt",
        set: "sparse-window",
        light: "morning-cool",
        cam: "neg-window",
        focus: "lips-gaze",
        expr: "qingleng",
        aes: "baiyueguang",
      },
    },
    {
      id: "softlife-coffee",
      emoji: "☕",
      title: "soft life 金辉",
      desc: "慢晨咖啡",
      extra: "coffee mug optional, lived-in soft morning",
      picks: {
        combo: "combo-softlife-coffee",
        intensity: "fresh",
        act: "golden-idle",
        imply: "i1",
        pose: "sit_cross",
        cloth: "cream-knit",
        set: "cream-room",
        light: "golden-hour",
        cam: "ms-v",
        focus: "collarbone",
        expr: "sleepy",
        aes: "softlife",
        hair: "messy",
      },
    },
    {
      id: "hotel-robe",
      emoji: "🏨",
      title: "酒店浴袍",
      desc: "刚到 · 暧昧",
      extra: "travel bag far corner, quiet arrival",
      picks: {
        combo: "combo-hotel-arrival",
        intensity: "sensual-implied",
        act: "solo-display",
        imply: "i2",
        pose: "bed_edge",
        cloth: "satin-robe",
        set: "hotel-suite",
        light: "bedside-tungsten",
        cam: "ms-v",
        focus: "strap",
        expr: "knowing-lens",
        aes: "chunyu",
      },
    },
    {
      id: "coquette-bow",
      emoji: "🎀",
      title: "coquette 软欲",
      desc: "蕾丝边仍遮盖",
      extra: "soft bow detail, covered lace trim, not explicit",
      picks: {
        combo: "combo-coquette-bow-soft",
        intensity: "pure-desire",
        act: "self-gaze",
        imply: "i1",
        pose: "mirror-strap",
        cloth: "cami_set",
        set: "vanity-night",
        light: "window-45",
        cam: "xhs-cover",
        focus: "strap",
        expr: "tiny-smirk",
        aes: "coquette",
      },
    },
  ];

  const state = {
    mode: "figure",
    picks: {},
    extra: "",
    shots: [],
    shotIndex: 0,
    comboQuery: "",
    comboGroup: "all",
    openGroups: { subject: true, zone: true, scale: true, posecloth: true },
    activePreset: null,
  };

  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  function catalog() {
    if (state.mode === "figure") return FIGURE;
    if (state.mode === "youth") return YOUTH || {};
    return EROTIC;
  }

  function presetsForMode() {
    if (state.mode === "figure") return PRESETS_FIGURE;
    if (state.mode === "youth") return PRESETS_YOUTH;
    return PRESETS_EROTIC;
  }

  function applyPreset(presetId) {
    const preset = presetsForMode().find((p) => p.id === presetId);
    if (!preset) return;
    const base = defaultsPicks(state.mode);
    state.picks = sanitizeAllPicks({ ...base, ...preset.picks });
    // 主体默认仍东亚 early 20s，除非预设里写了
    state.extra = preset.extra || "";
    state.activePreset = preset.id;
    syncShotFromPicks();
    // 组合包搜索滚到当前
    state.comboQuery = "";
    state.comboGroup = "all";
    renderAll();
    toast(`已套用：${preset.title}`);
  }

  function renderPresets() {
    const box = $("#presetBar");
    if (!box) return;
    const list = presetsForMode();
    box.innerHTML = `
      <div class="preset-head">
        <strong>一键预设</strong>
        <span class="preset-sub">${
          state.mode === "figure" ? "Figure SFW · 点一下套完整参数" : state.mode === "youth" ? "Youth 纯欲暗示 · 点一下套完整参数" : "Erotic 18+ · 点一下套完整参数"
        }</span>
      </div>
      <div class="preset-grid" role="list">
        ${list
          .map(
            (p) => `
          <button type="button" class="preset-card ${
            state.activePreset === p.id ? "is-on" : ""
          }" data-preset="${escapeAttr(p.id)}" role="listitem">
            <span class="preset-emoji" aria-hidden="true">${p.emoji}</span>
            <span class="preset-title">${escapeHtml(p.title)}</span>
            <span class="preset-desc">${escapeHtml(p.desc)}</span>
          </button>`
          )
          .join("")}
      </div>`;
    box.querySelectorAll(".preset-card").forEach((btn) => {
      btn.addEventListener("click", () => applyPreset(btn.dataset.preset));
    });
  }

  function listFor(name) {
    if (["age", "hair", "body", "eth", "sex", "cast"].includes(name))
      return SUBJECT[name] || [];
    return catalog()[name] || [];
  }

  /**
   * 点菜策略（横向 vs 纵向）
   * ─────────────────────────────────────────────
   * · single     整维单选（人种/年龄/尺度…）
   * · vertical   纵向叠层：同 group 互斥（主造型只 1），跨 group 可叠（造型+刘海+发态）
   * · free       横向多选：同层可多个（道具多件、身体焦点多点）
   * · exclusiveGroupSets：多个 group 共享「只能留一个」（如姿的站/走/坐大族）
   *
   * 反例：发型 L2造型 不可同时选「黑长直+丸子+马尾」——那是互斥主造型，不是叠层。
   */
  const FIELD_POLICY = {
    // 主体：见 docs/维度点菜策略-逐层分析.md（按 group 不是整维瞎多选）
    eth: { mode: "single", tag: "单选", hint: "L2人种互斥" },
    // age/body：L2 主轴 S + L3 修饰 S（纵向，非整维 single）
    age: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "年龄主带1 · L3带可叠1",
      defaultGroupMax: 1,
      fieldMax: 2,
    },
    sex: { mode: "single", tag: "单选", hint: "L2性别互斥" },
    body: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "体型主型1 · L3读法可叠1",
      defaultGroupMax: 1,
      fieldMax: 2,
    },
    cast: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "人数S · 关系S · L3读法S",
      defaultGroupMax: 1,
      fieldMax: 3,
    },
    // 发型：L2造型S · 刘海/分区/色/质S · 发态M(2)
    hair: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "主造型只1 · 刘海/色S · 发态可2",
      defaultGroupMax: 1,
      groupMax: { L3发态: 2 },
      fieldMax: 6,
    },
    makeup: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "妆壳S · 妆件M(3)",
      defaultGroupMax: 1,
      groupMax: { L3妆件: 3 },
      fieldMax: 5,
    },
    expr: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "表情与分轨互斥 · 视线S可叠",
      defaultGroupMax: 1,
      exclusiveGroupSets: [["L2表情", "L2分轨"]],
      fieldMax: 3,
    },
    // 衣着：各 L2 槽位 S；状态/配/面料/衣色 M；子 L3 版型 S（依赖父品类）
    cloth: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "外搭/上装/下装各S · 状态M · 版型S",
      defaultGroupMax: 1,
      groupMax: {
        L3状态: 3,
        L4配: 3,
        L5面料: 2,
        L5图案: 1,
        L5衣色: 2,
      },
      fieldMax: 12,
    },
    pose: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "大姿族互斥1 · 细姿M(2)",
      defaultGroupMax: 1,
      exclusiveGroupSets: [
        ["L2站", "L2走", "L2靠", "L2坐", "L2镜床", "L2其它", "L2运动", "L2表演"],
      ],
      groupMax: { L3细姿: 2, L3任务: 1 },
      fieldMax: 4,
    },
    // 道具：同层横向多选
    prop: {
      mode: "free",
      tag: "横向多选",
      hint: "可多件道具 · none 清空",
      defaultGroupMax: 4,
      fieldMax: 4,
      noneId: "none",
    },
    // 场景：主场只1 · L3锚点可叠
    set: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "主场景只1 · 可叠场锚",
      defaultGroupMax: 1,
      exclusiveGroupSets: [["L2城", "L2室内", "L2运动", "L2户外", "L2特殊"]],
      groupMax: {
        L3地标: 1,
        L3室内: 2,
        L3城: 2,
        L3户外: 2,
        L3特殊: 1,
      },
      fieldMax: 3,
    },
    // 光：主光型1 · 方位/辅光/色温可叠（蚌式≠伦勃朗）
    light: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "主光型只1 · 可叠方位/辅光",
      defaultGroupMax: 1,
      exclusiveGroupSets: [["L2自然", "L2实用", "L2棚"]],
      groupMax: { L3辅光: 2, L3光效: 1, L3方位: 1, L3光比: 1, L3器材感: 1, L3色温: 1 },
      fieldMax: 5,
    },
    // 镜头：景别/角度/画幅/焦段 各1 纵向
    cam: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "景别·角度·画幅各1 · 构图可叠",
      defaultGroupMax: 1,
      groupMax: { L3构图: 2 },
      fieldMax: 6,
    },
    // 调色：主 look 1
    grade: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "主调色只1 · 质感可叠1",
      defaultGroupMax: 1,
      exclusiveGroupSets: [["L2调色", "L2胶片", "L2数码"]],
      groupMax: { L3质感: 1 },
      fieldMax: 2,
    },
    // 专属
    zone: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "大区S · 标签可M(2)",
      defaultGroupMax: 1,
      groupMax: { 专属标签: 2 },
      exclusiveGroupSets: [["专属大区"]],
      fieldMax: 3,
    },
    intensity: { mode: "single", tag: "单选", hint: "尺度S" },
    imply: { mode: "single", tag: "单选", hint: "I级S" },
    aes: { mode: "single", tag: "单选", hint: "美学壳S" },
    dynamic: { mode: "single", tag: "单选", hint: "权力S" },
    finish: { mode: "single", tag: "单选", hint: "结局S" },
    exposure: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "E级S · E细S",
      defaultGroupMax: 1,
      fieldMax: 2,
    },
    act: {
      mode: "vertical",
      tag: "纵向叠层",
      hint: "行为S · 体位S可叠",
      defaultGroupMax: 1,
      fieldMax: 3,
    },
    focus: {
      mode: "free",
      tag: "横向多选",
      hint: "暗示焦点可多点",
      defaultGroupMax: 2,
      fieldMax: 2,
    },
    bodyfocus: {
      mode: "free",
      tag: "横向多选",
      hint: "身体焦点可多点",
      defaultGroupMax: 2,
      fieldMax: 2,
    },
    fantasy: {
      mode: "free",
      tag: "横向多选",
      hint: "幻想项≤2",
      defaultGroupMax: 2,
      fieldMax: 2,
    },
  };
  const MULTI_MAX_FALLBACK = 8;

  function policyOf(key) {
    return (
      FIELD_POLICY[key] || {
        mode: "single",
        tag: "单选",
        hint: "",
        defaultGroupMax: 1,
        fieldMax: 1,
      }
    );
  }

  function isMulti(key) {
    const m = policyOf(key).mode;
    return m === "vertical" || m === "free";
  }

  function asIdList(v) {
    if (v == null || v === "") return [];
    if (Array.isArray(v)) return v.filter(Boolean);
    return [v];
  }

  function findOpt(list, id) {
    if (!list?.length) return { id: "", label: "", en: "", group: "" };
    const first = asIdList(id)[0];
    return list.find((x) => x.id === first) || list[0];
  }

  function optById(list, id) {
    return (list || []).find((x) => x.id === id) || null;
  }

  function groupOf(list, id) {
    return optById(list, id)?.group || "(none)";
  }

  function groupMaxFor(pol, group) {
    if (pol.groupMax && pol.groupMax[group] != null) return pol.groupMax[group];
    if (pol.mode === "free") return pol.defaultGroupMax || pol.fieldMax || 4;
    return pol.defaultGroupMax != null ? pol.defaultGroupMax : 1;
  }

  function exclusiveSetFor(pol, group) {
    const sets = pol.exclusiveGroupSets || [];
    for (const s of sets) {
      if (s.includes(group)) return s;
    }
    return null;
  }

  /** 多层点选 → 有序条目列表（用于拼装 en） */
  function resolveMany(list, pickVal, fallbackId) {
    let ids = asIdList(pickVal);
    if (!ids.length && fallbackId) ids = [fallbackId];
    const out = [];
    const seen = new Set();
    for (const id of ids) {
      const o = (list || []).find((x) => x.id === id);
      if (o && !seen.has(o.id)) {
        out.push(o);
        seen.add(o.id);
      }
    }
    if (!out.length) {
      const fb =
        (fallbackId && (list || []).find((x) => x.id === fallbackId)) ||
        (list && list[0]);
      if (fb) out.push(fb);
    }
    return out;
  }

  function joinEn(items) {
    return (items || [])
      .map((x) => x.en)
      .filter(Boolean)
      .join("; ");
  }

  function joinLabel(items) {
    const s = (items || [])
      .map((x) => x.label)
      .filter(Boolean)
      .join(" · ");
    return s || "—";
  }

  /**
   * 按策略切换选中：
   * - single：整维替换
   * - vertical：同 group 达 max 则挤掉旧；exclusiveGroupSets 跨组互斥
   * - free：同组可多，受 fieldMax
   */
  function optionsForKey(key) {
    if (["eth", "age", "body", "sex", "cast", "hair"].includes(key)) return SUBJECT[key] || [];
    return catalog()[key] || SUBJECT[key] || [];
  }

  /** 在已有 arr 上应用一次「点选 id」（不读写 state） */
  function applySelectToArr(key, arr, id) {
    const pol = policyOf(key);
    const opts = optionsForKey(key);
    let next = arr.slice();
    if (next.includes(id)) return next.filter((x) => x !== id);

    const g = groupOf(opts, id);
    const noneId = pol.noneId;
    if (noneId && id === noneId) return [noneId];
    if (noneId) next = next.filter((x) => x !== noneId);

    const exSet = exclusiveSetFor(pol, g);
    if (exSet) {
      next = next.filter((x) => !exSet.includes(groupOf(opts, x)));
    } else {
      const gMax = groupMaxFor(pol, g);
      const inGroup = next.filter((x) => groupOf(opts, x) === g);
      if (inGroup.length >= gMax) {
        const dropIds = new Set(inGroup.slice(0, inGroup.length - gMax + 1));
        next = next.filter((x) => !dropIds.has(x));
      }
    }
    next = next.concat([id]);
    const fMax = pol.fieldMax || MULTI_MAX_FALLBACK;
    if (next.length > fMax) next = next.slice(next.length - fMax);
    return next;
  }

  function togglePick(key, id) {
    const pol = policyOf(key);
    if (pol.mode === "single" || !isMulti(key)) {
      state.picks[key] = id;
      return;
    }
    state.picks[key] = applySelectToArr(key, asIdList(state.picks[key]), id);
  }

  /** 软推荐 / 预设 merge 时按策略清洗（避免塞入互斥 L2） */
  function sanitizePickList(key, ids) {
    const pol = policyOf(key);
    const raw = asIdList(ids);
    if (!raw.length) return pol.mode === "single" ? "" : [];
    if (pol.mode === "single") return raw[raw.length - 1];
    let arr = [];
    for (const id of raw) {
      if (arr.includes(id)) continue;
      // applySelectToArr 在已含 id 时会取消；此处只做强制加入
      arr = applySelectToArr(key, arr, id);
    }
    return arr;
  }

  function sanitizeAllPicks(picks) {
    const out = { ...picks };
    Object.keys(out).forEach((k) => {
      if (FIELD_POLICY[k] || isMulti(k)) out[k] = sanitizePickList(k, out[k]);
    });
    return out;
  }

  /* ---------- 软推荐搭配 Soft Prior ---------- */
  const REC = window.DIM_RECOMMEND;
  let recState = { key: null, rec: null, altIndex: -1 };

  function applyMergeToPicks(merge) {
    if (!merge) return;
    Object.keys(merge).forEach((k) => {
      const v = merge[k];
      if (v == null) return;
      if (isMulti(k) || Array.isArray(v)) {
        state.picks[k] = sanitizePickList(k, v);
      } else {
        state.picks[k] = sanitizePickList(k, v);
      }
    });
  }

  function showRecommendFor(field, id, isNowSelected) {
    const panel = $("#recPanel");
    if (!panel || !REC) return;
    if (!isNowSelected) {
      // 取消选中时若就是当前推荐 trigger，可保留面板
      return;
    }
    const hit = REC.lookup(field, id);
    if (!hit) return;
    recState = { key: `${field}:${id}`, rec: hit, altIndex: -1 };
    panel.hidden = false;
    const title = $("#recTitle");
    const src = $("#recSource");
    if (title) title.textContent = hit.title || "—";
    if (src) src.textContent = (hit.source || "常见搭配") + " · 非强制·可忽略";
    const alts = $("#recAlts");
    if (alts) {
      alts.innerHTML = (hit.alts || [])
        .map(
          (a, i) =>
            `<button type="button" class="rec-alt-btn" data-alti="${i}">备选：${escapeHtml(
              a.title || "另一版"
            )}</button>`
        )
        .join("");
      alts.querySelectorAll(".rec-alt-btn").forEach((b) => {
        b.addEventListener("click", () => {
          const i = +b.dataset.alti;
          const alt = hit.alts[i];
          if (!alt?.merge) return;
          applyMergeToPicks(alt.merge);
          recState.altIndex = i;
          state.activePreset = null;
          syncShotFromPicks();
          renderAll();
          toast("已应用备选搭配（可再改）");
        });
      });
    }
  }

  function applyCurrentRecommend() {
    if (!recState.rec?.merge) {
      toast("当前无推荐");
      return;
    }
    applyMergeToPicks(recState.rec.merge);
    state.activePreset = null;
    syncShotFromPicks();
    renderAll();
    toast("已应用软推荐（可继续改，非唯一答案）");
  }

  function dismissRecommend() {
    recState = { key: null, rec: null, altIndex: -1 };
    const panel = $("#recPanel");
    if (panel) panel.hidden = true;
  }

  function defaultsPicks(mode) {
    if (mode === "figure") {
      return {
        eth: "eastasian",
        age: "e20",
        sex: "woman",
        body: "slim",
        cast: "solo",
        hair: "long_straight",
        zone: "B",
        combo: "combo-street-midstride",
        pose: "walk_midstride",
        cloth: "outer_coat",
        prop: "none",
        set: "street_city",
        light: "window_soft",
        makeup: "commute",
        cam: "full",
        expr: "soft_smile",
        grade: "natural",
      };
    }
    if (mode === "youth") {
      return {
        eth: "eastasian",
        age: "e20",
        sex: "woman",
        body: "slim",
        cast: "solo",
        hair: "long_straight",
        combo: "combo-window-lace",
        intensity: "pure-desire",
        act: "window-risk",
        imply: "i1",
        pose: "over_shoulder",
        cloth: "shirt_only",
        prop: "none",
        set: "window_sill",
        light: "window_back",
        cam: "mcu",
        focus: "collarbone",
        makeup: "home_soft",
        expr: "half_lidded",
        aes: "chunyu",
        grade: "jp_cream",
      };
    }
    return {
      eth: "eastasian",
      age: "e20",
      sex: "woman",
      body: "slim",
      cast: "solo",
      hair: "messy",
      combo: "combo-japanese-hotel",
      intensity: "explicit",
      act: "solo-display",
      exposure: "e1",
      finish: "none",
      dynamic: "equal",
      pose: "bed_edge",
      cloth: "shirt_blouse",
      prop: "none",
      set: "hotel",
      light: "tungsten",
      cam: "mcu",
      makeup: "bare",
      expr: "bedroom_eyes",
      fantasy: "none",
      grade: "natural",
      bodyfocus: "full",
    };
  }

  function clone(o) {
    return JSON.parse(JSON.stringify(o));
  }

  function newShot(i, picks) {
    return {
      id: "s" + Date.now() + "_" + i,
      title: "Shot " + (i + 1),
      picks: picks ? clone(picks) : defaultsPicks(state.mode),
      extra: "",
    };
  }

  function currentShot() {
    return state.shots[state.shotIndex];
  }

  function syncPicksFromShot() {
    const sh = currentShot();
    if (!sh) return;
    state.picks = sanitizeAllPicks(clone(sh.picks));
    state.extra = sh.extra || "";
  }

  function syncShotFromPicks() {
    const sh = currentShot();
    if (!sh) return;
    sh.picks = clone(state.picks);
    sh.extra = state.extra;
  }

  function countWords(text) {
    return (text || "").trim().split(/\s+/).filter(Boolean).length;
  }

  /** 对齐 skill：形态 A 完整句四段散文（模板在 prose-templates.js；缺失时回退 legacyEn） */
  function buildPromptFrom(picks, extra, mode) {
    const eth = findOpt(SUBJECT.eth, picks.eth || "eastasian");
    const age = findOpt(SUBJECT.age, picks.age);
    const body = findOpt(SUBJECT.body, picks.body);
    const hair = resolveMany(SUBJECT.hair, picks.hair, "long_straight");
    const cast = resolveMany(SUBJECT.cast, picks.cast, "solo");
    const ex = (extra || "").trim();

    if (mode === "figure") {
      const zone = findOpt(FIGURE.zone, picks.zone);
      const combo = findOpt(FIGURE.combo, picks.combo);
      const pose = resolveMany(FIGURE.pose, picks.pose, "walk_midstride");
      const cloth = resolveMany(FIGURE.cloth, picks.cloth, "outer_coat");
      const prop = resolveMany(FIGURE.prop, picks.prop, "none");
      const set = resolveMany(FIGURE.set, picks.set, "street_city");
      const light = resolveMany(FIGURE.light, picks.light, "window_soft");
      const makeup = resolveMany(FIGURE.makeup, picks.makeup, "commute");
      const cam = resolveMany(FIGURE.cam, camFromCombo(picks.cam, combo), "full");
      const expr = resolveMany(FIGURE.expr, picks.expr, "soft_smile");
      const grade = resolveMany(FIGURE.grade, picks.grade, "natural");
      const en = proseEn("figure", {
        eth, age, body, hair, cast, ex, zone, combo,
        pose, cloth, prop, set, light, makeup, cam, expr, grade,
      });
      return {
        en,
        words: countWords(en),
        zh: {
          skill: "figure-photo · SFW",
          pack: `${zone.label} · ${combo.label}`,
          pose: joinLabel(pose),
          cloth: `${joinLabel(cloth)} · ${joinLabel(prop)}`,
          set: joinLabel(set),
          light: `${joinLabel(light)} · ${joinLabel(grade)}`,
          cam: joinLabel(cam),
          note: `${joinLabel(makeup)} · ${joinLabel(expr)} · 多选叠层 · 六层`,
        },
        chips: [zone.label, combo.label, joinLabel(pose), joinLabel(cloth), joinLabel(set)].filter(Boolean),
        short: `${combo.label} · ${joinLabel(pose)}`,
      };
    }

    if (mode === "youth") {
      const cat = YOUTH || {};
      const combo = findOpt(cat.combo, picks.combo);
      const intensity = findOpt(cat.intensity, picks.intensity);
      const act = resolveMany(cat.act, picks.act, "window-risk");
      const imply = findOpt(cat.imply, picks.imply);
      const pose = resolveMany(cat.pose, picks.pose, "over_shoulder");
      const cloth = resolveMany(cat.cloth, picks.cloth, "shirt_only");
      const set = resolveMany(cat.set, picks.set, "window_sill");
      const light = resolveMany(cat.light, picks.light, "window_back");
      const cam = resolveMany(cat.cam, camFromCombo(picks.cam, combo), "mcu");
      const focus = resolveMany(cat.focus, picks.focus, "collarbone");
      const expr = resolveMany(cat.expr, picks.expr, "half_lidded");
      const aes = resolveMany(cat.aes, picks.aes, "chunyu");
      const makeup = resolveMany(cat.makeup, picks.makeup, "home_soft");
      const prop = resolveMany(cat.prop, picks.prop, "none");
      const grade = resolveMany(cat.grade, picks.grade, "jp_cream");
      const en = proseEn("youth", {
        eth, age, body, hair, cast, ex, combo, intensity, act, imply,
        pose, cloth, set, light, cam, focus, expr, aes, makeup, prop, grade,
      });
      return {
        en,
        words: countWords(en),
        zh: {
          skill: "youth-seduction · 纯欲暗示",
          pack: `${combo.label} · ${intensity.label} · ${joinLabel(aes)}`,
          pose: `${joinLabel(pose)} · ${joinLabel(act)}`,
          cloth: `${joinLabel(cloth)} · ${imply.label}`,
          set: joinLabel(set),
          light: `${joinLabel(light)} · ${joinLabel(grade)}`,
          cam: joinLabel(cam),
          note: `${joinLabel(focus)} · ${joinLabel(expr)} · 多选叠层`,
        },
        chips: [combo.label, intensity.label, joinLabel(pose), imply.label, joinLabel(focus)],
        short: `${combo.label} · ${joinLabel(pose)}`,
      };
    }

    const combo = findOpt(EROTIC.combo, picks.combo);
    const intensity = findOpt(EROTIC.intensity, picks.intensity);
    const act = resolveMany(EROTIC.act, picks.act, "solo-display");
    const finish = resolveMany(EROTIC.finish, picks.finish, "none");
    const dynamic = resolveMany(EROTIC.dynamic, picks.dynamic, "equal");
    const pose = resolveMany(EROTIC.pose, picks.pose, "bed_edge");
    const cloth = resolveMany(EROTIC.cloth, picks.cloth, "shirt_blouse");
    const exposure = findOpt(EROTIC.exposure, picks.exposure || "e1");
    const set = resolveMany(EROTIC.set, picks.set, "hotel");
    const light = resolveMany(EROTIC.light, picks.light, "tungsten");
    const fantasy = resolveMany(EROTIC.fantasy, picks.fantasy, "none");
    const cam = resolveMany(EROTIC.cam, camFromCombo(picks.cam, combo), "mcu");
    const expr = resolveMany(EROTIC.expr, picks.expr, "bedroom_eyes");
    const focus = resolveMany(EROTIC.bodyfocus, picks.bodyfocus, "full");
    const makeup = resolveMany(EROTIC.makeup, picks.makeup, "bare");
    const en = proseEn("erotic", {
      eth, age, body, hair, cast, ex, combo, intensity, act, finish,
      dynamic, pose, cloth, exposure, set, light, fantasy, cam, expr, focus, makeup,
    });
    return {
      en,
      words: countWords(en),
      zh: {
        skill: "erotic-prompt · NSFW 18+",
        pack: `${combo.label} · ${intensity.label}`,
        pose: joinLabel(pose),
        cloth: `${joinLabel(cloth)} · ${exposure.label}`,
        set: joinLabel(set),
        light: joinLabel(light),
        cam: joinLabel(cam),
        note: `${joinLabel(act)} · ${joinLabel(finish)} · 多选叠层+专属E`,
      },
      chips: [combo.label, intensity.label, joinLabel(act), exposure.label, joinLabel(pose)],
      short: `${combo.label} · ${joinLabel(act)}`,
    };
  }

  /** 组合包的机位意图优先于默认机位：镜前/全身类组合强制全身景别，避免首句机位与组合构图自相矛盾 */
  function camFromCombo(picksCam, combo) {
    const en = ((combo && combo.en) || "").toLowerCase();
    const label = (combo && combo.label) || "";
    if (/\bmirror\b/.test(en) || /\bfull\b/.test(en) || /full-body/.test(en) || /全身|对镜|镜前/.test(label)) {
      return ["full"];
    }
    return picksCam;
  }

  /** en 输出：优先形态 A 散文模板；PROSE_TEMPLATES 未加载时回退旧堆砌实现（保底不白屏） */
  function proseEn(mode, ctx) {
    if (window.PROSE_TEMPLATES) return window.PROSE_TEMPLATES.build(mode, ctx).en;
    return legacyEn(mode, ctx);
  }

  function legacyEn(mode, ctx) {
    const ethWord =
      ctx.eth.id === "override" ? "adult woman (ethnicity per user note)" : `adult ${ctx.eth.en} woman`;
    const idLine = `an ${ethWord} ${ctx.age.en}, mature facial proportions, clearly adult, hair: ${joinEn(
      ctx.hair
    )}, ${ctx.body.en}, cast: ${joinEn(ctx.cast)}`;
    const ex = ctx.ex;

    if (mode === "figure") {
      const shot = `This is a ${joinEn(ctx.cam)} with photoreal lifestyle photography, freezing a single readable pose moment (${ctx.zone.en}; recipe ${ctx.combo.en}).`;
      const main = `Main subject: ${idLine}; hair: ${joinEn(ctx.hair)}. Pose stack: ${joinEn(ctx.pose)}. Wardrobe stack (L2–L5): ${joinEn(ctx.cloth)}. Hands/prop: ${joinEn(ctx.prop)}. Makeup: ${joinEn(ctx.makeup)}. Expression: ${joinEn(ctx.expr)}.${ex ? " " + ex : ""} SFW, fully non-explicit.`;
      const env = `Environmental background: ${joinEn(ctx.set)}; only 2–4 anchors, no interior inventory.`;
      const comp = `Composition and atmosphere: visual center on posture line; ${joinEn(ctx.light)}; color grade ${joinEn(ctx.grade)}; warm-neutral East Asian skin undertone unless ethnicity overridden; masterpiece, best quality.`;
      return [shot, main, env, comp].join("\n\n");
    }

    if (mode === "youth") {
      const shot = `This is a ${joinEn(ctx.cam)} with intimate cinematic still photography, freezing one solitary pure-desire moment (${ctx.combo.en}; ${joinEn(ctx.aes)}).`;
      const main = `Main subject: ${idLine}; hair: ${joinEn(ctx.hair)}. Pose stack: ${joinEn(ctx.pose)}. Implication focus: ${joinEn(ctx.focus)}. Act: ${joinEn(ctx.act)}. Intensity: ${ctx.intensity.en}. Wardrobe stack: ${joinEn(ctx.cloth)} (${ctx.imply.en}). Makeup: ${joinEn(ctx.makeup)}. Prop: ${joinEn(ctx.prop)}. Expression: ${joinEn(ctx.expr)}.${ex ? " " + ex : ""} Soft-sensual implied only; no genitals, no penetration, no explicit sex; adult 18+ solo.`;
      const env = `Environmental background: ${joinEn(ctx.set)}; only 2–4 anchors; no second person body.`;
      const comp = `Composition and atmosphere: visual center on implication; ${joinEn(ctx.light)}; grade ${joinEn(ctx.grade)}; quiet self-seduction tension; warm-neutral East Asian undertone; masterpiece, best quality.`;
      return [shot, main, env, comp].join("\n\n");
    }

    const finishLine = ctx.finish.some((f) => f.id && f.id !== "none")
      ? ` Finish/fluids: ${joinEn(ctx.finish)}.`
      : "";
    const fantasyLine = ctx.fantasy.some((f) => f.id && f.id !== "none")
      ? ` Fantasy assist: ${joinEn(ctx.fantasy)}.`
      : "";
    const shot = `This is a ${joinEn(ctx.cam)} with cinematic erotic photography, freezing one peak instant (${ctx.combo.en}, ${ctx.intensity.en}).`;
    const main = `Main subject: ${idLine}; hair: ${joinEn(ctx.hair)}. Pose stack: ${joinEn(ctx.pose)}. Act/connection: ${joinEn(ctx.act)}.${finishLine} Dynamic: ${joinEn(ctx.dynamic)}. Wardrobe stack: ${joinEn(ctx.cloth)}. Exposure scale (specialty): ${ctx.exposure.en}. Makeup: ${joinEn(ctx.makeup)}. Expression: ${joinEn(ctx.expr)}. Body focus: ${joinEn(ctx.focus)}.${fantasyLine} Hands simple (hair or sheets).${ex ? " " + ex : ""} Adult 18+ only.`;
    const env = `Environmental background: ${joinEn(ctx.set)}; 2–4 anchors only.`;
    const comp = `Composition and atmosphere: visual center on act-readable anatomy; ${joinEn(ctx.light)}; intimate still; masterpiece, best quality.`;
    return [shot, main, env, comp].join("\n\n");
  }

  function buildCurrent() {
    return buildPromptFrom(state.picks, state.extra, state.mode);
  }

  function buildSeries() {
    return state.shots
      .map((sh, i) => {
        const b = buildPromptFrom(sh.picks, sh.extra, state.mode);
        return `### Shot ${i + 1}/${state.shots.length} · ${sh.title}\n**Continuity lock**: East Asian · early twenties · photoreal\n\n${b.en}`;
      })
      .join("\n\n---\n\n");
  }

  function buildCmd() {
    const b = buildCurrent();
    const cmd =
      state.mode === "figure"
        ? "/figure-photo-prompt"
        : state.mode === "youth"
          ? "/youth-seduction-prompt"
          : "/erotic-prompt";
    // 命令已路由到对应 skill，其自身规则即形态 A 与篇幅目标；不再附加尾注
    return `${cmd}\n\n${b.en}`;
  }

  /* ---------- combo picker ---------- */
  function comboList() {
    return catalog().combo || [];
  }

  function comboGroups() {
    const set = new Set();
    comboList().forEach((c) => {
      if (c.group) set.add(c.group);
    });
    return ["all", ...[...set]];
  }

  function filteredCombos() {
    const q = state.comboQuery.trim().toLowerCase();
    const g = state.comboGroup;
    return comboList().filter((c) => {
      if (g !== "all" && c.group !== g) return false;
      if (!q) return true;
      const hay = `${c.label} ${c.id} ${c.group || ""} ${c.en || ""} ${c.look || ""}`.toLowerCase();
      return hay.includes(q);
    });
  }

  /** 组合包实例图：来自 combo-gallery-data.js */
  const COMBO_IMG_MAP = (() => {
    const m = new Map();
    const items = window.COMBO_GALLERY?.items || [];
    items.forEach((it) => {
      if (it?.id && it?.img) m.set(it.id, it.img);
    });
    return m;
  })();

  function comboThumb(id) {
    return COMBO_IMG_MAP.get(id) || "";
  }

  /** 以指定 combo 派生 lightbox 条目（不修改 state，纯预览） */
  function comboLbItems(list) {
    const skill = state.mode;
    return list.map((c) => {
      const derived = buildPromptFrom({ ...state.picks, combo: c.id }, state.extra, state.mode);
      return {
        img: comboThumb(c.id),
        label: c.label,
        id: c.id,
        group: c.group || "",
        skill,
        look: c.look || "",
        prompt: derived.en,
      };
    });
  }

  function openComboLightbox(list, id) {
    const idx = Math.max(
      0,
      list.findIndex((c) => c.id === id)
    );
    window.Lightbox?.open(comboLbItems(list), idx);
  }

  function renderComboPicker() {
    const box = $("#comboPicker");
    if (!box) return;
    const groups = comboGroups();
    const selected = state.picks.combo;
    const q = state.comboQuery.trim();
    const g = state.comboGroup;
    const items = filteredCombos();
    const cur = findOpt(comboList(), selected) || { label: "—", id: "", group: "", look: "" };
    const curThumb = comboThumb(cur.id);

    /* 分组折叠：搜索/单组筛选时平铺；否则按组折叠（默认展开选中组，上限 3 组） */
    let gridHtml = "";
    if (items.length === 0) {
      gridHtml = `<p class="combo-empty">无匹配，试试别的关键词</p>`;
    } else if (q || g !== "all") {
      gridHtml = items.map((c, i) => comboCard(c, selected, i)).join("");
    } else {
      const byGroup = new Map();
      items.forEach((c) => {
        const key = c.group || "其他";
        if (!byGroup.has(key)) byGroup.set(key, []);
        byGroup.get(key).push(c);
      });
      if (!state.comboOpenGroups) state.comboOpenGroups = new Set();
      if (state.comboOpenGroups.size === 0 && cur.group) state.comboOpenGroups.add(cur.group);
      // 组头 + 展开组卡片
      let idx = 0;
      byGroup.forEach((list, grp) => {
        const open = state.comboOpenGroups.has(grp);
        gridHtml += `<button type="button" class="combo-group-head ${open ? "open" : ""}" data-group="${escapeAttr(
          grp
        )}" aria-expanded="${open}">${escapeHtml(grp)} <span class="combo-group-n">${list.length}</span></button>`;
        if (open) {
          gridHtml += `<div class="combo-group-body">${list
            .map((c) => comboCard(c, selected, idx++))
            .join("")}</div>`;
        }
      });
    }

    box.innerHTML = `
      <div class="combo-toolbar">
        <label class="combo-search-wrap">
          <span class="sr-only">搜索组合包</span>
          <input type="search" id="comboSearch" placeholder="搜索组合包（中文 / id / 画面）…" value="${escapeAttr(
            state.comboQuery
          )}" autocomplete="off" />
        </label>
        <select id="comboGroupSel" aria-label="分组">
          ${groups
            .map(
              (grp) =>
                `<option value="${escapeAttr(grp)}" ${grp === state.comboGroup ? "selected" : ""}>${
                  grp === "all" ? "全部分组" : grp
                }</option>`
            )
            .join("")}
        </select>
        <span class="combo-meta">${items.length} / ${comboList().length}</span>
      </div>
      <div class="combo-current">
        ${
          curThumb
            ? `<button type="button" class="combo-current-img" aria-label="查看当前组合大图" title="查看大图"><img src="${escapeAttr(
                curThumb
              )}" alt="" loading="lazy" /></button>`
            : ""
        }
        <div class="combo-current-meta">
          <strong>当前配方</strong>
          <span class="combo-current-name">${escapeHtml(cur.label || "—")}</span>
          <code>${escapeHtml(cur.id || "")}</code>
          ${cur.look ? `<span class="combo-current-look">${escapeHtml(cur.look)}</span>` : ""}
        </div>
      </div>
      <div class="combo-grid" id="comboGrid" role="listbox" aria-label="组合包列表">${gridHtml}</div>`;

    $("#comboSearch")?.addEventListener("input", (e) => {
      state.comboQuery = e.target.value;
      renderComboPicker();
      const el = $("#comboSearch");
      if (el) {
        el.focus();
        const v = el.value;
        el.setSelectionRange(v.length, v.length);
      }
    });
    $("#comboGroupSel")?.addEventListener("change", (e) => {
      state.comboGroup = e.target.value;
      renderComboPicker();
    });
    // 整卡点击 = 选中（图 + 文字区都选中）；大图预览走右上角 ⤢ 按钮
    $$("#comboGrid .combo-select-btn").forEach((btn) => {
      btn.addEventListener("click", () => pickCombo(btn.dataset.combo));
    });
    $$("#comboGrid .combo-thumb-btn").forEach((btn) => {
      btn.addEventListener("click", () => pickCombo(btn.dataset.combo));
    });
    $$("#comboGrid .combo-zoom-btn").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        openComboLightbox(items, btn.dataset.combo);
      });
    });
    $$("#comboGrid .combo-group-head").forEach((head) => {
      head.addEventListener("click", () => {
        const grp = head.dataset.group;
        if (state.comboOpenGroups.has(grp)) {
          state.comboOpenGroups.delete(grp);
        } else {
          state.comboOpenGroups.add(grp);
          while (state.comboOpenGroups.size > 3) {
            const oldest = state.comboOpenGroups.values().next().value;
            state.comboOpenGroups.delete(oldest);
          }
        }
        renderComboPicker();
      });
    });
    $(".combo-current-img")?.addEventListener("click", () => {
      openComboLightbox([cur].filter((c) => c.id), cur.id);
    });
  }

  function comboCard(c, selected, idx) {
    const on = c.id === selected ? "is-on" : "";
    const thumb = comboThumb(c.id);
    return `<div class="combo-card ${thumb ? "has-thumb" : ""} ${on}" data-combo="${escapeAttr(c.id)}">
      ${
        thumb
          ? `<button type="button" class="combo-thumb-btn" data-combo="${escapeAttr(
              c.id
            )}" aria-label="选中 ${escapeAttr(c.label)}" title="点击选中 ${escapeAttr(c.label)}"><img src="${escapeAttr(
              thumb
            )}" alt="" loading="lazy" /></button>
            <button type="button" class="combo-zoom-btn" data-combo="${escapeAttr(
              c.id
            )}" aria-label="预览 ${escapeAttr(c.label)} 大图" title="查看大图">⤢</button>`
          : ""
      }
      ${on ? `<span class="combo-check-badge" aria-hidden="true">✓</span>` : ""}
      <button type="button" class="combo-select-btn" data-combo="${escapeAttr(
        c.id
      )}" role="option" aria-selected="${c.id === selected}">
        <span class="combo-card-label">${escapeHtml(c.label)}</span>
        ${
          c.look
            ? `<span class="combo-card-look">${escapeHtml(c.look)}</span>`
            : `<span class="combo-card-group">${escapeHtml(c.group || "")}</span>`
        }
      </button>
    </div>`;
  }

  function pickCombo(id) {
    state.picks.combo = id;
    state.activePreset = null;
    syncPicksFromCombo(id);
    syncShotFromPicks();
    renderPresets();
    renderComboPicker();
    renderFields();
    refreshPreview();
    renderShotStrip();
    toast("已选组合包（主题维度已联动，可再改）");
  }

  /* ---------- 组合包主题联动：点选组合包后按主题词自动填维度（仅当前表单存在的字段） ---------- */
  const COMBO_THEME_DIMS = [
    ["酒店", { set: "hotel" }],
    ["温泉", { set: "bathroom", light: "steam_diffuse", pose: "sit_edge", cloth: "towel" }],
    ["咖啡", { set: "cafe", prop: "cup_drink" }],
    ["奶茶", { set: "cafe", prop: "boba" }],
    ["厨房", { set: "kitchen" }],
    ["床", { set: "bedroom", pose: "bed_edge" }],
    ["窗", { set: "window_sill", pose: "window_pose" }],
    ["镜自拍", { set: "vanity", pose: "mirror_self" }],
    ["对镜", { set: "vanity", pose: "mirror_self" }],
    ["浴", { set: "bathroom", light: "steam_diffuse", cloth: "towel" }],
    ["淋浴", { set: "shower" }],
    ["沙发", { set: "indoor_home", pose: "sit_cross" }],
    ["阳台", { set: "balcony_rooftop" }],
    ["街", { set: "street_city", pose: "walk_midstride" }],
    ["胡同", { set: "street_alley" }],
    ["巷弄", { set: "street_alley" }],
    ["地铁", { set: "metro_transit" }],
    ["车", { set: "car_interior" }],
    ["图书馆", { set: "library", prop: "book" }],
    ["书店", { set: "bookstore", prop: "book" }],
    ["办公室", { set: "office" }],
    ["海滩", { set: "beach", cloth: "swim", light: "golden" }],
    ["花园", { set: "garden_cn", prop: "flower" }],
    ["花海", { set: "nature_outdoor", prop: "flower" }],
    ["花店", { set: "flower_shop" }],
    ["露营", { set: "nature_outdoor", cloth: "sport" }],
    ["滑雪", { set: "nature_outdoor", cloth: "sport", light: "high_key" }],
    ["网球", { set: "gym_sport", cloth: "sport" }],
    ["瑜伽", { set: "gym_sport", pose: "yoga_asana", cloth: "sport" }],
    ["健身", { set: "gym_sport", cloth: "sport" }],
    ["拳", { set: "gym_sport", cloth: "sport" }],
    ["芭蕾", { set: "dance_studio", pose: "dance_line" }],
    ["舞台", { set: "stage_theater", light: "spotlight_stage" }],
    ["走秀", { set: "stage_theater", pose: "walk_midstride" }],
    ["屋顶", { set: "rooftop" }],
    ["天台", { set: "rooftop" }],
    ["停车场", { set: "parking" }],
    ["泳池", { set: "pool_deck", cloth: "swim" }],
    ["霓虹", { set: "night_neon", light: "neon_mix", grade: "neon_night" }],
    ["雨", { light: "overcast", grade: "cool_mute" }],
    ["国风", { set: "garden_cn", cloth: "new_chinese" }],
    ["汉服", { cloth: "new_chinese" }],
    ["旗袍", { cloth: "new_chinese" }],
    ["港风", { set: "night_neon", grade: "neon_night" }],
    ["证件", { set: "studio", light: "softbox_studio", cam: "cu", makeup: "id_neutral" }],
    ["大头贴", { set: "set_photo_booth", light: "flash_on", cam: "cu", pose: "hand_face", expr: "laugh" }],
    ["拍贴", { set: "set_photo_booth", light: "flash_on", cam: "cu", expr: "laugh" }],
    ["樱花", { set: "set_sakura_path", grade: "jp_cream" }],
    ["银杏", { set: "set_ginkgo" }],
    ["美术馆", { set: "set_museum", light: "softbox_studio" }],
    ["画廊", { set: "set_gallery_opening" }],
    ["钢琴", { set: "set_conservatory", light: "window_soft", pose: "sit_edge" }],
    ["电竞", { set: "set_arcade", light: "neon_mix" }],
    ["公园", { set: "garden_cn", light: "window_soft" }],
    ["机场", { set: "airport", prop: "luggage" }],
    ["影院", { set: "cinema_lobby" }],
    ["洗衣", { set: "laundromat" }],
    ["夜市", { set: "night_market", light: "neon_mix" }],
    ["校园", { set: "campus_adult" }],
    ["聚会", { set: "rooftop", pose: "hand_face" }],
    ["私房", { set: "bedroom", light: "tungsten" }],
    ["居家", { set: "indoor_home", cloth: "lounge" }],
    ["玄关", { set: "indoor_home" }],
    ["外滩", { set: "landmark_travel" }],
    ["婚礼", { set: "stage_theater", cloth: "formal" }],
    ["婚纱", { cloth: "formal" }],
    ["新娘", { cloth: "formal" }],
  ];

  function syncPicksFromCombo(id) {
    const c = findOpt(catalog().combo, id);
    if (!c) return;
    const blob = `${c.label} ${c.look} ${c.id}`.toLowerCase();
    const merge = {};
    for (const [cn, dims] of COMBO_THEME_DIMS) {
      if (!blob.includes(cn)) continue;
      for (const [field, val] of Object.entries(dims)) {
        if (field in state.picks && !(field in merge)) merge[field] = val;
      }
    }
    if (Object.keys(merge).length) applyMergeToPicks(merge);
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
  function escapeAttr(s) {
    return escapeHtml(s).replace(/'/g, "&#39;");
  }

  /* ---------- field chips ---------- */
  function fieldGroups() {
    if (state.mode === "figure") return FIELD_GROUPS_FIGURE;
    if (state.mode === "youth") return FIELD_GROUPS_YOUTH;
    return FIELD_GROUPS_EROTIC;
  }

  function renderFields() {
    const root = $("#fieldGroups");
    if (!root) return;
    root.innerHTML = fieldGroups()
      .map((g) => {
        const open = state.openGroups[g.id] !== false;
        return `
        <details class="field-group" data-gid="${g.id}" ${open ? "open" : ""}>
          <summary>
            <span>${g.title}</span>
            <span class="field-group-hint">${g.hint || "点选即可，可搜"}</span>
          </summary>
          <div class="field-group-body">
            ${g.fields
              .map((f) => {
                const list = listFor(f.list);
                const pol = policyOf(f.key);
                const multi = isMulti(f.key);
                const items = multi
                  ? resolveMany(list, state.picks[f.key], null)
                  : [findOpt(list, state.picks[f.key])];
                const curLab = multi ? joinLabel(items) : items[0]?.label || "—";
                const tagClass =
                  pol.mode === "free"
                    ? "field-multi-tag is-free"
                    : multi
                      ? "field-multi-tag is-vertical"
                      : "field-single-tag";
                const tagText =
                  pol.tag || (multi ? "纵向叠层" : "单选");
                const tagTitle = pol.hint || tagText;
                return `
                <div class="field-block ${multi ? "is-multi" : "is-single"} mode-${escapeAttr(
                  pol.mode || "single"
                )}" data-field="${f.key}">
                  <div class="field-head">
                    <label>${f.label}<span class="${tagClass}" title="${escapeAttr(
                  tagTitle
                )}">${escapeHtml(tagText)}</span></label>
                    <span class="field-cur" title="${escapeAttr(curLab)}">${escapeHtml(curLab)}</span>
                    <input type="search" class="field-filter" data-fkey="${f.key}" data-flist="${
                  f.list
                }" placeholder="筛…" />
                  </div>
                  <div class="chip-select" data-chips="${f.key}" data-list="${f.list}" data-multi="${
                  multi ? "1" : "0"
                }">
                    ${renderChips(list, f.key, "")}
                  </div>
                </div>`;
              })
              .join("")}
          </div>
        </details>`;
      })
      .join("");

    root.querySelectorAll("details.field-group").forEach((d) => {
      d.addEventListener("toggle", () => {
        state.openGroups[d.dataset.gid] = d.open;
      });
    });

    root.querySelectorAll(".field-filter").forEach((inp) => {
      inp.addEventListener("input", () => {
        const key = inp.dataset.fkey;
        const list = listFor(inp.dataset.flist);
        const box = root.querySelector(`[data-chips="${key}"]`);
        if (box) box.innerHTML = renderChips(list, key, inp.value);
        bindChipClicks(box);
      });
    });

    root.querySelectorAll(".chip-select").forEach((box) => bindChipClicks(box));
  }

  function renderChips(list, key, filterText) {
    const q = (filterText || "").trim().toLowerCase();
    const selected = new Set(asIdList(state.picks[key]));
    let lastG = null;
    const parts = [];
    let n = 0;
    for (const o of list) {
      const hay = `${o.label} ${o.id} ${o.group || ""}`.toLowerCase();
      if (q && !hay.includes(q)) continue;
      if (o.group && o.group !== lastG) {
        lastG = o.group;
        parts.push(`<div class="chip-group-label">${escapeHtml(o.group)}</div>`);
      }
      const on = selected.has(o.id) ? "is-on" : "";
      parts.push(
        `<button type="button" class="chip-opt ${on}" data-key="${escapeAttr(key)}" data-val="${escapeAttr(
          o.id
        )}">${escapeHtml(o.label)}</button>`
      );
      n++;
      if (n >= 100 && q) break;
      if (n >= 120 && !q) break; // 无筛选时也限制 DOM 体积，靠搜索展开
    }
    if (!n) parts.push(`<span class="chip-empty">无匹配</span>`);
    else if (!q && list.length > 120)
      parts.push(`<span class="chip-empty">已显示前 120，请用上方筛选看更多</span>`);
    return parts.join("");
  }

  function bindChipClicks(box) {
    if (!box) return;
    box.querySelectorAll(".chip-opt").forEach((btn) => {
      btn.addEventListener("click", () => {
        const key = btn.dataset.key;
        const val = btn.dataset.val;
        togglePick(key, val);
        state.activePreset = null;
        syncShotFromPicks();
        const block = btn.closest(".field-block");
        const list = listFor(box.dataset.list);
        const items = isMulti(key)
          ? resolveMany(list, state.picks[key], null)
          : [findOpt(list, state.picks[key])];
        const lab = block?.querySelector(".field-cur");
        if (lab) lab.textContent = isMulti(key) ? joinLabel(items) : items[0]?.label || "—";
        const sel = new Set(asIdList(state.picks[key]));
        box.querySelectorAll(".chip-opt").forEach((b) => {
          b.classList.toggle("is-on", sel.has(b.dataset.val));
        });
        const nowOn = sel.has(val);
        showRecommendFor(key, val, nowOn);
        renderPresets();
        refreshPreview();
        renderShotStrip();
      });
    });
  }

  function renderExtra() {
    const ta = $("#dirExtra");
    if (ta && ta.value !== state.extra) ta.value = state.extra;
  }

  /* ---------- preview / shots ---------- */
  function refreshPreview() {
    const built = buildCurrent();
    const pre = $("#dirPreview");
    const zh = $("#dirZh");
    const chips = $("#dirChips");
    const wc = $("#dirWordCount");
    if (pre) pre.textContent = built.en;
    if (wc) {
      const w = built.words;
      // 篇幅规格与 skill 对齐：figure/youth Main 100–180 · 全文 200–380 · 逾 420 压缩；erotic 200–400 · 逾 440 压缩
      const max = state.mode === "erotic" ? 440 : 420;
      const ok = w <= max;
      wc.textContent = `约 ${w} 英文词 · 目标 ${
        state.mode === "erotic" ? "200–400" : "200–380"
      } · 上限约 ${max}`;
      wc.classList.toggle("is-warn", !ok);
    }
    if (zh) {
      zh.innerHTML = `
        <div><b>Skill</b> ${escapeHtml(built.zh.skill)}</div>
        <div><b>Shot</b> ${state.shotIndex + 1}/${state.shots.length} · ${escapeHtml(
        currentShot()?.title || ""
      )}</div>
        <div><b>选题</b> ${escapeHtml(built.zh.pack)}</div>
        <div><b>姿势</b> ${escapeHtml(built.zh.pose)}</div>
        <div><b>服饰</b> ${escapeHtml(built.zh.cloth)}</div>
        <div><b>场景</b> ${escapeHtml(built.zh.set)}</div>
        <div><b>光/镜</b> ${escapeHtml(built.zh.light)} · ${escapeHtml(built.zh.cam)}</div>
        <div><b>备注</b> ${escapeHtml(built.zh.note)}</div>`;
    }
    if (chips) {
      chips.innerHTML = built.chips.map((c) => `<span class="chip">${escapeHtml(c)}</span>`).join("");
    }
    const series = $("#dirSeries");
    if (series) {
      series.innerHTML = state.shots
        .map((sh, i) => {
          const s = buildPromptFrom(sh.picks, sh.extra, state.mode).short;
          return `<button type="button" class="s-item ${
            i === state.shotIndex ? "active" : ""
          }" data-si="${i}">#${i + 1} ${escapeHtml(sh.title)} — ${escapeHtml(s)}</button>`;
        })
        .join("");
      series.querySelectorAll(".s-item").forEach((el) => {
        el.addEventListener("click", () => selectShot(+el.dataset.si));
      });
    }
  }

  function renderShotStrip() {
    const strip = $("#shotStrip");
    if (!strip) return;
    strip.innerHTML = state.shots
      .map((sh, i) => {
        const short = buildPromptFrom(sh.picks, sh.extra, state.mode).short;
        return `
        <div class="shot-card ${i === state.shotIndex ? "active" : ""}" data-si="${i}">
          ${
            state.shots.length > 1
              ? `<button type="button" class="shot-del" data-del="${i}" title="删除">×</button>`
              : ""
          }
          <div class="shot-num">Shot ${i + 1}</div>
          <div class="shot-title">${escapeHtml(sh.title)}</div>
          <div class="shot-tags">${escapeHtml(short)}</div>
        </div>`;
      })
      .join("");

    strip.querySelectorAll(".shot-card").forEach((card) => {
      card.addEventListener("click", (e) => {
        if (e.target.closest(".shot-del")) return;
        selectShot(+card.dataset.si);
      });
    });
    strip.querySelectorAll(".shot-del").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        deleteShot(+btn.dataset.del);
      });
    });
  }

  function selectShot(i) {
    syncShotFromPicks();
    state.shotIndex = Math.max(0, Math.min(i, state.shots.length - 1));
    syncPicksFromShot();
    renderAll();
  }

  function addShot(duplicate) {
    syncShotFromPicks();
    const base = duplicate ? clone(currentShot().picks) : defaultsPicks(state.mode);
    const extra = duplicate ? currentShot().extra : "";
    const sh = newShot(state.shots.length, base);
    sh.extra = extra;
    if (duplicate) sh.title = currentShot().title + " 变体";
    state.shots.push(sh);
    state.shotIndex = state.shots.length - 1;
    syncPicksFromShot();
    renderAll();
  }

  function deleteShot(i) {
    if (state.shots.length <= 1) return;
    syncShotFromPicks();
    state.shots.splice(i, 1);
    if (state.shotIndex >= state.shots.length) state.shotIndex = state.shots.length - 1;
    syncPicksFromShot();
    renderAll();
  }

  function varyShots() {
    syncShotFromPicks();
    // 已有非空分镜将被覆盖时先确认（空态/全新不弹窗）。
    // 注意：picks 经 sanitizeAllPicks 补全，须与补全后的默认值比较，否则空态也会误判为「有内容」
    const defaults = JSON.stringify(sanitizeAllPicks(defaultsPicks(state.mode)));
    const hasContent = state.shots.length > 1 || state.shots.some(
      (s) => s.extra || (s.title && s.title !== "Shot 1") ||
        JSON.stringify(s.picks) !== defaults
    );
    if (hasContent && !confirm("一键 4 镜将覆盖当前所有分镜，继续？")) return;
    const base = clone(state.picks);
    const poses = listFor("pose");
    const cams = listFor("cam");
    const sets = listFor("set");
    const lights = listFor("light");
    state.shots = [];
    for (let i = 0; i < 4; i++) {
      const p = clone(base);
      if (poses[i % poses.length]) p.pose = poses[i % poses.length].id;
      if (cams[(i * 2) % cams.length]) p.cam = cams[(i * 2) % cams.length].id;
      if (sets[(i + 1) % sets.length]) p.set = sets[(i + 1) % sets.length].id;
      if (lights[(i + 2) % lights.length]) p.light = lights[(i + 2) % lights.length].id;
      const sh = newShot(i, p);
      sh.title = "Shot " + (i + 1);
      sh.extra = state.extra;
      state.shots.push(sh);
    }
    state.shotIndex = 0;
    syncPicksFromShot();
    renderAll();
    toast("已生成 4 镜变体");
  }

  function randomizeShot() {
    state.activePreset = null;
    const pick = (arr) => arr[Math.floor(Math.random() * arr.length)].id;
    state.picks.eth = pick(SUBJECT.eth);
    state.picks.age = pick(SUBJECT.age);
    state.picks.sex = pick(SUBJECT.sex || [{ id: "woman" }]);
    state.picks.body = pick(SUBJECT.body);
    state.picks.cast = pick(SUBJECT.cast || [{ id: "solo" }]);
    state.picks.hair = pick(SUBJECT.hair);
    state.picks.combo = pick(comboList());
    if (state.mode === "figure") {
      state.picks.zone = pick(FIGURE.zone);
      state.picks.pose = pick(FIGURE.pose);
      state.picks.cloth = pick(FIGURE.cloth);
      state.picks.prop = pick(FIGURE.prop);
      state.picks.set = pick(FIGURE.set);
      state.picks.light = pick(FIGURE.light);
      state.picks.cam = pick(FIGURE.cam);
      state.picks.makeup = pick(FIGURE.makeup);
      state.picks.expr = pick(FIGURE.expr);
      state.picks.grade = pick(FIGURE.grade);
    } else if (state.mode === "youth") {
      const Y = YOUTH || {};
      state.picks.intensity = pick(Y.intensity);
      state.picks.act = pick(Y.act);
      state.picks.imply = pick(Y.imply);
      state.picks.pose = pick(Y.pose);
      state.picks.cloth = pick(Y.cloth);
      state.picks.set = pick(Y.set);
      state.picks.light = pick(Y.light);
      state.picks.cam = pick(Y.cam);
      state.picks.focus = pick(Y.focus);
      state.picks.expr = pick(Y.expr);
      state.picks.aes = pick(Y.aes);
    } else {
      state.picks.intensity = pick(EROTIC.intensity);
      state.picks.act = pick(EROTIC.act);
      state.picks.finish = pick(EROTIC.finish);
      state.picks.dynamic = pick(EROTIC.dynamic);
      state.picks.pose = pick(EROTIC.pose);
      state.picks.cloth = pick(EROTIC.cloth);
      state.picks.set = pick(EROTIC.set);
      state.picks.light = pick(EROTIC.light);
      state.picks.fantasy = pick(EROTIC.fantasy);
      state.picks.cam = pick(EROTIC.cam);
      state.picks.expr = pick(EROTIC.expr);
      state.picks.bodyfocus = pick(EROTIC.bodyfocus);
    }
    syncShotFromPicks();
    renderAll();
    toast("已随机当前镜");
  }

  /* ---------- recipes ---------- */
  function loadRecipes() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    } catch {
      return [];
    }
  }
  function saveRecipes(list) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
  }
  function refreshRecipeSelect() {
    const sel = $("#recipeSelect");
    if (!sel) return;
    const list = loadRecipes().filter((r) => r.mode === state.mode);
    sel.innerHTML =
      `<option value="">— 已存配方 —</option>` +
      list.map((r) => `<option value="${r.id}">${escapeHtml(r.name)}</option>`).join("");
  }
  function saveCurrentRecipe() {
    syncShotFromPicks();
    const name = ($("#recipeName")?.value || "").trim() || `配方 ${new Date().toLocaleString()}`;
    const list = loadRecipes();
    const recipe = {
      id: "r_" + Date.now(),
      name,
      mode: state.mode,
      shots: clone(state.shots),
      shotIndex: state.shotIndex,
      savedAt: Date.now(),
    };
    list.unshift(recipe);
    saveRecipes(list.slice(0, 40));
    refreshRecipeSelect();
    const sel = $("#recipeSelect");
    if (sel) sel.value = recipe.id;
    toast("已保存");
  }
  function loadRecipe(id) {
    const r = loadRecipes().find((x) => x.id === id);
    if (!r) return;
    state.mode = r.mode;
    state.shots = clone(r.shots);
    state.shotIndex = r.shotIndex || 0;
    applyModeClass();
    syncPicksFromShot();
    renderAll();
    refreshRecipeSelect();
    toast("已加载");
  }
  function deleteRecipe() {
    const id = $("#recipeSelect")?.value;
    if (!id) return;
    const name = $("#recipeSelect")?.selectedOptions?.[0]?.textContent?.trim() || id;
    if (!confirm(`删除配方「${name}」？此操作不可恢复`)) return;
    saveRecipes(loadRecipes().filter((r) => r.id !== id));
    refreshRecipeSelect();
    toast("已删除");
  }
  function exportRecipe() {
    syncShotFromPicks();
    const data = { mode: state.mode, shots: state.shots };
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `director-${state.mode}-${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(a.href);
  }
  function importRecipe(file) {
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const data = JSON.parse(reader.result);
        if (!data || typeof data !== "object" || !Array.isArray(data.shots)) {
          toast("导入失败：文件缺少 shots 字段");
          return;
        }
        if (!confirm("导入将覆盖当前导演台的模式与分镜，继续？")) return;
        state.mode = data.mode || "figure";
        state.shots = data.shots.length ? data.shots : [newShot(0)];
        state.shotIndex = 0;
        applyModeClass();
        syncPicksFromShot();
        renderAll();
        refreshRecipeSelect();
        toast("已导入");
      } catch {
        toast("导入失败：不是合法的 JSON 文件");
      }
    };
    reader.readAsText(file);
  }

  function toast(msg) {
    const el = $("#dirToast");
    if (!el) return;
    el.textContent = msg;
    el.style.opacity = "1";
    setTimeout(() => (el.style.opacity = "0"), 1400);
  }

  async function copyText(text, btn) {
    try {
      await navigator.clipboard.writeText(text);
      if (btn) {
        const old = btn.textContent;
        btn.textContent = "已复制";
        setTimeout(() => (btn.textContent = old), 1200);
      }
    } catch {
      if (btn) btn.textContent = "失败";
    }
  }

  function applyModeClass() {
    const root = $("#directorRoot");
    root?.classList.toggle("mode-nsfw", state.mode === "erotic");
    root?.classList.toggle("mode-sfw", state.mode === "figure");
    root?.classList.toggle("mode-youth", state.mode === "youth");
    $$(".skill-switch button").forEach((b) => {
      b.classList.remove("active-sfw", "active-nsfw", "active-youth");
      if (b.dataset.mode === "figure" && state.mode === "figure") b.classList.add("active-sfw");
      if (b.dataset.mode === "youth" && state.mode === "youth") b.classList.add("active-youth");
      if (b.dataset.mode === "erotic" && state.mode === "erotic") b.classList.add("active-nsfw");
    });
    const tip = $("#modeTip");
    if (tip) {
      tip.textContent =
        state.mode === "figure"
          ? "SFW · 姿态优先 · Main 100–180 · 全文 200–380 词 · 禁默认私房"
          : state.mode === "youth"
            ? "纯欲暗示 · 姿态+暗示焦点优先 · Main 100–180 · 全文 200–380 词 · 禁止露骨 · I3 须点名"
            : "NSFW 18+ · 连接优先 · Main 100–180 · 全文 200–400 词 · 默认自展 E1/E2";
    }
  }

  function setMode(mode) {
    syncShotFromPicks();
    state.mode = mode;
    state.comboQuery = "";
    state.comboGroup = "all";
    state.activePreset = null;
    state.shots = [newShot(0, defaultsPicks(mode))];
    state.shotIndex = 0;
    applyModeClass();
    syncPicksFromShot();
    renderAll();
    refreshRecipeSelect();
  }

  function renderAll() {
    renderPresets();
    renderComboPicker();
    renderFields();
    renderExtra();
    renderShotStrip();
    refreshPreview();
  }

  function bindChrome() {
    $$(".skill-switch button").forEach((b) => {
      b.addEventListener("click", () => setMode(b.dataset.mode));
    });
    $("#btnAddShot")?.addEventListener("click", () => addShot(false));
    $("#btnDupShot")?.addEventListener("click", () => addShot(true));
    $("#btnVaryShots")?.addEventListener("click", varyShots);
    $("#btnDirRandom")?.addEventListener("click", randomizeShot);
    $("#btnDirCopy")?.addEventListener("click", (e) =>
      copyText(buildCurrent().en, e.currentTarget)
    );
    $("#btnDirCopyCmd")?.addEventListener("click", (e) => copyText(buildCmd(), e.currentTarget));
    $("#btnDirCopySeries")?.addEventListener("click", (e) =>
      copyText(buildSeries(), e.currentTarget)
    );
    $("#btnSaveRecipe")?.addEventListener("click", saveCurrentRecipe);
    $("#btnLoadRecipe")?.addEventListener("click", () => {
      const id = $("#recipeSelect")?.value;
      if (id) loadRecipe(id);
    });
    $("#btnDelRecipe")?.addEventListener("click", deleteRecipe);
    $("#btnExportRecipe")?.addEventListener("click", exportRecipe);
    $("#btnImportRecipe")?.addEventListener("click", () => $("#recipeFile")?.click());
    $("#recipeFile")?.addEventListener("change", (e) => {
      const f = e.target.files?.[0];
      if (f) importRecipe(f);
      e.target.value = "";
    });
    $("#dirExtra")?.addEventListener("input", (e) => {
      state.extra = e.target.value;
      syncShotFromPicks();
      refreshPreview();
    });
    $("#btnRecApply")?.addEventListener("click", applyCurrentRecommend);
    $("#btnRecDismiss")?.addEventListener("click", dismissRecommend);
    $("#btnResetDefaults")?.addEventListener("click", () => {
      state.picks = defaultsPicks(state.mode);
      state.extra = "";
      state.activePreset = null;
      syncShotFromPicks();
      renderAll();
      toast("已恢复默认");
    });
  }

  function init() {
    if (!$("#directorRoot")) return;
    state.shots = [newShot(0)];
    state.shotIndex = 0;
    syncPicksFromShot();
    applyModeClass();
    bindChrome();
    renderAll();
    refreshRecipeSelect();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
