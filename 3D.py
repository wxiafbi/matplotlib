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
<<<<<<< HEAD
# plt.xlim(-1, 1)
# plt.ylim(-10, 10)

plt.xlabel("x")
plt.ylabel("y")
plt.axis([-1, 1, -10, 10])
ax.scatter(x, y, z, color='black')  # 绘制3D散点图
ax.plot_trisurf(x, y, z)  # 绘制3D曲平面
=======
plt.xlabel("x")
plt.ylabel("y")
plt.xticks()
ax.scatter(x, y, z, color='black')  # 绘制3D散点图
ax.plot_trisurf(x, y, z)  # 绘制3D曲平面
plt.grid()
>>>>>>> 8297aa47894b4f73ba8b20d284cf06f59a0ed4e2

plt.show()
