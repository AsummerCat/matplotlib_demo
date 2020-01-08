# -*- coding:utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

'''
折线图图表 测试
'''


'''
绘制余弦 正弦 
'''


def draw_cos_sin():
    # -np.pi, np.pi, 之间有 256点 包含最后一个点
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

    # 余弦函数  # 正弦函数
    c, s = np.cos(x), np.sin(x)
    # 绘制表格
    plt.figaspect(1)
    # 绘制 自变量   因变量
    plt.plot(x, c, "r*")
    #  原线 自变量 颜色 线宽 线类型 标签 透明度
    plt.plot(x, s, color="blue", linewidth=1.0, linestyle="-", label="SIN", alpha=0.5)
    # 加入标题
    plt.title("cos&sin")
    # 加入网格线
    plt.grid()
    # 以上部分已经可以生成出图表了

    '''
    定位 边框 上下左右
    '''
    # 添加横轴纵轴编辑器 绘制基础点位置
    # 添加编辑器
    ax = plt.gca()
    # 定位上下左右图表

    # set_position 设置位置居中
    ax.spines['left'].set_position('center')
    # 左边的线 放入到数据域 0的这个位置
    # ax.spines['left'].set_position(("data", 0))
    ax.spines['bottom'].set_position('center')
    # set_color设置颜色无
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # 设置 x轴y轴参数 显示位置 底部显示x轴点 和左边显示y轴点
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # 设置横轴 横轴标示的位置  标示的内容
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', '$+\pi/2$', '$+\pi$'])
    # 设置纵轴 -1,1 5个点 并且显示
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

    # 标记点 设置大小
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        # 设置字体大小
        label.set_fontsize(16)
        # 设置label的小方块的格式  背景颜色 边缘  透明度
        label.set_bbox(dict(facecolor="yellow", edgecolor="none", alpha=0.2))

    # 图例图 就是左边有个标记样式的
    plt.legend(loc='upper left')

    # 控制显示范围 x轴最小 x轴最大 y轴最小 y轴最大
    # plt.axis([-1, 1, -0.5, 1])

    # 填充区域纵坐标     轴 范围 颜色 透明度
    plt.fill_between(x, 0, 0.5, color="green", alpha="0.53")
    # 填充区域纵坐标     轴 范围 颜色 透明度
    plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="black", alpha="0.53")
    # 填充区域横坐标     轴 范围 颜色 透明度
    plt.fill_betweenx(x, 0, 0.5, color="red", alpha="0.53")

    # 标记点  在1,1的地方并且 在 0,np.cos(1)之间
    plt.plot([1, 1], [0, np.cos(1)], "y", linewidth=6, linestyle='-.', color="purple")

    # 标记点 添加注释    注释名称 点的位置   标记的偏移量 x+10 y+30   相对位置 箭头类型
    plt.annotate("cos(1)", xy=(1, np.cos(1)), xycoords="data", xytext=(+10, +30), textcoords="offset points",
                 # 标记箭头设置 标记符号 箭头弧度
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # 生成图表
    plt.show()


'''
绘制直线
"绘制2x+1的直线"
'''


def draw_line():
    x = np.linspace(-5, 5, 256)
    y = 2 * x + 1
    # 绘制 '-r'表示上色
    '''
    颜色
b: blue 
g: green 
r: red 
c: cyan 
m: magenta 
y: yellow 
k: black 
w: white
'-.'+颜色 表示按颜色 -.-.-.-.
':'+颜色 表示 ......
'.'+颜色 表示 粗线的......
'--'+颜色 表示 - - - - - -
'-'+颜色 表示 ---------实线
'r*' 表示 ***********s
''
 
    '''
    plt.plot(x, y, '-r', label='y=2x+1')
    plt.plot(x, 2 * x - 1, '-.g', label='y=2x-1')
    plt.plot(x, 2 * x + 3, ':b', label='y=2x+3')
    plt.plot(x, 2 * x - 3, '--m', label='y=2x-3')
    plt.plot(x, 2 * x - 3, '.m', label='y=2x-3')
    plt.title("'Graph of y=2x+1'")
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # 正弦余弦函数
    draw_cos_sin()
    # 直线 "绘制2x+1的直线"
    # draw_line()

    pass
