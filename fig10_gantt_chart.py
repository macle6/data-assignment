import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

tasks = [
    "制定计划",
    "方案设计",
    "资源调配",
    "第一阶段",
    "第二阶段",
    "第三阶段",
    "项目总结"
]
start_str = [
    "2022/3/1",
    "2022/3/13",
    "2022/3/22",
    "2022/4/2",
    "2022/4/16",
    "2022/5/11",
    "2022/5/26"
]
days = [11,8,10,13,24,14,7]

#转为日期
start_dates = [datetime.strptime(s,"%Y/%m/%d") for s in start_str]
base = datetime(2022,3,1)
start_days = [(d-base).days for d in start_dates]

fig, ax = plt.subplots(figsize=(10,5),dpi=120)
fig.patch.set_facecolor("#0b132b")
ax.set_facecolor("#0b132b")

y_pos = list(range(len(tasks)))
#甘特图是水平条形图
ax.barh(y_pos, days, left=start_days, height=0.55, color="#2b64cc")

ax.set_yticks(y_pos)
ax.set_yticklabels(tasks,color="white")
ax.tick_params(axis="x",labelcolor="white")

ax.set_title("Project Schedule Gantt Chart",color="white")

plt.tight_layout()
plt.show()