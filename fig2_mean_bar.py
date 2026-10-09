#图表2：带均值线的销售量柱状图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 中文配置
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 数据
data = {
    "区域": ["华北", "华南", "东北", "西北", "西南", "华东"],
    "销售量": [2354, 1902, 3524, 2698, 2896, 2563]
}
df = pd.DataFrame(data)
mean_val = df["销售量"].mean()  # 计算均值

# 画布
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
fig.patch.set_facecolor('#192340')
ax.set_facecolor('#192340')

bar_width = 0.6
x_pos = np.arange(len(df["区域"]))

# 绘制柱状图
bars = ax.bar(x_pos, df["销售量"], width=bar_width, color="#0088ee")

# 绘制黄色均值水平线
ax.axhline(y=mean_val, color="#ffcc00", linestyle="-", linewidth=2)

# ========== 均值文字：线的右侧，向右偏移0.25，不遮挡华东柱子 ==========
ax.text(x_pos[-1] + 0.25, mean_val, f'均值：{mean_val:.0f}', color='white', va='center', fontsize=10)

# X轴设置
ax.set_xticks(x_pos)
ax.set_xticklabels(df["区域"], color="white", fontsize=10)

# Y轴范围
ax.set_ylim(0, 4000)
ax.set_yticks([0,1000,2000,3000,4000])
ax.set_yticklabels(["0","1000","2000","3000","4000"], color="white")

# 网格线
ax.grid(axis='y', color='#444466', linestyle='--')
ax.set_axisbelow(True)

# 在柱子顶部添加数字
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 60,
            f"{height}", ha="center", va="bottom", color="white", fontsize=9)

# 隐藏边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 保存图片（运行自动存到images文件夹）
plt.savefig("../images/pic2_mean_bar.png", dpi=150, bbox_inches="tight")
plt.tight_layout()
plt.show()