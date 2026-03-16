#!/usr/bin/env python3
"""
引用检查脚本
检查Markdown文件是否包含引用
"""

import os
import re
import sys

def check_file(file_path):
    """检查单个文件是否有引用"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有句子（中文句号或英文句点）但没有引用
    has_sentences = '。' in content or '. ' in content
    has_citations = '[^' in content or '[[' in content
    
    # 排除引用文件本身
    if 'references/' in file_path:
        return None
    
    if has_sentences and not has_citations:
        return file_path
    return None

def main():
    docs_dir = "docs"
    issues = []
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                result = check_file(file_path)
                if result:
                    issues.append(result)
    
    if issues:
        print("⚠️  以下文件可能有未添加引用的问题：")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    else:
        print("✅ 所有文件都包含引用！")
        return 0

if __name__ == "__main__":
    sys.exit(main())
