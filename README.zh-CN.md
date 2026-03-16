<p align="right">
  <a href="./README.md"><img src="https://img.shields.io/badge/Language-English-blue" alt="English"></a>
  <a href="./README.zh-CN.md"><img src="https://img.shields.io/badge/语言-中文-red" alt="中文"></a>
</p>

# ARIS-GCA-Bees

一个关于**蜜蜂功能性自我意识**的计算神经行为学项目，通过 [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) 的自动化研究流程生成。

## 项目简介

本仓库汇集了一个理论驱动型计算研究项目的代码、图表、结果、过程记录与论文材料。项目提出了一个关于**蜜蜂功能性自我意识的统一预测编码模型**，见最终在线[汇总文档](https://cunyikang.github.io/ARIS-GCA-Bees/), 包含中英版本。

项目的核心观点是：在昆虫中央复合体（central complex, CX）中，如果用一个共同的潜变量——**精度（precision）**——来表征预测编码过程，那么它可以同时解释四类行为表现：

- 元认知放弃行为（opt-out）
- 工具使用预期
- 与阶层角色相符的学习
- 一般认知能力（GCA）

## 核心问题

本项目试图回答：蜜蜂身上看似彼此分离的“自我相关”行为，能否由一个统一的计算原理来解释？

项目给出的答案是肯定的：

- **元认知表现与精度之间呈倒 U 型关系**
- **更高的一般认知能力，反而可能对应更差的元认知校准**
- **昼夜节律扰动可能使元认知–GCA 的相关方向发生翻转**

因此，本仓库更适合被理解为一个**理论 + 模拟**项目，其价值在于提出可检验的经验预测。

## 仓库结构

```text
ARIS-GCA-Bees/
├── code/                  # 模拟代码
├── figures/               # 图表生成脚本与导出图
├── paper/                 # 论文文件
├── process/               # 研究流程报告与评审记录
├── results/               # 数值模拟结果
├── README.md
└── README.zh-CN.md
```

## 关键文件

- `process/RESEARCH_PIPELINE_REPORT.md` —— 完整研究流程总结
- `code/experiment_r2_4domain.py` —— Round 2 主模拟脚本
- `figures/generate_figures.py` —— 图表生成脚本
- `paper/main.tex` —— 论文 LaTeX 主文件
- `paper/main.html` —— 论文 HTML 版本

## 项目亮点

- 以 **precision** 为核心参数的统一预测编码模型
- 对元认知最优点的解析推导
- 模拟得到的 **元认知–GCA 负相关**
- 在节律扰动条件下出现的 **符号翻转**
- 从想法生成、模拟、评审到成稿的完整研究链条

## 如何使用本仓库

### 1. 先理解项目逻辑

建议先阅读：

- [`ARIS项目`](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) 
- [`想法构建`](./process/IDEA_REPORT.md)
- [`自动审阅`](./process/AUTO_REVIEW.md)
- [`写作框架`](./process/PAPER_PLAN.md)
- [`研究流程`](./process/RESEARCH_PIPELINE_REPORT.md)

### 2. 运行主模拟

```bash
python code/experiment_r2_4domain.py
```

### 3. 生成图表

```bash
python figures/generate_figures.py
```

## 项目流程

本仓库遵循如下研究生成流程：

```text
想法发现
→ pilot 测试
→ 完整模拟
→ 自动评审循环
→ 论文规划
→ 论文撰写
```

## 当前状态

本项目当前处于**理论建模与模拟验证**阶段。  
它不是经验数据仓库。其主要价值在于：

- 概念形式化
- 计算统一解释
- 可证伪预测生成
- 面向论文写作的研究打包

## 论文

当前工作标题：

**A Unified Predictive Coding Account of Functional Self-Awareness in Bees: Analytically Derived Precision Trade-offs Across Four Behavioral Domains**

相关文件：

- [`HTML 介绍页面`](./docs/index.html)
- [`HTML 中文`](./docs/paper/zh/main.html)
- [`HTML 英文`](./docs/paper/en/main.html)


## 引用方式

若在正式发表前引用本仓库，可暂按如下方式引用：

```text
Kang, C. (2026). ARIS-GCA-Bees: A unified predictive coding account of functional self-awareness in bees. GitHub repository.
```

## 联系方式

维护者：**Cunyi Kang**

如有问题、建议或合作意向，欢迎在 GitHub 提交 issue。
