# 项目结构说明

## 📁 目录结构

```
异世界魔法泄漏到现实，然而我最接近裂缝/
│
├── .github/                    # GitHub 配置
│   └── workflows/              # GitHub Actions 工作流
│       └── markdown-lint.yml   # Markdown 格式检查
│
├── image/                      # 图片资源
│   └── 封面.jpg                # 小说封面图片
│
├── 人物/                       # 角色资料
│   ├── 陈宇（帕顿）.md         # 主角档案
│   ├── 林远山.md               # 导师档案
│   ├── 小雨.md                 # 水系魔法师
│   ├── 大伟.md                 # 土系魔法师
│   ├── 老周.md                 # 风系魔法师
│   ├── 张浩.md                 # 悲剧英雄
│   ├── 莉娜.md                 # 异世界魔法师
│   ├── 莫尔斯长老.md           # 异世界长老
│   └── 角色索引.md             # 角色总览和战力对比
│
├── 小说/                       # 正文章节
│   ├── 第一章：这是一个超大的裂缝.md
│   ├── 第二章：失控的力量.md
│   ├── 第三章：崩溃边缘.md
│   ├── 第四章：转折点.md
│   ├── 第五章：魔法.md
│   ├── 第六章：黑暗中的光芒.md
│   ├── 第七章：守护者之夜.md
│   ├── 第八章：正义的代价.md
│   ├── 第九章：裂缝的另一端.md
│   └── 第十章：新的开始.md
│
├── .gitignore                  # Git 忽略配置
├── .markdownlint.jsonc         # Markdown lint 配置
├── CONTRIBUTING.md             # 贡献指南
├── LICENSE                     # 开源许可证 (CC BY-NC-SA 4.0)
├── README.md                   # 项目主文档
├── RELEASE.md                  # 发布说明
├── 封面.md                     # 封面页
└── 目录.md                     # 章节目录
```

## 📄 核心文件说明

### 主要文档

| 文件 | 用途 | 说明 |
|------|------|------|
| `README.md` | 项目主页 | 包含故事简介、快速开始、角色介绍等 |
| `目录.md` | 导航页面 | 所有章节的链接列表 |
| `封面.md` | 封面页 | 展示封面图片和基本信息 |
| `CONTRIBUTING.md` | 贡献指南 | 如何参与项目改进 |
| `LICENSE` | 许可证 | CC BY-NC-SA 4.0 许可协议 |
| `RELEASE.md` | 发布说明 | 版本更新记录 |

### 配置文件

| 文件 | 用途 | 说明 |
|------|------|------|
| `.gitignore` | Git 配置 | 定义需要忽略的文件 |
| `.markdownlint.jsonc` | 格式检查 | Markdown lint 规则配置 |
| `.github/workflows/markdown-lint.yml` | CI/CD | 自动检查 Markdown 格式 |

### 内容目录

#### 人物/
存放所有角色的详细档案，包括：
- 背景故事
- 能力设定
- 性格特点
- 战力评级
- 角色关系

**重要文件**：
- `角色索引.md` - 所有角色的总览，包含战力对比和关系图

#### 小说/
存放所有章节的正文章件，按章节顺序编号。

**阅读顺序**：
1. 第一章 → 第二章 → ... → 第十章
2. 每章末尾都有导航链接，可跳转到上一章/下一章

#### image/
存放项目使用的图片资源。
- `封面.jpg` - 小说封面图片

## 🔗 文件关系

```
README.md (入口)
    ↓
封面.md / 目录.md
    ↓
小说/第一章.md → 小说/第二章.md → ... → 小说/第十章.md
    ↓
人物/角色索引.md
    ↓
各角色详细档案
```

## 📝 编辑建议

### 修改章节内容
1. 进入 `小说/` 目录
2. 找到对应的章节文件
3. 保持 Markdown 格式规范
4. 确保标题为 H1 级别
5. 保留底部的导航链接

### 添加新角色
1. 在 `人物/` 目录创建新文件
2. 文件名格式：`角色名.md`
3. 参考现有角色档案的格式
4. 在 `角色索引.md` 中添加条目

### 修改配置
- `.gitignore` - 添加需要忽略的文件类型
- `.markdownlint.jsonc` - 调整 Markdown 检查规则
- GitHub Actions - 修改自动化检查流程

## 🎯 最佳实践

1. **保持一致性**：所有章节和角色档案使用统一的格式
2. **检查链接**：确保所有内部链接都有效
3. **预览效果**：在 Markdown 编辑器中预览修改
4. **提交信息**：使用清晰的 commit message
5. **分支管理**：重大修改先创建分支

## 🛠️ 工具推荐

### Markdown 编辑器
- [VS Code](https://code.visualstudio.com/) + Markdown 插件
- [Typora](https://typora.io/)
- [Markdown Editor](https://markdown-editor.github.io/)

### 格式检查
- [markdownlint](https://github.com/DavidAnson/markdownlint)
- GitHub Actions 自动检查

### 版本控制
- Git
- GitHub Desktop

---

<div align="center">

*最后更新：2026年6月*

[⬆ 返回顶部](#项目结构说明) | [📖 返回 README](./README.md)

</div>
