#!/bin/bash
# Build and deploy to GitHub Pages (gh-pages branch)
set -e

cd "$(dirname "$0")"

echo "Building site..."
python3 build.py

echo ""
echo "Deploying to gh-pages..."
cd output

git init
git checkout -b gh-pages
git add -A
git commit -m "Deploy $(date +%Y-%m-%d)"
git remote add origin https://github.com/romelikethecity/b2bsalestools.git
git push --force origin gh-pages

# Clean up temp git repo in output
rm -rf .git

echo ""
echo "Deployed to gh-pages. Site will be live at b2bsalestools.com shortly."
