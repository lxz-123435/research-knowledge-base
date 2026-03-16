#!/bin/bash
# 自动部署脚本
# 添加内容后自动部署到网站

cd ~/.openclaw/workspace/research-knowledge-base-mkdocs

echo "📦 部署网站..."

# 构建并部署
python3 -m mkdocs build --clean
python3 -m mkdocs gh-deploy --force

echo "✅ 部署完成!"
echo "🌐 网站地址: https://lxz-123435.github.io/research-knowledge-base/"
