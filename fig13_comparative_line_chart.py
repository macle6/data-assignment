import matplotlib.pyplot as plt

month = ["1月", "2月", "3月", "4月", "5月", "6月"]
y2021 = [1686, 1345, 1934, 1658, 1865, 1936]
y2022 = [1385, 1846, 1654, 1936, 2564, 2236]

plt.style.use('dark_background')
plt.figure(figsize=(10,6))

line1 = plt.plot(month, y2021, marker='o', color='#e8647c', label='2021年')
line2 = plt.plot(month, y2022, marker='o', color='#2993d8', label='2022年')

# 标注2021每个点
for x,val in enumerate(y2021):
    plt.text(x, val+35, str(val), ha="center", color="#e8647c", fontsize=9)

# 标注2022每个点
for x,val in enumerate(y2022):
    plt.text(x, val+35, str(val), ha="center", color="#2993d8", fontsize=9)


plt.title("13 对比折线图", fontsize=15)
plt.ylim(0, 3000)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()