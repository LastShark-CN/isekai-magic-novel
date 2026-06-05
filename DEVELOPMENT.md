# 本地开发指南

## 🚀 快速开始

### 前置要求

- [Git](https://git-scm.com/) - 版本控制
- [VS Code](https://code.visualstudio.com/) 或其他 Markdown 编辑器（推荐）
- 现代浏览器（用于预览）

### 克隆项目

```bash
git clone https://github.com/LastShark-CN/异世界魔法泄漏到现实.git
cd 异世界魔法泄漏到现实
```

## 📖 阅读和预览

### 方法一：使用 VS Code

1. 安装 VS Code
2. 安装以下扩展：
   - **Markdown All in One** - Markdown 增强功能
   - **Markdown Preview Enhanced** - 实时预览
   - **markdownlint** - 格式检查
3. 打开任意 `.md` 文件
4. 按 `Ctrl+Shift+V` (Windows/Linux) 或 `Cmd+Shift+V` (Mac) 预览

### 方法二：使用 Typora

1. 下载并安装 [Typora](https://typora.io/)
2. 打开项目文件夹
3. 直接点击 `.md` 文件即可预览

### 方法三：使用 GitHub

1. 在浏览器中访问仓库
2. 点击任意 `.md` 文件
3. GitHub 会自动渲染 Markdown

## 🔍 检查链接

### 手动检查

确保所有相对路径链接都正确：
- `./目录.md` - 根目录的文件
- `../目录.md` - 上一级目录的文件
- `./小说/第一章.md` - 子目录的文件

### 自动检查工具

#### 使用 lychee（推荐）

```bash
# 安装 lychee
cargo install lychee

# 检查所有 Markdown 文件中的链接
lychee --verbose "./**/*.md"
```

#### 使用 markdown-link-check

```bash
# 安装
npm install -g markdown-link-check

# 检查单个文件
markdown-link-check README.md

# 检查所有文件
find . -name "*.md" -exec markdown-link-check {} \;
```

## ✏️ 编辑内容

### 修改章节

1. 进入 `小说/` 目录
2. 打开要修改的章节文件
3. 进行编辑
4. 保存并在预览中检查效果

### 添加新角色

1. 在 `人物/` 目录创建新文件
2. 参考现有角色档案格式
3. 在 `人物/角色索引.md` 中添加条目
4. 在其他相关文件中添加链接

### 格式规范

遵循 [.markdownlint.jsonc](./.markdownlint.jsonc) 中的规则：

- ✅ 第一行必须是 H1 标题
- ✅ 标题前后保留空行
- ✅ 段落之间保留空行
- ✅ 使用一致的列表格式
- ❌ 避免过长的单行（可选）

## 🧪 测试

### 本地预览测试

1. 在 VS Code 中打开文件
2. 切换到预览模式
3. 检查以下内容：
   - 标题层级是否正确
   - 图片是否正常显示
   - 链接是否可点击
   - 格式是否美观

### 链接完整性检查

```bash
# 使用 grep 查找可能的断链
grep -r "\[.*\](\.\/" --include="*.md" | grep -v "^Binary"

# 手动验证每个链接指向的文件是否存在
```

### GitHub Actions 测试

推送代码后，GitHub Actions 会自动运行：
- Markdown lint 检查
- 链接有效性验证

查看结果：
1. 访问仓库的 "Actions" 标签
2. 点击最近的工作流运行
3. 查看详细日志

## 📝 提交更改

### Git 工作流程

```bash
# 1. 查看修改
git status

# 2. 添加修改
git add .

# 3. 提交（使用清晰的 commit message）
git commit -m "类型: 简洁的描述"

# 示例：
git commit -m "fix: 修复第五章的链接错误"
git commit -m "feat: 添加新角色莉娜的详细档案"
git commit -m "docs: 更新 README 的项目统计"

# 4. 推送到远程
git push origin main
```

### Commit Message 规范

格式：`类型: 描述`

**类型**：
- `feat` - 新功能
- `fix` - 修复问题
- `docs` - 文档更新
- `style` - 格式调整（不影响代码含义）
- `refactor` - 重构
- `test` - 测试相关
- `chore` - 构建过程或辅助工具变动

**示例**：
```
fix: 修正目录中第五章的链接
feat: 添加角色战力对比表格
docs: 完善贡献指南
style: 统一章节标题格式
```

## 🐛 常见问题

### Q: 图片无法显示？

A: 检查以下几点：
1. 图片文件是否在 `image/` 目录
2. 路径是否正确（注意大小写）
3. 文件格式是否支持（建议使用 JPG/PNG）

### Q: 链接点击无效？

A: 检查：
1. 目标文件是否存在
2. 路径是否正确（`./` vs `../`）
3. 文件名是否完全匹配（包括扩展名）
4. 是否有空格或特殊字符

### Q: Markdown 格式检查报错？

A: 
1. 查看 `.markdownlint.jsonc` 了解规则
2. 运行 `markdownlint "**/*.md"` 查看详细错误
3. 根据提示修复问题
4. 必要时可以临时禁用某条规则

### Q: 如何批量修改所有章节的导航？

A: 可以使用脚本或搜索替换：
```bash
# 使用 sed 批量替换（Linux/Mac）
sed -i 's/旧文本/新文本/g' 小说/*.md

# Windows PowerShell
(Get-Content 小说/*.md) -replace '旧文本', '新文本' | Set-Content 小说/*.md
```

## 🛠️ 有用的小技巧

### 1. 快速查找断链

```bash
# 查找所有以 ./ 开头的链接
grep -rh "\[.*\](\./" --include="*.md" | sort -u

# 检查这些链接对应的文件是否存在
```

### 2. 统计字数

```bash
# Linux/Mac
wc -w 小说/*.md

# Windows PowerShell
Get-Content 小说/*.md | Measure-Object -Word
```

### 3. 生成目录列表

```bash
# 列出所有章节
ls 小说/*.md | sort

# 提取所有 H1 标题
grep "^# " 小说/*.md
```

### 4. 批量检查文件格式

```bash
# 检查所有文件是否以 H1 标题开头
for file in 小说/*.md; do
  head -n 1 "$file" | grep -q "^# " || echo "$file 缺少 H1 标题"
done
```

## 📚 学习资源

- [Markdown 官方指南](https://www.markdownguide.org/)
- [GitHub Flavored Markdown](https://github.github.com/gfm/)
- [markdownlint 规则说明](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
- [Git 教程](https://git-scm.com/book/zh/v2)

---

<div align="center">

**祝你编辑愉快！** ✨

[⬆ 返回顶部](#本地开发指南) | [📖 返回 README](./README.md)

</div>
