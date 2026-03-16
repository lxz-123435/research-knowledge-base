#!/bin/bash
# Research OS 一键部署脚本

cd ~/.openclaw/workspace/research-knowledge-base-mkdocs

echo "📦 添加所有更改..."
git add .

echo "📝 请输入提交信息（直接回车使用默认信息）:"
read commit_msg
if [ -z "$commit_msg" ]; then
  commit_msg="update: $(date '+%Y-%m-%d %H:%M')"
fi

echo "🔄 提交更改: $commit_msg"
git commit -m "$commit_msg"

echo "🚀 推送到GitHub..."
git push

echo "✅ 已推送！GitHub Actions将自动构建并部署网站。"
echo "📄 等待约30秒后访问: https://lxz-123435.github.io/research-knowledge-base/"
