import os
import re

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the 15 items with their details
items = [
    {
        "id": "fragmented-pipeline",
        "title": "The Fragmented Multi-Model Pipeline Era",
        "desc": "The early engineering standard where modalities were treated as isolated data islands. Chained models sequentially.",
        "year": "Pre-2021",
        "paper_link": "N/A"
    },
    {
        "id": "dual-tower-clip",
        "title": "The Dual-Tower Contrastive Alignment Era (CLIP)",
        "desc": "Sparked the modern multi-modal foundation boom by proving distinct modalities could share a single continuous vector space.",
        "year": "2021",
        "paper_link": "[Radford et al., 2021](https://arxiv.org/abs/2103.00020)"
    },
    {
        "id": "cross-attention-flamingo",
        "title": "The Connected Cross-Attention Adapter Era",
        "desc": "Injected visual perception directly into generative text decoding parameter lines (Flamingo / LLaVA).",
        "year": "2022",
        "paper_link": "[Alayrac et al., 2022](https://arxiv.org/abs/2204.14198)"
    },
    {
        "id": "unified-omni",
        "title": "The Unified Omni Autoregressive Token Era",
        "desc": "The current modern state-of-the-art foundation infrastructure standard seen in frontier systems.",
        "year": "2023-Present",
        "paper_link": "[OpenAI GPT-4o / Gemini](https://arxiv.org/abs/2312.11805)"
    },
    {
        "id": "mlp-adapter",
        "title": "MLP-Adapter Architectures",
        "desc": "Employs a simple, low-rank Multi-Layer Perceptron (MLP) or linear matrix to scale and project the terminal hidden states.",
        "year": "2023",
        "paper_link": "[LLaVA Paper](https://arxiv.org/abs/2304.08485)"
    },
    {
        "id": "perceptual-bottlenecks",
        "title": "Perceptual Cross-Attention Bottlenecks",
        "desc": "Decouples raw pixel token dimensions from the language model's hidden layers using cross-attention bottlenecks.",
        "year": "2021",
        "paper_link": "[Jaegle et al., 2021](https://arxiv.org/abs/2103.03206)"
    },
    {
        "id": "unified-native",
        "title": "Unified Native Transformers",
        "desc": "Completely merges data modalities at step zero. A single, unified multi-modal tokenizer.",
        "year": "2024",
        "paper_link": "[Chameleon Team, 2024](https://arxiv.org/abs/2405.09818)"
    },
    {
        "id": "sparse-moe",
        "title": "Sparsely Routed Multi-Modal MoE",
        "desc": "Combines multi-modal sequence ingestion with Mixture-of-Experts (MoE) layers.",
        "year": "2024",
        "paper_link": "[DeepSeek-V3, 2024](https://arxiv.org/abs/2412.19437)"
    },
    {
        "id": "linear-patch",
        "title": "Linear Patch Embedding Layers",
        "desc": "Slashes convolutional scaling constraints by applying a 2D convolution flattening local spatial pixel regions.",
        "year": "2020",
        "paper_link": "[Dosovitskiy et al., 2020](https://arxiv.org/abs/2010.11929)"
    },
    {
        "id": "mla-cache",
        "title": "Multi-Head Latent Attention",
        "desc": "Slashes inference VRAM overheads by compressing cache dimensions down into a low-rank latent vector.",
        "year": "2024",
        "paper_link": "[DeepSeek-V2, 2024](https://arxiv.org/abs/2405.04434)"
    },
    {
        "id": "quadratic-inflation",
        "title": "The Quadratic Token Inflation Wall",
        "desc": "Passing patches alongside long text prompts causes the self-attention matrix to hit a quadratic memory footprint wall.",
        "year": "2017",
        "paper_link": "[Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)"
    },
    {
        "id": "indirect-prompt-injection",
        "title": "Multi-Modal Indirect Prompt Injection",
        "desc": "Unified MLLMs process pixels and text tokens inside a shared attention space, creating vulnerabilities to hidden text commands.",
        "year": "2023",
        "paper_link": "[Bagdasaryan et al., 2023](https://arxiv.org/abs/2307.10490)"
    },
    {
        "id": "spatio-temporal-video",
        "title": "Spatio-Temporal Video Generative Flow-Matching",
        "desc": "Drives next-generation advanced cinematic pre-visualization and industrial simulation loops.",
        "year": "2024",
        "paper_link": "[Sora / OpenAI, 2024](https://openai.com/sora)"
    },
    {
        "id": "autonomous-bev",
        "title": "Autonomous Vehicle Bird's-Eye-View Actuation",
        "desc": "Coordinates real-time perception and navigation for advanced self-driving automotive fleets.",
        "year": "2022",
        "paper_link": "[BEVFormer, 2022](https://arxiv.org/abs/2203.17270)"
    },
    {
        "id": "clinical-diagnostic",
        "title": "High-Resolution Clinical Diagnostic Tracking",
        "desc": "Ingests massive multi-megapixel data matrices alongside conversational electronic health records.",
        "year": "2023",
        "paper_link": "[Moor et al., 2023](https://arxiv.org/abs/2303.13375)"
    }
]

# Create detail pages
os.makedirs("pages", exist_ok=True)
for item in items:
    page_content = f"""# {item['title']}

## Overview
{item['desc']}

**Year:** {item['year']}
**First Paper:** {item['paper_link']}

## Architecture Diagram
```mermaid
flowchart TD
    A[Input Modalities] --> B[{item['title']}]
    B --> C[Unified Output]
```

## Detailed Information
This page provides an in-depth look at {item['title']}. (Detailed content goes here).
[Back to README](../README.md)
"""
    with open(f"pages/{item['id']}.md", "w", encoding="utf-8") as f:
        f.write(page_content)

# Replace bullets in README with tables
section1_table = "| Era / Concept | Description | Year | Paper Link |\n| --- | --- | --- | --- |\n"
for i in range(0, 4):
    section1_table += f"| [{items[i]['title']}](pages/{items[i]['id']}.md) | {items[i]['desc']} | {items[i]['year']} | {items[i]['paper_link']} |\n"

section2_table = "| Variant | Mechanism / Description | Year | Paper Link |\n| --- | --- | --- | --- |\n"
for i in range(4, 8):
    section2_table += f"| [{items[i]['title']}](pages/{items[i]['id']}.md) | {items[i]['desc']} | {items[i]['year']} | {items[i]['paper_link']} |\n"

section3_table = "| Layer / Concept | Profile | Year | Paper Link |\n| --- | --- | --- | --- |\n"
for i in range(8, 10):
    section3_table += f"| [{items[i]['title']}](pages/{items[i]['id']}.md) | {items[i]['desc']} | {items[i]['year']} | {items[i]['paper_link']} |\n"

section4_table = "| Challenge | Problem & Mitigation | Year | Paper Link |\n| --- | --- | --- | --- |\n"
for i in range(10, 12):
    section4_table += f"| [{items[i]['title']}](pages/{items[i]['id']}.md) | {items[i]['desc']} | {items[i]['year']} | {items[i]['paper_link']} |\n"

section5_table = "| Application | Details | Year | Paper Link |\n| --- | --- | --- | --- |\n"
for i in range(12, 15):
    section5_table += f"| [{items[i]['title']}](pages/{items[i]['id']}.md) | {items[i]['desc']} | {items[i]['year']} | {items[i]['paper_link']} |\n"

# Regex replacements
import re

# Section 1
content = re.sub(r'\*   \*\*The Fragmented Multi-Model Pipeline Era.*?(?=\n---)', section1_table + '\n', content, flags=re.DOTALL)

# Section 2
content = re.sub(r'- ### A\. MLP-Adapter Architectures.*?(?=\n---)', section2_table + '\n', content, flags=re.DOTALL)

# Section 3
content = re.sub(r'\*   \*\*Linear Patch Embedding Layers.*?(?=\n---)', section3_table + '\n', content, flags=re.DOTALL)

# Section 4
content = re.sub(r'- ### The Quadratic Token Inflation.*?(?=\n---)', section4_table + '\n', content, flags=re.DOTALL)

# Section 5
content = re.sub(r'\*   \*\*Spatio-Temporal Video Generative.*?(?=\n---)', section5_table + '\n', content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
