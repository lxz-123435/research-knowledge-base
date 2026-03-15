#!/usr/bin/env python3
"""
AI 研究资料分析脚本
功能：自动解析PDF、生成摘要、分类、生成笔记
"""

import os
import sys
import json
import subprocess
from datetime import datetime

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
            return text[:5000]  # 限制长度
    except Exception as e:
        return f"Error reading PDF: {e}"

def generate_summary(text, filename):
    """生成摘要（模拟AI摘要，实际可接入GPT API）"""
    # 提取文件名中的关键信息
    name_without_ext = os.path.splitext(filename)[0]
    
    # 简单的关键词提取
    keywords = []
    for kw in ["UNCTAD", "OECD", "IMF", "WTO", "WEF", "商务部", "国家数据局", "欧盟", "美国"]:
        if kw in name_without_ext:
            keywords.append(kw)
    
    # 尝试提取年份
    import re
    years = re.findall(r"20\d{2}", name_without_ext)
    
    summary = f"""# {name_without_ext}

## 基本信息

- **文件名**: {filename}
- **来源**: {keywords[0] if keywords else '未知'}
- **年份**: {years[0] if years else '未知'}

## 内容摘要

（AI摘要待生成 - 可接入GPT API自动生成）

## 核心观点

1. （待分析）
2. （待分析）
3. （待分析）

## 关键词

{', '.join(keywords) if keywords else '待添加'}

## 相关资料

- （待添加关联资料）

---
*自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    return summary

def auto_classify(filename):
    """自动分类"""
    filename_lower = filename.lower()
    
    # 政策类
    if any(kw in filename_lower for kw in ["政策", "商务部", "国家数据局", "国务院", "欧盟", "美国"]):
        return "policy"
    
    # 数据报告类
    if any(kw in filename_lower for kw in ["unctad", "oecd", "imf", "wto", "wef", "报告", "统计"]):
        return "data"
    
    # 案例类
    if any(kw in filename_lower for kw in ["案例", "企业", "并购", "投资"]):
        return "cases"
    
    # 理论类
    if any(kw in filename_lower for kw in ["理论", "思想", "观点", "研究"]):
        return "theory"
    
    return "data"  # 默认

def process_file(pdf_path):
    """处理单个文件"""
    filename = os.path.basename(pdf_path)
    print(f"处理: {filename}")
    
    # 1. 读取内容
    content = read_pdf(pdf_path)
    
    # 2. 生成摘要
    summary = generate_summary(content, filename)
    
    # 3. 自动分类
    category = auto_classify(filename)
    
    # 4. 确定目标目录
    target_dir = os.path.join(DOCS_DIR, category)
    os.makedirs(target_dir, exist_ok=True)
    
    # 5. 保存笔记
    note_filename = os.path.splitext(filename)[0] + ".md"
    note_path = os.path.join(target_dir, note_filename)
    
    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"  -> 已生成笔记: {note_path}")
    print(f"  -> 分类: {category}")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python ai_analyze.py <PDF文件路径>")
        print("或: python ai_analyze.py <目录路径>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if os.path.isfile(target):
        # 单个文件
        process_file(target)
    elif os.path.isdir(target):
        # 目录
        for f in os.listdir(target):
            if f.endswith('.pdf'):
                process_file(os.path.join(target, f))
    else:
        print(f"错误: {target} 不存在")

if __name__ == "__main__":
    main()
