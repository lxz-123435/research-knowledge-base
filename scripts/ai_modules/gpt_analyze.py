#!/usr/bin/env python3
"""
GPT 深度分析模块
功能：调用GPT API进行深度知识分析
"""

import os
import sys
import json
import re

# 配置
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
DOCS_DIR = os.path.expanduser("~/.openclaw/workspace/research-knowledge-base-mkdocs/docs")

def call_gpt(prompt, model="gpt-3.5-turbo"):
    """调用GPT API"""
    if not OPENAI_API_KEY:
        return None, "未设置 OPENAI_API_KEY"
    
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
        
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一个知识管理专家，擅长从书籍和资料中提取洞见。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content, None
    except Exception as e:
        return None, str(e)

def extract_text_from_pdf(pdf_path, max_pages=5):
    """从PDF提取文本"""
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i, page in enumerate(reader.pages[:max_pages]):
                text += page.extract_text() + "\n"
            return text[:8000]  # 限制长度
    except Exception as e:
        return f"Error: {e}"

def generate_deep_insight(book_name, text):
    """生成深度洞见"""
    prompt = f"""请分析以下书籍内容，提取深度的思想洞见。

书名：{book_name}

内容摘要：
{text}

请按以下格式输出思想洞见：

## 一、核心问题
这本书试图回答什么问题？（列出3-5个）

## 二、核心观点
作者的主要观点是什么？（列出3-5个）

## 三、时代背景
这个故事发生在什么时代？有什么特点？

## 四、人物特质
主人公有什么独特的性格特质？

## 五、当代启示
这个故事对今天有什么启示？（分点列出）

## 六、一句话总结
用一句话概括这本书的核心洞见。
"""
    
    return call_gpt(prompt)

def generate_concepts(book_name, text):
    """提取概念"""
    prompt = f"""请从以下书籍中提取3-5个关键概念。

书名：{book_name}

内容：
{text[:5000]}

请为每个概念给出：
1. 概念名称
2. 一句话定义
3. 相关的关键词

用JSON格式输出：
[
  {{"name": "概念1", "definition": "定义", "keywords": ["关键词1", "关键词2"]}},
  ...
]
"""
    
    result, error = call_gpt(prompt)
    if error:
        return None, error
    
    # 尝试解析JSON
    try:
        # 提取JSON部分
        json_match = re.search(r'\[.*\]', result, re.DOTALL)
        if json_match:
            concepts = json.loads(json_match.group())
            return concepts, None
    except:
        pass
    
    return result, None

def generate_framework(book_name, text):
    """生成分析框架"""
    prompt = f"""请为以下书籍生成一个分析框架。

书名：{book_name}

内容摘要：
{text[:5000]}

请输出一个分析框架，包含：
1. 框架名称
2. 核心理论
3. 分析维度（3-5个）
4. 每个维度的关键问题
"""
    
    return call_gpt(prompt)

def generate_essay(book_name, insight, concepts):
    """生成评论随笔"""
    concepts_text = "\n".join([f"- {c['name']}: {c['definition']}" for c in concepts]) if concepts else "无"
    
    prompt = f"""请根据以下洞见，撰写一篇评论随笔。

书名：{book_name}

核心洞见：
{insight}

关键概念：
{concepts_text}

要求：
1. 标题简洁有力
2. 结构：引入 → 展开 → 启示 → 结语
3. 融入个人思考
4. 字数800-1500字
5. 有温度、有深度
"""
    
    return call_gpt(prompt)

def process_with_gpt(pdf_path, generate_essay_flag=False):
    """使用GPT处理书籍"""
    filename = os.path.basename(pdf_path)
    book_name = os.path.splitext(filename)[0]
    
    print(f"📖 使用GPT深度分析: {book_name}")
    
    # 1. 提取文本
    print("  → 提取文本...")
    text = extract_text_from_pdf(pdf_path)
    
    if text.startswith("Error"):
        print(f"  ❌ 文本提取失败: {text}")
        return
    
    # 2. 生成深度洞见
    print("  → 生成深度洞见...")
    insight, error = generate_deep_insight(book_name, text)
    if error:
        print(f"  ⚠️ 洞见生成失败: {error}")
        insight = "# 思想洞见\n\n（待GPT分析）"
    
    # 3. 提取概念
    print("  → 提取关键概念...")
    concepts, error = generate_concepts(book_name, text)
    if error:
        print(f"  ⚠️ 概念提取失败: {error}")
        concepts = []
    
    # 4. 生成分析框架
    print("  → 生成分析框架...")
    framework, error = generate_framework(book_name, text)
    if error:
        print(f"  ⚠️ 框架生成失败: {error}")
        framework = "# 分析框架\n\n（待GPT分析）"
    
    # 5. 保存洞见
    insight_dir = os.path.join(DOCS_DIR, "02_knowledge", "insights")
    os.makedirs(insight_dir, exist_ok=True)
    
    insight_filename = f"GPT_{book_name[:20]}.md"
    insight_path = os.path.join(insight_dir, insight_filename)
    
    with open(insight_path, 'w', encoding='utf-8') as f:
        f.write(f"# {book_name} - 思想洞见\n\n")
        f.write(f"> GPT自动生成于 2026-03-15\n\n")
        f.write(insight)
    
    print(f"  ✅ 洞见已保存: {insight_path}")
    
    # 6. 保存框架
    framework_dir = os.path.join(DOCS_DIR, "02_knowledge", "frameworks")
    os.makedirs(framework_dir, exist_ok=True)
    
    framework_filename = f"GPT_{book_name[:20]}_framework.md"
    framework_path = os.path.join(framework_dir, framework_filename)
    
    with open(framework_path, 'w', encoding='utf-8') as f:
        f.write(f"# {book_name} - 分析框架\n\n")
        f.write(f"> GPT自动生成于 2026-03-15\n\n")
        f.write(framework)
    
    print(f"  ✅ 框架已保存: {framework_path}")
    
    # 7. 生成随笔（可选）
    if generate_essay_flag:
        print("  → 生成评论随笔...")
        essay, error = generate_essay(book_name, insight, concepts)
        if error:
            print(f"  ⚠️ 随笔生成失败: {error}")
        else:
            essay_dir = os.path.join(DOCS_DIR, "04_outputs", "essays")
            os.makedirs(essay_dir, exist_ok=True)
            
            essay_filename = f"GPT_{book_name[:20]}.md"
            essay_path = os.path.join(essay_dir, essay_filename)
            
            with open(essay_path, 'w', encoding='utf-8') as f:
                f.write(f"# {book_name} - 评论随笔\n\n")
                f.write(f"> GPT自动生成于 2026-03-15\n\n")
                f.write(essay)
            
            print(f"  ✅ 随笔已保存: {essay_path}")
    
    print("\n🎉 GPT分析完成!")
    
    return {
        "insight": insight_path,
        "framework": framework_path,
        "concepts": concepts
    }

def main():
    if not OPENAI_API_KEY:
        print("❌ 请先设置 OPENAI_API_KEY 环境变量")
        print("   export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)
    
    if len(sys.argv) < 2:
        print("📝 用法:")
        print("  python gpt_analyze.py <PDF文件>")
        print("  python gpt_analyze.py <PDF文件> --essay  # 同时生成随笔")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    generate_essay_flag = "--essay" in sys.argv
    
    if not os.path.exists(pdf_path):
        print(f"❌ 文件不存在: {pdf_path}")
        sys.exit(1)
    
    process_with_gpt(pdf_path, generate_essay_flag)

if __name__ == "__main__":
    main()
