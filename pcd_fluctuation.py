import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import open3d as o3d

pcd = pd.read_excel('./velodyne_10frame_merge_without_empty_2.xlsx')
cnames = list(pcd.columns.values)

gt10ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 10)]
gt10ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 10)]
gt10ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 10)]

gt20ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 20)]
gt20ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 20)]
gt20ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 20)]

gt35ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 35)]
gt35ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 35)]
gt35ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 35)]

gt48ref03 = pcd.loc[(pcd['Ref'] == 0.03) & (pcd['GT'] == 48)]
gt48ref65 = pcd.loc[(pcd['Ref'] == 0.65) & (pcd['GT'] == 48)]
gt48ref95 = pcd.loc[(pcd['Ref'] == 0.95) & (pcd['GT'] == 48)]

print(gt10ref03['Ref'][0])

fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20,4))

xticks = (0.03, 0.65, 0.95)
xtickslabels = ['3%', '65%', '95']

gt10ref03.plot(x='Ref', y='R', kind='scatter', ax=axes[0], color='C1', xticks=xticks, xlim=(0,1), title='10 m')
gt10ref65.plot(x='Ref', y='R', kind='scatter', ax=axes[0], color='C2', xticks=xticks, xlim=(0,1), title='10 m')
gt10ref95.plot(x='Ref', y='R', kind='scatter', ax=axes[0], color='C3', xticks=xticks, xlim=(0,1), title='10 m')

gt20ref03.plot(x='Ref', y='R', kind='scatter', ax=axes[1], color='C1', xticks=xticks, xlim=(0,1), title='20 m')
gt20ref65.plot(x='Ref', y='R', kind='scatter', ax=axes[1], color='C2', xticks=xticks, xlim=(0,1), title='20 m')
gt20ref95.plot(x='Ref', y='R', kind='scatter', ax=axes[1], color='C3', xticks=xticks, xlim=(0,1), title='20 m')

gt35ref03.plot(x='Ref', y='R', kind='scatter', ax=axes[2], color='C1', xticks=xticks, xlim=(0,1), title='35 m')
gt35ref65.plot(x='Ref', y='R', kind='scatter', ax=axes[2], color='C2', xticks=xticks, xlim=(0,1), title='35 m')
gt35ref95.plot(x='Ref', y='R', kind='scatter', ax=axes[2], color='C3', xticks=xticks, xlim=(0,1), title='35 m')

gt48ref03.plot(x='Ref', y='R', kind='scatter', ax=axes[3], color='C1', xticks=xticks, xlim=(0,1), title='48 m')
gt48ref65.plot(x='Ref', y='R', kind='scatter', ax=axes[3], color='C2', xticks=xticks, xlim=(0,1), title='48 m')
gt48ref95.plot(x='Ref', y='R', kind='scatter', ax=axes[3], color='C3', xticks=xticks, xlim=(0,1), title='48 m')

plt.show()