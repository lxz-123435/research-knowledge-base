# 🔬 Research Knowledge Base

> 把 **"搜资料 → 读资料 → 做笔记 → 写报告"** 的研究流程系统化与自动化。

一个基于 **MkDocs + GitHub Pages + AI辅助** 的个人研究知识管理系统。

适用于：

* 政策研究
* 智库研究
* 学术研究
* 数据分析

---

# 🌐 Online Access

**Website**

[https://lxz-123435.github.io/research-knowledge-base/](https://lxz-123435.github.io/research-knowledge-base/)

**GitHub Repository**

[https://github.com/lxz-123435/research-knowledge-base](https://github.com/lxz-123435/research-knowledge-base)

---

# 🧠 System Architecture

本系统构建了一个 **研究知识管理框架**：

```
资料收集
 ↓
AI解析
 ↓
知识整理
 ↓
研究框架
 ↓
研究成果
```

核心目标：

**把研究流程自动化。**

---

# 🧩 Core Modules

```
Research Knowledge Base
│
├── research/      # 研究主题（按问题分类）
├── sources/      # 资料来源（按机构分类）
├── notes/        # 阅读笔记（知识提炼）
├── theory/       # 理论文章
├── policy/       # 政策研究
├── data/         # 数据报告
├── cases/        # 案例库
├── templates/    # 写作模板
└── tools/       # 研究工具
```

系统采用 **双维度结构**：

### 1️⃣ 研究主题（Research Topics）

```
research/
├── AI-governance
├── Data-assets
├── Outward-investment
├── Computing-power
├── Critical-minerals
└── Green-finance
```

每个研究主题包含：

* 研究问题
* 核心资料
* 关键数据
* 研究框架

---

### 2️⃣ 资料来源（Data Sources）

```
sources/
├── UNCTAD
├── OECD
├── IMF
├── WTO
├── 商务部
└── 国家数据局
```

便于按机构追踪报告和政策。

---

# 📊 Dataset Overview

| Category | Count |
| -------- | ----- |
| 理论文章 | 21 |
| 政策文件 | ~25 |
| 数据报告 | ~47 |
| 案例资料 | ~14 |
| 研究主题 | 6 |
| 资料来源 | 8 |

---

# 🚀 Quick Start

## 1 Clone Repository

```bash
git clone https://github.com/lxz-123435/research-knowledge-base.git
cd research-knowledge-base
```

---

## 2 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3 Local Preview

```bash
python3 -m mkdocs serve
```

访问：

```
http://localhost:8000
```

---

## 4 Deploy Website

```bash
python3 -m mkdocs gh-deploy
```

---

# 🔄 Research Workflow

系统支持完整研究流程：

```
发现资料
↓
下载 PDF
↓
AI解析
↓
生成摘要
↓
加入知识库
↓
形成研究框架
↓
撰写报告
```

---

# 📥 Adding New Materials

## 方法一：手动添加

将 PDF 放入：

```
docs/data/
docs/policy/
docs/cases/
```

更新 `index.md`。

部署：

```bash
python3 -m mkdocs gh-deploy
```

---

## 方法二：Inbox 自动处理（推荐）

把 PDF 放入：

```
inbox/
```

运行：

```bash
bash scripts/deploy.sh
```

系统将自动：

```
检测新文件
→ 解析资料
→ 构建网站
→ 部署到 GitHub Pages
→ 移动文件到 processed/
```

---

# 🛠 Automation Scripts

## deploy.sh

```bash
bash scripts/deploy.sh
```

功能：

```
处理新资料
构建网站
自动部署
```

---

## ai_analyze.py（开发中）

```bash
python3 scripts/ai_analyze.py <PDF>
```

功能：

```
读取 PDF
生成摘要
自动分类
生成 Markdown 笔记
```

---

# 🤖 AI Support

系统支持 AI 辅助研究：

```
PDF 自动解析
知识摘要
研究思路建议
结构化笔记生成
```

未来计划：

```
自动抓政策
自动抓研究报告
AI生成研究框架
AI研究助手
```

---

# 📁 Directory Structure

```
research-knowledge-base/
│
├── docs/
│ ├── research/
│ ├── sources/
│ ├── notes/
│ ├── policy/
│ ├── data/
│ ├── cases/
│ ├── theory/
│ ├── templates/
│ └── tools/
│
├── scripts/
│ ├── deploy.sh
│ └── ai_analyze.py
│
├── inbox/
├── processed/
│
├── mkdocs.yml
└── requirements.txt
```

---

# 📝 Writing Templates

## Policy Report

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

---

## Reading Notes

```markdown
# 笔记标题

## 资料来源
## 核心观点
## 我的思考
## 相关资料
```

---

# 📜 License

MIT License

---

# 🙏 Acknowledgements

* MkDocs
* Material for MkDocs
* OpenClaw
