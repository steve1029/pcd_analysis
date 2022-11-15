import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import open3d as o3d

pcd = pd.read_excel('./velodyne_10frame_merge_without_empty_2.xlsx')

cnames = list(pcd.columns.values)

gt10ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 10)]
gt10ref20 = pcd.loc[(pcd['Ref'] == 0.20) & (pcd['GT'] == 10)]
gt10ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 10)]
gt10ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 10)]

gt20ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 20)]
gt20ref20 = pcd.loc[(pcd['Ref'] == 0.20) & (pcd['GT'] == 20)]
gt20ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 20)]
gt20ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 20)]

gt35ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 35)]
gt35ref20 = pcd.loc[(pcd['Ref'] == 0.20) & (pcd['GT'] == 35)]
gt35ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 35)]
gt35ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 35)]

gt48ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 48)]
gt48ref20 = pcd.loc[(pcd['Ref'] == 0.20) & (pcd['GT'] == 48)]
gt48ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 48)]
gt48ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 48)]

fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20,4))

xticks = (0.3, 0.6, 0.9)
xtickslabels = ['3%', '65%', '95%']

kind = 'scatter'
x = 'Ref'
y = 'R'

axes[0].set_xlim(0.1,1.1)
axes[1].set_xlim(0.1,1.1)
axes[2].set_xlim(0.1,1.1)
axes[3].set_xlim(0.1,1.1)

axes[0].set_xticks(xticks)
axes[1].set_xticks(xticks)
axes[2].set_xticks(xticks)
axes[3].set_xticks(xticks)

axes[0].set_xticklabels(xtickslabels)
axes[1].set_xticklabels(xtickslabels)
axes[2].set_xticklabels(xtickslabels)
axes[3].set_xticklabels(xtickslabels)

axes[0].set_title('10 m')
axes[1].set_title('20 m')
axes[2].set_title('35 m')
axes[3].set_title('48 m')

axes[0].set_ylabel('Distance (m)')
axes[0].set_xlabel('Reflectivity')
axes[1].set_xlabel('Reflectivity')
axes[2].set_xlabel('Reflectivity')
axes[3].set_xlabel('Reflectivity')

"""
gt10ref03.plot(x=x, y=y, kind=kind, ax=axes[0], color='C1')
gt10ref20.plot(x=x, y=y, kind=kind, ax=axes[0], color='C2')
gt10ref65.plot(x=x, y=y, kind=kind, ax=axes[0], color='C3')
gt10ref95.plot(x=x, y=y, kind=kind, ax=axes[0], color='C4')

gt20ref03.plot(x=x, y=y, kind=kind, ax=axes[1], color='C1')
gt20ref20.plot(x=x, y=y, kind=kind, ax=axes[1], color='C2')
gt20ref65.plot(x=x, y=y, kind=kind, ax=axes[1], color='C3')
gt20ref95.plot(x=x, y=y, kind=kind, ax=axes[1], color='C4')

gt35ref03.plot(x=x, y=y, kind=kind, ax=axes[2], color='C1')
gt35ref20.plot(x=x, y=y, kind=kind, ax=axes[2], color='C2')
gt35ref65.plot(x=x, y=y, kind=kind, ax=axes[2], color='C2')
gt35ref95.plot(x=x, y=y, kind=kind, ax=axes[2], color='C3')

gt48ref03.plot(x=x, y=y, kind=kind, ax=axes[3], color='C1')
gt48ref20.plot(x=x, y=y, kind=kind, ax=axes[3], color='C2')
gt48ref65.plot(x=x, y=y, kind=kind, ax=axes[3], color='C2')
gt48ref95.plot(x=x, y=y, kind=kind, ax=axes[3], color='C3')
"""
def plot_custom_x(y, loc, axis, color) -> None:

    x = np.ones_like(y) * loc 
    axis.scatter(x, y, c=color)

    return None

x1 = 0.3
#x2 = 0.3
x3 = 0.6
x4 = 0.9

plot_custom_x(gt10ref03['R'], x1, axes[0], 'C0')
#plot_custom_x(gt10ref20['R'], x2, axes[0], 'C2')
plot_custom_x(gt10ref65['R'], x3, axes[0], 'C1')
plot_custom_x(gt10ref95['R'], x4, axes[0], 'C2')

plot_custom_x(gt20ref03['R'], x1, axes[1], 'C0')
#plot_custom_x(gt20ref20['R'], x2, axes[1], 'C2')
plot_custom_x(gt20ref65['R'], x3, axes[1], 'C1')
plot_custom_x(gt20ref95['R'], x4, axes[1], 'C2')

plot_custom_x(gt35ref03['R'], x1, axes[2], 'C0')
#plot_custom_x(gt35ref20['R'], x2, axes[2], 'C2')
plot_custom_x(gt35ref65['R'], x3, axes[2], 'C1')
plot_custom_x(gt35ref95['R'], x4, axes[2], 'C2')

plot_custom_x(gt48ref03['R'], x1, axes[3], 'C0')
#plot_custom_x(gt48ref20['R'], x2, axes[3], 'C2')
plot_custom_x(gt48ref65['R'], x3, axes[3], 'C1')
plot_custom_x(gt48ref95['R'], x4, axes[3], 'C2')

axes[0].axhline(10, label='GT', color='k')
axes[1].axhline(20, label='GT', color='k')
axes[2].axhline(35, label='GT', color='k')
axes[3].axhline(48, label='GT', color='k')

axes[0].legend(loc='best')
axes[1].legend(loc='best')
axes[2].legend(loc='best')
axes[3].legend(loc='best')

fig.savefig('./velodyne_pcd_analysis.png', dpi=300, bbox_inches='tight')

fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20,4))
cols10 = [gt10ref03['R'], gt10ref65['R'], gt10ref95['R']]
cols20 = [gt20ref03['R'], gt20ref65['R'], gt20ref95['R']]
cols35 = [gt35ref03['R'], gt35ref65['R'], gt35ref95['R']]
cols48 = [gt48ref03['R'], gt48ref65['R'], gt48ref95['R']]

labels = ['3%', '65%', '95%']

bplot0 = axes[0].boxplot(cols10, labels=labels, patch_artist=True, notch=True)
bplot1 = axes[1].boxplot(cols20, labels=labels, patch_artist=True, notch=True)
bplot2 = axes[2].boxplot(cols35, labels=labels, patch_artist=True, notch=True)
bplot3 = axes[3].boxplot(cols48, labels=labels, patch_artist=True, notch=True)

axes[0].set_ylim( 9.9, 10.3)
axes[1].set_ylim(19.9, 20.4)
axes[2].set_ylim(34.9, 35.2)
axes[3].set_ylim(47.5, 48.5)

axes[0].axhline(10, label='GT', color='b')
axes[1].axhline(20, label='GT', color='b')
axes[2].axhline(35, label='GT', color='b')
axes[3].axhline(48, label='GT', color='b')

axes[0].set_title('10 m')
axes[1].set_title('20 m')
axes[2].set_title('35 m')
axes[3].set_title('48 m')

axes[0].set_ylabel('Distance (m)')
axes[0].set_xlabel('Reflectivity')
axes[1].set_xlabel('Reflectivity')
axes[2].set_xlabel('Reflectivity')
axes[3].set_xlabel('Reflectivity')

axes[0].legend(loc='best')
axes[1].legend(loc='best')
axes[2].legend(loc='best')
axes[3].legend(loc='best')

colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot0, bplot1, bplot2, bplot3):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

fig.savefig('./velodyne_pcd_analysis_boxplot.png', dpi=300, bbox_inches='tight')