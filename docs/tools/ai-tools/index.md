# AI 自动化工具

> 让知识管理更高效

---

## 输入 → 输出流程

```
给我输入                          我的输出
─────────────────────────────────────────────────

📥 放文件到 inbox/         →  📝 自动生成...
   • PDF书籍                    • 01_sources/ 书籍资料
   • 论文                       • 02_knowledge/ 笔记/概念/框架/洞见
                                • 03_research/ 研究主题/项目
                                • 04_outputs/ 随笔/报告

🚀 部署网站：
   python3 scripts/ai_modules/manual_add.py
   # 选择 "7. 部署网站"
```

---

## 工具列表

### 1. GPT 深度分析（推荐）

使用GPT API进行深度分析，自动生成洞见、框架、甚至随笔

```bash
# 设置API Key
export OPENAI_API_KEY='your-api-key'

# 分析PDF（生成洞见+框架）
python3 scripts/ai_modules/gpt_analyze.py <PDF文件>

# 分析PDF（生成洞见+框架+随笔）
python3 scripts/ai_modules/gpt_analyze.py <PDF文件> --essay
```

**功能：**
- ✅ 自动提取核心问题
- ✅ 自动生成深度洞见
- ✅ 自动提取关键概念
- ✅ 自动生成分析框架
- ✅ 可选：自动生成评论随笔

---

### 2. 基础AI提取

从PDF自动提取核心观点、概念、框架

```bash
python3 scripts/ai_modules/ai_extract.py <PDF文件>
```

**功能：**
- 自动提取书籍信息
- 自动识别核心问题
- 自动提取关键概念
- 自动分析文章结构

---

### 2. 基础AI提取

从PDF自动提取核心观点、概念、框架

```bash
python3 scripts/ai_modules/ai_extract.py <PDF文件>
```

**功能：**
- 自动提取书籍信息
- 自动识别核心问题
- 自动提取关键概念
- 自动分析文章结构

---

### 3. 知识图谱

生成概念之间的关联网络

```bash
python3 scripts/ai_modules/knowledge_graph.py
```

**功能：**
- 扫描所有概念
- 分析概念关联
- 生成可视化图谱

---

### 3. 知识图谱

生成概念之间的关联网络

```bash
python3 scripts/ai_modules/knowledge_graph.py
```

**功能：**
- 扫描所有概念
- 分析概念关联
- 生成可视化图谱

---

### 4. 研究综述

自动生成主题研究综述

```bash
python3 scripts/ai_modules/research_summary.py <主题>
```

**功能：**
- 汇总相关书籍
- 汇总相关概念
- 汇总相关框架
- 生成研究综述

---

### 4. 研究综述

自动生成主题研究综述

```bash
python3 scripts/ai_modules/research_summary.py <主题>
```

**功能：**
- 汇总相关书籍
- 汇总相关概念
- 汇总相关框架
- 生成研究综述

---

### 5. 写作模板

根据主题生成文章框架

```bash
python3 scripts/ai_modules/write_template.py <主题> [论文|报告|评论]
```

**功能：**
- 生成论文框架
- 生成报告框架
- 生成评论框架

---

### 5. 写作模板

根据主题生成文章框架

```bash
python3 scripts/ai_modules/write_template.py <主题> [论文|报告|评论]
```

**功能：**
- 生成论文框架
- 生成报告框架
- 生成评论框架

---

### 6. 交互式工具箱

```bash
bash scripts/research_tools.sh
```

进入交互式菜单，选择功能运行。

---

### 7. 手动添加模块

交互式手动添加内容（不通过AI）

```bash
python3 scripts/ai_modules/manual_add.py
```

**可添加的内容：**
- 📚 书籍
- 📝 阅读笔记
- 💡 概念
- 🗂️ 分析框架
- 💭 思想洞见
- ✍️ 评论随笔

---

## 使用流程

### 完整流程示例

```bash
# 1. 放入新书
cp new_book.pdf inbox/

# 2. AI自动提取
python3 scripts/ai_modules/ai_extract.py inbox/new_book.pdf

# 3. 生成知识图谱
python3 scripts/ai_modules/knowledge_graph.py

# 4. 生成研究综述
python3 scripts/ai_modules/research_summary.py "媒体与权力"

# 5. 生成写作框架
python3 scripts/ai_modules/write_template.py "媒体与权力" 论文

# 6. 部署网站
python3 -m mkdocs gh-deploy
```

---

## 快速开始

### 处理一本新书

```bash
# 放入 inbox
cp my_book.pdf ~/.openclaw/workspace/research-knowledge-base-mkdocs/inbox/

# 运行提取
python3 scripts/ai_modules/ai_extract.py ~/.openclaw/workspace/research-knowledge-base-mkdocs/inbox/my_book.pdf
```

### 生成知识图谱

```bash
python3 scripts/ai_modules/knowledge_graph.py
```

### 生成写作模板

```bash
python3 scripts/ai_modules/write_template.py "你想写的主题"
```

---

*持续更新中...*
