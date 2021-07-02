from docx.shared import Mm
from docxtpl import InlineImage
from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate, AbstractConverter

from core.img import ProsperityIndex, PassengerLoadFactor, PriceIndex, InternationalTraveler, DomesticTraveler, \
    InlandAviation, InternationalAviation
from core.util import random_list, append_list


def init_data_base(csv_tpl: CsvTemplate, pdbc_tpl: PdbcTemplate):
    data_dict = csv_tpl.csv_to_df()
    pdbc_tpl.update_table(data_dict['城市数据_加盐.csv'], "t_city_data")
    pdbc_tpl.update_table(data_dict['市场数据_加盐.csv'], "t_market_data")
    pdbc_tpl.update_table(data_dict['景气指数_加盐.csv'], "t_prosperity_index")
    pdbc_tpl.update_table(data_dict['量价指数_加盐.csv'], "t_volume_price_index")
    pdbc_tpl.update_table(data_dict['旅客规模_加盐.csv'], "t_passenger_size")
    pdbc_tpl.update_table(data_dict['旅客特征_加盐.csv'], "t_passenger_characteristics")
    pdbc_tpl.update_table(data_dict['日均旅客量.csv'], "t_average_daily_passenger_volume")


def generate_img(word_tpl: WordTemplate, data_dict: dict):
    # 景气指数
    ProsperityIndex(data_dict['景气指数']).build(word_tpl.img_out_path + "/景气指数.png")
    # 载客率
    PassengerLoadFactor(data_dict['市场数据']).build(word_tpl.img_out_path + "/客座率指数.png")
    # 价格指数
    PriceIndex(data_dict['量价指数']).build(word_tpl.img_out_path + "/量价指数.png")
    # 国际旅行者
    InternationalTraveler(data_dict['旅客特征']).build(word_tpl.img_out_path + "/2017年上半年民航国际旅行者特征.png")
    # 国内旅行者
    DomesticTraveler(data_dict['旅客特征']).build(word_tpl.img_out_path + "/2017年上半年民航国内旅行者特征.png")
    # 国内民航表格
    InlandAviation(data_dict['旅客规模']).build(word_tpl.img_out_path + "/2017年上半年民航国内市场旅客概况.png")
    # 国际民航表格
    InternationalAviation(data_dict['旅客规模']).build(word_tpl.img_out_path + "/2017年上半年民航国际市场旅客概况.png")


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
