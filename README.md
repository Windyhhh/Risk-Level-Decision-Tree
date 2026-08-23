# ⚠️ Risk Level Decision Tree | 风险等级决策树分析系统

> **Intelligent construction site safety risk assessment using decision tree classification. Automatically classify risk levels (low/medium/high) based on multiple safety factors, with tree visualization and report generation.**
>
> 基于决策树分类的工地安全智能风险评估。根据多维度安全因素自动分类风险等级（低/中/高），含决策树可视化和报告生成。

---

## 🌟 Features | 核心特性

- **Decision Tree Classification** — CART algorithm for risk level prediction
- **Construction Site Safety** — Tailored for construction safety assessment
- **Multi-factor Analysis** — Multiple safety indicators as input features
- **Tree Visualization** — Graphviz-based decision tree diagram
- **Report Generation** — Automated analysis report with interpretation
- **Excel Data Support** — Load data from .xlsx files
- **Risk Levels** — Low / Medium / High classification

---

## 📁 Project Structure | 项目结构

```
Risk-Level-Decision-Tree/
├── main.py                        # Main entry point
├── decision_tree_analysis.py      # Core decision tree analysis
├── generate_report.py             # Report generation
├── 数据.xlsx                       # Input data (Excel)
├── 决策树.png                      # Decision tree visualization
├── 决策树分析报告.md               # Analysis report
├── 决策树分析结果.txt              # Analysis results
├── 决策树分析解读.txt              # Interpretation
├── 决策树项目完整文档.txt          # Complete documentation
├── 快速参考指南.md                 # Quick reference
├── 执行总结.md                     # Execution summary
├── 项目完成总结.txt                # Project completion summary
├── 风险等级决策树分析系统爆款博客.md
├── 📖_文件索引.md
├── 参考.txt
└── README.md
```

---

## 🚀 Quick Start | 快速开始

```bash
pip install pandas numpy scikit-learn matplotlib graphviz openpyxl

# Run full analysis
python main.py

# Run decision tree analysis only
python decision_tree_analysis.py

# Generate report
python generate_report.py
```

---

## 🔬 Methodology | 方法

1. **Data Loading** — Load construction safety data from Excel
2. **Preprocessing** — Encode categorical variables, handle missing values
3. **Feature Selection** — Identify key safety risk factors
4. **Model Training** — Train CART decision tree classifier
5. **Evaluation** — Accuracy, precision, recall, F1-score
6. **Visualization** — Export decision tree as PNG
7. **Report** — Generate detailed analysis report

---

## 📊 Risk Levels | 风险等级

| Level | Description | Action |
|-------|-------------|--------|
| 🟢 Low | Safe conditions | Normal monitoring |
| 🟡 Medium | Potential hazards | Increased inspection |
| 🔴 High | Imminent danger | Immediate intervention |

---

## 📄 License | 许可证

MIT License.

---

<div align="center">

**Built with ⚠️ for construction safety intelligence**

[GitHub](https://github.com/Windyhhh/Risk-Level-Decision-Tree)

</div>
