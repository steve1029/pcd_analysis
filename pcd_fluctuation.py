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

print(gt10ref03)