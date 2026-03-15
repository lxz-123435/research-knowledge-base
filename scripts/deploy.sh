#!/bin/bash
# 自动部署脚本
# 用法: ./deploy.sh

set -e

echo "========================================="
echo "   研究资料库自动部署脚本"
echo "========================================="

# 进入项目目录
cd ~/.openclaw/workspace/research-knowledge-base-mkdocs

# 1. 构建网站
echo "[1/3] 构建网站..."
python3 -m mkdocs build --clean

# 2. 部署到GitHub Pages
echo "[2/3] 部署到GitHub Pages..."
python3 -m mkdocs gh-deploy --force

# 3. 完成
echo "[3/3] 完成!"
echo ""
echo "网站已更新: https://lxz-123435.github.io/research-knowledge-base/"
echo "========================================="
