# 研究资料库系统设计文档 (Research OS v1.0)

---

## 一、系统架构

| 层级 | 技术 |
|------|------|
| 托管平台 | GitHub Pages |
| 静态网站生成 | MkDocs + mkdocs-material |
| 源文件管理 | Markdown (.md) + PDF |
| 部署方式 | `mkdocs gh-deploy` |
| AI辅助 | OpenClaw + Python脚本 |

---

## 二、网站结构 (docs/)

```
docs/
│
├── research/          ⭐ 研究主题层（按问题/主题）
│   ├── AI-governance/         # AI治理
│   ├── Data-assets/           # 数据资产
│   ├── Outward-investment/    # 对外投资
│   ├── Computing-power/       # 算力产业
│   ├── Critical-minerals/     # 关键矿产
│   └── Green-finance/         # 绿色金融
│
├── sources/           ⭐ 资料来源层（按机构）
│   ├── UNCTAD/               # 联合国贸发会议
│   ├── OECD/                 # 经合组织
│   ├── IMF/                  # 国际货币基金
│   ├── WTO/                  # 世贸组织
│   ├── China-commerce/       # 商务部
│   ├── China-data-bureau/    # 国家数据局
│   ├── EU/                   # 欧盟
│   └── US/                   # 美国
│
├── notes/             ⭐ 阅读笔记层（知识提炼）
│   ├── reading-notes/        # 阅读笔记
│   ├── frameworks/          # 研究框架
│   └── ideas/               # 想法观点
│
├── theory/                   # 理论文章 (21篇)
│
├── policy/                   # 政策研究
│   ├── China-ministry-commerce/   # 商务部 (8份)
│   ├── EU-policy/                 # 欧盟 (4份)
│   ├── US-policy/                 # 美国 (4份)
│   ├── ASEAN/                    # 东盟 (1份)
│   └── ...
│
├── data/                     # 数据资料
│   ├── UNCTAD-reports/      # 18份
│   ├── OECD-reports/        # 8份
│   ├── WTO-reports/         # 4份
│   ├── IMF-reports/         # 1份
│   ├── WEF-reports/         # 1份
│   ├── IEA-reports/         # 1份
│   ├── FDI-reports/         # 4份
│   └── Yangtze-Delta/      # 11份
│
├── cases/                    # 案例库
│   ├── Shanghai-cases/      # 2份
│   ├── ESG-reports/         # 3份
│   ├── Shanghai-stock-exchange/  # 2份
│   └── ...
│
├── templates/                # 写作模板
│
└── tools/                   # 研究工具
```

---

## 三、工作流程

```
用户放文件 → 待上传资料YYYYMMDD/
     ↓
AI分析内容 → 提取关键词、年份、机构
     ↓
自动分类 → policy / data / cases / theory
     ↓
生成 index.md → 列出所有文件
     ↓
部署网站 → mkdocs gh-deploy
     ↓
移动文件 → 已上传资料YYYYMMDD/
```

---

## 四、关键路径

| 项目 | 路径 |
|------|------|
| 网站源文件 | `~/.openclaw/workspace/research-knowledge-base-mkdocs/` |
| 配置文件 | `mkdocs.yml` |
| 部署命令 | `python3 -m mkdocs gh-deploy --force` |
| 自动化脚本 | `scripts/ai_analyze.py` |
| 自动部署 | `scripts/deploy.sh` |
| GitHub仓库 | https://github.com/lxz-123435/research-knowledge-base |
| 网站地址 | https://lxz-123435.github.io/research-knowledge-base/ |

---

## 五、自动化脚本

### 1. AI分析脚本 (scripts/ai_analyze.py)

功能：
- 读取PDF内容
- 生成摘要模板
- 自动分类（policy/data/cases/theory）
- 生成Markdown笔记

使用：
```bash
python3 scripts/ai_analyze.py <文件或目录>
```

### 2. 部署脚本 (scripts/deploy.sh)

功能：
- 构建网站
- 部署到GitHub Pages
- 显示访问地址

使用：
```bash
bash scripts/deploy.sh
```

---

## 六、当前数据统计

| 类别 | 数量 |
|------|------|
| 理论文章 | 21篇 |
| 政策文件 | ~25份 |
| 数据报告 | ~47份 |
| 案例资料 | ~14份 |
| 研究主题 | 6个 |
| 资料来源 | 8个机构 |

---

## 七、访问结构

| URL | 内容 |
|-----|------|
| `/` | 首页 |
| `/research/` | 研究主题 |
| `/sources/` | 资料来源 |
| `/notes/` | 阅读笔记 |
| `/theory/` | 理论文章 |
| `/policy/` | 政策研究 |
| `/data/` | 数据资料 |
| `/cases/` | 案例库 |
| `/templates/` | 写作模板 |
| `/tools/` | 研究工具 |

---

## 八、优缺点分析

### ✅ 优点

1. **双维度分类** - 研究主题 + 资料来源
2. **知识提炼层** - notes/ 阅读笔记
3. **自动化** - 部署脚本
4. **AI友好** - Markdown格式便于AI读取
5. **持续扩展** - 目录结构清晰

### ⚠️ 待优化

1. **大文件问题** - 2个PDF超过50MB（建议Git LFS）
2. **标签系统** - 尚未添加
3. **时间维度** - 政策未按年份分类
4. **自动抓取** - 尚未实现自动抓取政策
5. **AI摘要** - 脚本仅为模板，未接入GPT API

---

## 九、建议优化方向（优先级排序）

| 优先级 | 优化项 | 理由 |
|--------|--------|------|
| ⭐⭐⭐ | 标签系统 | 知识关联 |
| ⭐⭐⭐ | 自动抓取 | 真正解放双手 |
| ⭐⭐ | 时间维度 | 政策追踪 |
| ⭐ | 大文件LFS | GitHub限制 |
| ⭐⭐⭐⭐ | AI摘要API | 自动生成笔记 |

---

## 十、最终目标

**把"搜资料 → 读资料 → 做笔记 → 写报告"整个研究流程自动化**

形成：
- 个人研究知识库
- 智能分类系统  
- AI研究助手
- 持续更新的政策库

---

*最后更新: 2026-03-15*
