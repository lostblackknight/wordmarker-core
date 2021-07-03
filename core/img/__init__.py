import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import List
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from abc import ABCMeta, abstractmethod


class Chart(metaclass=ABCMeta):
    def __init__(self, df):
        self.df = df
        self.fig: Figure = plt.figure()
        self.ax_list: List[Axes] = []

    @abstractmethod
    def _set_fig(self):
        # 设置fig
        pass

    @abstractmethod
    def _append_ax_list(self) -> List[Axes]:
        # 添加轴，并将轴的列表返回
        pass

    @abstractmethod
    def _process_df(self):
        # 处理数据
        pass

    @abstractmethod
    def _process_ax_list(self):
        pass

    def build(self, filename=None):
        # 输出图片，暂时展示
        self._set_fig()
        self.ax_list = self._append_ax_list()
        # 将轴添加到fig上
        for ax in self.ax_list:
            self.fig.add_axes(ax)
        self._process_df()
        self._process_ax_list()
        # self.fig.show()
        if filename:
            self.fig.savefig(filename, format='png')


class ProsperityIndex(Chart):
    """
    景气指数
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(20, 15)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
        self.fig.gca()
        self.fig.subplots_adjust(wspace=None, hspace=0)  # 调整布局

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax1 = plt.subplot(111)
        return [ax1]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数
        self.df.sort_values(by=['起飞年', '起飞星期'], inplace=True, ascending=True)
        self.df["time"] = range(0, len(self.df))
        # 设置索引
        self.df.set_index("time", inplace=True)

        self.__x = self.df.index
        self.__y = self.df['景气指数']

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据
        self.ax_list[0].plot(range(len(self.__x)), self.__y, color='orange')
        self.ax_list[0].grid(axis="y", linestyle='--')  # 网格
        self.ax_list[0].patch.set_facecolor("black")
        self.ax_list[0].set_title("景气指数", fontdict={'size': 40})
        for self.size in self.ax_list[0].get_yticklabels():  # 获取y轴上所有坐标，并设置字号
            self.size.set_fontname(' Microsoft YaHei')  # 雅黑
            self.size.set_fontsize('18')
        self.ax_list[0].set_xticks([])


class PassengerLoadFactor(Chart):
    """
    载客率
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(20, 15)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
        self.fig.gca()
        self.fig.subplots_adjust(wspace=None, hspace=0)  # 调整布局

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax1 = plt.subplot(311)
        ax2 = plt.subplot(312)
        ax3 = plt.subplot(313)
        return [ax1, ax2, ax3]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数
        data_per = pd.PeriodIndex(
            year=self.df['year_id'],
            month=self.df['month_id'],
            freq="M")
        self.df["time"] = data_per
        data_inland = self.df.loc[self.df['market_id'] == '国内', ['month_id', '旅客量', '客座率', 'time']].sort_values(
            by='time')
        data_international = self.df.loc[self.df['market_id'] == '国际', ['旅客量', '客座率', 'time']].sort_values(by='time')
        data_HongKong = self.df.loc[self.df['market_id'] == '港澳台', ['旅客量', '客座率', 'time']].sort_values(by='time')
        # 设置索引
        data_inland.set_index("time", inplace=True)
        data_international.set_index("time", inplace=True)
        data_HongKong.set_index("time", inplace=True)
        # __两个下划线开头的标识符或函数名，为私有，只能在类内部访问(形式上的)
        self.__x_inland = data_inland.index
        self.__y_inland = data_inland[['客座率']]
        self.__x_international = data_inland.index
        self.__y_international = data_inland[['客座率']]
        self.__x_HongKong = data_inland.index
        self.__y_HongKong = data_inland[['客座率']]

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据
        self.ax_list[0].plot(range(len(self.__x_inland)), self.__y_inland, color='orange')
        self.ax_list[0].grid(axis="y", linestyle='--')  # 网格
        self.ax_list[0].patch.set_facecolor("black")
        self.ax_list[0].set_title("客座率指数", fontdict={'size': 40})
        for self.size in self.ax_list[0].get_yticklabels():  # 获取y轴上所有坐标，并设置字号
            self.size.set_fontname(' Microsoft YaHei')  # 雅黑
            self.size.set_fontsize('18')
        self.ax_list[0].set_xticks([])

        self.ax_list[1].plot(range(len(self.__x_inland)), self.__y_international, color='orange')
        self.ax_list[1].grid(axis="y", linestyle='--')  # 网格
        self.ax_list[1].patch.set_facecolor("black")
        for self.size in self.ax_list[1].get_yticklabels():  # 获取y轴上所有坐标，并设置字号
            self.size.set_fontname(' Microsoft YaHei')  # 雅黑
            self.size.set_fontsize('18')
        self.ax_list[1].set_xticks([])

        self.ax_list[2].plot(range(len(self.__x_inland)), self.__y_HongKong, color='orange')
        self.ax_list[2].grid(axis="y", linestyle='--')  # 网格
        self.ax_list[2].patch.set_facecolor("black")  # 背景色
        self.ax_list[2].set_xticks([])
        for self.size in self.ax_list[2].get_yticklabels():  # 获取y轴上所有坐标，并设置字号
            self.size.set_fontname(' Microsoft YaHei')  # 雅黑
            self.size.set_fontsize('18')
        self.ax_list[2].set_xticks([])


class PriceIndex(Chart):
    """
    价格指数
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(20, 15)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
        self.fig.gca()
        self.fig.subplots_adjust(wspace=None, hspace=0)  # 调整布局

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax1 = plt.subplot(311)
        ax2 = plt.subplot(312)
        ax3 = plt.subplot(313)
        return [ax1, ax2, ax3]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数
        self.df.sort_values(by=['起飞年', '起飞星期'], inplace=True, ascending=True)
        self.df["time"] = range(0, len(self.df))

        # 设置索引
        self.df.set_index("time", inplace=True)

        # __两个下划线开头的标识符或函数名，为私有，只能在类内部访问(形式上的)
        self.__x_inland = self.df.index
        self.__y_inland = self.df[['国内市场运输量指数']]
        self.__y2_inland = self.df[['国内市场价格指数']]
        self.__x_international = self.df.index
        self.__y_international = self.df[['国际市场运输量指数']]
        self.__y2_international = self.df[['国际市场价格指数']]
        self.__x_HongKong = self.df.index
        self.__y_HongKong = self.df[['港澳台市场运输量指数']]
        self.__y2_HongKong = self.df[['港澳台市场价格指数']]

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据
        self.ax_list[0].plot(range(len(self.__x_inland)), self.__y_inland, color='orange')
        self.ax_list[0].plot(range(len(self.__x_inland)), self.__y2_inland)
        self.ax_list[0].grid(axis="y", linestyle='--')  # 网格
        self.ax_list[0].patch.set_facecolor("black")
        self.ax_list[0].set_title("量价指数", fontdict={'size': 40})
        for self.size in self.ax_list[0].get_yticklabels():  # 获取y轴上所有坐标，并设置字号
            self.size.set_fontname(' Microsoft YaHei')  # 雅黑
            self.size.set_fontsize('18')
        self.ax_list[0].set_xticks([])

        self.ax_list[1].plot(range(len(self.__x_inland)), self.__y_international, color='orange')
        self.ax_list[1].plot(range(len(self.__x_inland)), self.__y2_international)
        self.ax_list[1].grid(axis="y", linestyle='--')  # 网格
        self.ax_list[1].patch.set_facecolor("black")
        for self.size in self.ax_list[1].get_yticklabels():  # 获取y轴上所有坐标，并设置字号
            self.size.set_fontname(' Microsoft YaHei')  # 雅黑
            self.size.set_fontsize('18')
        self.ax_list[1].set_xticks([])

        self.ax_list[2].plot(range(len(self.__x_inland)), self.__y_HongKong, color='orange')
        self.ax_list[2].plot(range(len(self.__x_inland)), self.__y2_HongKong)
        self.ax_list[2].grid(axis="y", linestyle='--')  # 网格
        self.ax_list[2].patch.set_facecolor("black")  # 背景色
        self.ax_list[2].set_xticks([])
        for self.size in self.ax_list[2].get_yticklabels():  # 获取y轴上所有坐标，并设置字号
            self.size.set_fontname(' Microsoft YaHei')  # 雅黑
            self.size.set_fontsize('18')
        self.ax_list[2].set_xticks([])


class InternationalTraveler(Chart):
    """
    国际旅行者
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(20, 15)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
        plt.suptitle("2017年上半年民航国际旅行者特征", fontdict={'size': 40})
        self.fig.gca()
        self.fig.subplots_adjust(wspace=None, hspace=0.15)  # 调整布局

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax1 = plt.subplot(311)
        ax2 = plt.subplot(323)
        ax3 = plt.subplot(324)
        ax4 = plt.subplot(325)
        ax5 = plt.subplot(326)
        return [ax1, ax2, ax3, ax4, ax5]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数
        self.ax2_data = [self.df.loc[self.df['year_id'] == 2017, '国际航线当天预定'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线预订提前1-3'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线预订提前4-7'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线预订提前8-15'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线预订提前16-30'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线预订提前31-60'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线预订提前60+'].mean()]
        self.ax2_labels = ['当天预定', '1-3天', '4-7天', '8-15天', '16-30天', '31-60天', '60天以上']

        self.ax3_data = [self.df.loc[self.df['year_id'] == 2017, '国际航线团队旅客比例'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线自由旅客比例'].mean()]
        self.ax3_labels = ['团队旅客', '自由行旅者']

        self.ax4_people = ['6人及以上', '4-6人', '三人同行', '双人出行', '单独出行']
        self.ax4_y_pos = np.arange(5)
        self.ax4_performance = [self.df.loc[self.df['year_id'] == 2017, '国际航线出行6+'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国际航线出行4-6人'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国际航线出行三人'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国际航线出行双人'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国际航线单独出行'].mean()]

        self.ax5_data = [self.df.loc[self.df['year_id'] == 2017, '国际航线提前值机1小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线提前值机1-3小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线提前值机3-6小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线提前值机6-12小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线提前值机12-24小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国际航线提前值机24+'].mean()]
        self.ax5_ingredients = ['1以内', '1-3小时', '3-6小时', '6-12小时', '12-24小时', '24以上']

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据

        self.ax_list[0].set_title('国际市场旅客目的地偏好')

        self.ax_list[1].bar(range(len(self.ax2_data)), self.ax2_data, tick_label=self.ax2_labels,color=['r','g','b','c','m','y','k'])
        self.ax_list[1].set_title('提前预定天数分布')

        self.ax_list[2].explode = (0, 0)
        self.ax_list[2].pie(self.ax3_data, explode=self.ax_list[2].explode, labels=self.ax3_labels, autopct='%1.1f%%',
                            shadow=True, startangle=90)
        self.ax_list[2].set_title('团队散客比例')

        self.ax_list[3].barh(self.ax4_y_pos, self.ax4_performance, align='center',color=['g','y','c','m','r','k'])
        self.ax_list[3].set_yticks(self.ax4_y_pos)
        self.ax_list[3].set_yticklabels(self.ax4_people)
        self.ax_list[3].invert_yaxis()
        self.ax_list[3].set_title('自由行旅客同行人数分布')

        def func(pct, allvals):
            absolute = int(pct / 100. * np.sum(allvals))
            return "{:.1f}%\n({:d} g)".format(pct, absolute)

        wedges, texts, autotexts = self.ax_list[4].pie(self.ax5_data, autopct=lambda pct: func(pct, self.ax5_data),
                                                       textprops=dict(color="w"))
        self.ax_list[4].legend(wedges, self.ax5_ingredients,
                               loc="center left",
                               bbox_to_anchor=(1, 0, 0.5, 1),)
        self.ax_list[4].set_title("国际提前值机时间分布")


class DomesticTraveler(Chart):
    """
    国内旅行者
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(20, 15)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
        plt.suptitle("2017年上半年民航国内旅行者特征", fontdict={'size': 40})
        self.fig.gca()
        self.fig.subplots_adjust(wspace=None, hspace=0.15)  # 调整布局

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax1 = plt.subplot(331)
        ax2 = plt.subplot(322)
        ax3 = plt.subplot(334)
        ax4 = plt.subplot(324)
        ax5 = plt.subplot(337)
        ax6 = plt.subplot(338)
        ax7 = plt.subplot(339)
        return [ax1, ax2, ax3, ax4, ax5, ax6, ax7]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数

        self.ax1_labels = ['女', '男']
        self.ax1_sizes = [self.df.loc[self.df['year_id'] == 2017, '国内航线女比例'].mean(),
                          self.df.loc[self.df['year_id'] == 2017, '国内航线男比例'].mean()]
        self.ax1_explode = (0, 0)

        self.ax2_data = [self.df.loc[self.df['year_id'] == 2017, '国内航线年龄0-18'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线年龄19-23'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线年龄24-30'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线年龄31-40'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线年龄41-50'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线年龄51-60'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线年龄60+'].mean()]

        self.ax2_labels = ['0-18', '19-23', '24-30', '31-40', '41-50', '51-60', '60+']

        self.ax3_data = [self.df.loc[self.df['year_id'] == 2017, '国内航线当天预定'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线预订提前1-3'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线预订提前4-7'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线预订提前8-15'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线预订提前16-30'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线预订提前31-60'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线预订提前60+'].mean()]
        # self.ax3_data = [7, 10, 19, 23, 18, 12, 11]
        self.ax3_labels = ['当天预定', '1-3天', '4-7天', '8-15天', '16-30天', '31-60天', '60天及以上']

        self.ax4_people = ['6人及以上', '4-6人', '三人同行', '双人出行', '单独出行']
        self.ax4_y_pos = np.arange(5)
        self.ax4_performance = [self.df.loc[self.df['year_id'] == 2017, '国内航线出行6+'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国内航线出行4-6人'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国内航线出行三人'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国内航线出行双人'].mean(),
                                self.df.loc[self.df['year_id'] == 2017, '国内航线单独出行'].mean()]

        self.ax5_labels = ['团队旅客', '自由行旅者']
        self.ax5_sizes = [self.df.loc[self.df['year_id'] == 2017, '国内航线团队旅客比例'].mean(),
                          self.df.loc[self.df['year_id'] == 2017, '国内航线自由旅客比例'].mean()]
        self.ax5_explode = (0, 0)

        self.ax7_data = [self.df.loc[self.df['year_id'] == 2017, '国内航线提前值机1小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线提前值机1-3小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线提前值机3-6小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线提前值机6-12小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线提前值机12-24小时'].mean(),
                         self.df.loc[self.df['year_id'] == 2017, '国内航线提前值机24+'].mean()]
        self.ax7_ingredients = ['1以内', '1-3小时', '3-6小时', '6-12小时', '12-24小时', '24以上']

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据
        self.ax_list[0].pie(self.ax1_sizes, explode=self.ax1_explode, labels=self.ax1_labels, autopct='%1.1f%%',
                            shadow=True, startangle=90)
        self.ax_list[0].set_title('性别分布')

        self.ax_list[1].bar(range(len(self.ax2_data)), self.ax2_data, tick_label=self.ax2_labels,color=['r','g','c','m','y','k','b'])
        self.ax_list[1].set_title('年龄分布')

        self.ax_list[2].bar(range(len(self.ax3_data)), self.ax3_data, tick_label=self.ax3_labels,color=['r','g','c','m','y','k','b'])
        self.ax_list[2].set_title('提前预定天数分布')

        self.ax_list[3].barh(self.ax4_y_pos, self.ax4_performance, align='center',color=['g','y','c','m','r'])
        self.ax_list[3].set_yticks(self.ax4_y_pos)
        self.ax_list[3].set_yticklabels(self.ax4_people)
        self.ax_list[3].invert_yaxis()
        self.ax_list[3].set_title('自由行同行人数分布')

        self.ax_list[4].pie(self.ax5_sizes, explode=self.ax5_explode, labels=self.ax5_labels, autopct='%1.1f%%',
                            shadow=True, startangle=90)
        self.ax_list[4].set_title('团队散客比例')

        def func(pct, allvals):
            absolute = int(pct / 100. * np.sum(allvals))
            return "{:.1f}%\n({:d} g)".format(pct, absolute)

        wedges, texts, autotexts = self.ax_list[6].pie(self.ax7_data, autopct=lambda pct: func(pct, self.ax7_data),
                                                       textprops=dict(color="w"), normalize=False)
        self.ax_list[6].legend(wedges, self.ax7_ingredients,
                               loc="center left",
                               bbox_to_anchor=(1, 0, 0.5, 1))
        self.ax_list[6].set_title("提前值机时间分布")


class JatujakMarket(Chart):
    """
    假日市场概况
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(20, 15)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax = plt.bar
        return [ax]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数
        pass

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据
        pass


class InlandAviation(Chart):
    """
    国内民航表格
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(10, 5)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax1 = plt.subplot(111)
        return [ax1]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数
        self.data = [[int(self.df.loc[self.df['year_id'] == 2017, '国内市场旅客量'].mean()/10000),
                      int(self.df.loc[self.df['year_id'] == 2017, '国内市场客公里'].mean()),
                      round(self.df.loc[self.df['year_id'] == 2017, '国内市场重复购买率'].mean(),2)]]
        self.labels = ["人数（万）",
                       "平均飞行距离（公里）",
                       "重复购买率"]

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据
        self.ax_list[0].axis('tight')
        self.ax_list[0].axis('off')
        self.ax_list[0].table(cellText=self.data,colLabels=self.labels,cellLoc="center",loc="center")
        self.ax_list[0].set_title("2017年上半年民航国内市场旅客概况", fontdict={'size': 40})


class InternationalAviation(Chart):
    """
    国际民航表格
    """

    def __init__(self, df):
        super().__init__(df)

    def _set_fig(self):
        # 设置图像的属性
        self.fig.set_size_inches(10, 5)  # 设置大小
        self.fig.set_dpi(80)  # 设置dpi
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码

    def _append_ax_list(self) -> List[Axes]:
        # 创建ax 放入ax_list列表
        ax1 = plt.subplot(111)
        return [ax1]

    def _process_df(self):
        # 处理数据，生成建立ax所需的参数
        self.data = [[int(self.df.loc[self.df['year_id'] == 2017, '国际市场旅客量'].mean()/1000),
                      int(self.df.loc[self.df['year_id'] == 2017, '国际市场客公里'].mean()),
                      round(self.df.loc[self.df['year_id'] == 2017, '国际市场重复购买率'].mean(),2)]]
        self.labels = ["人数（万）",
                       "平均飞行距离（公里）",
                       "重复购买率"]

    def _process_ax_list(self):
        # 设置ax_list中ax的样式，并添加数据
        self.ax_list[0].axis('tight')
        self.ax_list[0].axis('off')
        self.ax_list[0].table(cellText=self.data, colLabels=self.labels,cellLoc="center", loc="center")
        self.ax_list[0].set_title("2017年上半年民航国际市场旅客概况", fontdict={'size': 40})
