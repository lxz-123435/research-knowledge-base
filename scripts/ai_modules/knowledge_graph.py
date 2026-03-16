#!/usr/bin/env python3
"""
知识图谱生成模块
功能：分析概念之间的关联，生成可视化图谱
"""

import os
import json
from pathlib import Path

# 配置
DOCS_DIR = os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs/docs")

def scan_concepts():
    """扫描所有概念"""
    concepts = {}
    concepts_dir = os.path.join(DOCS_DIR, "02_knowledge", "concepts")
    
    if not os.path.exists(concepts_dir):
        return concepts
    
    for f in os.listdir(concepts_dir):
        if f.endswith('.md') and f != 'index.md':
            name = f.replace('.md', '')
            path = os.path.join(concepts_dir, f)
            
            # 读取内容，提取关联
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 提取关联的概念
            related = []
            for other_file in os.listdir(concepts_dir):
                if other_file != f and other_file.endswith('.md'):
                    other_name = other_file.replace('.md', '')
                    if other_name in content:
                        related.append(other_name)
            
            concepts[name] = {
                "related": related,
                "path": path
            }
    
    return concepts

def scan_relationships():
    """扫描所有知识关联"""
    relationships = []
    
    # 概念之间的关系
    concepts = scan_concepts()
    for name, info in concepts.items():
        for rel in info["related"]:
            relationships.append({
                "from": name,
                "to": rel,
                "type": "concept_to_concept"
            })
    
    # 扫描概念与其他模块的关联
    # 概念 -> 研究主题
    topics_dir = os.path.join(DOCS_DIR, "03_research", "topics")
    if os.path.exists(topics_dir):
        for root, dirs, files in os.walk(topics_dir):
            for f in files:
                if f.endswith('.md'):
                    topic_path = os.path.relpath(root, topics_dir)
                    with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    for concept in concepts:
                        if concept in content:
                            relationships.append({
                                "from": concept,
                                "to": topic_path,
                                "type": "concept_to_topic"
                            })
    
    return relationships

def generate_graph_data():
    """生成图谱数据"""
    concepts = scan_concepts()
    relationships = scan_relationships()
    
    # 生成节点
    nodes = []
    for name in concepts.keys():
        nodes.append({
            "id": name,
            "label": name,
            "type": "concept"
        })
    
    # 添加研究主题节点
    topics_dir = os.path.join(DOCS_DIR, "03_research", "topics")
    if os.path.exists(topics_dir):
        for root, dirs, files in os.walk(topics_dir):
            for f in files:
                if f == 'index.md':
                    topic = os.path.relpath(root, topics_dir)
                    nodes.append({
                        "id": topic,
                        "label": topic,
                        "type": "topic"
                    })
    
    # 生成边
    edges = []
    for rel in relationships:
        edges.append({
            "from": rel["from"],
            "to": rel["to"],
            "type": rel["type"]
        })
    
    return {
        "nodes": nodes,
        "edges": edges
    }

def generate_knowledge_map():
    """生成知识地图页面"""
    concepts = scan_concepts()
    relationships = scan_relationships()
    graph_data = generate_graph_data()
    
    # 统计
    concept_count = len(concepts)
    topic_count = len([n for n in graph_data["nodes"] if n["type"] == "topic"])
    rel_count = len(relationships)
    
    html = f"""# 知识图谱

> 自动生成的知识关联网络

---

## 统计

| 类型 | 数量 |
|------|------|
| 概念 | {concept_count} |
| 研究主题 | {topic_count} |
| 关联关系 | {rel_count} |

---

## 概念网络

### 概念列表

| 概念 | 关联概念 |
|------|----------|
"""
    
    for name, info in sorted(concepts.items()):
        related = info["related"]
        if related:
            html += f"| {name} | {', '.join(related)} |\n"
        else:
            html += f"| {name} | （暂无） |\n"
    
    html += """
---

## 关联关系

"""
    
    for rel in relationships:
        if rel["type"] == "concept_to_concept":
            html += f"- {rel['from']} ←→ {rel['to']}\n"
        else:
            html += f"- {rel['from']} → {rel['to']} (研究主题)\n"
    
    html += f"""
---

## 图谱数据

```json
{json.dumps(graph_data, ensure_ascii=False, indent=2)}
```

---

*图谱自动生成于 2026-03-15*
"""
    
    # 保存
    output_path = os.path.join(DOCS_DIR, "02_knowledge", "knowledge-graph.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 已生成知识图谱: {output_path}")
    print(f"   - 概念: {concept_count}")
    print(f"   - 主题: {topic_count}")
    print(f"   - 关联: {rel_count}")
    
    return output_path

def main():
    print("🔍 扫描知识库...")
    
    concepts = scan_concepts()
    print(f"\n📚 找到 {len(concepts)} 个概念")
    
    for name, info in concepts.items():
        print(f"   - {name}: {len(info['related'])} 个关联")
    
    print("\n🔗 分析关联...")
    relationships = scan_relationships()
    print(f"   找到 {len(relationships)} 个关联")
    
    print("\n📊 生成图谱...")
    generate_knowledge_map()
    
    print("\n✅ 完成!")

if __name__ == "__main__":
    main()
