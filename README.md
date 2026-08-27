<div align="center">

# ⛑️ Risk-Level-Decision-Tree

### Construction-safety risk assessment with decision trees.

Multi-factor risk classification, tree visualization and report generation.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

</div>

---

**Risk-Level-Decision-Tree** classifies **construction-safety risk levels** with a decision tree — multi-factor analysis, tree visualization and automatic report generation.

> [!NOTE]
> 中文项目：施工安全风险评估——决策树分类评估，多因子分析，树可视化，报告生成。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Risk-Level-Decision-Tree.git
cd Risk-Level-Decision-Tree

pip install -r requirements.txt

# run the full analysis
python main.py

# generate the report
python generate_report.py
```

Data (`数据.xlsx`) and outputs (tree figure, report) are included.

---

## Features

- **Decision-tree classification** — risk-level prediction.
- **Multi-factor** — analyze multiple risk factors.
- **Report generation** — automated reports + tree visualization.

---

## Project Structure

```
Risk-Level-Decision-Tree/
├── main.py                    # entry
├── decision_tree_analysis.py # analysis
├── generate_report.py        # report
├── 数据.xlsx                  # input data
└── 决策树.png / 决策树分析报告.md
```

---

## License

MIT — free to use, modify and distribute.
