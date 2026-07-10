import os
import re

os.chdir(r"C:\Users\ishan\Documents\Projects\Awesome-Multimodal-Large-Language-Models")
readme_path = "README.md"
folder_name = os.path.basename(os.getcwd())

def git_commit(msg):
    os.system('git add .')
    os.system(f'git commit -m "{msg}"')
    os.system('git push')

# Step 1: Add emojis and banner (This is already done via the other script, I will just run it)
os.system('python add_banner_and_emojis.py')
git_commit("added emojis and banner")

# Step 2: SEO and Left Badges
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add SEO keywords/paragraph
seo_text = "\n\n*A curated list of awesome Multimodal Large Language Models (MLLMs), Vision-Language Models (VLMs), Omni-Models, and AI architectures integrating text, vision, and audio.*\n"

left_badges = '<p align="center">\n<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>\n<a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\n'

# Insert after title
content = re.sub(r'(# 🚀 Awesome-Multimodal-Large-Language-Models)', r'\1\n' + left_badges + '</p>\n' + seo_text, content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

git_commit("seo optimised and badges to left added")

# Step 3: Right Badges
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\n'
content = content.replace('</p>', right_badge + '</p>')

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

git_commit("badges to right added")

# Step 4: Star History
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

star_history = f"""
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2F{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

# Append at the bottom
if "## ⭐ Star History" not in content:
    content += star_history

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

git_commit("star history added")

# Step 5: Fix Star Plot (replace chartrepos with chart?repos)
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('chartrepos', 'chart?repos')

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

git_commit("fixed star plot")

# Step 6: Fix awesome link
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

git_commit("invalid awesome link fixed")
