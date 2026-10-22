import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
from matplotlib.colors import LinearSegmentedColormap

# ---------------------- 数据
percent = 0.85
bg_color = "#1a1a3a"
# 渐变：紫色 -> 红色
cmap = LinearSegmentedColormap.from_list("ring_c", ["#9944cc", "#ee4466"])

# ---------------------- 创建画布
fig, ax = plt.subplots(figsize=(6,6), facecolor=bg_color)
ax.set_facecolor(bg_color)
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-1.2,1.2)
ax.set_aspect("equal")
ax.axis("off")

# 灰色底环（占位15%）
base_wedge = Wedge((0,0), 1, 0, 360, width=0.15, color="#333344")
ax.add_patch(base_wedge)

# 绘制渐变进度环（85%）
n = 100
theta_end = 360 * percent
for i in range(n):
    t1 = theta_end / n * i
    t2 = theta_end / n * (i+1)
    c = cmap(i/n)
    w = Wedge((0,0), 1, t1, t2, width=0.15, color=c)
    ax.add_patch(w)

# 中心文字
ax.text(0, 0, "85%", color="white", fontsize=22, ha="center", va="center")

plt.tight_layout()
plt.show()