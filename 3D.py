import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image

fig = plt.figure()  # 创建一个画布
ax = Axes3D(fig, auto_add_to_figure=False)  # 画布上创建一个三维坐标系
# auto_add_to_figure=False，必须有这个参数设置，否则报错
# 但设置为False后需要手动为图像添加轴，即下面一行代码
fig.add_axes(ax)
img = np.asanyarray(Image.open('./143593.jpg'))
X = [0, 1]
Y = [0, 1, 2]
X, Y = np.meshgrid(X, Y)
Z = X + Y**2

# 以下是构成这个3d平面的6个点，分别对应x，y，z坐标
x = [0, 1, 0, 1, 0, 1]
y = [0, 0, 1, 1, 2, 2]
z = [0, 1, 1, 2, 2, 3]
plt.plot(x, y)
# imgplot = plt.imshow(img)
plt.xlabel("x")
plt.ylabel("y")
plt.xticks()
ax.scatter(x, y, z, color='black')  # 绘制3D散点图
ax.plot_trisurf(x, y, z)  # 绘制3D曲平面
plt.grid()

plt.show()
