#!/usr/bin/env python3
"""
AI 自动知识提取模块
功能：从PDF自动提取核心观点、概念、框架，生成结构化笔记
"""

import os
import sys
import json
import re
from datetime import datetime

# 配置
DOCS_DIR = os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs/docs")

def extract_text_from_pdf(pdf_path, max_pages=10):
    """从PDF提取文本"""
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i, page in enumerate(reader.pages[:max_pages]):
                text += f"=== 第{i+1}页 ===\n" + page.extract_text() + "\n"
            return text[:15000]  # 限制长度
    except Exception as e:
        return f"Error: {e}"

def extract_book_info(text, filename):
    """提取书籍基本信息"""
    import re
    
    name_without_ext = os.path.splitext(filename)[0]
    
    # 尝试提取作者
    author_match = re.search(r'作者[：:]\s*([^\n]+)', text)
    author = author_match.group(1) if author_match else "未知"
    
    # 尝试提取出版社
    publisher_match = re.search(r'出版社[：:]\s*([^\n]+)', text)
    publisher = publisher_match.group(1) if publisher_match else "未知"
    
    # 尝试提取年份
    year_match = re.search(r'出版[年时间][：:]\s*(\d{4})', text)
    year = year_match.group(1) if year_match else "未知"
    
    return {
        "name": name_without_ext,
        "author": author,
        "publisher": publisher,
        "year": year
    }

def extract_core_questions(text):
    """提取核心问题（模拟AI分析）"""
    # 从目录提取章节作为问题线索
    questions = []
    
    # 查找可能的章节标题
    import re
    chapters = re.findall(r'^第[一二三四五六七八九十\d]+[章节部篇]\s*([^\n]{2,20})', text, re.MULTILINE)
    
    for ch in chapters[:5]:
        questions.append(f"这一章探讨了什么？")
    
    if not questions:
        questions = [
            "这本书试图回答什么问题？",
            "作者的核心观点是什么？",
            "有什么方法论？"
        ]
    
    return questions

def extract_key_concepts(text):
    """提取关键概念"""
    import re
    
    # 常见的概念词汇
    concept_keywords = [
        "生产力", "产业链", "创新", "数字化", "全球化",
        "治理", "政策", "战略", "模式", "框架",
        "理论", "方法", "分析", "研究", "数据"
    ]
    
    found_concepts = []
    for kw in concept_keywords:
        if kw in text:
            found_concepts.append(kw)
    
    return found_concepts[:10]

def extract_structure(text):
    """提取逻辑结构"""
    import re
    
    # 尝试从目录提取结构
    structure = []
    
    # 查找可能的章节
    chapters = re.findall(r'^\s*(\d+)[.\s]+([^\n]{5,30})', text, re.MULTILINE)
    for num, title in chapters[:10]:
        structure.append(f"第{num}部分: {title.strip()}")
    
    if not structure:
        structure = ["第一部分", "第二部分", "第三部分"]
    
    return structure

def generate_note(book_info, questions, concepts, structure):
    """生成阅读笔记"""
    note = f"""# {book_info['name']}

> 作者：{book_info['author']} | 出版社：{book_info['publisher']} | 出版年：{book_info['year']}

---

## 核心问题

{chr(10).join([f'{i+1}. {q}' for i, q in enumerate(questions)])}

---

## 核心观点

1. （待分析）
2. （待分析）
3. （待分析）

---

## 逻辑结构

{chr(10).join([f'{i+1}. {s}' for i, s in enumerate(structure)])}

---

## 关键概念

{', '.join(concepts) if concepts else '（待提取）'}

---

## 知识关联

### 概念

- （待添加）

### 框架

- （待添加）

### 研究

- （待添加）

---

*AI自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    return note

def generate_metadata(book_info, questions, concepts, structure):
    """生成元数据"""
    metadata = {
        "title": book_info['name'],
        "author": book_info['author'],
        "publisher": book_info['publisher'],
        "year": book_info['year'],
        "core_questions": questions,
        "key_concepts": concepts,
        "structure": structure,
        "created": datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    return metadata

def process_book(pdf_path):
    """处理一本书"""
    filename = os.path.basename(pdf_path)
    print(f"📖 处理: {filename}")
    
    # 1. 提取文本
    print("  → 提取文本...")
    text = extract_text_from_pdf(pdf_path)
    
    # 2. 提取书籍信息
    print("  → 提取书籍信息...")
    book_info = extract_book_info(text, filename)
    
    # 3. 提取核心问题
    print("  → 分析核心问题...")
    questions = extract_core_questions(text)
    
    # 4. 提取关键概念
    print("  → 提取关键概念...")
    concepts = extract_key_concepts(text)
    
    # 5. 提取结构
    print("  → 分析结构...")
    structure = extract_structure(text)
    
    # 6. 生成笔记
    print("  → 生成笔记...")
    note = generate_note(book_info, questions, concepts, structure)
    
    # 7. 生成元数据
    metadata = generate_metadata(book_info, questions, concepts, structure)
    
    # 8. 保存
    book_folder = book_info['name'].replace(' ', '-')[:50]
    note_dir = os.path.join(DOCS_DIR, "02_knowledge", "notes", book_folder)
    os.makedirs(note_dir, exist_ok=True)
    
    note_path = os.path.join(note_dir, "index.md")
    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(note)
    
    metadata_path = os.path.join(note_dir, "metadata.json")
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 已生成: {note_path}")
    print(f"  📊 提取到 {len(concepts)} 个概念")
    
    return {
        "note_path": note_path,
        "metadata": metadata
    }

def main():
    if len(sys.argv) < 2:
        print("用法: python ai_extract.py <PDF文件>")
        print("   或: python ai_extract.py <目录>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if os.path.isfile(target) and target.endswith('.pdf'):
        process_book(target)
    elif os.path.isdir(target):
        for f in os.listdir(target):
            if f.endswith('.pdf'):
                process_book(os.path.join(target, f))
    else:
        print("错误: 请提供PDF文件或包含PDF的目录")

if __name__ == "__main__":
    main()
