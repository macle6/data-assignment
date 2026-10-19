import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

products = ["口红", "面膜", "隔离", "防晒", "精华"]
sales_2021 = [3568, 4135, 4436, 4106, 4936]
sales_2022 = [2569, 3241, 2965, 3209, 3541]

x = np.arange(len(products))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5), dpi=120)
fig.patch.set_facecolor("#0b132b")
ax.set_facecolor("#0b132b")

bar1 = ax.bar(x - width/2, sales_2021, width, label="2021销量", color="#4472c4")
bar2 = ax.bar(x + width/2, sales_2022, width, label="2022销量", color="#8cb4e8")

ax.set_xticks(x)
ax.set_xticklabels(products, color="white")
ax.tick_params(axis="y", labelcolor="white")
ax.set_ylabel("销量", color="white")
ax.set_title("化妆品销量对比柱状图", color="white")
ax.legend(labelcolor="white")

for bars in [bar1, bar2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=9,
            color="white"
        )

plt.tight_layout()
plt.show()