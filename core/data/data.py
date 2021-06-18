import pandas as pd
from pandas import DataFrame
from calendar import Calendar


class DateUtils:
    """
    ::

         计算日期
    """
    _months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def __init__(self):
        pass

    @staticmethod
    def _weeks_of_year_in_month(year, month):
        """
        .. note::

                 返回给定年份中给定月份中星期的列表

        :param year: 这是必填参数，用于指定日历的年份。
        :param month: 这是必填参数，用于指定日历的月份。
        :return: - 它返回给定年月份中由7个日期对象组成的星期列表
        """
        c = Calendar()
        _ = []
        for week_list in c.monthdatescalendar(year, month):
            y, w_n, wd = week_list[0].isocalendar()
            if y == year:
                _.append(w_n)
        _ = list(set(_))
        _.sort()
        return _

    def _weeks_of_year_in_quarter(self, year, quarter):
        """
        .. note::

                返回给定年份中该季度星期的列表

        :param year: 这是必填参数，用于指定日历的年份。
        :param quarter: 这是必填参数，表示年份的季度。
        :return: - 它返回给定年份中那一季度的由7个日期对象组成的星期列表
        """
        month_l = self._months[quarter * 3 - 3:quarter * 3]
        _ = []
        for month in month_l:
            _.extend(self._weeks_of_year_in_month(year, month))
        _ = list(set(_))
        _.sort()
        return _

    def _weeks_of_year_in_half_year(self, year, half_year):
        """
        .. note::

                 返回给定年份中上半年或下半年的星期列表

        :param year: 这是必填参数，用于指定日历的年份。
        :param half_year: 这是必填参数，表示年份的上半年或下半年。
        :return: - 它返回给定年份中上半年或下半年由7个日期对象组成的星期列表
        """
        _ = []
        for i in range(half_year * 2 - 1, half_year * 2 + 1):
            _.extend(self._weeks_of_year_in_quarter(year, i))
        _ = list(set(_))
        _.sort()
        return _

    def _months_of_year_in_quarter(self, quarter):
        """
         .. note::

                 返回给定季度的月份列表

        :param quarter: 这是必填参数，用于指定季度。
        :return: - 返回给定季度的月份列表
        """
        month_l = self._months[quarter * 3 - 3:quarter * 3]
        _ = []
        for month in month_l:
            _.append(month)
        _ = list(set(_))
        _.sort()
        return _

    def _months_of_year_half_year(self, half_year):
        """
        .. note::

                 返回上半年或下半年的月份列表

        :param half_year: 这是必填参数，表示上半年或下半年。
        :return: - 返回上半年或下半年的月份列表
        """
        _ = []
        for i in range(half_year * 2 - 1, half_year * 2 + 1):
            _.extend(self._months_of_year_in_quarter(i))
        _ = list(set(_))
        _.sort()
        return _


class MathOperation:
    """
    ::

        数学运算
    """

    @staticmethod
    def sum(data_list: list):
        """
        .. note::

                 对列表进行求和计算。

        :param data_list: 可迭代对象,列表
        :return: - 列表的总和
        """
        return pd.DataFrame(data_list)[0].sum()

    @staticmethod
    def min(data_list: list):
        """
        .. note::

                返回最小数

        :param data_list: 可迭代对象,列表
        :return: - 列表的最小值
        """
        return pd.DataFrame(data_list)[0].min()

    @staticmethod
    def max(data_list: list):
        """
        .. note::

             返回最大数

        :param data_list: 可迭代对象,列表
        :return: - 列表的最大值
        """
        return pd.DataFrame(data_list)[0].max()

    @staticmethod
    def mean(data_list: list):
        """
        .. note::

             返回一个平均值

        :param data_list: 可迭代对象,列表
        :return: - 列表的平均值
        """
        return pd.DataFrame(data_list)[0].mean()

    @staticmethod
    def variance(data_list: list):
        """
        .. note::

             返回一个方差

        :param data_list: 可迭代对象,列表
        :return: - 列表的方差
        """
        return pd.DataFrame(data_list)[0].var()


class ProsperityIndex(MathOperation, DateUtils):
    """
    ::

        关于景气指数的模块,涉及同比，峰值，最大值和最小值,平均值
    """

    def __init__(self, df: DataFrame, prosperity_index_label='景气指数'):
        super().__init__()
        self.__df = df
        self.__prosperity_index_label = prosperity_index_label

    def yoy(self, year, year_label='起飞年', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             同比

        :param year: 年份
        :param year_label: 年份的索引，默认值 ： 起飞年
        :param ref_type: 参考列的类型，目前只有W  "W"=星期
        :param ref_label: 参考列的索引：起飞星期
        :param req: 计算的周期:半年、季度、周
        :return: - 同比
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__yoy(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__yoy(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__yoy(year_label, year, ref_label, weeks))
                result[key] = v
        return result

    def peak_max(self, year, year_label='起飞年', ref_type=None, ref_label=None, req: dict = None):
        """
        .. note::

             最大值

        :param year: 年份
        :param year_label: 年份的索引，默认值 ： 起飞年
        :param ref_type: 参考列的类型，目前只有W  "W"=星期
        :param ref_label: 参考列的索引：起飞星期
        :param req: 比较的周期:半年、季度、周
        :return: - 最大值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__peek_max(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__peek_max(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__peek_max(year_label, year, ref_label, weeks))
                result[key] = v
        return result

    def peak_min(self, year, year_label='起飞年', ref_type=None, ref_label=None, req: dict = None):
        """
        .. note::

            最小值

        :param year: 年份
        :param year_label: 年份的索引，默认值 ： 起飞年
        :param ref_type: 参考列的类型，目前只有W  "W"=星期
        :param ref_label: 参考列的索引：起飞星期
        :param req: 比较的周期:半年、季度、周
        :return: - 最小值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__peek_min(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__peek_min(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__peek_min(year_label, year, ref_label, weeks))
                result[key] = v
        return result

    def peek_average(self, year, year_label='起飞年', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

            平均值

        :param year: 年份
        :param year_label: 年份的索引，默认值 ： 起飞年
        :param ref_type: 参考列的类型，目前只有W  "W"=星期
        :param ref_label: 参考列的索引：起飞星期
        :param req: 比较的周期:半年、季度、周
        :return: - 平均值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__peek_average(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__peek_average(year_label, year, ref_label, weeks))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__peek_average(year_label, year, ref_label, weeks))
                result[key] = v
        return result

    def __yoy(self, year_label, year, ref_label, ref_type_data):
        """
        .. note::

            计算同比增长率

        :param year_label: 年份的索引，默认值 ： 起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :return: - 同比增长率
        """
        current = self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__prosperity_index_label].sum()
        previous = self.__df[self.__df[year_label].isin([year - 1]) & self.__df[ref_label].isin(ref_type_data)][
            self.__prosperity_index_label].sum()
        return ((current - previous) / previous) * 100

    def __peek_max(self, year_label, year, ref_label, ref_type_data):
        """
        .. note::

            求最大值的函数

        :param year_label: 年份的索引，默认值 ： 起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :return: - 最大值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__prosperity_index_label].max()

    def __peek_min(self, year_label, year, ref_label, ref_type_data):
        """
        .. note::

            求最小值的函数

        :param year_label: 年份的索引，默认值 ： 起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :return: - 最小值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__prosperity_index_label].min()

    def __peek_average(self, year_label, year, ref_label, ref_type_data):
        """
        .. note::

            求平均值的函数

        :param year_label: 年份的索引，默认值 ： 起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :return: - 平均值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__prosperity_index_label].mean()


class VolumePriceIndex(MathOperation, DateUtils):
    """
    ::

        量价指数
    """

    def __init__(self, df: DataFrame, traffic_index_label='运输量指数', price_index_label='价格指数',
                 domestic_market_traffic_index_label='国内市场运输量指数', international_market_traffic_index_label='国际市场运输量指数',
                 hmt_market_traffic_index_label='港澳台市场运输量指数', domestic_market_price_index_label='国内市场价格指数',
                 international_market_price_index_label='国际市场价格指数', hmt_market_price_index_label='港澳台市场价格指数'):
        super().__init__()
        self.__df = df
        self.__traffic_index_label = traffic_index_label
        self.__price_index_label = price_index_label
        self.__domestic_market_traffic_index_label = domestic_market_traffic_index_label
        self.__international_market_traffic_index_label = international_market_traffic_index_label
        self.__hmt_market_traffic_index_label = hmt_market_traffic_index_label
        self.__domestic_market_price_index_label = domestic_market_price_index_label
        self.__international_market_price_index_label = international_market_price_index_label
        self.__hmt_market_price_index_label = hmt_market_price_index_label
        self.__exponent = [self.__traffic_index_label, self.__price_index_label,
                           self.__domestic_market_traffic_index_label, self.__international_market_traffic_index_label,
                           self.__hmt_market_traffic_index_label, self.__domestic_market_price_index_label,
                           self.__international_market_price_index_label, self.__hmt_market_price_index_label]

    def yoy(self, year, counts, year_label='起飞年', ref_type=None, ref_label=None,
            req: dict = None):
        """
         .. note::

             同比增幅

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型
        :param ref_label: 参考列的索引：起飞星期
        :param req: 计算的周期:半年、季度、周
        :return: - 同比
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__yoy(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__yoy(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__yoy(year_label, year, ref_label, weeks, counts))
                result[key] = v
        return result

    def peak_max(self, year, counts, year_label='起飞年', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             最大值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，目前只有W  "W"=星期
        :param ref_label: 参考列的索引：起飞星期
        :param req: 计算的周期:半年、季度、周
        :return: - 最大值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__peek_max(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__peek_max(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__peek_max(year_label, year, ref_label, weeks, counts))
                result[key] = v
        return result

    def peak_min(self, year, counts, year_label='起飞年', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             最小值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，目前只有W  "W"=星期
        :param ref_label: 参考列的索引：起飞星期
        :param req: 计算的周期:半年、季度、周
        :return: - 最小值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__peek_min(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__peek_min(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__peek_min(year_label, year, ref_label, weeks, counts))
                result[key] = v
        return result

    def peak_average(self, year, counts, year_label='起飞年', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             平均值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，目前只有W  "W"=星期
        :param ref_label: 参考列的索引：起飞星期
        :param req: 计算的周期:半年、季度、周
        :return: - 平均值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_month(year, i)
                        v.append(self.__peek_average(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_quarter(year, i)
                        v.append(self.__peek_average(year_label, year, ref_label, weeks, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'W' and i > 0:
                        weeks = self._weeks_of_year_in_half_year(year, i)
                        v.append(self.__peek_average(year_label, year, ref_label, weeks, counts))
                result[key] = v
        return result

    def __yoy(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求同比增幅的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :param counts: 数组exponent中的索引
        :return: - 同比增幅
        """
        current = self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()
        previous = self.__df[self.__df[year_label].isin([year - 1]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()
        return ((current - previous) / previous) * 100

    def __peek_max(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求最大值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :param counts: 数组exponent中的索引
        :return: - 最大值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].max()

    def __peek_min(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求最小值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :param counts: 数组exponent中的索引
        :return: - 最小值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].min()

    def __peek_average(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求平均值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞星期
        :param ref_type_data: 周
        :param counts: 数组exponent中的索引
        :return: - 平均值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].mean()


class PassengerLoadFactor(MathOperation, DateUtils):
    """
    ::

        客座率
    """

    def __init__(self, df: DataFrame, passenger_load_factor_label='客座率'):
        super().__init__()
        self.__df = df
        self.__passenger_load_factor_label = passenger_load_factor_label

    def yoy(self, year, year_label='year_id', market=None, market_label='market_id', ref_type=None, ref_label=None,
            req: dict = None):
        """
        .. note::

            同比

        :param year: 年份
        :param year_label: 年份的索引，默认值 =  year_id
        :param market: 地区
        :param market_label: 默认值 =  market_id
        :param ref_type: 参考列类型：月份 M
        :param ref_label: 参考列索引 month_id
        :param req: 计算的周期:半年、季度、周
        :return: - 同比
        """
        r = req

        market_list = list(self.__df[market_label].drop_duplicates())

        market_list_len = len(market_list)

        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = [i]
                            v.append(self.__yoy(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_in_quarter(i)
                            v.append(self.__yoy(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_half_year(i)
                            v.append(self.__yoy(year_label, year, ref_label, months, market, market_label))
                result[key] = v
        return result

    def peek_max(self, year, year_label='year_id', market=None, market_label='market_id', ref_type=None, ref_label=None,
                 req: dict = None):
        """
        .. note::

            最大值

        :param year: 年份
        :param year_label: 年份的索引，默认值 =  year_id
        :param market: 地区
        :param market_label: 默认值 =  market_id
        :param ref_type: 参考列类型：月份 M
        :param ref_label: 参考列索引 month_id
        :param req: 计算的周期:半年、季度、周
        :return: - 最大值
        """
        r = req

        market_list = list(self.__df[market_label].drop_duplicates())

        market_list_len = len(market_list)

        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = [i]
                            v.append(self.__peek_max(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_in_quarter(i)
                            v.append(self.__peek_max(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_half_year(i)
                            v.append(self.__peek_max(year_label, year, ref_label, months, market, market_label))
                result[key] = v
        return result

    def peek_min(self, year, year_label='year_id', market=None, market_label='market_id', ref_type=None, ref_label=None,
                 req: dict = None):
        """
        .. note::

            最小值

        :param year: 年份
        :param year_label: 年份的索引，默认值 =  year_id
        :param market: 地区
        :param market_label: 默认值 =  market_id
        :param ref_type: 参考列类型：月份 M
        :param ref_label: 参考列索引 month_id
        :param req: 计算的周期:半年、季度、周
        :return: - 最小值
        """
        r = req

        market_list = list(self.__df[market_label].drop_duplicates())

        market_list_len = len(market_list)

        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = [i]
                            v.append(self.__peek_min(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_in_quarter(i)
                            v.append(self.__peek_min(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_half_year(i)
                            v.append(self.__peek_min(year_label, year, ref_label, months, market, market_label))
                result[key] = v
        return result

    def peek_var(self, year, year_label='year_id', market=None, market_label='market_id', ref_type=None, ref_label=None,
                 req: dict = None):
        """
        .. note::

            方差

        :param year: 年份
        :param year_label: 年份的索引，默认值 =  year_id
        :param market: 地区
        :param market_label: 默认值 =  market_id
        :param ref_type: 参考列类型：月份 M
        :param ref_label: 参考列索引 month_id
        :param req: 计算的周期:半年、季度、周
        :return: - 方差
        """
        r = req

        market_list = list(self.__df[market_label].drop_duplicates())

        market_list_len = len(market_list)

        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = [i]
                            v.append(self.__peek_var(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_in_quarter(i)
                            v.append(self.__peek_var(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_half_year(i)
                            v.append(self.__peek_var(year_label, year, ref_label, months, market, market_label))
                result[key] = v
        return result

    def peek_mean(self, year, year_label='year_id', market=None, market_label='market_id', ref_type=None,
                  ref_label=None,
                  req: dict = None):
        """
        .. note::

            平均值

        :param year: 年份
        :param year_label: 年份的索引，默认值 =  year_id
        :param market: 地区
        :param market_label: 默认值 =  market_id
        :param ref_type: 参考列类型：月份 M
        :param ref_label: 参考列索引 month_id
        :param req: 计算的周期:半年、季度、周
        :return: - 平均值
        """
        r = req

        market_list = list(self.__df[market_label].drop_duplicates())

        market_list_len = len(market_list)

        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = [i]
                            v.append(self.__peek_mean(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_in_quarter(i)
                            v.append(self.__peek_mean(year_label, year, ref_label, months, market, market_label))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    for m in range(market_list_len):
                        if ref_type == 'M' and market == market_list[m] and i > 0:
                            months = self._months_of_year_half_year(i)
                            v.append(self.__peek_mean(year_label, year, ref_label, months, market, market_label))
                result[key] = v
        return result

    def __yoy(self, year_label, year, ref_label, ref_type_data, market, market_label):
        """
        .. note::

            同比增长率

        :param year_label: 参考列索引
        :param year: 年份
        :param ref_label: 参考列索引
        :param ref_type_data: months
        :param market: 地区
        :param market_label: 参考列索引
        :return: - 同比增长率
        """
        current = self.__df[
            self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data) & self.__df[
                market_label].isin(
                [market])][
            self.__passenger_load_factor_label].sum()
        previous = self.__df[
            self.__df[year_label].isin([year - 1]) & self.__df[ref_label].isin(ref_type_data) & self.__df[
                market_label].isin(
                [market])][
            self.__passenger_load_factor_label].sum()
        return ((current - previous) / previous) * 100

    def __peek_max(self, year_label, year, ref_label, ref_type_data, market, market_label):
        """
        .. note::

            求最大值函数

        :param year_label: 参考列索引
        :param year: 年份
        :param ref_label: 参考列索引
        :param ref_type_data: months
        :param market: 地区
        :param market_label: 参考列索引
        :return: - 最大值
        """
        return self.__df[
                   self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data) & self.__df[
                       market_label].isin(
                       [market])][self.__passenger_load_factor_label].max() * 100

    def __peek_min(self, year_label, year, ref_label, ref_type_data, market, market_label):
        """
         .. note::

            求最小值函数

        :param year_label: 参考列索引
        :param year: 年份
        :param ref_label: 参考列索引
        :param ref_type_data: months
        :param market: 地区
        :param market_label: 参考列索引
        :return: - 最小值
        """
        return self.__df[
                   self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data) & self.__df[
                       market_label].isin(
                       [market])][self.__passenger_load_factor_label].min() * 100

    def __peek_var(self, year_label, year, ref_label, ref_type_data, market, market_label):
        """
         .. note::

            求方差函数

        :param year_label: 参考列索引
        :param year: 年份
        :param ref_label: 参考列索引
        :param ref_type_data: months
        :param market: 地区
        :param market_label: 参考列索引
        :return: - 方差
        """
        return self.__df[
                   self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data) & self.__df[
                       market_label].isin(
                       [market])][self.__passenger_load_factor_label].var() * 100

    def __peek_mean(self, year_label, year, ref_label, ref_type_data, market, market_label):
        """
         .. note::

            求平均值函数

        :param year_label: 参考列索引
        :param year: 年份
        :param ref_label: 参考列索引
        :param ref_type_data: months
        :param market: 地区
        :param market_label: 参考列索引
        :return: - 平均值
        """
        return self.__df[
                   self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data) & self.__df[
                       market_label].isin(
                       [market])][self.__passenger_load_factor_label].mean() * 100


class PassengerSize(MathOperation, DateUtils):
    """
    ::

        旅客规模
    """

    def __init__(self, df: DataFrame, passenger_volume='旅客量', off_kilometers='客公里',
                 repeat_purchase_rate='重复购买率', domestic_market_passenger_volume='国内市场旅客量',
                 international_market_passenger_volume='国际市场旅客量', domestic_market_passenger_kilometers=
                 '国内市场客公里', international_market_passenger_kilometers='国际市场客公里',
                 repeat_purchase_rate_in_the_domestic_market='国内市场重复购买率',
                 repeat_purchase_rate_in_the_international_market='国际市场重复购买率'):
        super().__init__()
        self.__df = df
        self._passenger_volume = passenger_volume
        self._off_kilometers = off_kilometers
        self._repeat_purchase_rate = repeat_purchase_rate
        self._domestic_market_passenger_volume = domestic_market_passenger_volume
        self._international_market_passenger_volume = international_market_passenger_volume
        self._domestic_market_passenger_kilometers = domestic_market_passenger_kilometers
        self._international_market_passenger_kilometers = international_market_passenger_kilometers
        self._repeat_purchase_rate_in_the_domestic_market = repeat_purchase_rate_in_the_domestic_market
        self._repeat_purchase_rate_in_the_international_market = repeat_purchase_rate_in_the_international_market
        self.__exponent = [self._passenger_volume, self._off_kilometers, self._repeat_purchase_rate,
                           self._domestic_market_passenger_volume, self._international_market_passenger_volume,
                           self._domestic_market_passenger_kilometers, self._international_market_passenger_kilometers,
                           self._repeat_purchase_rate_in_the_domestic_market,
                           self._repeat_purchase_rate_in_the_international_market]

    def yoy(self, year, counts, year_label='year_id', ref_type=None, ref_label=None,
            req: dict = None):
        """
         .. note::

             同比增幅

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型,月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 同比
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__yoy(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__yoy(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__yoy(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_max(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             最大值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 最大值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_max(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_max(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_max(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_min(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             最小值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 最小值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_min(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_min(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_min(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_sum(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             求和

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 求和
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_sum(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_sum(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_sum(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_average(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             平均值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 平均值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_average(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_average(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_average(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def __yoy(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求同比增幅的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 同比增幅
        """
        current = self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()
        previous = self.__df[self.__df[year_label].isin([year - 1]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()
        return ((current - previous) / previous) * 100

    def __peek_max(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求最大值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 最大值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].max()

    def __peek_min(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求最小值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 最小值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].min()

    def __peek_sum(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求和的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 和
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()

    def __peek_average(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求平均值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 平均值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].mean()


class PassengerCharacteristics(MathOperation, DateUtils):
    """
    ::

        旅客特征
    """

    def __init__(self, df: DataFrame, percentage_of_males_on_domestic_routes='国内航线男比例',
                 proportion_of_women_on_domestic_routes='国内航线女比例', age_24_30_on_domestic_routes='国内航线年龄24-30',
                 age_60_on_domestic_routes='国内航线年龄60+', domestic_flight_booking_1_3_in_advance=
                 '国内航线预订提前1-3', domestic_flight_booking_16_30_in_advance='国内航线预订提前16-30',
                 percentage_of_domestic_flight_team_passengers='国内航线团队旅客比例',
                 domestic_flight_counter_check_in='国内航线柜台值机', check_in_for_domestic_flights_1_3_hours_in_advance
                 ='国内航线提前值机1-3小时'):
        super().__init__()
        self.__df = df
        self._percentage_of_males_on_domestic_routes = percentage_of_males_on_domestic_routes
        self._proportion_of_women_on_domestic_routes = proportion_of_women_on_domestic_routes
        self.age_24_30_on_domestic_routes = age_24_30_on_domestic_routes
        self.age_60_on_domestic_routes = age_60_on_domestic_routes
        self.domestic_flight_booking_1_3_in_advance = domestic_flight_booking_1_3_in_advance
        self.domestic_flight_booking_16_30_in_advance = domestic_flight_booking_16_30_in_advance
        self.percentage_of_domestic_flight_team_passengers = percentage_of_domestic_flight_team_passengers
        self.domestic_flight_counter_check_in = domestic_flight_counter_check_in
        self.check_in_for_domestic_flights_1_3_hours_in_advance = check_in_for_domestic_flights_1_3_hours_in_advance
        self.__exponent = [self._percentage_of_males_on_domestic_routes, self._proportion_of_women_on_domestic_routes,
                           self.age_24_30_on_domestic_routes, self.age_60_on_domestic_routes,
                           self.domestic_flight_booking_1_3_in_advance, self.domestic_flight_booking_16_30_in_advance,
                           self.percentage_of_domestic_flight_team_passengers, self.domestic_flight_counter_check_in,
                           self.check_in_for_domestic_flights_1_3_hours_in_advance]

    def yoy(self, year, counts, year_label='year_id', ref_type=None, ref_label=None,
            req: dict = None):
        """
         .. note::

             同比增幅

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型,月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 同比
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__yoy(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__yoy(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__yoy(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_max(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             最大值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 最大值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_max(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_max(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_max(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_min(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             最小值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 最小值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_min(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_min(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_min(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_sum(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             求和

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 求和
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_sum(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_sum(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_sum(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def peak_average(self, year, counts, year_label='year_id', ref_type=None, ref_label=None, req: dict = None):
        """
         .. note::

             平均值

        :param year: 年份
        :param counts: 数组exponent中的索引
        :param year_label: 参考列的索引：起飞年
        :param ref_type: 参考列的类型，月
        :param ref_label: 参考列的索引：起飞月
        :param req: 计算的周期:半年、季度、周
        :return: - 平均值
        """
        r = req
        result = {}
        for key, value in r.items():
            if key == 'M':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = [i]
                        v.append(self.__peek_average(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Q':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_in_quarter(i)
                        v.append(self.__peek_average(year_label, year, ref_label, months, counts))
                result[key] = v
            elif key == 'Y':
                v = []
                for i in value:
                    if ref_type == 'M' and i > 0:
                        months = self._months_of_year_half_year(i)
                        v.append(self.__peek_average(year_label, year, ref_label, months, counts))
                result[key] = v
        return result

    def __yoy(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求同比增幅的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 同比增幅
        """
        current = self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()
        previous = self.__df[self.__df[year_label].isin([year - 1]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()
        if previous != 0:
            return ((current - previous) / previous) * 100
        else:
            return 0

    def __peek_max(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求最大值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 最大值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].max()

    def __peek_min(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求最小值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 最小值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].min()

    def __peek_sum(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求和的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 和
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].sum()

    def __peek_average(self, year_label, year, ref_label, ref_type_data, counts):
        """
         .. note::

             求平均值的函数

        :param year_label: 参考列的索引：起飞年
        :param year: 年份
        :param ref_label: 参考列的索引：起飞月
        :param ref_type_data: 月
        :param counts: 数组exponent中的索引
        :return: - 平均值
        """
        return self.__df[self.__df[year_label].isin([year]) & self.__df[ref_label].isin(ref_type_data)][
            self.__exponent[counts]].mean()
