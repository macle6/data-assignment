import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Arc

plt.rcParams['font.sans-serif'] = ['SimHei']
percent = 0.65
bg_color = "#162040"
water_color = "#0070cc"

fig, ax = plt.subplots(figsize=(7, 6), facecolor=bg_color)
ax.set_facecolor(bg_color)
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect("equal")
ax.axis("off")

# 外轮廓：上面开口圆弧
arc = Arc((0, 0), width=1.3, height=0.7, theta1=20, theta2=160, color=water_color, lw=2)
ax.add_patch(arc)

# 下半椭圆（水，占65%）
water = Ellipse((0, -0.15), width=1.2, height=0.65*0.7, color=water_color)
ax.add_patch(water)

# 文字
ax.text(0, 0.9, "2022 年上半年目标完成率", color="white", fontsize=15, ha="center", weight="bold")
ax.text(0, 0.62, "截至 6 月 30 日销售目标总体完成率达到 65%", color="white", fontsize=11, ha="center")
ax.text(-1.1, -1.1, "*注：数据来源于公司销售系统", color="#cccccc", fontsize=8, ha="left")

plt.tight_layout()
plt.show()