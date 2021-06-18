from core.data import Data
from docx.shared import Mm
from docxtpl import InlineImage
from core.text import AbstractConverter
from core.util import random_list, append_list
from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate


def init_data_base(csv_tpl: CsvTemplate, pdbc_tpl: PdbcTemplate):
    data_dict = csv_tpl.csv_to_df()
    pdbc_tpl.update_table(data_dict['城市数据_加盐.csv'], "t_city_data")
    pdbc_tpl.update_table(data_dict['市场数据_加盐.csv'], "t_market_data")
    pdbc_tpl.update_table(data_dict['景气指数_加盐.csv'], "t_prosperity_index")
    pdbc_tpl.update_table(data_dict['量价指数_加盐.csv'], "t_volume_price_index")
    pdbc_tpl.update_table(data_dict['旅客规模_加盐.csv'], "t_passenger_size")
    pdbc_tpl.update_table(data_dict['旅客特征_加盐.csv'], "t_passenger_characteristics")
    pdbc_tpl.update_table(data_dict['日均旅客量.csv'], "t_average_daily_passenger_volume")


def generate_img(word_tpl: WordTemplate):
    print(word_tpl.img_out_path)


def generate_word(word_tpl: WordTemplate, file_name: str, text: AbstractConverter):
    context = {
        'theme': text.get_value("meta.title"),
        'header': {
            'title': text.get_value("header.title"),
            'paragraphs': text.get_value("header.paragraphs"),
            'author': text.get_value("header.another"),
            'date': text.get_value("header.date"),
        },
        'main': [
            {
                'h1': '上半年行业发展综述',
                'h1_section': [
                    {
                        'h2': '1.全行业宏观概况——' + text.get_value("main.上半年行业发展综述.全行业宏观概况.综述"),
                        'h2_section': [
                            {
                                'h3': None,
                                'h3_section': [
                                    {
                                        'img_title': '图1.景气指数',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('景气指数.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.景气指数.综述")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.景气指数.国内")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.景气指数.国际")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.景气指数.港澳台")),
                                        ],
                                    },
                                    {
                                        'img_title': '图2.量价指数',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('量价指数.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.量价指数.综述")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.量价指数.国内")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.量价指数.国际")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.量价指数.港澳台")),
                                        ],
                                    },
                                    {
                                        'img_title': '图3.客座率指数',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('客座率指数.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.客座率指数.综述")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.客座率指数.国内")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.客座率指数.国际")),
                                            random_list(text.get_value("main.上半年行业发展综述.全行业宏观概况.客座率指数.港澳台")),
                                        ],
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'h2': '2.上半年民航旅客规模及特征',
                        'h2_section': [
                            {
                                'h3': '国内市场：',
                                'h3_section': [
                                    {
                                        'img_title': '图4.2017年上半年民航国内市场旅客概况',
                                        'img': InlineImage(word_tpl.tpl,
                                                           word_tpl.get_img_file('2017年上半年民航国内市场旅客概况.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value("main.上半年行业发展综述.上半年民航旅客规模及特征.国内市场.国内市场旅客概况"),
                                    },
                                    {
                                        'img_title': '图5.2017年上半年民航国内旅行者特征',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年上半年民航国内旅行者特征.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value("main.上半年行业发展综述.上半年民航旅客规模及特征.国内市场.国内旅行者特征"),
                                    },
                                ]
                            },
                            {
                                'h3': '国际市场：',
                                'h3_section': [
                                    {
                                        'img_title': '图6.2017年上半年民航国际市场旅客概况',
                                        'img': InlineImage(word_tpl.tpl,
                                                           word_tpl.get_img_file('2017年上半年民航国际市场旅客概况.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value("main.上半年行业发展综述.上半年民航旅客规模及特征.国际市场.国际市场旅客概况"),
                                    },
                                    {
                                        'img_title': '图7.2017年上半年民航国际旅行者特征',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年上半年民航国际旅行者特征.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value("main.上半年行业发展综述.上半年民航旅客规模及特征.国际市场.国际旅行者特征"),
                                    }
                                ]
                            }
                        ]
                    },
                ],
            },
            {
                'h1': '上半年行业热点透视',
                'h1_section': [
                    {
                        'h2': None,
                        'h2_section': [
                            {
                                'h3': text.get_value("main.上半年行业热点透视.节假日出行.综述"),
                                'h3_section': [
                                    {
                                        'img_title': '图8.2017年上半年节假日市场概况',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年上半年节假日市场概况.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            random_list(text.get_value("main.上半年行业热点透视.节假日出行.节假日市场概况.国内")),
                                            random_list(text.get_value("main.上半年行业热点透视.节假日出行.节假日市场概况.国际")),
                                            random_list(text.get_value("main.上半年行业热点透视.节假日出行.节假日市场概况.港澳台")),
                                        ],
                                    }
                                ]
                            },
                            {
                                'h3': text.get_value('main.上半年行业热点透视.“萨德”致中—韩航线失利.综述'),
                                'h3_section': [
                                    {
                                        'img_title': '图9.赴韩旅客量增长走势',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('赴韩旅客量增长走势.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value("main.上半年行业热点透视.“萨德”致中—韩航线失利.赴韩旅客量增长走势"),
                                    }
                                ]
                            },
                            {
                                'h3': text.get_value('main.上半年行业热点透视.中-澳旅游年助力民航市场.综述'),
                                'h3_section': [
                                    {
                                        'img_title': '图10.中澳间执飞航线图',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('中澳间执飞航线图.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value('main.上半年行业热点透视.中-澳旅游年助力民航市场.中澳间执飞航线'),
                                    },
                                    {
                                        'img_title': '图11.上半年赴澳旅客量增长走势',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('上半年赴澳旅客量增长走势.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value('main.上半年行业热点透视.中-澳旅游年助力民航市场.上半年赴澳旅客量增长走势'),
                                    },
                                    {
                                        'img_title': '图12.2017上半年赴澳目的地分布情况',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017上半年赴澳目的地分布情况.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value('main.上半年行业热点透视.中-澳旅游年助力民航市场.上半年赴澳目的地分布情况'),
                                    }
                                ]
                            }
                        ]
                    },
                ]
            },
            {
                'h1': '下半年市场展望与预测',
                'h1_section': [
                    {
                        'h2': '1.市场趋势预测',
                        'h2_section': [
                            {
                                'h3': '指数预测',
                                'h3_section': [
                                    {
                                        'img_title': '图13.景气指数预测走势图',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('景气指数预测走势图.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            random_list(text.get_value("main.下半年市场展望与预测.市场趋势预测.指数预测.景气指数.国内")),
                                            random_list(text.get_value("main.下半年市场展望与预测.市场趋势预测.指数预测.景气指数.国际")),
                                            random_list(text.get_value("main.下半年市场展望与预测.市场趋势预测.指数预测.景气指数.港澳台")),
                                        ],
                                    },
                                    {
                                        'img_title': '图14.量价指数值预测走势图',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('量价指数值预测走势图.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            random_list(text.get_value("main.下半年市场展望与预测.市场趋势预测.指数预测.量价指数.国内")),
                                            random_list(text.get_value("main.下半年市场展望与预测.市场趋势预测.指数预测.量价指数.国际")),
                                            # random_list(text.get_value("main.下半年市场展望与预测.市场趋势预测.指数预测.量价指数.港澳台")),
                                        ],
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'h2': '2.下半年热点展望',
                        'h2_section': [
                            {
                                'h3': '暑运前瞻',
                                'h3_section': [
                                    {
                                        'img_title': '图15.2017年暑运市场概况展望',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年暑运市场概况展望.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            random_list(
                                                text.get_value("main.下半年市场展望与预测.市场趋势预测.下半年热点展望.暑运前瞻.暑运市场概况.国内")),
                                            random_list(
                                                text.get_value("main.下半年市场展望与预测.市场趋势预测.下半年热点展望.暑运前瞻.暑运市场概况.国际")),
                                            random_list(
                                                text.get_value("main.下半年市场展望与预测.市场趋势预测.下半年热点展望.暑运前瞻.暑运市场概况.港澳台")),
                                        ],
                                    },
                                    {
                                        'img_title': '图16.2017年暑运国内重点市场',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年暑运国内重点市场.png'),
                                                           width=Mm(160)),
                                        'explanation':
                                            text.get_value("main.下半年市场展望与预测.市场趋势预测.下半年热点展望.暑运前瞻.暑运国内重点市场"),
                                    },
                                    {
                                        'img_title': '图17.2017年暑运出入境重点航线',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年暑运出入境重点航线.png'),
                                                           width=Mm(160)),
                                        'explanation': text.get_value("main.下半年市场展望与预测.市场趋势预测.下半年热点展望.暑运前瞻.暑运出入境重点航线"),
                                    }
                                ]
                            },
                            {
                                'h3': '十一黄金周展望',
                                'h3_section': [
                                    {
                                        'img_title': '图18.2017年十一黄金周出入境热点',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年十一黄金周出入境热点.png'),
                                                           width=Mm(160)),
                                        'explanation': append_list(
                                            text.get_value("main.下半年市场展望与预测.市场趋势预测.下半年热点展望.十一黄金周展望.综述"),
                                            text.get_value("main.下半年市场展望与预测.市场趋势预测.下半年热点展望.十一黄金周展望.十一黄金周出入境热点"))
                                    },
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        'footer': {
            'title': text.get_value("footer.title"),
            'paragraphs': text.get_value("footer.paragraphs"),
        },
    }
    word_tpl.append(context)
    word_tpl.build(file_name)


class TextConverter(AbstractConverter):

    def __init__(self, word_tpl: WordTemplate, data: Data):
        super().__init__(word_tpl)
        self.data = data

    def year(self):
        """
        获取年份
        :return: 年份
        """
        year = self.data.maximum_Year()
        return year

    def prosperity_index_increase(self):
        """
        判断景气指数的变化
        :return: 变化值
        """
        increase = self.data.prosperity_index_compare()
        return increase

    def last_year(self):
        """
        获取年份
        :return: 年份
        """
        last_year = self.data.maximum_Year() - 1
        return last_year

    def prosperity_index_in(self):
        """
        国内航线
        :return: 航线
        """
        route_in = self.data.route()
        return route_in

    def prosperity_index_out(self):
        """
        国际航线
        :return: 航线
        """
        route_out = self.data.route()
        return route_out

    def prosperity_index_hmt(self):
        """
        港澳台航线
        :return: 航线
        """
        route_hmt = self.data.route()
        return route_hmt

    def prosperity_index_in_yoy(self):
        """
        景气指数同比增幅
        :return: 同比增幅的值
        """
        yoy = self.data.prosperity_index_domestic_yoy()
        return yoy

    def prosperity_index_in_compare(self):
        """
        增速的比较
        :return: 变化值
        """
        result = self.data.increase(float(self.data.domestic_prosperity_index_yoy_compare()))
        return result

    def prosperity_index_in_growth_rate(self):
        """
        增速
        :return: 增速
        """
        rate = self.data.domestic_prosperity_index_yoy_compare()
        return rate

    def prosperity_index_in_stable(self):
        """
         .. note::

            判断市场是否稳定

        :return: 稳定否
        """
        rate = self.data.domestic_prosperity_index_yoy_compare()
        if float(rate) > 0:
            return '稳步上升'
        else:
            return '不稳定'

    def prosperity_index_in_stable2(self):
        """
          .. note::

                判断市场是否稳定

        :return: 稳定否
        """
        rate = self.data.prosperity_index_domestic_yoy()
        if float(rate) > 0:
            return '稳步上升'
        else:
            return '不稳定'

    def prosperity_index_num(self):
        """
        景气指数
        :return: 景气指数
        """
        result = self.data.prosperity_index_in_number(self.data.maximum_Year())
        return result

    def prosperity_index_compare(self):
        """
        .. note::

            今明两年景气指数相比较

        :return: 比较的差值
        """
        this_year = self.data.prosperity_index_in_number(self.data.maximum_Year())
        last_year = self.data.prosperity_index_in_number(self.data.maximum_Year() - 1)
        difference = float(this_year) - float(last_year)
        result = self.data.increase(difference)
        return result

    def prosperity_index_out_num(self):
        """
        .. note::

            国际景气指数

        :return: 国际景气指数
        """
        result = self.data.prosperity_index_foreign_number(self.data.maximum_Year())
        return result

    def prosperity_index_out_compare(self):
        """
         .. note::

            今明两年国际景气指数相比较

        :return: 上升或下降
        """
        this_year = self.data.prosperity_index_foreign_number(self.data.maximum_Year())
        last_year = self.data.prosperity_index_foreign_number(self.data.maximum_Year() - 1)
        difference = float(this_year) - float(last_year)
        result = self.data.increase(difference)
        return result

    def prosperity_index_out_growth_rate(self):
        """
        .. note::

            今明两年国际景气指数相比较的差值

        :return: 比较的差值
        """
        this_year = self.data.prosperity_index_foreign_number(self.data.maximum_Year())
        last_year = self.data.prosperity_index_foreign_number(self.data.maximum_Year() - 1)
        difference = float(this_year) - float(last_year)
        return '%.2f' % difference

    def prosperity_index_out_yoy(self):
        """
         .. note::

            国际景气指数同比增幅

        :return: 同比增幅
        """
        result = self.data.prosperity_index_foreign_yoy()
        return result

    def prosperity_index_out_peak(self):
        """
         .. note::

            国际景气指数峰值

        :return: 峰值
        """
        result = self.data.foreign_springFestival_max()
        return result

    def prosperity_index_hmt_compare(self):
        """
         .. note::

            港澳台航线景气指数比较

        :return: 变化
        """
        result = self.data.prosperity_index_compare_hmk()
        return result

    def prosperity_index_hmt_yoy(self):
        """
         .. note::

            港澳台景气指数同比增幅

        :return: 同比增幅
        """
        result = self.data.prosperity_index_hkm_yoy()
        return result

    def prosperity_index_hmt_rate(self):
        """
         .. note::

            港澳台景气指数的差值

        :return: 差值
        """
        result = self.data.hkm_prosperity_index_index_compare()
        return result

    def prosperity_index_hmt_yoy_compare(self):
        """
         .. note::

            港澳台景气指数同比增幅的比较

        :return: 同比增幅的比较
        """
        result = self.data.domestic_prosperity_index_yoy()
        return result

    def prosperity_index_hmt_yoy_rate(self):
        """
         .. note::

            港澳台景气指数同比增幅的差值

        :return: 同比增幅的差值
        """
        result = self.data.hkm_prosperity_index_yoy_compare()
        return result

    def prosperity_index_hmt_num(self):
        """
         .. note::

            港澳台景气指数

        :return: 港澳台景气指数
        """
        result = self.data.prosperity_index_hkm_number(self.data.maximum_Year())
        return result

    def volume_price_index_trend(self):
        """
         .. note::

            市场运输量指数整体趋势

        :return: 市场运输量指数整体趋势
        """
        result = self.data.volume_price_index_trend(0)
        return result

    def volume_price_index_trend2(self):
        """
         .. note::

            市场运输量指数整体趋势

        :return: 市场运输量指数整体趋势
        """
        this_year = self.data.volume_price_index_average(self.data.maximum_Year(), 0)
        last_year = self.data.volume_price_index_average(self.data.maximum_Year() - 1, 0)
        result = float(this_year) - float(last_year)
        if result > 0:
            return "升"
        else:
            return "降"

    def volume_price_index_trend3(self):
        """
         .. note::

            市场价格指数整体趋势

        :return: 市场价格指数整体趋势
        """
        this_year = self.data.volume_price_index_average(self.data.maximum_Year(), 1)
        last_year = self.data.volume_price_index_average(self.data.maximum_Year() - 1, 1)
        result = float(this_year) - float(last_year)
        if result > 0:
            return "升"
        else:
            return "降"

    def volume_price_index_trend4(self):
        """
         .. note::

            整体运输量指数与去年相比

        :return: 变化趋势
        """
        result = self.data.volume_price_index_trend(0)
        return result

    def volume_price_index_trend5(self):
        """
         .. note::

            价格指数在国际航线巿场的变化

        :return: 变化趋势
        """
        result = self.data.volume_price_index_trend(1)
        return result

    def volume_price_index_trend_in_out(self):
        """
         .. note::

            价格指数在国内、国际航线市场的变化趋势

        :return: 变化趋势
        """
        result_in = self.data.volume_price_index_average(self.data.maximum_Year(), 5)
        result_out = self.data.volume_price_index_average(self.data.maximum_Year(), 6)
        average = (float(result_in) + float(result_out)) / 2
        result = self.data.increase(average)
        return result

    def volume_price_index_trend_hmt(self):
        """
         .. note::

            价格指数在港澳台航线市场的变化趋势

        :return: 变化趋势
        """
        result = self.data.volume_price_index_trend(7)
        return result

    def volume_price_index(self):
        """
         .. note::

             整体运输量指数

        :return:  整体运输量指数
        """
        result = self.data.volume_price_index_average(self.data.maximum_Year(), 0)
        return result

    def volume_price_index_rate(self):
        """
         .. note::

            整体运输量指数与去年相比的差值

        :return: 差值
        """
        result = self.data.volume_price_index_trend_rate(0)
        return result

    def traffic_index_in(self):
        """
         .. note::

            国内航线运输量指数

        :return: 国内航线运输量指数
        """
        result = self.data.volume_price_index_average(self.data.maximum_Year(), 2)
        return result

    def traffic_index_in_yoy(self):
        """
         .. note::

            国内航线运输量指数同比增幅

        :return:    同比增幅
        """
        result = self.data.volume_price_index_yoy(self.data.maximum_Year(), 2)
        return result

    def price_index_in(self):
        """
         .. note::

            国内航线价格指数

        :return: 国内航线价格指数
        """
        result = self.data.volume_price_index_average(self.data.maximum_Year(), 5)
        return result

    def price_index_in_yoy(self):
        """
         .. note::

            国内航线价格指数同比增幅

        :return: 同比增幅
        """
        result = self.data.volume_price_index_yoy(self.data.maximum_Year(), 5)
        return result

    def traffic_index_in_yoy_compare(self):
        """
         .. note::

            今明两年国内航线运输量指数的比较

        :return: 比较结果
        """
        this_year = self.data.volume_price_index_yoy(self.data.maximum_Year(), 2)
        last_year = self.data.volume_price_index_yoy(self.data.maximum_Year() - 1, 2)
        difference = float(this_year) - float(last_year)
        result = self.data.increase(difference)
        return result

    def traffic_index_in_yoy_rate(self):
        """
         .. note::

            今明两年国内航线运输量指数的比较的差值

        :return: - 差值
        """
        this_year = self.data.volume_price_index_yoy(self.data.maximum_Year(), 2)
        last_year = self.data.volume_price_index_yoy(self.data.maximum_Year() - 1, 2)
        result = float(this_year) - float(last_year)
        return result

    def price_index_in_yoy_compare(self):
        """
         .. note::

            今明两年国内航线价格指数同比增幅比较

        :return: 比较
        """
        this_year = self.data.volume_price_index_yoy(self.data.maximum_Year(), 5)
        last_year = self.data.volume_price_index_yoy(self.data.maximum_Year() - 1, 5)
        difference = float(this_year) - float(last_year)
        result = self.data.increase(difference)
        return result

    def price_index_in_yoy_rate(self):
        """
         .. note::

            今明两年国内航线价格指数同比增幅比较的差值

        :return: 比较的差值
        """
        this_year = self.data.volume_price_index_yoy(self.data.maximum_Year(), 5)
        last_year = self.data.volume_price_index_yoy(self.data.maximum_Year() - 1, 5)
        result = float(this_year) - float(last_year)
        return result

    def traffic_index_in_yoy_trend(self):

        """
         .. note::

            判断国内航线运输量指数同比增幅的趋势

        :return: 趋势
        """
        result = float(self.data.volume_price_index_yoy(self.data.maximum_Year(), 2))
        if result > 0:
            return "增长"
        else:
            return "下降"

    def price_index_in_yoy_trend(self):

        """
         .. note::

            判断国内航线价格指数同比增幅的趋势

        :return: 趋势
        """
        result = float(self.data.volume_price_index_yoy(self.data.maximum_Year(), 5))
        if result > 0:
            return "增长"
        else:
            return "下降"

    def traffic_index_out(self):
        """
         .. note::

            国际航线运输量指数最大值

        :return: 最大值
        """
        return self.data.volume_price_index_max(self.data.maximum_Year(), 3)

    def traffic_index_out_yoy(self):
        """
         .. note::

            国际航线运输量指数同比增幅

        :return: 同比增幅
        """
        return self.data.volume_price_index_yoy(self.data.maximum_Year(), 3)

    def traffic_index_out_trend(self):
        """
         .. note::

            国际航线运输量指数同比增幅的趋势

        :return: 趋势
        """
        result = float(self.data.volume_price_index_yoy(self.data.maximum_Year(), 3))
        if result > 0:
            return "加速"
        else:
            return "缓慢"

    def price_index_out_compare(self):
        """
         .. note::

            国际航线价格指数同比增幅的趋势

        :return: 趋势
        """
        result = float(self.data.volume_price_index_yoy(self.data.maximum_Year(), 6))
        if result > 0:
            return "升"
        else:
            return "降"

    def price_index_out_trend(self):
        """
         .. note::

            今明两年国际航线价格指数同比增幅的变化趋势

        :return: 变化趋势
        """
        return self.data.volume_price_index_trend(6)

    def price_index_out_yoy_rate(self):
        """
         .. note::

            今明两年国际航线价格指数同比增幅的变化的差值

        :return: 变化差值
        """
        return self.data.volume_price_index_trend_rate(6)

    def price_index_out_yoy(self):
        """
         .. note::

            国际航线价格指数同比增幅

        :return: 同比增幅
        """
        return self.data.volume_price_index_yoy(self.data.maximum_Year(), 6)

    def price_index_out_index(self):
        """
         .. note::

            国际价格指数最大值或最小值

        :return: 最大值或最小值
        """
        result = float(self.data.volume_price_index_yoy(self.data.maximum_Year(), 6))
        l_max = self.data.volume_price_index_max(self.data.maximum_Year(), 6)
        l_min = self.data.volume_price_index_min(self.data.maximum_Year(), 6)
        if result > 0:
            return f"升至{l_max}"
        else:
            return f"降至{l_min}"

    def traffic_index_hmt(self):
        """
         .. note::

            港澳台航线运输量指数

        :return: 港澳台航线运输量指数
        """
        return self.data.volume_price_index_average(self.data.maximum_Year(), 4)

    def traffic_index_hmt_yoy(self):
        """
         .. note::

            港澳台航线运输量指数同比增幅

        :return: 港澳台航线运输量指数同比增幅
        """
        return self.data.volume_price_index_yoy(self.data.maximum_Year(), 4)

    def price_index_hmt(self):
        """
         .. note::

            港澳台航线价格指数

        :return: 港澳台航线价格指数
        """
        return self.data.volume_price_index_average(self.data.maximum_Year(), 7)

    def price_index_hmt_yoy(self):
        """
         .. note::

             港澳台航线价格指数同比增幅

        :return: 港澳台航线价格指数同比增幅
        """
        return self.data.volume_price_index_yoy(self.data.maximum_Year(), 7)

    def traffic_index_hmt_yoy_compare(self):
        """
         .. note::

             港澳台航线运输量指数同比增幅比较

        :return: 港澳台航线运输量指数同比增幅比较变化
        """
        return self.data.volume_price_index_trend(4)

    def price_index_hmt_yoy_compare(self):
        """
         .. note::

             港澳台航线价格指数同比增幅比较

        :return: 港澳台航线价格指数同比增幅比较变化
        """
        return self.data.volume_price_index_trend(7)

    def price_index_hmt_yoy_rate(self):
        """
         .. note::

             港澳台航线价格指数同比增幅比较差值

        :return: 港澳台航线价格指数同比增幅比较变化差值
        """
        return self.data.volume_price_index_trend_rate(7)

    def passenger_loadFactor_index_in(self):
        """
         .. note::

            国内航线客座率指数

        :return: 国内航线客座率指数
        """
        result = self.data.passenger_load_factor_index("国内")
        return result

    def passenger_loadFactor_index_out(self):
        """
         .. note::

            国际航线客座率指数

        :return: 国际航线客座率指数
        """
        result = self.data.passenger_load_factor_index("国际")
        return result

    def passenger_loadFactor_index_hmt(self):
        """
         .. note::

            港澳台航线客座率指数

        :return: 港澳台航线客座率指数
        """
        result = self.data.passenger_load_factor_index("港澳台")
        return result

    def passenger_loadFactor_index_out_yoy(self):
        """
         .. note::

            国际地区的客座率同比增幅

        :return: 同比增幅
        """
        result = self.data.passenger_load_factor_yoy("国际")
        return result

    def passenger_loadFactor_index_hmt_yoy(self):
        """
         .. note::

            港澳台地区的客座率同比增幅

        :return: 同比增幅
        """
        result = self.data.passenger_load_factor_yoy("港澳台")
        return result

    def load_factor_compare_out(self):
        """
         .. note::

            国际航线客座率指数与去年相比

        :return: 比较的差值
        """
        l = float(self.data.passenger_load_factor("国际"))
        result = self.data.increase(l)
        return result

    def passenger_loadFactor_index_in_compare(self):
        """
         .. note::

            国内地区的客座率同比增幅与去年相比

        :return: 比较结果
        """
        l = float(self.data.passenger_load_factor_yoy_compare("国内"))
        result = self.data.increase(l)
        return result

    def passenger_loadFactor_index_in_rate(self):
        """
         .. note::

            国内地区的客座率同比增幅与去年相比

        :return: 比较的差值
        """
        result = self.data.passenger_load_factor_yoy_compare("国内")
        return result

    def passenger_loadFactor_index_out_compare(self):
        """
         .. note::

            国际地区的客座率同比增幅与去年相比

        :return: 比较结果
        """
        l = float(self.data.passenger_load_factor_yoy_compare("国际"))
        result = self.data.increase(l)
        return result

    def passenger_loadFactor_index_out_rate(self):
        """
         .. note::

            国际地区的客座率同比增幅与去年相比

        :return: 比较的差值
        """
        result = self.data.passenger_load_factor_yoy_compare("国际")
        return result

    def passenger_loadFactor_index_hmt_compare(self):
        """
         .. note::

            港澳台地区的客座率同比增幅与去年相比

        :return: 比较结果
        """
        l = float(self.data.passenger_load_factor_yoy_compare("港澳台"))
        result = self.data.increase(l)
        return result

    def passenger_loadFactor_index_hmt_rate(self):
        """
         .. note::

            港澳台地区的客座率同比增幅与去年相比

        :return: 比较的差值
        """
        result = self.data.passenger_load_factor_yoy_compare("港澳台")
        return result

    def passenger_loadFactor_index_hmt_height(self):
        """
         .. note::

            判断港澳台地区的客座率的高低

        :return: 高低
        """
        ll = float(self.data.passenger_load_factor_yoy_compare("港澳台"))
        if ll > 0:
            return "较高水平"
        else:
            return "低水平"

    def passenger_size_in(self):
        """
         .. note::

            上半年国内航线旅客规模

        :return: 上半年国内航线旅客规模
        """
        return self.data.passengerSize(3, self.data.maximum_Year())

    def passenger_size_compare(self):
        """
         .. note::

            上半年国内航线旅客规模同比增幅与去年相比

        :return: 比较值
        """
        ll = float(self.data.passenger_size_yoy(3))
        result = self.data.increase(ll)
        return result

    def passenger_size_in_yoy(self):
        """
         .. note::

            上半年国内航线旅客规模同比增幅

        :return: 上半年国内航线旅客规模同比增幅
        """
        return self.data.passenger_size_yoy(3)

    def kilometer2(self):
        """
         .. note::

            上半年国内航线平均飞行距离

        :return: 平均飞行距离
        """
        return self.data.passenger_size_average(self.data.maximum_Year(), 3)

    def kilometer1(self):
        """
         .. note::

            去年上半年国内航线平均飞行距离

        :return: 平均飞行距离
        """
        return self.data.passenger_size_average(self.data.maximum_Year() - 1, 3)

    def passenger_size_compare2(self):
        """
         .. note::

            上半年国内航线平均飞行距离与去年相比

        :return: 平均飞行距离比较结果
        """
        this_year = self.data.passenger_size_average(self.data.maximum_Year(), 3)
        last_year = self.data.passenger_size_average(self.data.maximum_Year() - 1, 3)
        result = this_year - last_year
        return self.data.increase(result)

    def repeat_purchase_rate_in(self):
        """
         .. note::

            国内航线人均重复购买率

        :return: 国内航线人均重复购买率
        """
        return self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year(), 7)

    def repeat_purchase_rate_in_last(self):
        """
         .. note::

            去年国内航线人均重复购买率

        :return: 去年国内航线人均重复购买率
        """
        return self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year() - 1, 7)

    def repeat_purchase_rate_in_compare(self):
        """
         .. note::

            今年国内航线人均重复购买率与去年比较

        :return: 比较结果
        """
        this_year = self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year(), 7)
        last_year = self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year() - 1, 7)
        result = float(this_year) - float(last_year)
        return self.data.increase(result)

    def repeat_purchase_rate_in_yoy(self):
        """
         .. note::

            今年国内航线人均重复购买率与去年比较数值

        :return: 比较数值
        """
        this_year = self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year(), 7)
        last_year = self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year() - 1, 7)
        return '%.2f' % (float(this_year) - float(last_year))

    def passenger_sex_ratio_in_compare(self):
        """
         .. note::

            上半年国内市场旅客性别比例相比

        :return: 比较差值结果
        """
        man = self.data.tourism_characteristics_average(self.data.maximum_Year(), 0)
        woman = self.data.tourism_characteristics_average(self.data.maximum_Year(), 1)
        result = float(man) - float(woman)
        if result > 0:
            return "超"
        else:
            return "低"

    def passenger_sex_ratio_in(self):
        """
         .. note::

            上半年国内市场旅客性别比例相比结果

        :return: 比较结果
        """
        man = self.data.tourism_characteristics_average(self.data.maximum_Year(), 0)
        woman = self.data.tourism_characteristics_average(self.data.maximum_Year(), 1)
        return '%.2f' % (float(man) - float(woman))

    def passenger_travel_ratio_24_30_in_compare(self):
        """
         .. note::

            24~30岁旅客出行比例同比比较结果

        :return: 比较结果
        """
        result = float(self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 2))
        return self.data.increase(result)

    def passenger_travel_ratio_24_30_in(self):
        """
         .. note::

            24~30岁旅客出行比例同比

        :return:24~30岁旅客出行比例同比
        """
        return self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 2)

    def passenger_travel_ratio_60_up_in_compare(self):
        """
         .. note::

            60岁以上旅客出行比例同比比较结果

        :return: 比较结果
        """
        result = float(self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 3))
        return self.data.increase(result)

    def passenger_travel_ratio_60_up_in(self):
        """
         .. note::

            60岁以上旅客出行比例同比

        :return: 60岁以上旅客出行比例同比
        """
        return self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 3)

    def book_in_advance_1_3_in_compare(self):
        """
         .. note::

            提前1-3天预订的旅客比例同比比较结果

        :return: 比较结果
        """
        result = float(self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 4))
        return self.data.increase(result)

    def book_in_advance_1_3_in(self):
        """
         .. note::

            提前1-3天预订的旅客比例同比

        :return: 提前1-3天预订的旅客比例同比
        """
        return self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 4)

    def book_in_advance_16_30_in_compare(self):
        """
         .. note::

            提前16-30天预订的旅客比例同比比较结果

        :return: 比较结果
        """
        result = float(self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 5))
        return self.data.increase(result)

    def book_in_advance_16_30_in(self):
        """
         .. note::

            提前16-30天预订的旅客比例同比

        :return: 提前16-30天预订的旅客比例同比
        """
        return self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 5)

    def travel_with_group_in(self):
        """
         .. note::

            国内跟团的数据

        :return: 国内跟团的数据
        """
        return self.data.tourism_characteristics_average(self.data.maximum_Year(), 6)

    def travel_with_group_in_yoy_compare(self):
        """
         .. note::

            与去年相比国内跟团的数据比较

        :return: 与去年相比国内跟团的数据比较
        """
        result = float(self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 6))
        return self.data.increase(result)

    def travel_with_group_in_yoy(self):
        """
         .. note::

            与去年相比国内跟团的数据比较的值

        :return: 与去年相比国内跟团的数据比较的值
        """
        return self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 6)

    def counter_check_in_yoy(self):
        """
         .. note::

            柜台值机比例同比

        :return: 柜台值机比例同比
        """
        return self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 7)

    def counter_check_in_yoy_compare(self):
        """
         .. note::

            柜台值机比例同比比较结果

        :return: 比较结果
        """
        result = float(self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 7))
        return self.data.increase(result)

    def counter_check_in_advance_3_in_yoy(self):
        """
         .. note::

            提前3小时以内值机旅客比例同比

        :return: 提前3小时以内值机旅客比例同比
        """
        return self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 8)

    def counter_check_in_advance_3_in_yoy_compare(self):
        """
         .. note::

            提前3小时以内值机旅客比例同比比较结果

        :return: 比较结果
        """
        result = float(self.data.tourism_characteristics_yoy(self.data.maximum_Year(), 8))
        return self.data.increase(result)

    def passenger_size_out(self):
        """
         .. note::

            国际航线旅客规模

        :return: 国际航线旅客规模
        """
        return self.data.passengerSize(4, self.data.maximum_Year())

    def passenger_size_out_yoy(self):
        """
         .. note::

            国际航线旅客规模同比增幅

        :return: 同比增幅
        """
        return self.data.passenger_size_yoy(4)

    def passenger_size_out_compare(self):
        """
         .. note::

            国际航线旅客规模增速与去年相比结果

        :return: 比较结果
        """
        domestic = self.data.passenger_size_yoy(3)
        foreign = self.data.passenger_size_yoy(4)
        return self.data.increase(float(domestic) - float(foreign))

    def passenger_size_out_growth_rate(self):
        """
         .. note::

            国际航线旅客规模增速与去年相比差值

        :return: 差值
        """
        domestic = self.data.passenger_size_yoy(3)
        foreign = self.data.passenger_size_yoy(4)
        result = float(domestic) - float(foreign)
        return result

    def average_flight_distance_out_last(self):
        """
         .. note::

            去年国外平均飞行距离

        :return: 平均飞行距离
        """
        return self.data.passenger_size_average(self.data.maximum_Year() - 1, 6)

    def average_flight_distance_out_last_compare(self):
        """
         .. note::

            国外平均飞行距离与去年相比较

        :return: 比较
        """
        this_year = self.data.passengerSize(6, self.data.maximum_Year())
        last_year = self.data.passengerSize(6, self.data.maximum_Year() - 1)
        result = float(this_year) - float(last_year)
        return self.data.increase(result)

    def average_flight_distance_out(self):
        """
         .. note::

            国外平均飞行距离

        :return: 平均飞行距离
        """
        return self.data.passenger_size_average(self.data.maximum_Year(), 6)

    def repeat_purchase_rate_out(self):
        """
         .. note::

            国际航线旅客重复购买率

        :return:  国际航线旅客重复购买率
        """
        return self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year(), 8)

    def repeat_purchase_rate_out_compare(self):
        """
         .. note::

             上上年与去年国际航线旅客重复购买率相比较

        :return:  比较结果
        """
        last_year = self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year() - 1, 8)
        the_year_before_last = self.data.repeat_purchase_rate_per_capita(self.data.maximum_Year() - 2, 8)
        result = float(last_year) - float(the_year_before_last)
        return self.data.increase(result)
