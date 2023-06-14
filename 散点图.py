import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def scatterGraph():
    """散点图"""
    n = 1024  # data size
    X = np.random.normal(0, 1, n)  # 每一个点的X值
    Y = np.random.normal(0, 1, n)  # 每一个点的Y值
    T = np.arctan2(Y, X)  # for color value
    """输入X和Y作为location，size=75，颜色为T，color map用默认值，
    透明度alpha 为 50%。 x轴显示范围定位(-1.5，1.5)，
    并用xtick()函数来隐藏x坐标轴，y轴同理："""
    plt.scatter(X, Y, s=10, c=T, alpha=.5)
    plt.xlim(-1.5, 1.5)
    plt.xticks(())  # ignore xticks
    plt.ylim(-1.5, 1.5)
    plt.yticks(())  # ignore yticks
    # plt.yticks('1')  # ignore yticks
    plt.show()

# scatterGraph()
def threedGraph():
    """绘制3D图形"""
    fig = plt.figure()
    ax = Axes3D(fig) #先定义一个图像窗口，在窗口上添加3D坐标轴
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)  # x-y 平面的网格 #
    R = np.sqrt(X ** 2 + Y ** 2)
    # height value
    Z = np.sin(R)
    #做出一个三维曲面，并将一个 colormap rainbow 填充颜色，
    # 之后将三维图像投影到 XY 平面上做一个等高线图。 plot 3D 图像：
    #rstride 和 cstride 分别代表 row 和 column 的跨度。
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
    #如果 zdir 选择了x，那么效果将会是对于 XZ 平面的投影
    ax.set_zlim(-2, 2)
    plt.show()
    # plt.close()
threedGraph()