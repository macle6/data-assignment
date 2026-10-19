import matplotlib.pyplot as plt
import numpy as np

# ==========修复中文乱码，放在最前面==========
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# ==========================================

# 严格对应样图从上往下顺序：华东、西南、西北、东北、华南、华北
regions = ["华东", "西南", "西北", "东北", "华南", "华北"]
sales =     [2109, 1369, 1872, 1536, 1946, 4321]
place1 =    [2212, 2952, 2449, 2785, 2375,    0]
place2 =    [1080, 1080, 1080, 1080, 1080, 1080]

n = len(regions)
y = np.arange(n)
bar_height = 0.5

fig, ax = plt.subplots(figsize=(12, 5.5), dpi=110)
bg_color = "#172042"
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# 三段堆叠
bar1 = ax.barh(y, sales, height=bar_height, color="#0a3474")
bar2 = ax.barh(y, place1, height=bar_height, left=sales, color="#7398cb")
bar3 = ax.barh(y, place2, height=bar_height, left=np.add(sales, place1), color="#882b38")

# 深蓝色条末端标注销量数字
for bar, num in zip(bar1, sales):
    w = bar.get_width()
    ax.text(w - 60, bar.get_y() + bar_height/2, f"{num}",
            va="center", color="white", fontsize=8.5)

ax.set_yticks(y)
ax.set_yticklabels(regions, color="white", fontsize=9)

# =========关键！反转Y轴，列表第一个元素（华东）跑到画布最上方=========
ax.invert_yaxis()

# 隐藏x刻度和边框
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title("数值百分比堆叠条形图", color="white", fontsize=12)
plt.tight_layout()
plt.show()