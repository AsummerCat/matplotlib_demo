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
散点图1
'''
def scatter_chart_1():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    N = 100
    x = np.random.randn(N)
    y = np.random.randn(N)
    plt.scatter(x, y)

    plt.title("散点图示例01")  # 显示图表名称
    plt.xlabel("x轴")  # x轴名称
    plt.ylabel("y轴")  # y轴名称
    plt.text(+1.2, -1, "By:cat", fontsize=16, color="purple")

    plt.show()

'''
柱状图
'''


def bar_chart():
    # 调节图形大小，宽，高
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


# https://www.imooc.com/video/14983


def pie_chart():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 10))

    # 标签
    labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其它']
    # 数据
    sizes = [2, 5, 12, 70, 2, 9]
    # 每一块离开中心距离
    explode = (0, 0, 0, 0, 0, 0)
    # 自定义颜色列表
    colors = ['r', 'g', 'y', 'b']
    # 构造拼图   每一块离开中心距离  标签 控制饼图内百分比设置 控制饼图内百分比设置  显示阴影 起始绘制角度>90y轴正方向画起 自定义颜色
    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150, colors=colors)
    # 标题
    plt.title("饼图示例-8月份家庭支出")

    # 文本信息
    plt.text(1, -1.2, 'By:cat')

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size(30)
    for t in p_text:
        t.set_size(20)
    # 添加图例
    plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3)
    # loc =  'upper right' 位于右上角
    # bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边
    # ncol=2 分两列
    # borderaxespad = 0.3图例的内边距

    # 将饼图显示为正圆形
    # plt.gca().set_aspect('equal')
    # 或者
    plt.axis('equal')
    # 保存图表
    plt.savefig(r"E:\饼图02.png", dpi=200, bbox_inches='tight')
    # 显示图表
    plt.show()


if __name__ == '__main__':
    # 散点图
    # scatter_chart()
    # 散点图1
    # scatter_chart_1()
    # 柱状图
    # bar_chart()
    # 饼图
    pie_chart()


    pass
