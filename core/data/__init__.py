import pandas as pd
import random

from core.data.data import ProsperityIndex, PassengerLoadFactor, VolumePriceIndex, PassengerSize, \
    PassengerCharacteristics


class Data:

    def __init__(self, d: dict):
        self.__data = d

    def prosperity_index_in_number(self, year):
        """
        .. note::

                获取国内景气指数

        :return: 景气指数
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.peek_average(year, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def prosperity_index_foreign_number(self, year):
        """
        .. note::

                获取国外景气指数

        :return: 景气指数
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.peek_average(year, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def prosperity_index_hkm_number(self, year):
        """
        .. note::

                获取港澳台景气指数

        :return: 景气指数
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.peek_average(year, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def maximum_Year(self):
        """
        .. note::

                求最大年份的函数

        :return: 最大年
        """
        df = self.__data['景气指数']
        pi = pd.DataFrame(df)
        Max = pi['起飞年'].max()
        return Max - 1

    @staticmethod
    def route():
        """
         .. note::

                航线的数量

        :return: 航线
        """
        number = random.randint(110, 190)
        return number

    @staticmethod
    def increase(result):
        """
         .. note::

                判断数据上升还是下降

        :param result:  a
        :return: 数据上升还是下降
        """
        goup = ["上升", "上涨", "升高"]
        drop = ["下降", "降低", "下滑"]
        if isinstance(result, dict):
            if result['Y'][0] > 0:
                a = random.choice(goup)
                return a
            else:
                a = random.choice(drop)
                return a
        else:
            if result > 0:
                a = random.choice(goup)
                return a
            else:
                a = random.choice(drop)
                return a

    def prosperity_index_compare(self):
        """
        .. note::

                比较今明两年景气指数的差值

        :return: 差值
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.peek_average(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = pi.peek_average(self.maximum_Year() - 1, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        difference = ll['Y'][0] - lll['Y'][0]
        result = self.increase(difference)
        return result

    def prosperity_index_compare_hmk(self):
        """
        .. note::

                比较今明两年港澳台景气指数的差值

        :return: 差值
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.peek_average(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = pi.peek_average(self.maximum_Year() - 1, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        difference = ll['Y'][0] - lll['Y'][0]
        result = self.increase(difference)
        return result

    def prosperity_index_domestic_yoy(self):
        """
        .. note::

                计算国内景气指数同比增幅

        :return: 景气指数同比增幅
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.yoy(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def prosperity_index_foreign_yoy(self):
        """
        .. note::

                计算国外景气指数同比增幅

        :return: 景气指数同比增幅
         """
        # 当前使用国内数据
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.yoy(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def prosperity_index_hkm_yoy(self):
        """
        .. note::

                计算港澳台景气指数同比增幅

        :return: 景气指数同比增幅
        """
        # 当前使用国内数据
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.yoy(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def domestic_prosperity_index_yoy_compare(self):
        """
        .. note::

                计算国内景气指数同比增幅的比较

        :return: 差值
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.yoy(self.maximum_Year() - 1, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = pi.yoy(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        difference = lll['Y'][0] - ll['Y'][0]
        result = '%.2f' % difference
        return result

    def domestic_prosperity_index_yoy(self):
        """
        .. note::

                计算国内景气指数同比增幅的比较

        :return: 比较
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.yoy(self.maximum_Year() - 1, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = pi.yoy(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        difference = lll['Y'][0] - ll['Y'][0]
        result = self.increase(difference)
        return result

    def hkm_prosperity_index_index_compare(self):
        """
        .. note::

                计算港澳台景气指数的比较

        :return: 差值
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.peek_average(self.maximum_Year() - 1, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = pi.peek_average(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        difference = lll['Y'][0] - ll['Y'][0]
        result = '%.2f' % difference
        return result

    def hkm_prosperity_index_yoy_compare(self):
        """
        .. note::

                计算港澳台景气指数同比增幅的比较

        :return: 差值
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.yoy(self.maximum_Year() - 1, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = pi.yoy(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        difference = lll['Y'][0] - ll['Y'][0]
        result = '%.2f' % difference
        return result

    def foreign_springFestival_max(self):
        """
        .. note::

                计算国外春节时期景气指数的峰值

        :return: 峰值
        """
        df = self.__data['景气指数']
        pi = ProsperityIndex(df, "景气指数")
        ll = pi.peak_max(self.maximum_Year(), ref_type="W", ref_label='起飞星期', req={"M": [2]})
        return '%.2f' % ll['M'][0]

    def passenger_load_factor(self, market_):
        """
          .. note::

                比较前后两年的客座率，得出差值

        :param market_: 地区
        :return: 差值
        """
        df = self.__data['市场数据']
        plf = PassengerLoadFactor(df)
        l = plf.peek_mean(self.maximum_Year() - 1, market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
        ll = plf.peek_mean(self.maximum_Year(), market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
        dif = ll['Y'][0] - l['Y'][0]
        return '%.2f' % dif

    def passenger_load_factor_yoy_compare(self, market_):
        """
          .. note::

                比较前后两年的客座率同比增幅，得出差值

        :param market_: 地区
        :return: 差值
        """
        df = self.__data['市场数据']
        plf = PassengerLoadFactor(df)
        l = plf.yoy(self.maximum_Year() - 1, market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
        ll = plf.yoy(self.maximum_Year(), market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
        dif = ll['Y'][0] - l['Y'][0]
        return '%.2f' % dif

    def passenger_load_factor_index(self, market_):
        """
          .. note::

                各地区客座率的值

        :param market_: 地区
        :return: 各地区客座率
        """
        df = self.__data['市场数据']
        plf = PassengerLoadFactor(df)
        ll = plf.peek_mean(self.maximum_Year(), market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def passenger_load_factor_yoy(self, market_):
        """
          .. note::

                各地区客座率的同比增幅

        :param market_: 地区
        :return: 各地区客座率同比增幅
        """
        df = self.__data['市场数据']
        plf = PassengerLoadFactor(df)
        ll = plf.yoy(self.maximum_Year(), market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def volume_price_index_average(self, year, exponent):
        """
          .. note::

                计算量价指数的平均值

        :param year: 年份
        :param exponent: 指数的索引
        :return: 平均值
        """
        df = self.__data['量价指数']
        plf = VolumePriceIndex(df)
        ll = plf.peak_average(year, exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def volume_price_index_yoy(self, year, exponent):
        """
          .. note::

                计算量价指数的同比增幅

        :param year: 年份
        :param exponent: 指数的索引
        :return: 同比增幅
        """
        df = self.__data['量价指数']
        plf = VolumePriceIndex(df)
        ll = plf.yoy(year, exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def volume_price_index_max(self, year, exponent):
        """
          .. note::

                计算量价指数的最大值

        :param year: 年份
        :param exponent: 指数的索引
        :return: 最大值
        """
        df = self.__data['量价指数']
        plf = VolumePriceIndex(df)
        ll = plf.peak_max(year, exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def volume_price_index_min(self, year, exponent):
        """
          .. note::

                计算量价指数的最小值

        :param year: 年份
        :param exponent: 指数的索引
        :return: 最小值
        """
        df = self.__data['量价指数']
        plf = VolumePriceIndex(df)
        ll = plf.peak_min(year, exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def volume_price_index_trend_rate(self, exponent):
        """
          .. note::

                量价指数今明两年的变化趋势的差值

        :param exponent: 指数的索引
        :return: 变化趋势的差值
        """
        df = self.__data['量价指数']
        plf = VolumePriceIndex(df)
        ll = plf.peak_average(self.maximum_Year() - 1, exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = plf.peak_average(self.maximum_Year(), exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        result = lll['Y'][0] - ll['Y'][0]
        return '%.2f' % result

    def volume_price_index_trend(self, exponent):
        """
          .. note::

                量价指数今明两年的变化趋势

        :param exponent: 指数的索引
        :return: 变化趋势
        """
        df = self.__data['量价指数']
        plf = VolumePriceIndex(df)
        ll = plf.peak_average(self.maximum_Year() - 1, exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        lll = plf.peak_average(self.maximum_Year(), exponent, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
        difference = lll['Y'][0] - ll['Y'][0]
        result = self.increase(difference)
        return result

    def passengerSize(self, counts, year):
        """
          .. note::

                国内外旅客规模

        :param year: 年份
        :param counts: 索引
        :return: 旅客规模
        """
        df = self.__data['旅客规模']
        plf = PassengerSize(df)
        ll = plf.peak_sum(year, counts, ref_type="M", ref_label='month_id', req={"Y": [1]})
        return ll['Y'][0]

    def passenger_size_yoy(self, counts):
        """
          .. note::

                国内外旅客规模同比增幅

        :param counts: 索引
        :return: 同比增幅
        """
        df = self.__data['旅客规模']
        plf = PassengerSize(df)
        ll = plf.yoy(self.maximum_Year(), counts, ref_type="M", ref_label='month_id', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def passenger_size_average(self, year, counts):
        """
          .. note::

                国内外旅客规模平均公里

        :param year: 年份
        :param counts: 索引
        :return: 国内外旅客规模平均公里
        """
        df = self.__data['旅客规模']
        plf = PassengerSize(df)
        ll = plf.peak_average(year, counts, ref_type="M", ref_label='month_id', req={"Y": [1]})
        return round(ll['Y'][0])

    def repeat_purchase_rate_per_capita(self, year, counts):
        """
          .. note::

                国内外航线人均重复购买率

        :param year: 年份
        :param counts: 索引
        :return: 国内外航线人均重复购买率
        """
        df = self.__data['旅客规模']
        plf = PassengerSize(df)
        ll = plf.peak_average(year, counts, ref_type="M", ref_label='month_id', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def tourism_characteristics_average(self, year, counts):
        """
          .. note::

                旅客特征各项的平均值

        :param year: 年份
        :param counts: 索引
        :return: 旅客特征各项的平均值
        """
        df = self.__data['旅客特征']
        plf = PassengerCharacteristics(df)
        ll = plf.peak_average(year, counts, ref_type="M", ref_label='month_id', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]

    def tourism_characteristics_yoy(self, year, counts):
        """
          .. note::

                旅客特征各项的同比增幅

        :param year: 年份
        :param counts: 索引
        :return: 旅客特征各项的同比增幅
        """
        df = self.__data['旅客特征']
        plf = PassengerCharacteristics(df)
        ll = plf.yoy(year, counts, ref_type="M", ref_label='month_id', req={"Y": [1]})
        return '%.2f' % ll['Y'][0]
