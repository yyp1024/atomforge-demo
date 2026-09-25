# -*- coding: utf-8 -*-
"""抽取 HTML 内联 <script> 到临时 .js，供 `node --check` 做语法校验。

用法: python scripts/check-js.py [html_path]
默认检查同目录 index.html，输出 _check.js（可删）。
"""
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\55556\Doubao\chats\2026-09-26\new-chat\atoms-demo\index.html"
out_path = r"C:\Users\55556\Doubao\chats\2026-09-26\new-chat\atoms-demo\_check.js"

with open(path, encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(scripts))
print("script blocks:", len(scripts), "chars:", sum(len(s) for s in scripts))
