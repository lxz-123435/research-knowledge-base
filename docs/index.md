# 政策研究资料库

个人研究知识库系统 (Research OS) - 把"搜资料 → 读资料 → 做笔记 → 写报告"整个研究流程自动化。

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

### 📚 资料来源（按机构）
- [UNCTAD](sources/UNCTAD/index.md) - 联合国贸发会议
- [OECD](sources/OECD/index.md) - 经合组织
- [IMF](sources/IMF/index.md) - 国际货币基金
- [商务部](sources/China-commerce/index.md) - 商务部
- [国家数据局](sources/China-data-bureau/index.md) - 国家数据局

### 📝 阅读笔记
- [阅读笔记](notes/reading-notes/index.md) - 资料分析总结
- [框架模型](notes/frameworks/index.md) - 研究分析框架
- [想法观点](notes/ideas/index.md) - 原创思考

### 📁 资料库
- [理论文章](theory/achievement-view/index.md) - 理论文献
- [政策研究](policy/index.md) - 政策文件
- [数据资料](data/index.md) - 研究报告
- [案例库](cases/index.md) - 企业案例

### 🛠️ 工具
- [研究工具](tools/index.md) - 自动化脚本

---

## 快速开始

### 添加新资料
1. 把PDF放到 `待上传资料YYYYMMDD/`
2. 运行: `python3 scripts/ai_analyze.py <文件>`
3. 运行: `bash scripts/deploy.sh`

### 部署网站
```bash
bash scripts/deploy.sh
```

---

## 网站地址

🔗 **https://lxz-123435.github.io/research-knowledge-base/**

---

*AI 研究操作系统 v1.0*
