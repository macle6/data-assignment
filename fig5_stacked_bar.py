#图表5：层叠柱形图
import matplotlib.pyplot as plt
import pandas as pd

# 数据
data = {
    "季度": ["2021Q1", "Q2", "Q3", "Q4", "2022Q1", "Q2"],
    "销售额": [3121, 4086, 4321, 4601, 4936, 4231],
    "利润额": [1020, 1421, 1502, 1623, 1781, 1432]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 7), dpi=100)
fig.patch.set_facecolor('#192340')
ax.set_facecolor('#192340')

x = list(range(len(df["季度"])))
width = 0.45
offset = 0.12

bar_sale = ax.bar([i - offset for i in x], df["销售额"], width, color="#0068b4")
bar_profit = ax.bar([i + offset for i in x], df["利润额"], width, color="#d9485c")

# ========== 重点修改：文字放到柱子顶部上方 ==========
# 销售额文字
for i, bar in enumerate(bar_sale):
    h = bar.get_height()
    ax.text(bar.get_x()+bar.get_width()/2, h + 80, f"{h}", color="white", ha="center", fontsize=9)

# 利润额文字
for i, bar in enumerate(bar_profit):
    h = bar.get_height()
    ax.text(bar.get_x()+bar.get_width()/2, h + 80, f"{h}", color="white", ha="center", fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(df["季度"], color="white")
ax.tick_params(axis='y', colors='white')

ax.grid(axis='y', color='#444466', linestyle='--')
ax.set_axisbelow(True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()