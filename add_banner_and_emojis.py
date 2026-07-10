import os
import re

# 1. Create SVG Banner
os.makedirs("assets", exist_ok=True)
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#8A2BE2;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#4B0082;stop-opacity:1" />
      <animate attributeName="x1" values="0%;100%;0%" dur="5s" repeatCount="indefinite" />
      <animate attributeName="x2" values="100%;0%;100%" dur="5s" repeatCount="indefinite" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" rx="15" ry="15"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white">
    Awesome Multimodal LLMs
  </text>
  <circle cx="10%" cy="50%" r="15" fill="white" opacity="0.6">
    <animate attributeName="r" values="10;20;10" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="90%" cy="50%" r="15" fill="white" opacity="0.6">
    <animate attributeName="r" values="20;10;20" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>"""

with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

# 2. Add emojis and banner to README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Add banner at the top if not already there
if "![Banner]" not in content:
    content = re.sub(r'# Awesome-Multimodal-Large-Language-Models', 
                     '![Banner](assets/banner.svg)\n\n# 🚀 Awesome-Multimodal-Large-Language-Models', 
                     content)

# Replace headers with emojis
content = re.sub(r'## Multimodal Large Language Models', r'## 🧠 Multimodal Large Language Models', content)
content = re.sub(r'## 1\. The Macro Chronological Evolution', r'## 🕰️ 1. The Macro Chronological Evolution', content)
content = re.sub(r'## 2\. Core Functional & Architectural Variants', r'## 🏗️ 2. Core Functional & Architectural Variants', content)
content = re.sub(r'## 3\. The Multi-Modal Ingestion & Caching Matrix', r'## ⚡ 3. The Multi-Modal Ingestion & Caching Matrix', content)
content = re.sub(r'## 4\. Production Engineering Challenges & Hardening Mitigations', r'## 🛡️ 4. Production Engineering Challenges & Hardening Mitigations', content)
content = re.sub(r'## 5\. Frontier Real-World AI Infrastructure Applications', r'## 🌍 5. Frontier Real-World AI Infrastructure Applications', content)
content = re.sub(r'## References', r'## 📚 References', content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
