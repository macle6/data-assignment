#图表1：渐变柱状图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle


plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


data = {
    "区域": ["华北", "华南", "东北", "西北", "西南", "华东"],
    "销售量": [2354, 1902, 3524, 2698, 2896, 2563]
}
df = pd.DataFrame(data)


fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
fig.patch.set_facecolor('#192340')
ax.set_facecolor('#192340')

bar_width = 0.6
x_pos = np.arange(len(df["区域"]))
# 统一渐变
cmap = LinearSegmentedColormap.from_list("bar_gradient", ["#0055bb", "#00ccff"])


for i, (x, val) in enumerate(zip(x_pos, df["销售量"])):
    left = x
    right = x + bar_width
    # 生成渐变贴图
    grad_data = np.linspace(0, 1, 256).reshape(-1, 1)
    ax.imshow(grad_data, extent=[left, right, 0, val], aspect="auto", cmap=cmap)

# ---------------------- 4. 坐标轴，文字居中 ----------------------
ax.set_xticks(x_pos + bar_width / 2)
ax.set_xticklabels(df["区域"], color="white", fontsize=10)

ax.set_xlim(-0.3, len(df["区域"])-0.1) # 给左右留出空白，防止第一个柱子被切掉！！
ax.set_ylim(0, 4000)
ax.set_yticks([0, 1000, 2000, 3000, 4000])
ax.set_yticklabels(["0", "1000", "2000", "3000", "4000"], color="white")

ax.grid(axis='y', color='#444466', linestyle='--')
ax.set_axisbelow(True)

# ---------------------- 5. 顶部数字居中 ----------------------
for i, val in enumerate(df["销售量"]):
    bar_center = x_pos[i] + bar_width / 2
    ax.text(bar_center, val + 80, str(val),
            ha="center", va="bottom",
            color="white", fontsize=9)

# ---------------------- 6. 隐藏边框 ----------------------
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()