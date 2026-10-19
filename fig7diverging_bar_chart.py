import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

regions = ["华东", "西北", "东北", "华北", "华南"]
data2022 = [36, 31, 18, 13, 9]
data2021 = [42, 26, 19, 12, 5]
offset = 1.5  # 中间空白半宽：空隙总宽度 = offset*2
y = list(range(len(regions)))

fig, ax = plt.subplots(figsize=(10,5),dpi=120)

# 左侧：起点是 -offset，再向左延伸数值长度
for i, val in enumerate(data2022):
    ax.barh(y[i], -val, left=-offset, height=0.6, facecolor="none", edgecolor="black", hatch="|", linewidth=0)

# 右侧：起点是 +offset，再向右延伸数值长度
for i, val in enumerate(data2021):
    ax.barh(y[i], val, left=offset, height=0.6, facecolor="none", edgecolor="black", hatch="|", linewidth=0)


ax.set_yticks(y)
ax.set_yticklabels(regions)
ax.invert_yaxis()

ax.set_xticks([-40,-30,-20,-10,0,10,20,30,40])
ax.set_xticklabels(["40%","30%","20%","10%","0%","10%","20%","30%","40%"])

ax.set_title("Regional Percentage Comparison")
ax.grid(False)
plt.tight_layout()
plt.show()