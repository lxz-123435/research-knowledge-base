# 🔬 研究资料库 (Research Knowledge Base)

> 把"搜资料 → 读资料 → 做笔记 → 写报告"整个研究流程自动化

一个基于 MkDocs + GitHub Pages 的个人研究知识管理系统。

---

## 🌐 在线访问

**网站地址**: https://lxz-123435.github.io/research-knowledge-base/

**GitHub 仓库**: https://github.com/lxz-123435/research-knowledge-base

---

## 📁 网站结构

```
├── research/      # 研究主题（按问题分类）
├── sources/       # 资料来源（按机构分类）
├── notes/         # 阅读笔记（知识提炼）
├── theory/        # 理论文章
├── policy/        # 政策研究
├── data/          # 数据资料
├── cases/         # 案例库
├── templates/     # 写作模板
└── tools/         # 研究工具
```

### 研究主题 (research/)

| 主题 | 说明 |
|------|------|
| [AI-governance](./research/AI-governance/) | AI治理与监管 |
| [Data-assets](./research/Data-assets/) | 数据资产化 |
| [Outward-investment](./research/Outward-investment/) | 中国企业对外投资 |
| [Computing-power](./research/Computing-power/) | 算力产业 |
| [Critical-minerals](./research/Critical-minerals/) | 关键矿产 |
| [Green-finance](./research/Green-finance/) | 绿色金融 |

### 资料来源 (sources/)

| 机构 | 说明 |
|------|------|
| UNCTAD | 联合国贸易和发展会议 |
| OECD | 经济合作与发展组织 |
| IMF | 国际货币基金组织 |
| WTO | 世界贸易组织 |
| 商务部 | 中国商务部 |
| 国家数据局 | 国家数据局 |

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/lxz-123435/research-knowledge-base.git
cd research-knowledge-base
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 本地预览

```bash
python3 -m mkdocs serve
```

然后打开 http://localhost:8000

### 4. 部署网站

```bash
python3 -m mkdocs gh-deploy
```

---

## 📥 添加新资料

### 方式一：手动添加

1. 把 PDF 文件放到对应目录：
   - `docs/data/` - 数据报告
   - `docs/policy/` - 政策文件
   - `docs/cases/` - 案例资料

2. 更新目录的 `index.md` 列表

3. 部署：
   ```bash
   python3 -m mkdocs gh-deploy
   ```

### 方式二：使用 inbox（推荐）

1. 把 PDF 放入 `inbox/` 目录

2. 运行部署脚本：
   ```bash
   bash scripts/deploy.sh
   ```

3. 系统会自动：
   - 处理新文件
   - 构建网站
   - 部署到 GitHub Pages
   - 移动已处理文件到 `processed/`

---

## 🛠️ 自动化脚本

### deploy.sh - 一键部署

```bash
bash scripts/deploy.sh
```

功能：
- 检测 inbox/ 中的新文件
- 自动处理
- 构建并部署网站

### ai_analyze.py - AI分析（开发中）

```bash
python3 scripts/ai_analyze.py <PDF文件>
```

功能：
- 读取 PDF 内容
- 生成摘要
- 自动分类
- 生成 Markdown 笔记

---

## 📊 数据统计

| 类别 | 数量 |
|------|------|
| 理论文章 | 21篇 |
| 政策文件 | ~25份 |
| 数据报告 | ~47份 |
| 案例资料 | ~14份 |
| 研究主题 | 6个 |
| 资料来源 | 8个机构 |

---

## 🔧 配置说明

### mkdocs.yml

网站配置文件，主要参数：

```yaml
site_name: 政策研究资料库
site_url: https://lxz-123435.github.io/research-knowledge-base/
theme:
  name: material
  language: zh
```

### 目录结构

```
research-knowledge-base/
├── docs/                    # 网站内容 (Markdown)
│   ├── index.md            # 首页
│   ├── research/           # 研究主题
│   ├── sources/            # 资料来源
│   ├── notes/              # 阅读笔记
│   ├── policy/             # 政策研究
│   ├── data/               # 数据资料
│   ├── cases/              # 案例库
│   ├── theory/             # 理论文章
│   ├── templates/          # 写作模板
│   └── tools/              # 研究工具
├── scripts/                # 自动化脚本
│   ├── deploy.sh           # 部署脚本
│   └── ai_analyze.py      # AI分析脚本
├── inbox/                  # 新资料待处理
├── processed/               # 已处理资料
├── mkdocs.yml             # 网站配置
└── requirements.txt       # Python依赖
```

---

## 🎯 研究主题

### 如何使用研究主题

每个研究主题页面包含：

1. **研究问题** - 需要回答的核心问题
2. **核心资料** - 相关资料链接
3. **关键数据** - 重要数据表格
4. **研究框架** - 分析思路

### 添加新研究主题

1. 创建目录：`docs/research/新主题/`
2. 创建 `index.md`，包含：
   - 研究问题
   - 核心资料
   - 关键数据
   - 研究框架
3. 在 `mkdocs.yml` 的 `nav` 中添加

---

## 📝 写作模板

### 政策报告模板

```markdown
# 标题

## 摘要

## 背景

## 主要内容

## 核心观点

## 政策含义

## 数据支撑

## 参考资料
```

### 阅读笔记模板

```markdown
# 笔记标题

## 资料来源

## 核心观点

## 我的思考

## 相关资料

---
```

---

## 🔄 持续更新

1. **定期添加新资料**
   - 把 PDF 放入 inbox/
   - 运行 deploy.sh

2. **更新研究主题**
   - 在对应目录添加新资料链接
   - 更新研究问题和框架

3. **添加阅读笔记**
   - 在 notes/reading-notes/ 添加
   - 关联相关资料

---

## 🤖 AI 辅助

系统支持 AI 辅助研究：

1. **资料分析** - AI 自动解析 PDF
2. **知识提炼** - AI 生成摘要
3. **研究建议** - AI 提供研究思路

未来计划：
- 自动抓取政策更新
- 自动抓取报告更新
- AI 生成研究框架

---

## 📜 许可证

MIT License

---

## 🙏 致谢

- [MkDocs](https://www.mkdocs.org/) - 静态网站生成器
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - 主题
- [OpenClaw](https://openclaw.ai/) - AI 助手

---

*本资料库旨在为政策研究、学术分析和 AI 辅助研究提供系统化的知识管理平台。*

*持续更新中...*
