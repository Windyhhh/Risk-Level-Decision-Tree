<div align="center">

# 施工安全风险评估 | Risk-Level-Decision-Tree

### Decision-tree construction-safety risk assessment.

Predict worksite safety risk levels from 8 key features — interpretable, fast, and report-ready.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

</div>

---

**Risk-Level-Decision-Tree** builds a decision-tree model that automatically grades **construction-worksite safety risk** from **8 key features** — with high interpretability (4-level tree), millisecond-level inference, and automated report generation.

> [!NOTE]
> 中文项目：工地安全风险等级智能评估——决策树分类，8 特征预测风险等级，可解释、毫秒级、自动出报告。

---

## Features

- **Decision-tree classification** — grades risk from 8 features.
- **Interpretable** — shallow 4-level tree, easy to audit.
- **Real-time** — millisecond inference.
- **Report generation** — automated analysis reports + tree visualization.
- **Balanced dataset** — 200 samples, ~equal low/mid/high risk distribution (66.5% train accuracy).

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Risk-Level-Decision-Tree.git
cd Risk-Level-Decision-Tree

pip install -r requirements.txt

python main.py              # run the full analysis
python generate_report.py   # produce the report
```

---

## Project Structure

```
Risk-Level-Decision-Tree/
├── main.py                    # entry
├── decision_tree_analysis.py  # model training
├── generate_report.py         # report + tree image
├── 数据.xlsx                  # worksite data
└── 决策树.png / 决策树分析报告.md
```

---

## License

MIT — free to use, modify and distribute.
