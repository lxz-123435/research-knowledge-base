#!/usr/bin/env python3
"""
手动添加模块 - 增强版
功能：交互式添加书籍、笔记、概念、框架、洞见、随笔
"""

import os
import sys
from datetime import datetime

# 配置
DOCS_DIR = os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs/docs")

def input_with_default(prompt, default=""):
    """带默认值的输入"""
    if default:
        result = input(f"{prompt} [{default}]: ").strip()
        return result if result else default
    return input(f"{prompt}: ").strip()

def input_multiline(prompt):
    """多行输入"""
    print(f"\n{prompt}（输入完成后按 Ctrl+D）:")
    try:
        content = sys.stdin.read().strip()
        return content
    except:
        return ""

def add_book():
    """添加书籍"""
    print("\n📚 添加书籍")
    print("=" * 50)
    
    name = input_with_default("书名")
    author = input_with_default("作者", "未知")
    publisher = input_with_default("出版社", "未知")
    year = input_with_default("出版年", "未知")
    pages = input_with_default("页数", "未知")
    category = input_with_default("分类", "其他")
    
    # 原文链接
    print("\n原文链接（直接回车跳过）:")
    douban = input_with_default("  豆瓣链接", "无")
    amazon = input_with_default("  亚马逊链接", "无")
    jd = input_with_default("  京东链接", "无")
    
    # 主要内容
    description = input_multiline("主要内容简介")
    
    # 目录
    print("\n目录（每行一章，回车后按 Ctrl+D 结束）:")
    try:
        toc = sys.stdin.read().strip()
    except:
        toc = ""
    
    # 构建内容
    links = []
    if douban and douban != "无":
        links.append(f"- [豆瓣读书]({douban})")
    if amazon and amazon != "无":
        links.append(f"- [亚马逊]({amazon})")
    if jd and jd != "无":
        links.append(f"- [京东]({jd})")
    
    content = f"""# {name}

> 作者：{author} | 出版社：{publisher}

---

## 书籍信息

| 项目 | 内容 |
|------|------|
| 书名 | {name} |
| 作者 | {author} |
| 出版社 | {publisher} |
| 出版年 | {year} |
| 页数 | {pages} |
| 分类 | {category} |

---

## 原文链接

{chr(10).join(links) if links else "- （暂无）"}

---

## 内容简介

{description if description else "（待补充）"}

---

## 目录

{toc if toc else "（待补充）"}

---

## 核心主题

- （待总结）

---

## 相关知识

### 概念

- （待添加）

### 框架

- （待添加）

### 洞见

- （待添加）

### 研究

- （待添加）

---

## 知识流动

```
这本书 → 阅读笔记 → 概念 → 框架 → 洞见 → 研究 → 随笔
```

---

*手动添加于 {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    
    # 保存
    filename = f"{name}.md"
    path = os.path.join(DOCS_DIR, "01_sources", "books", filename)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ 已添加: {path}")
    return path

def add_note():
    """添加阅读笔记"""
    print("\n📝 添加阅读笔记")
    print("=" * 50)
    
    book_name = input_with_default("书名")
    core_question = input_with_default("核心问题")
    core_view = input_with_default("核心观点")
    structure = input_with_default("逻辑结构")
    method = input_with_default("方法论")
    inspiration = input_with_default("现实启发")
    
    content = f"""# {book_name} - 阅读笔记

> 添加于 {datetime.now().strftime('%Y-%m-%d')}

---

## 核心问题

{core_question}

---

## 核心观点

{core_view}

---

## 逻辑结构

{structure}

---

## 方法论

{method}

---

## 现实启发

{inspiration}

---

## 知识关联

- 概念: （待添加）
- 框架: （待添加）
- 研究: （待添加）

---

*手动添加*
"""
    
    # 保存
    folder = os.path.join(DOCS_DIR, "02_knowledge", "notes", book_name)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "index.md")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ 已添加: {path}")
    return path

def add_concept():
    """添加概念"""
    print("\n💡 添加概念")
    print("=" * 50)
    
    name = input_with_default("概念名称")
    definition = input_with_default("定义")
    keywords = input_with_default("关键词（逗号分隔）")
    source = input_with_default("来源书籍", "未知")
    
    content = f"""# {name}

## 定义

{definition}

## 关键词

{keywords}

## 来源

- {source}

## 相关概念

- （待添加）

## 关联研究

- （待添加）

---

*手动添加于 {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    
    # 保存
    filename = f"{name}.md"
    path = os.path.join(DOCS_DIR, "02_knowledge", "concepts", filename)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ 已添加: {path}")
    return path

def add_framework():
    """添加框架"""
    print("\n🗂️ 添加分析框架")
    print("=" * 50)
    
    name = input_with_default("框架名称")
    theory = input_with_default("核心理论")
    dimensions = input_with_default("分析维度（逗号分隔）")
    application = input_with_default("应用场景")
    
    content = f"""# {name}

## 核心理论

{theory}

## 分析维度

{dimensions}

## 应用场景

{application}

## 相关概念

- （待添加）

## 案例

- （待添加）

---

*手动添加于 {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    
    # 保存
    filename = f"{name}.md"
    path = os.path.join(DOCS_DIR, "02_knowledge", "frameworks", filename)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ 已添加: {path}")
    return path

def add_insight():
    """添加洞见"""
    print("\n💭 添加思想洞见")
    print("=" * 50)
    
    title = input_with_default("标题")
    source = input_with_default("来源书籍")
    content = input_with_default("核心内容")
    detail = input_multiline("详细分析")
    
    content_full = f"""# {title}

> 思想洞见 · 来自《{source}》
> 添加于 {datetime.now().strftime('%Y-%m-%d')}

---

## 核心内容

{content}

---

## 详细分析

{detail if detail else '（待补充）'}

---

## 启示

- （待总结）

---

## 标签

```
待添加
```

---

## 相关内容

- 概念: （待添加）
- 框架: （待添加）
- 研究: （待添加）

---

*手动添加*
"""
    
    # 保存
    filename = f"{title}.md"
    path = os.path.join(DOCS_DIR, "02_knowledge", "insights", filename)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content_full)
    
    print(f"\n✅ 已添加: {path}")
    return path

def add_essay():
    """添加随笔"""
    print("\n✍️ 添加评论随笔")
    print("=" * 50)
    
    title = input_with_default("标题")
    source = input_with_default("来源书籍")
    content = input_multiline("正文")
    
    content_full = f"""# {title}

> 读《{source}》有感
> 添加于 {datetime.now().strftime('%Y-%m-%d')}

---

{content if content else '（待撰写）'}

---

**Tags:** 待添加

---

*手动添加*
"""
    
    # 保存
    filename = f"{title}.md"
    path = os.path.join(DOCS_DIR, "04_outputs", "essays", filename)
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content_full)
    
    print(f"\n✅ 已添加: {path}")
    return path

def deploy_site():
    """部署网站"""
    print("\n🚀 部署网站...")
    print("=" * 50)
    
    os.chdir(os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs"))
    
    import subprocess
    
    # 构建
    print("📦 构建网站...")
    result = subprocess.run(["python3", "-m", "mkdocs", "build", "--clean"], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ 构建失败: {result.stderr}")
        return
    
    # 部署
    print("🚀 部署到GitHub...")
    result = subprocess.run(["python3", "-m", "mkdocs", "gh-deploy", "--force"], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ 部署失败: {result.stderr}")
        return
    
    print("\n✅ 部署完成!")
    print("🌐 网站地址: https://lxz-123435.github.io/research-knowledge-base/")

def main():
    print("=" * 50)
    print("   手动添加模块 - 研究知识库")
    print("=" * 50)
    
    while True:
        print("\n请选择要添加的内容类型:")
        print("  1. 📚 书籍")
        print("  2. 📝 阅读笔记")
        print("  3. 💡 概念")
        print("  4. 🗂️ 分析框架")
        print("  5. 💭 思想洞见")
        print("  6. ✍️ 评论随笔")
        print("  7. 🚀 部署网站")
        print("  0. 🚪 退出")
        
        choice = input("\n选择: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            add_note()
        elif choice == "3":
            add_concept()
        elif choice == "4":
            add_framework()
        elif choice == "5":
            add_insight()
        elif choice == "6":
            add_essay()
        elif choice == "7":
            deploy_site()
        elif choice == "0":
            print("\n再见!")
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    main()
