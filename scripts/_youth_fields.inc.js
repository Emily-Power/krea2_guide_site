  const FIELD_GROUPS_YOUTH = [
    {
      id: "subject",
      title: "① 主体",
      hint: "18+ · 默认东亚 early twenties · 独处",
      fields: [
        { key: "eth", list: "eth", label: "人种" },
        { key: "age", list: "age", label: "年龄" },
        { key: "hair", list: "hair", label: "发型" },
        { key: "body", list: "body", label: "体型" },
      ],
    },
    {
      id: "scale",
      title: "② 尺度 · 行为 · 暴露 I",
      hint: "默认 pure-desire + I1/I2；I3 内衣须点名；禁露骨",
      fields: [
        { key: "intensity", list: "intensity", label: "尺度" },
        { key: "act", list: "act", label: "行为瞬间" },
        { key: "imply", list: "imply", label: "暴露 I" },
      ],
    },
    {
      id: "posecloth",
      title: "③ 姿势 · 暗示 · 服饰 · 表情",
      fields: [
        { key: "pose", list: "pose", label: "姿势" },
        { key: "focus", list: "focus", label: "暗示焦点" },
        { key: "cloth", list: "cloth", label: "服饰状态" },
        { key: "expr", list: "expr", label: "表情" },
      ],
    },
    {
      id: "scene",
      title: "④ 场景 · 光 · 镜头 · 美学壳",
      fields: [
        { key: "set", list: "set", label: "场景" },
        { key: "light", list: "light", label: "布光" },
        { key: "cam", list: "cam", label: "镜头画幅" },
        { key: "aes", list: "aes", label: "美学壳" },
      ],
    },
  ];
