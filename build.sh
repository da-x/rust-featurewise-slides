#!/bin/bash

set -eu

npm install
npm run build

git rm -f .gitignore
git add -f *.html css dist js plugin
git commit -am "Prepare GH pages"
git branch -D gh-pages 2>/dev/null || true
git branch gh-pages HEAD
git reset --hard HEAD~1
