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


class ProsperityIndex(MathOperation, DateUtils):
    """
    ::

        关于景气指数的模块,涉及同比，最大值和最小值。
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
                        print(weeks)
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
                        v.append(self.__peek_max(year_label, year, ref_label, weeks))
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



