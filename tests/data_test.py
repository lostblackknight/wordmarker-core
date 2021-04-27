import unittest

import pandas as pd

from core.data.data import ProsperityIndex, DateUtils, PassengerLoadFactor


class MyTestCase(unittest.TestCase):

    def test(self):
        df = pd.read_csv('../data/in/市场数据_加盐.csv', encoding='gbk')

        plf = PassengerLoadFactor(df)

        ll = plf.yoy(2017, market='国内', ref_type='M', ref_label='month_id', req={
            "M": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "Q": [1, 2, 3, 4],
            "Y": [1, 2]
        })

        print(ll['M'])
        print(ll['Q'])
        print(ll['Y'])

        ll = plf.peek_max(2017, market='港澳台', ref_type='M', ref_label='month_id', req={
            "M": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "Q": [1, 2, 3, 4],
            "Y": [1, 2]
        })

        print(ll['M'])
        print(ll['Q'])
        print(ll['Y'])

        ll = plf.peek_min(2017, market='港澳台', ref_type='M', ref_label='month_id', req={
            "M": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "Q": [1, 2, 3, 4],
            "Y": [1, 2]
        })

        print(ll['M'])
        print(ll['Q'])
        print(ll['Y'])


if __name__ == '__main__':
    unittest.main()
