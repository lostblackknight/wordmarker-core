import unittest

import pandas as pd

from core.data.data import ProsperityIndex, DateUtils, PassengerLoadFactor, VolumePriceIndex, PassengerSize


class MyTestCase(unittest.TestCase):

    # def test(self):
    #     df = pd.read_csv('../data/in/市场数据_加盐.csv')
    #
    #     plf = PassengerLoadFactor(df)
    #
    #     ll = plf.yoy(2017, market='国内', ref_type='M', ref_label='month_id', req={
    #         "M": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    #         "Q": [1, 2, 3, 4],
    #         "Y": [1, 2]
    #     })
    #
    #     print(ll['M'])
    #     print(ll['Q'])
    #     print(ll['Y'])
    #
    #     ll = plf.peek_max(2017, market='港澳台', ref_type='M', ref_label='month_id', req={
    #         "M": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    #         "Q": [1, 2, 3, 4],
    #         "Y": [1, 2]
    #     })
    #
    #     print(ll['M'])
    #     print(ll['Q'])
    #     print(ll['Y'])
    #
    #     ll = plf.peek_min(2017, market='港澳台', ref_type='M', ref_label='month_id', req={
    #         "M": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    #         "Q": [1, 2, 3, 4],
    #         "Y": [1, 2]
    #     })
    #
    #     print(ll['M'])
    #     print(ll['Q'])
    #     print(ll['Y'])

    # def test(self):
    #     df = pd.read_csv('../data/in/量价指数_加盐.csv')
    #     plf = VolumePriceIndex(df)
    #     l = plf.peak_max(2017, 0, ref_type="W", ref_label='起飞星期', req={"Y": [1,2]})
    #     ll = plf.peak_min(2016, 7, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
    #     lll = plf.peak_average(2017, 1, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
    #     llll = plf.yoy(2016, 5, ref_type="W", ref_label='起飞星期', req={"Y": [1,2]})
    #     print(l)
    #     print(ll)
    #     print(lll)
    #     print(llll)

    def test(self):
        df = pd.read_csv('../data/in/旅客规模_加盐.csv')
        plf = PassengerSize(df)
        l = plf.peak_max(2017, 0, ref_type="M", ref_label='month_id', req={"Y": [1]})
        ll = plf.peak_sum(2016, 0, ref_type="M", ref_label='month_id', req={"Y": [1]})
        lll = plf.peak_average(2017, 0, ref_type="M", ref_label='month_id', req={"Y": [1]})
        llll = plf.yoy(2017, 0, ref_type="M", ref_label='month_id', req={"Y": [1]})
        lllll = plf.peak_average(2017, 7, ref_type="M", ref_label='month_id', req={"Y": [1]})
        llllll = plf.peak_average(2016, 7, ref_type="M", ref_label='month_id', req={"Y": [1]})
        print(llllll['Y'][0] - lllll['Y'][0])

if __name__ == '__main__':
    unittest.main()