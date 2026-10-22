import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_label = ["5月","6月","7月","8月","9月","10月","11月","12月","1月","2月","3月"]
y_sale = [146,198,296,412,506,615,789,1021,3782,3215,2936]
x_raw = np.arange(len(x_label))

#平滑插值
x_new = np.linspace(0, len(x_raw)-1, 300)
spl = make_interp_spline(x_raw, y_sale, k=3)
y_smooth = spl(x_new)

fig, ax = plt.subplots(figsize=(9,5), dpi=120)
fig.patch.set_facecolor("#0b132b")
ax.set_facecolor("#0b132b")

ax.plot(x_new, y_smooth, color="#c86464", linewidth=1.6)
ax.scatter(x_raw, y_sale, color="#c86464", s=18, zorder=5)

ax.set_xticks(x_raw)
ax.set_xticklabels(x_label)
ax.tick_params(axis="x", labelcolor="white", labelsize=8)
ax.tick_params(axis="y", labelcolor="white", labelsize=8)
ax.set_title("Smooth Line Chart", color="white")

plt.tight_layout()
plt.show()