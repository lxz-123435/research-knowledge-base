# Zotero + Better BibTeX + Obsidian 引用系统配置指南

## 第一步：Zotero 配置

### 1.1 安装 Zotero
下载安装：https://www.zotero.org/

### 1.2 安装 Better BibTeX 插件
1. 打开 Zotero
2. 工具 → 附加组件
3. 点击齿轮图标 → 从文件安装附加组件
4. 下载：https://github.com/retorquere/zotero-better-bibtex/releases
5. 选择 `zotero-better-bibtex.xpi` 文件安装

### 1.3 配置 Better BibTeX 导出
1. 编辑 → 首选项 → Better BibTeX
2. **Citation Key Format** 设置为：
   ```
   [auth.lower][year]
   ```
3. 勾选 **Keep updated**（自动同步）

### 1.4 创建自动导出任务
1. 在你的 Zotero 库中，右键点击 "My Library"
2. 选择 "导出库..."
3. 格式选择 **Better BibTeX**
4. 勾选 **Keep updated**
5. 保存为 `references.bib` 到目录：
   ```
   research-knowledge-base-mkdocs/references/
   ```

---

## 第二步：Obsidian 配置

### 2.1 安装 Citations 插件
1. 打开 Obsidian
2. 设置 → 附加组件
3. 浏览 → 搜索 "Citations"
4. 安装并启用

### 2.2 配置 Citations
1. 设置 → Citations
2. **Citation database** 设置为：
   ```
   /path/to/research-knowledge-base-mkdocs/references/references.bib
   ```
3. 引用格式：`[@{citekey}]`

### 2.3 安装 Obsidian Git 插件（推荐）
1. 附加组件 → 搜索 "Git"
2. 安装 Obsidian Git
3. 配置自动同步到 `research-knowledge-base-mkdocs`

---

## 第三步：在 Markdown 中引用

### 3.1 基础引用
```markdown
产业生态系统理论最早由 Moore [@moore1993] 提出。
```

### 3.2 多个引用
```markdown
已有研究表明...[@moore1993; @vargo2004; @iea2025]
```

### 3.3 页面末尾添加参考文献
```markdown
## 参考文献

[@moore1993]: Moore, J. F. (1993). Predators and prey: A new ecology of competition. Harvard Business Review, 71(3), 75-86.

[@iea2025]: IEA. (2025). World Energy Investment 2025. Paris: International Energy Agency.
```

---

## 第四步：MkDocs 网站支持

### 4.1 安装插件
```bash
pip install mkdocs-bibtex
```

### 4.2 配置 mkdocs.yml
```yaml
plugins:
  - search
  - bibtex:
      cite_format: square
```

---

## 工作流程图

```
阅读PDF/Zotero
      ↓
添加文献到Zotero
      ↓
Better BibTeX 自动导出
      ↓
references.bib 更新
      ↓
Obsidian 引用 → 写作
      ↓
Git 推送 → MkDocs 网站
```

---

## Citation Key 命名规则

| 类型 | 格式 | 示例 |
|------|------|------|
| 论文 | author + year | moore1993 |
| 报告 | 机构 + year | iea2025 |
| 政策 | 部门 + year | mof2023 |
| 书籍 | author + year | porter1985 |

---

## 快速检查

运行引用检查：
```bash
python3 scripts/citation_check.py
```

---

*最后更新: 2026-03-16*
