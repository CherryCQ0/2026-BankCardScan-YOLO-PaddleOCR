import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 定义维度与模拟数据 (基于您的描述)
categories = ['推理吞吐量\n(FPS)', '端到端延迟\n(ms)', '内存峰值占用\n(GB)']
N = len(categories)

rtx_data = [85, 20, 4.5]   # RTX 4060：高FPS，低延迟，高内存
i5_data = [12, 180, 1.2]   # i5-8250U：低FPS，高延迟，低内存

# 标准化处理 (映射到 0-100% 用于雷达图展示)
rtx_norm = [rtx_data[0]/100 * 100, rtx_data[1]/200 * 100, rtx_data[2]/5 * 100]
i5_norm = [i5_data[0]/100 * 100, i5_data[1]/200 * 100, i5_data[2]/5 * 100]

# 闭合雷达图多边形
rtx_norm += rtx_norm[:1]
i5_norm += i5_norm[:1]
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# 绘制网格与标签
plt.xticks(angles[:-1], categories, color='black', size=12)
ax.set_rlabel_position(30)
plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="grey", size=10)
plt.ylim(0, 100)

# 绘制 RTX 4060
ax.plot(angles, rtx_norm, linewidth=2, linestyle='solid', label='RTX 4060 (高性能 GPU)', color='#5DADE2')
ax.fill(angles, rtx_norm, '#5DADE2', alpha=0.4)

# 绘制 i5-8250U
ax.plot(angles, i5_norm, linewidth=2, linestyle='solid', label='i5-8250U (轻量级 CPU)', color='#F4D03F')
ax.fill(angles, i5_norm, '#F4D03F', alpha=0.4)

# 绘制图例与标题
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.title('图 5-1 系统在异构计算环境下的多维性能对比雷达图', size=14, y=1.1, fontweight='bold')

plt.tight_layout()
plt.savefig('radar_chart.png', dpi=300, bbox_inches='tight')