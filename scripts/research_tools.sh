#!/bin/bash
# 研究知识库自动化工具
# 功能：一键运行所有AI模块

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AI_MODULES="$SCRIPT_DIR/ai_modules"

echo "========================================="
echo "   研究知识库 AI 工具箱"
echo "========================================="
echo ""

# 显示菜单
show_menu() {
    echo "请选择功能:"
    echo ""
    echo "1. AI提取 - 从PDF自动提取知识"
    echo "2. 知识图谱 - 生成概念关联图谱"
    echo "3. 研究综述 - 生成主题研究综述"
    echo "4. 写作模板 - 生成文章框架"
    echo "5. 一键部署 - 部署网站"
    echo "0. 退出"
    echo ""
}

# 主菜单
while true; do
    show_menu
    read -p "请选择 (0-5): " choice
    
    case $choice in
        1)
            echo ""
            read -p "请输入PDF文件路径: " pdf_path
            if [ -f "$pdf_path" ]; then
                python3 "$AI_MODULES/ai_extract.py" "$pdf_path"
            else
                echo "文件不存在: $pdf_path"
            fi
            ;;
        2)
            echo ""
            echo "生成知识图谱..."
            python3 "$AI_MODULES/knowledge_graph.py"
            ;;
        3)
            echo ""
            read -p "请输入研究主题: " topic
            if [ -n "$topic" ]; then
                python3 "$AI_MODULES/research_summary.py" "$topic"
            fi
            ;;
        4)
            echo ""
            read -p "请输入主题: " topic
            echo "选择文章类型:"
            echo "1. 论文"
            echo "2. 报告"
            echo "3. 评论"
            read -p "请选择 (1-3): " type
            
            case $type in
                1) article_type="论文" ;;
                2) article_type="报告" ;;
                3) article_type="评论" ;;
                *) article_type="论文" ;;
            esac
            
            python3 "$AI_MODULES/write_template.py" "$topic" "$article_type"
            ;;
        5)
            echo ""
            echo "部署网站..."
            cd ~/.openclaw/workspace/research-knowledge-base-mkdocs
            python3 -m mkdocs build --clean
            python3 -m mkdocs gh-deploy --force
            echo "✅ 部署完成!"
            ;;
        0)
            echo "再见!"
            exit 0
            ;;
        *)
            echo "无效选择，请重试"
            ;;
    esac
    
    echo ""
    echo "-----------------------------------------"
    echo ""
done
