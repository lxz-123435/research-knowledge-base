#!/usr/bin/env python3
"""
写作模板生成模块
功能：根据研究主题自动生成文章框架
"""

import os
import json
from datetime import datetime

# 配置
DOCS_DIR = os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs/docs")

def get_related_materials(topic):
    """获取相关材料"""
    materials = {
        "books": [],
        "notes": [],
        "concepts": [],
        "frameworks": [],
        "insights": []
    }
    
    topic_lower = topic.lower()
    
    # 扫描书籍
    books_dir = os.path.join(DOCS_DIR, "01_sources", "books")
    if os.path.exists(books_dir):
        for f in os.listdir(books_dir):
            if f.endswith('.md'):
                with open(os.path.join(books_dir, f), 'r', encoding='utf-8') as file:
                    content = file.read()
                    if topic_lower in content.lower():
                        materials["books"].append(f.replace('.md', ''))
    
    # 扫描概念
    concepts_dir = os.path.join(DOCS_DIR, "02_knowledge", "concepts")
    if os.path.exists(concepts_dir):
        for f in os.listdir(concepts_dir):
            if f.endswith('.md') and f != 'index.md':
                with open(os.path.join(concepts_dir, f), 'r', encoding='utf-8') as file:
                    content = file.read()
                    if topic_lower in content.lower():
                        materials["concepts"].append(f.replace('.md', ''))
    
    # 扫描框架
    frameworks_dir = os.path.join(DOCS_DIR, "02_knowledge", "frameworks")
    if os.path.exists(frameworks_dir):
        for f in os.listdir(frameworks_dir):
            if f.endswith('.md') and f != 'index.md':
                with open(os.path.join(frameworks_dir, f), 'r', encoding='utf-8') as file:
                    content = file.read()
                    if topic_lower in content.lower():
                        materials["frameworks"].append(f.replace('.md', ''))
    
    # 扫描洞见
    insights_dir = os.path.join(DOCS_DIR, "02_knowledge", "insights")
    if os.path.exists(insights_dir):
        for f in os.listdir(insights_dir):
            if f.endswith('.md') and f != 'index.md':
                with open(os.path.join(insights_dir, f), 'r', encoding='utf-8') as file:
                    content = file.read()
                    if topic_lower in content.lower():
                        materials["insights"].append(f.replace('.md', ''))
    
    return materials

def generate_article_framework(topic, article_type="论文"):
    """生成文章框架"""
    materials = get_related_materials(topic)
    
    if article_type == "论文":
        return generate_paper_framework(topic, materials)
    elif article_type == "报告":
        return generate_report_framework(topic, materials)
    elif article_type == "评论":
        return generate_essay_framework(topic, materials)
    else:
        return generate_paper_framework(topic, materials)

def generate_paper_framework(topic, materials):
    """生成论文框架"""
    framework = f"""# {topic} 研究论文

> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 摘要

（简要概述研究问题、方法和结论）

**关键词**: {topic}

---

## 一、引言

### 1.1 研究背景

（为什么要研究这个问题？）

### 1.2 研究问题

本研究试图回答以下问题：
1. {topic}的本质是什么？
2. {topic}有哪些特征？
3. 如何理解和应用{topic}？

### 1.3 研究意义

- 理论意义
- 实践意义

---

## 二、文献综述

### 2.1 核心概念

"""
    
    if materials["concepts"]:
        framework += "\n".join([f"- [{c}](../02_knowledge/concepts/{c}.md)" for c in materials["concepts"]])
    else:
        framework += "\n- （待补充）"
    
    framework += f"""

### 2.2 理论基础

"""
    
    if materials["frameworks"]:
        framework += "\n".join([f"- [{f}](../02_knowledge/frameworks/{f}.md)" for f in materials["frameworks"]])
    else:
        framework += "\n- （待补充）"
    
    framework += f"""

---

## 三、{topic}分析

### 3.1 {topic}的核心内涵

### 3.2 主要特征

| 特征 | 说明 |
|------|------|
| 特征1 | 说明 |
| 特征2 | 说明 |

### 3.3 案例分析

"""
    
    if materials["books"]:
        framework += "\n".join([f"- [{b}](../01_sources/books/{b}.md)" for b in materials["books"]])
    
    framework += """

---

## 四、结论与建议

### 4.1 主要结论

### 4.2 政策建议

### 4.3 研究展望

---

## 参考文献

"""
    
    if materials["books"]:
        framework += "\n".join([f"- [{b}]" for b in materials["books"]])
    
    framework += """

---

*本文框架由AI自动生成，供参考*
"""
    
    return framework

def generate_report_framework(topic, materials):
    """生成报告框架"""
    framework = f"""# {topic} 研究报告

> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 执行摘要

（简要结论）

---

## 一、背景

### 1.1 问题背景

### 1.2 研究目的

---

## 二、现状分析

### 2.1 核心数据

### 2.2 主要发现

"""
    
    if materials["concepts"]:
        framework += "\n**相关概念:** " + ", ".join([f"[{c}](../02_knowledge/concepts/{c}.md)" for c in materials["concepts"]])
    
    framework += """

---

## 三、问题与挑战

### 3.1 主要问题

### 3.2 成因分析

---

## 四、对策建议

### 4.1 短期建议

### 4.2 中长期建议

---

## 五、结论

---

*本报告框架由AI自动生成，供参考*
"""
    
    return framework

def generate_essay_framework(topic, materials):
    """生成评论框架"""
    framework = f"""# {topic} 评论

> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 开篇

（引入话题）

---

## 观点阐述

### 核心观点

"""
    
    if materials["insights"]:
        framework += "\n".join([f"- [{i}](../02_knowledge/insights/{i}.md)" for i in materials["insights"]])
    
    framework += f"""

### 论证

---

## 案例

"""
    
    if materials["books"]:
        framework += "\n".join([f"- [{b}](../01_sources/books/{b}.md)" for b in materials["books"]])
    
    framework += """

---

## 结语

（总结观点）

---

*本文框架由AI自动生成，供参考*
"""
    
    return framework

def create_article(topic, article_type="论文"):
    """创建文章"""
    print(f"📝 正在生成 [{topic}] 的{article_type}框架...")
    
    framework = generate_article_framework(topic, article_type)
    
    # 保存
    output_dir = os.path.join(DOCS_DIR, "04_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    # 根据类型选择子目录
    if article_type == "论文":
        subdir = "theory"
    elif article_type == "报告":
        subdir = "reports"
    else:
        subdir = "essays"
    
    output_dir = os.path.join(output_dir, subdir)
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{topic}.md"
    output_path = os.path.join(output_dir, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(framework)
    
    print(f"✅ 已生成: {output_path}")
    
    return output_path

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("📝 用法:")
        print("  python write_template.py <主题> [论文|报告|评论]")
        print("\n示例:")
        print("  python write_template.py 媒体权力 论文")
        print("  python write_template.py AI治理 报告")
        print("  python write_template.py 全球化 评论")
        sys.exit(0)
    
    topic = sys.argv[1]
    article_type = sys.argv[2] if len(sys.argv) > 2 else "论文"
    
    create_article(topic, article_type)

if __name__ == "__main__":
    main()
