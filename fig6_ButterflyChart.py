import matplotlib.pyplot as plt
import numpy as np

val_left = [2238, 2132, 2027, 1922, 1215]   #蓝色2022 降序：大→小
val_right = [2066, 1436, 1531, 1265, 1003] #红色2021 降序：大→小

n = len(val_left)
y = np.arange(n)
# 关键！反转y，把索引0放到最上面
y = np.flip(y)

bar_h = 0.5
gap_width = 400

fig, (axL, axR) = plt.subplots(1, 2, sharey=True, figsize=(11,5.2), dpi=110)
bg = "#172042"
fig.patch.set_facecolor(bg)
axL.set_facecolor(bg)
axR.set_facecolor(bg)

# 左边蓝色
barsL = axL.barh(y, val_left, height=bar_h, color="#007acc")
axL.set_xlim(0, max(val_left)+gap_width)
axL.invert_xaxis()
axL.set_yticks([])
axL.tick_params(axis="x", bottom=False, labelbottom=False)
for s in axL.spines.values():
    s.set_visible(False)

# 右边红色
barsR = axR.barh(y, val_right, height=bar_h, color="#e84c5c", left=gap_width)
axR.set_xlim(0, gap_width + max(val_right))
axR.tick_params(axis="x", bottom=False, labelbottom=False)
for s in axR.spines.values():
    s.set_visible(False)

# 数值标签
for bar, num in zip(barsL, val_left):
    axL.text(bar.get_width()+18, bar.get_y()+bar_h/2, str(num), va="center", c="white", fontsize=8.2)

for bar, num in zip(barsR, val_right):
    axR.text(gap_width + bar.get_width()+18, bar.get_y()+bar_h/2, str(num), va="center", c="white", fontsize=8.2)

plt.subplots_adjust(wspace=0)
plt.show()