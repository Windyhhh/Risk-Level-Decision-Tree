#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
决策树分析主程序
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import matplotlib
from datetime import datetime

# =================== 设置中文字体 ===================
try:
    matplotlib.font_manager.fontManager.addfont("C:\\Windows\\Fonts\\simhei.ttf")
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    print("✓ 使用SimHei字体")
except:
    try:
        matplotlib.font_manager.fontManager.addfont("/System/Library/Fonts/PingFang.ttc")
        matplotlib.rcParams['font.sans-serif'] = ['PingFang SC']
        matplotlib.rcParams['axes.unicode_minus'] = False
        print("✓ 使用PingFang SC字体")
    except:
        print("⚠ 未找到中文字体，使用默认字体")

# =================== 读取数据 ===================
print("\n【第一步】读取数据...")
df = pd.read_excel('数据.xlsx', sheet_name='Sheet1')
print(f"✓ 数据加载成功: {df.shape[0]} 行, {df.shape[1]} 列")

# =================== 数据预处理 ===================
print("\n【第二步】数据预处理...")
feature_columns = ['Num_Workers_On_Site', 'Avg_Experience_Years', 'Weather_Severity_Index', 
                   'Equipment_Age_Years', 'Safety_Training_Hours_Year', 'Near_Miss_Reports_Last_Month', 
                   'Overtime_Ratio', 'Compliance_Score']

X = df[feature_columns].values
y = df['Risk_Level'].values

le = LabelEncoder()
y_encoded = le.fit_transform(y)

print(f"✓ 特征数: {X.shape[1]}, 样本数: {X.shape[0]}")
risk_counts = {cls: sum(y_encoded==i) for i, cls in enumerate(le.classes_)}
print(f"✓ 目标变量分布: {risk_counts}")

# =================== 训练决策树 ===================
print("\n【第三步】训练决策树...")
dt_clf = tree.DecisionTreeClassifier(max_depth=4, random_state=42, min_samples_split=5)
model = dt_clf.fit(X, y_encoded)
print(f"✓ 树的深度: {dt_clf.get_depth()}, 叶节点数: {dt_clf.get_n_leaves()}")

# =================== 特征重要性 ===================
print("\n【第四步】特征重要性分析...")
feature_importance = pd.DataFrame({
    '特征': feature_columns,
    '重要性': dt_clf.feature_importances_
}).sort_values('重要性', ascending=False)
print(feature_importance.to_string(index=False))

# =================== 绘制决策树 ===================
print("\n【第五步】绘制决策树...")
feature_names_cn = ['现场工人数', '平均经验年数', '天气严重指数', 
                   '设备年龄年数', '安全培训小时数', '上月未遂事故报告数', 
                   '加班比例', '合规分数']

plt.figure(figsize=(24, 14))
tree.plot_tree(dt_clf, 
               feature_names=feature_names_cn, 
               class_names=list(le.classes_), 
               filled=True, 
               rounded=True,
               fontsize=10,
               proportion=True)

plt.title("风险等级决策树 (Risk Level Decision Tree)", fontsize=18, pad=20, weight='bold')
plt.tight_layout()

try:
    plt.savefig('决策树.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ 决策树已保存为 '决策树.png'")
except Exception as e:
    print(f"⚠ 保存图片时出错: {e}")

plt.close()

# =================== 生成分析报告 ===================
print("\n【第六步】生成分析报告...")

report = f"""# 风险等级决策树分析报告

**生成时间**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

---

## 一、数据概览

### 1.1 数据集信息
- **总样本数**: {df.shape[0]}
- **特征数**: {len(feature_columns)}
- **目标变量**: Risk_Level（风险等级）

### 1.2 目标变量分布
"""

for risk_level in ['Low', 'Medium', 'High']:
    count = risk_counts.get(risk_level, 0)
    percentage = (count / len(df)) * 100
    report += f"- **{risk_level}**: {count} 个样本 ({percentage:.1f}%)\n"

report += f"""
---

## 二、决策树模型信息

### 2.1 模型参数
- **树的最大深度**: {dt_clf.get_depth()}
- **叶节点数**: {dt_clf.get_n_leaves()}
- **分裂节点数**: {dt_clf.tree_.node_count - dt_clf.get_n_leaves()}

### 2.2 特征重要性排序

"""

for idx, row in feature_importance.iterrows():
    importance_pct = row['重要性'] * 100
    report += f"- **{row['特征']}**: {importance_pct:.2f}%\n"

report += f"""
---

## 三、决策树工作原理

### 3.1 树的结构
- 每个节点代表一个分裂条件
- Gini系数表示节点的纯度（越小越纯）
- samples表示该节点的样本数
- value表示不同类别的样本分布

### 3.2 预测流程
1. 从根节点开始
2. 根据分裂条件判断样本特征
3. 满足条件进入左分支，否则进入右分支
4. 递归进行直到到达叶节点
5. 叶节点的颜色和标签即为预测结果

---

## 四、风险等级判断规则

### 4.1 关键特征
根据特征重要性，以下特征最重要：
"""

for idx, (i, row) in enumerate(feature_importance.head(3).iterrows(), 1):
    report += f"{idx}. **{row['特征']}** (重要性: {row['重要性']*100:.2f}%)\n"

report += f"""
### 4.2 应用建议
1. 重点监控特征重要性排名前3的指标
2. 定期使用该模型评估工地风险等级
3. 针对高风险工地采取相应的安全措施
4. 定期收集新数据，重新训练模型

---

## 五、模型性能

- **训练集准确率**: {dt_clf.score(X, y_encoded):.4f}
- **模型复杂度**: 中等（深度为{dt_clf.get_depth()}）

---

**详细决策树可视化**: 见 '决策树.png' 文件

"""

with open('决策树分析报告.md', 'w', encoding='utf-8') as f:
    f.write(report)
print("✓ 分析报告已保存为 '决策树分析报告.md'")

print("\n" + "="*50)
print("✓ 所有处理完成！")
print("="*50)
print("\n生成的文件:")
print("  1. 决策树.png - 决策树可视化")
print("  2. 决策树分析报告.md - 详细分析报告")

