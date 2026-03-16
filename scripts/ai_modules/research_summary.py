#!/usr/bin/env python3
"""
研究综述自动生成模块
功能：自动汇总某研究主题的所有相关资料
"""

import os
import json
from datetime import datetime
from pathlib import Path

# 配置
DOCS_DIR = os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs/docs")

def scan_knowledge_base():
    """扫描知识库"""
    results = {
        "books": [],
        "notes": [],
        "concepts": [],
        "frameworks": [],
        "insights": [],
        "topics": []
    }
    
    # 扫描书籍
    books_dir = os.path.join(DOCS_DIR, "01_sources", "books")
    if os.path.exists(books_dir):
        for f in os.listdir(books_dir):
            if f.endswith('.md'):
                results["books"].append(f.replace('.md', ''))
    
    # 扫描笔记
    notes_dir = os.path.join(DOCS_DIR, "02_knowledge", "notes")
    if os.path.exists(notes_dir):
        for root, dirs, files in os.walk(notes_dir):
            for f in files:
                if f == 'index.md':
                    rel_path = os.path.relpath(root, notes_dir)
                    if rel_path != '.':
                        results["notes"].append(rel_path)
    
    # 扫描概念
    concepts_dir = os.path.join(DOCS_DIR, "02_knowledge", "concepts")
    if os.path.exists(concepts_dir):
        for f in os.listdir(concepts_dir):
            if f.endswith('.md') and f != 'index.md':
                results["concepts"].append(f.replace('.md', ''))
    
    # 扫描框架
    frameworks_dir = os.path.join(DOCS_DIR, "02_knowledge", "frameworks")
    if os.path.exists(frameworks_dir):
        for f in os.listdir(frameworks_dir):
            if f.endswith('.md') and f != 'index.md':
                results["frameworks"].append(f.replace('.md', ''))
    
    # 扫描洞见
    insights_dir = os.path.join(DOCS_DIR, "02_knowledge", "insights")
    if os.path.exists(insights_dir):
        for f in os.listdir(insights_dir):
            if f.endswith('.md') and f != 'index.md':
                results["insights"].append(f.replace('.md', ''))
    
    # 扫描研究主题
    topics_dir = os.path.join(DOCS_DIR, "03_research", "topics")
    if os.path.exists(topics_dir):
        for root, dirs, files in os.walk(topics_dir):
            for f in files:
                if f == 'index.md':
                    rel_path = os.path.relpath(root, topics_dir)
                    if rel_path != '.':
                        results["topics"].append(rel_path)
    
    return results

def search_related(keyword):
    """搜索相关内容"""
    kb = scan_knowledge_base()
    results = {
        "books": [],
        "notes": [],
        "concepts": [],
        "frameworks": [],
        "insights": [],
        "topics": []
    }
    
    keyword = keyword.lower()
    
    # 搜索书籍
    for book in kb["books"]:
        if keyword in book.lower():
            results["books"].append(book)
    
    # 搜索笔记
    for note in kb["notes"]:
        if keyword in note.lower():
            results["notes"].append(note)
    
    # 搜索概念
    for concept in kb["concepts"]:
        if keyword in concept.lower():
            results["concepts"].append(concept)
    
    # 搜索框架
    for fw in kb["frameworks"]:
        if keyword in fw.lower():
            results["frameworks"].append(fw)
    
    # 搜索洞见
    for insight in kb["insights"]:
        if keyword in insight.lower():
            results["insights"].append(insight)
    
    # 搜索研究主题
    for topic in kb["topics"]:
        if keyword in topic.lower():
            results["topics"].append(topic)
    
    return results

def generate_research_summary(topic_name):
    """生成研究综述"""
    print(f"🔍 正在生成 [{topic_name}] 的研究综述...")
    
    # 搜索相关内容
    related = search_related(topic_name)
    
    summary = f"""# {topic_name} 研究综述

> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 相关书籍

"""
    
    if related["books"]:
        for book in related["books"]:
            summary += f"- [{book}](../01_sources/books/{book}.md)\n"
    else:
        summary += "- （暂无）\n"
    
    summary += """
## 相关笔记

"""
    
    if related["notes"]:
        for note in related["notes"]:
            summary += f"- [{note}](../02_knowledge/notes/{note}/index.md)\n"
    else:
        summary += "- （暂无）\n"
    
    summary += """
## 相关概念

"""
    
    if related["concepts"]:
        for concept in related["concepts"]:
            summary += f"- [{concept}](../02_knowledge/concepts/{concept}.md)\n"
    else:
        summary += "- （暂无）\n"
    
    summary += """
## 相关框架

"""
    
    if related["frameworks"]:
        for fw in related["frameworks"]:
            summary += f"- [{fw}](../02_knowledge/frameworks/{fw}.md)\n"
    else:
        summary += "- （暂无）\n"
    
    summary += """
## 相关洞见

"""
    
    if related["insights"]:
        for insight in related["insights"]:
            summary += f"- [{insight}](../02_knowledge/insights/{insight}.md)\n"
    else:
        summary += "- （暂无）\n"
    
    summary += """
## 研究主题

"""
    
    if related["topics"]:
        for topic in related["topics"]:
            summary += f"- [{topic}](../03_research/topics/{topic}/index.md)\n"
    else:
        summary += "- （暂无）\n"
    
    # 统计
    total = sum(len(v) for v in related.values())
    summary += f"""
---

## 统计

共找到 {total} 个相关条目：

- 书籍: {len(related['books'])}
- 笔记: {len(related['notes'])}
- 概念: {len(related['concepts'])}
- 框架: {len(related['frameworks'])}
- 洞见: {len(related['insights'])}
- 研究主题: {len(related['topics'])}

---

*本综述由AI自动生成*
"""
    
    return summary, related

def create_research_summary(topic_name):
    """创建研究综述"""
    summary, related = generate_research_summary(topic_name)
    
    # 保存到文件
    output_dir = os.path.join(DOCS_DIR, "03_research", "topics", topic_name)
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "summary.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"✅ 已生成研究综述: {output_path}")
    
    return output_path

def list_all_topics():
    """列出所有研究主题"""
    kb = scan_knowledge_base()
    
    print("\n📚 知识库内容概览")
    print("=" * 40)
    print(f"📚 书籍: {len(kb['books'])}")
    print(f"📝 笔记: {len(kb['notes'])}")
    print(f"💡 概念: {len(kb['concepts'])}")
    print(f"🗂️ 框架: {len(kb['frameworks'])}")
    print(f"💭 洞见: {len(kb['insights'])}")
    print(f"🔬 主题: {len(kb['topics'])}")
    print("=" * 40)
    
    return kb

def main():
    import sys
    
    if len(sys.argv) < 2:
        # 显示概览
        kb = list_all_topics()
        
        print("\n📖 用法:")
        print("  python research_summary.py <主题名>  # 生成某主题综述")
        print("  python research_summary.py --scan        # 扫描知识库")
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "--scan":
        list_all_topics()
    else:
        topic = " ".join(sys.argv[1:])
        create_research_summary(topic)

if __name__ == "__main__":
    main()
