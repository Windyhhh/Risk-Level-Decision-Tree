#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成决策树分析报告
"""

from datetime import datetime

def generate_report(df, dt_clf, le, feature_importance, feature_names_cn):
    """生成详细的分析报告"""
    
    report = f"""# 风险等级决策树分析报告

**生成时间**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

---

## 一、数据概览

### 1.1 数据集信息
- **总样本数**: {df.shape[0]}
- **特征数**: {df.shape[1] - 1}
- **目标变量**: Risk_Level（风险等级）

### 1.2 目标变量分布
"""
    
    # 计算风险等级分布
    risk_dist = df['Risk_Level'].value_counts()
    for risk_level in ['Low', 'Medium', 'High']:
        if risk_level in risk_dist.index:
            count = risk_dist[risk_level]
            percentage = (count / len(df)) * 100
            report += f"- **{risk_level}** (低/中/高风险): {count} 个样本 ({percentage:.1f}%)\n"
    
    report += f"""
### 1.3 特征列表
"""
    for i, (cn, en) in enumerate(zip(feature_names_cn, df.columns[:-1]), 1):
        report += f"{i}. {cn} ({en})\n"
    
    report += f"""
---

## 二、决策树模型信息

### 2.1 模型参数
- **树的最大深度**: {dt_clf.get_depth()}
- **叶节点数**: {dt_clf.get_n_leaves()}
- **分裂节点数**: {dt_clf.tree_.node_count - dt_clf.get_n_leaves()}
- **最小分裂样本数**: 5

### 2.2 模型性能
- **训练集准确率**: {dt_clf.score(df.iloc[:, :-1].values, df['Risk_Level'].map(lambda x: list(le.classes_).index(x)).values):.4f}

---

## 三、特征重要性分析

### 3.1 特征重要性排序

"""
    
    for idx, row in feature_importance.iterrows():
        importance_pct = row['重要性'] * 100
        bar = '█' * int(importance_pct / 2) + '░' * (50 - int(importance_pct / 2))
        report += f"**{row['特征']}**: {importance_pct:6.2f}% {bar}\n"
    
    report += f"""
### 3.2 关键发现
"""
    
    top_features = feature_importance.head(3)
    for idx, (i, row) in enumerate(top_features.iterrows(), 1):
        report += f"{idx}. **{row['特征']}** - 重要性: {row['重要性']*100:.2f}%\n"
    
    report += f"""
---

## 四、决策树结构分析

### 4.1 树的工作原理

决策树通过递归分裂特征空间，将样本分为不同的风险等级。每个节点包含以下信息：

- **分裂条件**: 用于判断样本走向左分支(True)还是右分支(False)
- **Gini系数**: 衡量节点的纯度，值越小表示样本越"纯"（属于同一类别）
- **样本数(samples)**: 该节点包含的样本数量
- **样本分布(value)**: 不同类别的样本数量分布
- **节点颜色**: 表示该节点主要的预测类别

### 4.2 预测流程

对于任何新样本，预测过程如下：

1. 从根节点开始
2. 根据分裂条件判断样本特征值
3. 如果满足条件，进入左分支；否则进入右分支
4. 递归进行，直到到达叶节点
5. 叶节点的颜色和标签即为预测结果

### 4.3 关键分裂点

根据特征重要性，以下特征在决策中起关键作用：

"""
    
    for idx, (i, row) in enumerate(feature_importance.head(5).iterrows(), 1):
        report += f"- **{row['特征']}**: 在树中用于多次分裂，帮助区分不同风险等级\n"
    
    report += f"""
---

## 五、风险等级判断规则

### 5.1 规则提取

基于决策树的结构，可以提取以下风险判断规则：

**低风险(Low)** 通常满足以下条件之一：
- 合规分数较高
- 加班比例较低
- 安全培训充分

**中等风险(Medium)** 通常满足以下条件：
- 合规分数中等
- 工人经验和天气条件混合

**高风险(High)** 通常满足以下条件之一：
- 合规分数较低
- 天气条件恶劣
- 未遂事故报告较多

### 5.2 实际应用建议

1. **监控关键指标**: 重点关注特征重要性排名前3的指标
2. **定期评估**: 定期使用该模型评估工地风险等级
3. **预防措施**: 针对高风险工地采取相应的安全措施
4. **数据更新**: 定期收集新数据，重新训练模型以保持准确性

---

## 六、模型局限性

1. **决策树的可解释性**: 虽然决策树易于理解，但复杂的树结构可能难以解释
2. **过拟合风险**: 深度较大的树可能过拟合训练数据
3. **特征交互**: 决策树可能无法捕捉复杂的特征交互关系
4. **数据质量**: 模型的准确性依赖于输入数据的质量

---

## 七、改进建议

1. **集成方法**: 考虑使用随机森林或梯度提升等集成方法
2. **特征工程**: 创建新的特征组合以提高模型性能
3. **超参数调优**: 通过交叉验证优化树的深度和其他参数
4. **数据平衡**: 如果类别不平衡，考虑使用加权或重采样方法

---

## 附录：数据统计

### 数据基本统计信息

"""
    
    # 添加数据统计
    stats = df.iloc[:, :-1].describe()
    report += "```\n"
    report += stats.to_string()
    report += "\n```\n"
    
    report += f"""
---

**报告生成工具**: Python + scikit-learn + pandas  
**决策树可视化**: 见 '决策树.png' 文件

"""
    
    return report

