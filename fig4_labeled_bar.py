#图表4：标注柱形图
import pandas as pd
import matplotlib.pyplot as plt

# 中文设置
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 数据
data = {
    "商品": ["口红", "面膜", "隔离", "防晒", "精华", "面霜", "眼影", "气垫"],
    "销量": [9221, 5102, 6571, 5760, 6321, 8612, 2645, 5321]
}
df = pd.DataFrame(data)

# 每个柱子独立颜色，匹配Excel样图
bar_colors = ["#73c8d8", "#489687", "#e27049", "#ffc125", "#289cd8", "#0068b4", "#5c52b2", "#4c4299"]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
fig.patch.set_facecolor('#192340')
ax.set_facecolor('#192340')

# 绘制柱形
bars = ax.bar(df["商品"], df["销量"], color=bar_colors, width=0.6)

# 在柱子顶部添加数值标注
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 120,
        f"{height}",
        ha="center",
        va="bottom",
        color="white",
        fontsize=9
    )

# Y轴设置
ax.set_ylim(0, 10000)
ax.set_yticks([0, 2000, 4000, 6000, 8000, 10000])
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='x', colors='white')

# 只画水平网格线，灰色虚线
ax.grid(axis='y', color='#444466', linestyle='--')
ax.set_axisbelow(True)

# 隐藏全部边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()