#图表3：渐变圆柱柱形图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Ellipse
from matplotlib.colors import LinearSegmentedColormap

# 中文设置
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 数据
data = {
    "商品": ["口红", "面膜", "隔离", "防晒", "精华", "面霜"],
    "销量": [653, 523, 648, 856, 714, 785]
}
df = pd.DataFrame(data)

# 不改颜色：保留原来的蓝青渐变
cmap = LinearSegmentedColormap.from_list("bar_cyan", ["#00ddff", "#003399"])

# 画布
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
fig.patch.set_facecolor('#192340')
ax.set_facecolor('#192340')

bar_width = 0.55
x_pos = np.arange(len(df["商品"]))

# 控制圆柱顶部明显程度
cap_height = 18   # 这个数值调大，圆头就更明显
cap_light = "#00ddff"

for i, (x, val) in enumerate(zip(x_pos, df["销量"])):
    # 柱子主体：上下渐变，不改颜色
    grad = np.linspace(0, 1, 256).reshape(-1, 1)
    grad = np.hstack([grad, grad])

    ax.imshow(
        grad,
        extent=[x - bar_width / 2, x + bar_width / 2, 0, val],
        aspect="auto",
        cmap=cmap,
        vmin=0,
        vmax=1
    )

    # 顶部椭圆：让圆柱头更明显
    top_cap = Ellipse(
        (x, val),
        width=bar_width,
        height=cap_height,
        color=cap_light,
        zorder=4
    )
    ax.add_patch(top_cap)

    # 顶部再加一条边线，轮廓更清楚
    top_line = Arc(
        (x, val),
        width=bar_width,
        height=cap_height,
        angle=0,
        theta1=0,
        theta2=180,
        color="#ffffff",
        linewidth=1.5,
        zorder=5
    )
    ax.add_patch(top_line)

    # 柱子上方数值文字
    ax.text(x, val + cap_height / 2 + 8, f"{val}",
            ha="center", va="bottom", color="white", fontsize=10)


ax.set_xlim(-0.6, len(x_pos) - 0.4)
ax.set_ylim(0, 1000)
ax.set_xticks(x_pos)
ax.set_xticklabels(df["商品"], color="white", fontsize=10)
ax.set_yticks([0, 200, 400, 600, 800, 1000])
ax.set_yticklabels(["0", "200", "400", "600", "800", "1000"], color="white")

# 网格线
ax.grid(axis='y', color='#444466', linestyle='--')
ax.set_axisbelow(True)

# 隐藏四周边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.savefig("../images/pic3_cylinder_bar.png", dpi=150, bbox_inches="tight")
plt.tight_layout()
plt.show()