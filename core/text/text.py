import copy
import ast
from wordmarker.contexts import WordMarkerContext
from wordmarker.templates import WordTemplate
from jinja2 import Template, Environment, meta
from wordmarker.utils import YamlUtils
from abc import ABCMeta
import pandas as pd
import random
from core.data.data import PassengerLoadFactor, ProsperityIndex


class AbstractConverter(metaclass=ABCMeta):
    """
    .. note::

        此方法是用来实现的，定义的方法可以为@staticmethod修饰的方法，但不能有任何参数，也可以为由self一个参数构成的方法
    """

    def __init__(self, word_tpl: WordTemplate):
        self.word_tpl = word_tpl

    def convert_to_str(self) -> str:
        content = {}
        data = self.word_tpl.get_yaml_singleton_str()
        env = Environment()
        parse_rs = env.parse(data)
        for tag in meta.find_undeclared_variables(parse_rs):
            content[tag] = getattr(self, tag)()
        return Template(data).render(content)

    def convert_to_dict(self) -> dict:
        return ast.literal_eval(self.convert_to_str())

    def get_value(self, prop):
        prop_list = prop.split('.')
        yaml_dict = self.convert_to_dict()
        value = None
        temp_list = copy.deepcopy(prop_list)
        v = YamlUtils().get_value(yaml_dict, temp_list, prop, '')
        if v is not None:
            value = v
        return value


def prosperityIndex_test(word_tpl: WordTemplate, year):
    df = pd.read_csv('E:\PyCharmProjects\wordmarker-core\data\in\景气指数_加盐.csv')
    pi = ProsperityIndex(df, "景气指数")
    ll = pi.peek_average(year, ref_type="W", ref_label='起飞星期', req={"Y": [1]
    })
    lll = pi.yoy(year, ref_type="W", ref_label='起飞星期', req={"Y": [1]})
    result = increase(lll)
    ss: str = word_tpl.get_value('prosperityIndex.first')
    print(ss.format(this_year=year, data=ll['Y'][0], last_year=year-1, increase=result, data2=lll['Y'][0]))


def loadFactor_test(word_tpl2: WordTemplate, year, _market):
    df = pd.read_csv('E:\PyCharmProjects\wordmarker-core\data\in\市场数据_加盐.csv')
    plf = PassengerLoadFactor(df)
    l = plf.peek_var(year, market=_market, ref_type='M', ref_label='month_id', req={"Y": [1]})
    if l['Y'][0] > 0.05:
        result = "有小幅度动荡，市场环境较差"
    else:
        result = "较为稳定，巿场投放策略相对利好"
    ll = plf.yoy(year, market='国内', ref_type='M', ref_label='month_id', req={"Y": [1]})
    result2 = increase(ll)
    lll = plf.yoy(year, market='国际', ref_type='M', ref_label='month_id', req={"Y": [1]})
    result3 = increase(lll)
    domestic_l = plf.peek_mean(year, market='国内', ref_type='M', ref_label='month_id', req={"Y": [1]})
    domestic_ll = plf.peek_mean(year, market='国际', ref_type='M', ref_label='month_id', req={"Y": [1]})
    domestic_lll = plf.peek_mean(year, market='港澳台', ref_type='M', ref_label='month_id', req={"Y": [1]})
    rs1 = compare(year, "国内")
    rs2 = compare(year, "国际")
    rs3 = compare(year, "港澳台")
    result4 = increase(rs1)
    result5 = increase(rs2)
    result6 = increase(rs3)
    ss: str = word_tpl2.get_value('loadFactor.first.second')
    print(ss.format(this_year=year, area=_market, status=result, increase=result2, data=ll['Y'][0], speed=result3,
                    increase2=result3, data2=lll['Y'][0]))
    ss2: str = word_tpl2.get_value('loadFactor.second')
    print(ss2.format(increase=result2, data=ll['Y'][0], speed=result3, increase2=result3, data2=lll['Y'][0]))
    ss3: str = word_tpl2.get_value('loadFactor.third')
    print(ss3.format(data=domestic_l['Y'][0], increase=result4, data2=domestic_ll['Y'][0], increase2=result5,
                     data3=domestic_lll['Y'][0], increase3=result6, num=compare(year, "港澳台")))



def increase(result):
    """
     .. note::

            判断数据上升还是下降

    :param result:  a
    :return: 数据上升还是下降
    """
    goUp = ["上升", "增长", "上涨"]
    drop = ["下降", "降低"]
    if isinstance(result, dict):
        if result['Y'][0] > 0:
            a = random.choice(goUp)
            return a
        else:
            a = random.choice(drop)
            return a
    else:
        if result > 0:
            a = random.choice(goUp)
            return a
        else:
            a = random.choice(drop)
            return a


def compare(year_, market_):
    """
      .. note::

            比较前后两年的客座率，得出差值

    :param year_: 年份
    :param market_: 地区
    :return: 差值
    """
    df = pd.read_csv('E:\PyCharmProjects\wordmarker-core\data\in\市场数据_加盐.csv')
    plf = PassengerLoadFactor(df)
    domestic_l = plf.peek_mean(year_-1, market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
    domestic_ll = plf.peek_mean(year_, market=market_, ref_type='M', ref_label='month_id', req={"Y": [1]})
    dif = domestic_ll['Y'][0] - domestic_l['Y'][0]
    return dif


if __name__ == '__main__':
    WordMarkerContext('E:\PyCharmProjects\wordmarker-core\config.yaml')
    word_tpl = WordTemplate()
    word_tpl2 = WordTemplate()
    prosperityIndex_test(word_tpl, 2017)
    loadFactor_test(word_tpl2, 2017, "港澳台")
