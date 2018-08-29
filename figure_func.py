# - coding:utf-8 - #

"""
Created on 2018.07.03
@author: Marion
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# 可视化数据分析：定性分析（柱状图/饼状图） 定量分析（直方图、累积曲线） 关系分析（散点图）
def drawbar(data):
    f, ax = plt.subplots(figsize=(15, 12))
    plt.xticks(rotation='90')
    sns.barplot(x=data.index, y=data)
    plt.xlabel('Features', fontsize=15)
    plt.ylabel('missing values', fontsize=15)
    plt.title('missing data by feature', fontsize=15)
    plt.show()

def drawBar(grades):
    # 创建柱状图
    xticks = ['A', 'B', 'C', 'D', 'E']
    gradeGroup = {}
    # 对每一类进行频数统计
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1
    # 第一个参数为柱的横坐标
    # 第二个参数为柱的高度
    # 参数align为柱的对齐方式，以第一个参数为参考标准
    plt.bar(range(5), [gradeGroup.get(xtick, 0) for xtick in xticks], align='center')
    # 设置柱的文字说明
    # 第一个参数为文字说明的横坐标
    # 第二个参数为文字说明的内容
    plt.xticks(range(5), xticks)
    #设置横坐标的文字说明
    plt.xlabel('Grade')
    #设置纵坐标的文字说明
    plt.ylabel('Frequency')
    #设置标题
    plt.title('Grades Of Male Students')
    #绘图
    plt.show()

def drawPie(grades):
    labels = ['A', 'B', 'C', 'D', 'E']
    gradeGroup = {}
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1
    #创建饼形图
    #第一个参数为扇形的面积
    #labels参数为扇形的说明文字
    #autopct参数为扇形占比的显示格式
    plt.pie([gradeGroup.get(label, 0) for label in labels], labels=labels, autopct='%1.1f%%')
    plt.title('Grades Of Male Students')
    plt.show()

def drawHist(heights):
    # 创建直方图
    # 第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
    # 第二个参数为划分的区间个数
    plt.hist(heights, 100)
    plt.xlabel('Heights')
    plt.ylabel('Frequency')
    plt.title('Heights Of Male Students')
    plt.show()

def drawCumulativeHist(heights):
    #创建累积曲线
    #第一个参数为待绘制的定量数据
    #第二个参数为划分的区间个数
    #normed参数为是否无量纲化
    #histtype参数为'step'，绘制阶梯状的曲线
    #cumulative参数为是否累积
    plt.hist(heights, 20, normed=True, histtype='step', cumulative=True)
    plt.xlabel('Heights')
    plt.ylabel('Frequency')
    plt.title('Heights Of Male Students')
    plt.show()

def drawScatter(heights, weights):
    #创建散点图
    #第一个参数为点的横坐标
    #第二个参数为点的纵坐标
    fig, ax = plt.subplots()
    ax.scatter(x=heights, y=weights)
    # plt.scatter(heights, weights)
    plt.xlabel('heights')
    plt.ylabel('weights')
    plt.title('Relation')
    plt.show()


def plot_line(x, y):
    plt.figure(facecolor='w')
    plt.plot(x, y, 'r-', linewidth=0.5, label=u'真实数据')
    plt.title(u'%s模型预测房屋价格\nRMSE:%s' % (2, str(1)), fontsize=18)
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()


def drawBox(heights):
    #创建箱形图
    #第一个参数为待绘制的定量数据
    #第二个参数为数据的文字说明
    plt.boxplot([heights], labels=['Heights'])
    plt.title('Heights Of Male Students')
    plt.show()

    # for zbid, df in data_pd_dpzb_day.groupby('zb_id'):
    #     print(zbid)
    #     print(df)