# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

'''
散点图
'''


def scatter_chart():
    # 绘制表格
    fig = plt.figure()

    # 散点数 根
    n = 128
    # x轴 随机数
    X = np.random.normal(0, 1, n)
    # y轴 随机数
    Y = np.random.normal(0, 1, n)
    # 上色
    T = np.arctan2(Y, X)
    # 显示范围 二选一
    '''
     # 设置 三行三列 第一格子
    ax = fig.add_subplot(3, 3, 1)
    # 绘制散点 x,y s=点的大小 c=颜色上色 ,透明度
    ax.scatter(X, Y, s=75, c=T, alpha=.5)
      
      或者
    plt.axes([0.025, 0.025, 0.95, 0.95])
     # 绘制散点 x,y s=点的大小 c=颜色上色 ,透明度
    plt.scatter(X, Y, s=75, c=T, alpha=.5)
    '''
    # 设置 三行三列 第一格子
    ax = fig.add_subplot(3, 3, 1)
    # 绘制散点 x,y s=点的大小 c=颜色上色 ,透明度
    ax.scatter(X, Y, s=75, c=T, alpha=.5)

    # x的范围
    plt.xlim(-1.5, 1.5), plt.xticks([])
    # y的范围
    plt.ylim(-1.5, 1.5), plt.yticks([])
    # 可以查看图形的x轴的最小最大坐标和y轴的最小最大坐标
    plt.axis()
    # 设置横轴坐标
    plt.xlabel("x")
    # 设置纵轴坐标
    plt.ylabel("y")
    # 标题
    plt.title("scatter")
    # 生成图表
    plt.show()


'''
柱状图
'''


def bar_chart():
    # 绘制表格
    fig = plt.figure()

    fig.add_subplot(332)

    n = 10

    X = np.arange(n)

    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')

    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    # 添加注释
    for x, y in zip(X, Y1):
        ## 位置 格式 水平位置 垂直位置
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

    # 可以查看图形的x轴的最小最大坐标和y轴的最小最大坐标
    plt.axis()
    # 设置横轴坐标
    plt.xlabel("x")
    # 设置纵轴坐标
    plt.ylabel("y")
    plt.show()


'''
饼图
'''


def pie_chart():
    #https://www.imooc.com/video/14983
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # 标签
    labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其它']
    # 数据
    sizes = [2, 5, 12, 70, 2, 9]
    #
    explode = (0, 0, 0, 0, 0, 0)
    # 构造拼图      自动百分比  显示阴影 弧度
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
    # 标题
    plt.title("饼图示例-8月份家庭支出")

    # 显示图表
    plt.show()
    pass


if __name__ == '__main__':
    # 散点图
    # scatter_chart()
    # 柱状图
    # bar_chart()
    # 饼图
    pie_chart()
    pass
