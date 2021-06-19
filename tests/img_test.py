import unittest
import pandas as pd

from core.img import ProsperityIndex, PassengerLoadFactor, PriceIndex, InternationalTraveler, DomesticTraveler, \
    InlandAviation, InternationalAviation


class MyTestCase(unittest.TestCase):
    """
    传入的类型只能是 DataFrame, 数据库返回的也是DataFrame，要将列表转换为DataFrame

    传入文件名，即可输出图片，不传入，不输出
    """

    def test1(self):
        df = pd.read_csv('E:\PycharmProjects\wordmarker-core\data\in\景气指数_加盐.csv')
        ProsperityIndex(df).build()

    def test2(self):
        df = pd.read_csv('E:\PycharmProjects\wordmarker-core\data\in\市场数据_加盐.csv')
        PassengerLoadFactor(df).build()

    def test3(self):
        df = pd.read_csv('E:\PycharmProjects\wordmarker-core\data\in\量价指数_加盐.csv')
        PriceIndex(df).build()

    def test4(self):
        df = pd.read_csv('E:\PycharmProjects\wordmarker-core\data\in\旅客特征_加盐.csv')
        InternationalTraveler(df).build()

    def test5(self):
        df = pd.read_csv('E:\PycharmProjects\wordmarker-core\data\in\旅客特征_加盐.csv')
        DomesticTraveler(df).build()

    def test6(self):
        InlandAviation(None).build()

    def test7(self):
        InternationalAviation(None).build()


if __name__ == '__main__':
    unittest.main()
