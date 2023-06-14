
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import datetime
import time
# 从Excel文件中读取数据


def read_data_from_excel(file_name):
    data = pd.read_excel(file_name, sheet_name=None)
    return data


# 读取数据
file_name = '验证数据.xlsx'
sheets_data = read_data_from_excel(file_name)

# 处理数据
all_data = []
all_targets = []
all_time = []
for sheet_name, sheet_data in sheets_data.items():
    # print(sheet_name)
    # print(sheet_data)
    # print(type(sheet_data))
    sheet_data = sheet_data.dropna()
    if sheet_data.empty:  # 检查sheet是否为空
        continue
    data = (sheet_data.iloc[:, 1].values)*10
    # time_data = pd.to_datetime(sheet_data.iloc[:, 0])

    time_data = sheet_data.iloc[:, 0].values

    # timestamp = time.mktime(datetime.datetime.strptime(time_data, '%Y-%m-%d %H:%M:%S').timetuple())
    # print(time_data)
    # print('---------------')
    # print(type(time_data))
    target = sheet_data.iloc[0, -1]
    all_data.append(data)
    all_time = time_data
    all_targets.append(target)


print('===================')
for element in all_time:
    print(element)

# tux = torch.from_numpy(all_time)
fux = torch.from_numpy(all_data[0])

print(all_time)
print(type(all_time))
print(fux)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)

ax.scatter(x, y, z)

plt.show()
