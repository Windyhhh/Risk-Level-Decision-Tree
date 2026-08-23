#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
决策树分析脚本
根据数据.xlsx生成决策树模型，并输出分析报告
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import matplotlib
import os
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
print(f"✓ 列名: {list(df.columns)}")

# =================== 数据预处理 ===================
print("\n【第二步】数据预处理...")
feature_columns = ['Num_Workers_On_Site', 'Avg_Experience_Years', 'Weather_Severity_Index', 
                   'Equipment_Age_Years', 'Safety_Training_Hours_Year', 'Near_Miss_Reports_Last_Month', 
                   'Overtime_Ratio', 'Compliance_Score']

X = df[feature_columns].values
y = df['Risk_Level'].values

# 编码目标变量
le = LabelEncoder()
y_encoded = le.fit_transform(y)

print(f"✓ 特征数: {X.shape[1]}")
print(f"✓ 样本数: {X.shape[0]}")
print(f"✓ 目标变量分布: {dict(zip(le.classes_, [sum(y_encoded==i) for i in range(len(le.classes_))]))}")

# =================== 训练决策树 ===================
print("\n【第三步】训练决策树...")
dt_clf = tree.DecisionTreeClassifier(max_depth=4, random_state=42, min_samples_split=5)
model = dt_clf.fit(X, y_encoded)
print(f"✓ 决策树训练完成!")
print(f"✓ 树的深度: {dt_clf.get_depth()}")
print(f"✓ 叶节点数: {dt_clf.get_n_leaves()}")

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

# 保存图片
try:
    plt.savefig('决策树.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ 决策树已保存为 '决策树.png'")
except Exception as e:
    print(f"⚠ 保存图片时出错: {e}")

plt.close()

# =================== 生成分析报告 ===================
print("\n【第六步】生成分析报告...")
report = generate_report(df, dt_clf, le, feature_importance, feature_names_cn)
with open('决策树分析报告.md', 'w', encoding='utf-8') as f:
    f.write(report)
print("✓ 分析报告已保存为 '决策树分析报告.md'")

print("\n" + "="*50)
print("✓ 所有处理完成！")
print("="*50)

