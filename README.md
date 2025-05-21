[//]: # (# USB: A Comprehensive and Unified Safety Evaluation Benchmark for Multimodal Large Language Models)

<p align="center">
  <img src="image/title.png" width="800px"/>
</p>

<div align="center">
  <a href="#">📝 Paper</a> •
  <a href="https://huggingface.co/datasets/cgjacklin/USB/tree/main">🤗 Dataset</a> •
  <a href="https://anonymous.4open.science/r/USB-SafeBench-4EE3/README.md">💻 Code</a> •
  <a href="https://anonymous.4open.science/w/usb_for_leadboard_gitpage/">🏆 Leaderboard</a>
</div>

## 🔐 Introduction

USB is an advanced safety benchmark for Multimodal Large Language Models (MLLMs) that offers:

- **Modality**: 4 distinct modality combinations, encompassing all risk categories. USB-SafeBench includes: "Risky-Image/Risky-Text (RIRT)", "Risky-Image/Safe-Text (RIST)", "Safe-Image/Risky-Text (SIRT)", and "Safe-Image/Safe-Text (SIST)".
- **Category**: A hierarchical structure of 3 primary categories(National Safety、 Public Safety、Ethical Safety ), branching into 16 secondary categories and further expanding into 61 tertiary categories.
- **Language Coverage**: Comprehensive support for both English and Chinese languages.
- **Evaluation Domains**: Detailed assessment across vulnerability and sensitivity dimensions.

This refined architecture ensures a robust framework for assessing safety in MLLMs, enhancing both clarity and expressiveness of evaluation metrics.


## LeaderBoard

<p align="center">
  <img src="image/leaderboard.png" width="800px"/>
</p>

## Key Features

### 🎯 Comprehensive Coverage
- 4 modality combinations
- 3 major topics
- 16 secondary topics
- 61 fine-grained subtopics

### ✨ High Quality
- Rigorous quality control process
- Carefully curated dataset

### 🛡️ Adversarial Robustness
- Aggressive safety testing
- High attack success rates (ASR) against mainstream VLMs

## Structure

### Topics
- 3 Major Topics
- 16 Secondary Topics
- 61 Diverse Subtopics

### Modalities
- 4 risk-modality combinations

### Languages
- English
- Chinese

<p align="center">
  <img src="image/category_en.png" width="700px"/>
</p>

## Pipeline

<p align="center">
  <img src="image/overview.png" width="800px"/>
</p>

## Use Cases

USB-SafeBench is designed for:
- Evaluating MLLM safety
- Benchmarking security measures
- Improving model reliability
- Supporting safety research

This benchmark serves as an essential resource for developers and researchers working on enhancing MLLM security and reliability.

[//]: # (Please visit our [website]&#40;https://openstellarteam.github.io/ChineseSafetyQA/&#41;)
[//]: # (or check our [paper]&#40;https://arxiv.org/abs/2412.15265&#41; for more details.)
[//]: # (This is the evaluation repository for USB-SafeBench)
