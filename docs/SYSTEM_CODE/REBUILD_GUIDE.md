# 研究知识库完整重建代码

> 本文档包含重建整个网站所需的全部代码和配置

---

## 一、项目结构

```
research-knowledge-base/
├── mkdocs.yml              # 网站配置文件
├── requirements.txt         # Python依赖
├── README.md              # 项目说明
├── docs/                  # 网站内容
│   ├── index.md          # 首页
│   ├── knowledge-network.md  # 知识网络
│   ├── SYSTEM_DESIGN.md  # 系统设计
│   │
│   ├── research/         # 研究主题
│   │   ├── index.md
│   │   ├── AI-governance/
│   │   ├── Data-assets/
│   │   ├── Outward-investment/
│   │   ├── Computing-power/
│   │   ├── Critical-minerals/
│   │   ├── Green-finance/
│   │   └── Media-power/
│   │
│   ├── sources/          # 资料来源
│   │   └── index.md
│   │
│   ├── notes/           # 阅读笔记
│   │   ├── index.md
│   │   ├── research-method.md
│   │   ├── reading-notes/
│   │   ├── frameworks/
│   │   ├── ideas/
│   │   └── books/
│   │
│   ├── concepts/        # 概念库
│   │   └── index.md
│   │
│   ├── frameworks/      # 研究框架
│   │   └── index.md
│   │
│   ├── reading-map/    # 阅读地图
│   │   └── index.md
│   │
│   ├── policy/          # 政策研究
│   │   └── index.md
│   │
│   ├── data/           # 数据资料
│   │   └── index.md
│   │
│   ├── cases/          # 案例库
│   │   └── index.md
│   │
│   ├── theory/          # 理论文章
│   │   └── index.md
│   │
│   ├── templates/       # 写作模板
│   │   └── index.md
│   │
│   └── tools/          # 工具方法
│       └── index.md
│
├── scripts/              # 自动化脚本
│   ├── deploy.sh
│   └── ai_analyze.py
│
├── inbox/               # 待处理文件
└── processed/           # 已处理文件
```

---

## 二、核心配置文件

### 2.1 mkdocs.yml

```yaml
site_name: 政策研究资料库
site_description: 政策研究、理论文章、数据资料与案例库
site_author: Research Team
site_url: https://lxz-123435.github.io/research-knowledge-base/

repo_url: https://github.com/lxz-123435/research-knowledge-base
repo_name: lxz-123435/research-knowledge-base

remote_branch: gh-pages

theme:
  name: material
  language: zh
  palette:
    primary: indigo
    accent: indigo
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
    - toc.integrate
    - tags

plugins:
  - search

nav:
  - 首页: index.md
  - 知识地图: knowledge-network.md
  - 阅读地图:
    - reading-map/index.md
  - 概念库:
    - concepts/index.md
  - 研究框架:
    - frameworks/index.md
  - 研究主题:
    - research/index.md
    - research/AI-governance/index.md
    - research/Data-assets/index.md
    - research/Outward-investment/index.md
    - research/Computing-power/index.md
    - research/Critical-minerals/index.md
    - research/Green-finance/index.md
    - research/Media-power/index.md
  - 资料来源:
    - sources/index.md
  - 阅读笔记:
    - notes/index.md
    - notes/research-method.md
    - notes/reading-notes/index.md
    - notframeworks/index.md
    - notes/ideas/index.md
  - 工具与方法:
    - tools/index.md
    - tools/人物传记阅读五维模型.md
  - 理论文章:
    - theory/achievement-view/index.md
    # ... 更多理论文章

markdown_extensions:
  - attr_list
  - md_in_html
  - tables
  - admonition
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
  - toc:
      permalink: true

copyright: '政策研究资料库 &copy; 2024'

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/lxz-123435/research-knowledge-base

extra:
  tags: true
```

### 2.2 requirements.txt

```
# PDF处理
PyMuPDF>=1.23.0

# HTTP请求
requests>=2.31.0

# 网页解析
beautifulsoup4>=4.12.0

# Markdown处理
python-frontmatter>=1.1.0
```

---

## 三、核心页面代码

### 3.1 首页 (index.md)

```markdown
# 政策研究资料库

> 把"搜资料 → 读资料 → 做笔记 → 写报告"的研究流程系统化与自动化。

一个基于 **MkDocs + GitHub Pages + AI辅助** 的个人研究知识管理系统。

## 核心功能

| 功能 | 说明 |
|------|------|
| 🤖 AI分析 | 自动解析PDF、生成摘要 |
| 📂 智能分类 | 自动识别资料类型 |
| 🔗 知识关联 | 研究主题 + 资料来源双维度 |
| 📝 阅读笔记 | 从资料到知识的提炼 |
| 🚀 一键部署 | 自动部署到GitHub Pages |

## 网站结构

### 🔍 研究主题（按问题）
- [AI治理](research/AI-governance/index.md) - AI监管与政策框架
- [数据资产](research/Data-assets/index.md) - 数据要素与资产化
- [对外投资](research/Outward-investment/index.md) - 中国企业海外投资
- [算力产业](research/Computing-power/index.md) - AI基础设施
- [关键矿产](research/Critical-minerals/index.md) - 稀土与关键金属
- [绿色金融](research/Green-finance/index.md) - ESG与碳中和
- [媒体与权力](research/Media-power/index.md) - 新闻与权力

### 📚 资料来源（按机构）
- [UNCTAD](sources/UNCTAD/index.md) - 联合国贸发会议
- [OECD](sources/OECD/index.md) - 经合组织
- [IMF](sources/IMF/index.md) - 国际货币基金
- [商务部](sources/China-commerce/index.md) - 商务部
- [国家数据局](sources/China-data-bureau/index.md) - 国家数据局

### 📝 阅读笔记
- [阅读笔记](notes/reading-notes/index.md) - 资料分析总结
- [研究方法](notes/research-method.md) - 知识生产方法论
- [框架模型](notframeworks/index.md) - 研究分析框架
- [想法观点](notes/ideas/index.md) - 原创思考

### 📁 资料库
- [理论文章](theory/index.md) - 理论文献
- [政策研究](policy/index.md) - 政策文件
- [数据资料](data/index.md) - 研究报告
- [案例库](cases/index.md) - 企业案例

### 🛠️ 工具
- [研究工具](tools/index.md) - 自动化脚本

---

## 快速开始

### 添加新资料
1. 把PDF放到 `inbox/`
2. 运行: `bash scripts/deploy.sh`

### 部署网站
```bash
bash scripts/deploy.sh
```

---

## 网站地址

🔗 **https://lxz-123435.github.io/research-knowledge-base/**

---

*AI 研究操作系统 v1.0*
```

### 3.2 知识地图 (knowledge-network.md)

```markdown
---
title: 知识网络
---

# 知识地图

> 从阅读到写作的完整知识生产网络

---

## 🔄 知识流动

```
阅读笔记 → 概念 → 分析框架 → 研究主题 → 写作产出
   ↓           ↓           ↓           ↓
  notes    concepts   frameworks   research    theory
```

---

## 📚 核心概念

| 概念 | 说明 | 相关书籍 |
|------|------|----------|
| [新质生产力](../02_knowledge/concepts/新质生产力.md) | 高质量发展核心驱动力 | 政策文件 |
| [数据资产](../02_knowledge/concepts/数据资产.md) | 数字经济关键要素 | 数据报告 |
| [调查报道](../02_knowledge/concepts/调查报道.md) | 新闻采访方法论 | 法拉奇传 |
| [新闻自由](../02_knowledge/concepts/新闻自由.md) | 媒体权利与责任 | 法拉奇传 |
| [时代选择](../02_knowledge/concepts/时代选择.md) | 个人在时代中的选择 | 法拉奇传 |

[更多概念 →](../02_knowledge/concepts/)

---

## 🗂️ 分析框架

| 框架 | 说明 | 应用场景 |
|------|------|----------|
| [产业链分析](frameworks/产业链分析框架.md) | 产业竞争力分析 | 产业政策 |
| [访谈研究方法](frameworks/访谈研究方法.md) | 深度访谈技巧 | 人物研究 |
| [国家能力分析](frameworks/国家能力分析框架.md) | 政府能力评估 | 公共政策 |

[更多框架 →](frameworks/)

---

## 🔬 研究主题

| 主题 | 说明 | 核心问题 |
|------|------|----------|
| [AI治理](../research/AI-governance/) | AI监管与政策 | AI如何监管？ |
| [对外投资](../research/Outward-investment/) | 中国企业出海 | 投资趋势如何？ |
| [数据资产](../research/Data-assets/) | 数据要素市场化 | 价值如何实现？ |
| [媒体权力](../research/Media-power/) | 新闻与权力 | 媒体如何监督权力？ |

[更多研究 →](../research/)

---

## 📖 阅读笔记

| 书籍 | 核心概念 | 相关框架 |
|------|----------|----------|
| [命若朝霜](../notes/reading-notes/命若朝霜-红楼梦法律社会女性/) | 法律史，社会史 | 历史分析 |
| [法拉奇传](../notes/reading-notes/从不妥协-法拉奇传/) | 调查报道、新闻自由 | 访谈研究 |

[更多笔记 →](../notes/reading-notes/)

---

## 🚀 使用流程

1. **阅读** → 放入 inbox，用五层结构分析
2. **提炼** → 提取核心概念和分析框架
3. **连接** → 关联到研究主题
4. **产出** → 写作素材自动生成

---

*知识网络，持续更新中...*
```

---

## 四、研究主题模板

### 4.1 研究主题首页 (research/index.md)

```markdown
# 研究主题

按研究主题整理资料，打破资料类型的界限，围绕实际问题组织内容。

## 主题列表

### 🤖 AI与数字治理
- [AI治理](AI-governance/index.md) - AI监管与政策框架

### 💾 数据资产
- [数据资产](Data-assets/index.md) - 数据要素与资产化

### 🌏 对外投资
- [中国企业对外投资](Outward-investment/index.md) - 海外投资、跨境并购

### 💻 算力产业
- [算力产业](Computing-power/index.md) - AI基础设施

### ⛏️ 关键矿产
- [关键矿产](Critical-minerals/index.md) - 稀土与关键金属

### 🌿 绿色金融
- [绿色金融](Green-finance/index.md) - ESG与碳中和

### 📰 媒体与权力
- [媒体权力](Media-power/index.md) - 新闻与权力

---

*按研究主题整理资料，形成知识网络*
```

### 4.2 研究主题详情页模板 (research/主题/index.md)

```markdown
---
tags:
  - 标签1
  - 标签2
---

# 研究标题

## 研究问题

1. 问题1
2. 问题2
3. 问题3

## 核心资料

### 数据报告
- [报告名称](../data/目录/index.md)

### 政策文件
- [政策名称](../policy/目录/index.md)

## 关键数据

| 指标 | 说明 |
|------|------|
| 数据1 | 说明1 |
| 数据2 | 说明2 |

## 研究框架

### 1. 框架1
说明

### 2. 框架2
说明

## 📚 知识来源

### 关联书籍

- [书名](../notes/reading-notes/书名/index.md)

### 核心概念

- [概念名](../02_knowledge/concepts/概念名.md)

### 分析框架

- [框架名](frameworks/框架名.md)

---

## 📝 写作方向

| 类型 | 主题 |
|------|------|
| 政策报告 | 标题 |
| 专题研究 | 标题 |
| 案例分析 | 标题 |

---

*本页面将持续更新*
```

---

## 五、阅读笔记模板

### 5.1 读书笔记首页 (notes/reading-notes/index.md)

```markdown
# 阅读笔记

对阅读资料的分析、总结和思考。

## 笔记列表

### 2025年

- [《书名》](书名/index.md) - 作者

---

*添加笔记格式：*

\`\`\`markdown
# 笔记标题

## 资料来源

## 核心观点

## 我的思考

## 相关资料

---
\`\`\`
```

### 5.2 读书笔记详情页模板 (notes/reading-notes/书名/index.md)

```markdown
---
tags:
  - 标签1
  - 标签2
---

# 书名

> 作者 | 出版社 | 出版时间

---

## 一、核心问题

**这本书试图回答什么问题？**

（回答）

---

## 二、核心观点

**作者的主要结论是什么？**

1. 观点1
2. 观点2
3. 观点3

---

## 三、逻辑结构

**作者如何论证？**

| 部分 | 内容 |
|------|------|
| 第一部分 | 内容 |
| 第二部分 | 内容 |
| 第三部分 | 内容 |

---

## 四、方法论

**作者使用了什么分析方法？**

1. 方法1
2. 方法2

---

## 五、现实启发

**对中国政策或企业的启发？**

### 1. 启发1

### 2. 启发2

---

## 🔗 知识关联

### 概念链接

- [概念名](../02_knowledge/concepts/概念名.md)

### 框架链接

- [框架名](frameworks/框架名.md)

### 研究主题

- [研究名](../research/研究名/index.md)

---

## 写作素材

| 类型 | 主题 |
|------|------|
| 理论文章 | 标题 |
| 智库报告 | 标题 |

---

*笔记整理：Research Knowledge Base*
*日期：2026-03-15*
```

---

## 六、概念库模板

### 6.1 概念库首页 (concepts/index.md)

```markdown
# 概念库

> 从阅读中提炼的核心概念，形成知识网络

## 概念列表

### 经济与发展

- [新质生产力](新质生产力.md) - 高质量发展的核心驱动力
- [数据资产](数据资产.md) - 数字经济的关键生产要素

### 产业与投资

- [产业链重构](产业链重构.md) - 全球供应链调整
- [FDI](FDI.md) - 外国直接投资

### 新闻与媒体

- [调查报道](调查报道.md) - 新闻采访方法论
- [新闻自由](新闻自由.md) - 媒体权利与责任

### 思想与选择

- [时代选择](时代选择.md) - 个人在时代中的选择

---

*概念库持续更新中...*
```

### 6.2 概念详情页模板 (concepts/概念名.md)

```markdown
---
tags:
  - 标签1
---

# 概念名称

## 概念定义

（概念的定义说明）

## 理论来源

- 来源1
- 来源2

## 核心特征

| 特征 | 说明 |
|------|------|
| 特征1 | 说明1 |
| 特征2 | 说明2 |

## 相关研究

- [研究1](../research/研究1/index.md)
- [研究2](../research/研究2/index.md)

---

*更新于 2026-03-15*
```

---

## 七、框架库模板

### 7.1 框架库首页 (frameworks/index.md)

```markdown
# 研究框架库

> 分析问题和解决问题的方法论工具

## 框架列表

### 经济分析

- [产业链分析框架](产业链分析框架.md) - 产业竞争力分析

### 研究方法

- [访谈研究方法](访谈研究方法.md) - 深度访谈技巧

### 政策分析

- [政策评估框架](政策评估框架.md) - 政策效果评价

---

*框架库持续更新中...*
```

### 7.2 框架详情页模板 (frameworks/框架名.md)

```markdown
---
tags:
  - 框架
  - 标签
---

# 框架名称

## 框架定义

（框架的定义说明）

## 分析维度

### 1. 维度1

说明

### 2. 维度2

说明

## 核心指标

| 指标 | 说明 |
|------|------|
| 指标1 | 说明1 |

## 应用场景

- 场景1
- 场景2

## 典型案例

- 案例1

---

*更新于 2026-03-15*
```

---

## 八、自动化脚本

### 8.1 deploy.sh

```bash
#!/bin/bash
# 研究资料库自动部署脚本

set -e

echo "========================================="
echo "   研究资料库自动部署"
echo "========================================="

PROJECT_DIR="$HOME/.openclaw/workspace/research-knowledge-base-mkdocs"
INBOX="$PROJECT_DIR/inbox"
PROCESSED="$PROJECT_DIR/processed"

cd "$PROJECT_DIR"

# 1. 检查inbox是否有新文件
if [ -d "$INBOX" ] && [ "$(ls -A $INBOX 2>/dev/null)" ]; then
    echo "[1/4] 发现新文件，正在处理..."
    mkdir -p "$PROCESSED"
    
    for file in "$INBOX"/*.pdf; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            echo "  处理: $filename"
            mv "$file" "$PROCESSED/"
            echo "  -> 已移动到 processed/"
        fi
    done
else
    echo "[1/4] 没有新文件需要处理"
fi

# 2. 构建网站
echo "[2/4] 构建网站..."
python3 -m mkdocs build --clean

# 3. 部署到GitHub Pages
echo "[3/4] 部署到GitHub Pages..."
python3 -m mkdocs gh-deploy --force

# 4. 完成
echo "[4/4] 完成!"
echo ""
echo "========================================="
echo "网站已更新: https://lxz-123435.github.io/research-knowledge-base/"
echo "========================================="
```

### 8.2 ai_analyze.py (框架)

```python
#!/usr/bin/env python3
"""
AI 研究资料分析脚本
功能：自动解析PDF、生成摘要、分类
"""

import os
import sys

# 配置
DOCS_DIR = os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs/docs")

def read_pdf(pdf_path, max_pages=3):
    """读取PDF内容"""
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i, page in enumerate(reader.pages[:max_pages]):
                text += f"--- 第{i+1}页 ---\n" + page.extract_text() + "\n"
            return text[:5000]
    except Exception as e:
        return f"Error reading PDF: {e}"

def generate_summary(text, filename):
    """生成摘要"""
    name_without_ext = os.path.splitext(filename)[0]
    
    summary = f"""# {name_without_ext}

## 核心观点

1. （待分析）
2. （待分析）
3. （待分析）

## 关键词

（待添加）

## 相关资料

- （待添加）

---
*自动生成*
"""
    return summary

def auto_classify(filename):
    """自动分类"""
    filename_lower = filename.lower()
    
    if any(kw in filename_lower for kw in ["政策", "商务部", "国家数据局"]):
        return "policy"
    if any(kw in filename_lower for kw in ["unctad", "oecd", "报告"]):
        return "data"
    if any(kw in filename_lower for kw in ["案例", "企业"]):
        return "cases"
    
    return "data"

def process_file(pdf_path):
    """处理单个文件"""
    filename = os.path.basename(pdf_path)
    print(f"处理: {filename}")
    
    content = read_pdf(pdf_path)
    summary = generate_summary(content, filename)
    category = auto_classify(filename)
    
    target_dir = os.path.join(DOCS_DIR, category)
    os.makedirs(target_dir, exist_ok=True)
    
    note_filename = os.path.splitext(filename)[0] + ".md"
    note_path = os.path.join(target_dir, note_filename)
    
    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"  -> 已生成笔记: {note_path}")

def main():
    if len(sys.argv) < 2:
        print("用法: python ai_analyze.py <PDF文件路径>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if os.path.isfile(target):
        process_file(target)
    elif os.path.isdir(target):
        for f in os.listdir(target):
            if f.endswith('.pdf'):
                process_file(os.path.join(target, f))

if __name__ == "__main__":
    main()
```

---

## 九、部署步骤

### 9.1 初始化项目

```bash
# 1. 创建项目目录
mkdir research-knowledge-base
cd research-knowledge-base

# 2. 安装MkDocs
pip install mkdocs mkdocs-material

# 3. 初始化
mkdocs new .

# 4. 复制上面的 mkdocs.yml 配置
```

### 9.2 创建目录结构

```bash
# 创建所有必要目录
mkdir -p docs/{research,sources,notes,concepts,frameworks,reading-map,policy,data,cases,theory,templates,tools}
mkdir -p scripts
mkdir -p inbox
mkdir -p processed
```

### 9.3 部署到GitHub

```bash
# 1. 初始化Git
git init
git add .
git commit -m "init"

# 2. 连接GitHub
git remote add origin https://github.com/你的用户名/research-knowledge-base.git

# 3. 推送到main分支
git branch -M main
git push -u origin main

# 4. 配置GitHub Pages
# 在GitHub仓库设置中：Settings → Pages → Source选择gh-pages分支

# 5. 部署网站
python3 -m mkdocs gh-deploy
```

---

## 十、使用流程

### 10.1 添加新书

1. 放入 `inbox/`
2. 运行分析脚本或手动创建笔记
3. 运行 `bash scripts/deploy.sh`

### 10.2 知识关联

每本书需要：
1. 创建 `notes/reading-notes/书名/index.md`
2. 提炼概念 → 添加到 `concepts/`
3. 提炼框架 → 添加到 `frameworks/`
4. 连接研究 → 更新 `research/主题/index.md`

### 10.3 更新网站

```bash
python3 -m mkdocs gh-deploy
```

---

*完整代码整理：Research Knowledge Base*
