from docx.shared import Mm
from docxtpl import InlineImage

from core.data import Data
from core.text import AbstractConverter
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


def generate_word(word_tpl: WordTemplate, file_name: str):
    context = {
        'theme': '2017年航指数半年白皮书',
        'header': {
            'title': '导语：',
            'paragraphs': [
                '转眼间2017年已过半，同时航指数也迎来了它的第三个夏天。一路走来航指数已经推出了四篇白皮书系列文章，虽然每篇由于时间和篇幅所限很多热点未能做到更详尽的深挖，但每次发布之后都会在业内引起不小的反响与关注，也因此给航指数带来了大量的“粉丝”。很多热心的朋友在看了白皮书后与我们取得了联系、进一步深入探讨民航市场动向，也为我们提出了诸多宝贵意见，在此我们要表示衷心的感谢。未来航指数会一直坚持最初的宗旨：“来源于行业、服务于行业”，并以开放的态度力争为行业提供更好的分析“干货”。',
                '2017半年白皮书纵览上半年市场整体变化趋势，主要聚焦在国内、国际市场概况、旅客各类出行特征、节假日民航市场出行变化、国际出境热点分析等行业热点上。下半年展望中结合航指数网站相关数据，为分析判断提供科学有效的依据，对下半年的市场趋势及热点情况进行预判。',
            ],
            'author': '中国航信航指数团队',
            'date': '2017.7',
        },
        'main': [
            {
                'h1': '上半年行业发展综述',
                'h1_section': [
                    {
                        'h2': '1.全行业宏观概况——景气指数 显示民航市场整体运转良好，国内市场呈稳步上升态势；国际市场增速放缓，量价差距逐渐放缓；港澳台市场依旧在复苏之路上缓慢前行。',
                        'h2_section': [
                            {
                                'h3': None,
                                'h3_section': [
                                    {
                                        'img_title': '图1.景气指数',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('景气指数.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '2017年上半年民航全市场景气指数稳步上升：国内航线129，国际航线155，港澳台航线114。',
                                            '国内航线景气指数同比增幅为8%，增速超2016年同期4个百分点，市场稳步上升。',
                                            '国际航线景气指数增速放缓，同比增幅放缓至12%，但春节峰值周景气指数超越2016年峰值，达到178，再创新高。',
                                            '港澳台航线景气指数同比小幅下降1个百分点，市场依然在复苏道路上缓慢挣扎。',
                                        ],
                                    },
                                    {
                                        'img_title': '图2.量价指数',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('量价指数.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '2017年上半年民航市场运输量指数 整体上升；价格指数 在国内、国际航线市场趋于稳定，在港澳台航线市场有所上升。',
                                            '国内航线运输量指数179，同比增幅13%；价格指数93，同比增长3个百分点。',
                                            '国际航线量价差距逐渐放缓，运输量指数增速放缓，但上半年运输量指数依然突破250大关，以17%的同比增幅升至270；价格指数 则趋于稳定，同比持平。',
                                            '港澳台航线运输量指数148，同比下降6%；价格指数85，同比增幅8%，市场在复苏之路上缓慢前行。',
                                        ],
                                    },
                                    {
                                        'img_title': '图3.客座率指数',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('客座率指数.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '2017年上半年市场客座率 水平表现较为稳定，市场投放策略相对利好。',
                                            '国内航线客座率指数84%，国际航线客座率指数80%，均与2016年同期水平持平，产投比相对稳定。',
                                            '港澳台航线客座率指数77%，较2016年同期上涨1个百分点。',
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
                                        'explanation': [
                                            '2017年上半年国内航线旅客规模 7857万，较2016年同期增长14%。但平均飞行距离由2016年同期的1246公里缩短到1237公里。（参见图4）',
                                            '国内航线人均重复购买率 2.66，较2016年同期的2.64上升0.02次。',
                                            '旅客规模扩增、人均重复购买率几乎保持平稳，民航市场旅客覆盖面或将逐渐扩大化。',
                                        ],
                                    },
                                    {
                                        'img_title': '图5.2017年上半年民航国内旅行者特征',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年上半年民航国内旅行者特征.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图5所示，2017年上半年国内市场旅客性别比例基本与2016年同期保持稳定，男性旅客比例超女性7个百分点，依然占据市场主体优势。',
                                            '年龄分布方面有微小变化，24~30岁旅客出行比例同比下降1%，而60岁以上旅客出行比例同比上升1%，由航指数的节假日指数数据也可以看出60岁以上旅客在节假日出行比例上逐年上升，市场上层出不穷的“老年游”产品及充足的时间、良好的经济条件均促进了旅客的出游热情。',
                                            '上半年国内市场四成以上旅客提前预订天数 依然集中在航班起飞前3天内，但较2016年同期相比，提前1-3天预订的旅客比例下降1%，提前16-30天预订的旅客比例上升一个百分点。',
                                            '在国内市场中跟团出行市场比例较小，上半年仅有6%的旅客出行选择了跟团，较2016年同期下降1%；而在自由行旅客中超过半数为单独出行，1/4民航出行为双人结伴出行，两者较2016年同期均保持稳定。',
                                            '在值机环节虽然自助值机模式不断增加，柜台值机比例同比有4%的下降，但目前仍是旅客首选。提前3小时以内值机旅客比例同比下降3%，但仍占据七成以上的高位。',
                                        ],
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
                                        'explanation': [
                                            '2017年上半年民航国际航线旅客规模1667万人，同比增幅4%，增速低于国内市场10个百分点。平均飞行距离较2016年同期（2955公里）呈增长趋势，达到3243公里。（参见图6）',
                                            '国际航线旅客重复购买率1.93，继2016年上半年出现同比下降趋势后，2017年上半年同比呈现平稳状态，旅客出行习惯或将出现变动迹象。',
                                        ],
                                    },
                                    {
                                        'img_title': '图7.2017年上半年民航国际旅行者特征',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年上半年民航国际旅行者特征.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图7所示，2017年上半年国际市场中以旅游为目的的民航旅客目的地偏好出现小范围变化，去往日韩朝的旅客除41~50年龄段比例有所上升外，其他年龄段同比降幅均在2%左右；各年龄段去往北美洲、东南亚及西南太平洋的旅客比例均有1%—4%不同程度的同比上升。',
                                            '国际市场的提前预订周期明显长于国内市场，47%的旅客提前一个月开始预订，较2016年同期上升3个百分点。',
                                            '国际出行旅客跟团比例明显高于国内，但近年来也呈现出下降趋势，上半年有1/4旅客选择跟团出游，较2016年同期下降8个百分点；而在自由行的旅客中独自出行的比例也略少于国内出行，近半数自由行旅客为两人以上结伴出行，与2016年同期保持稳定。',
                                        ],
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
                                'h3': '节假日出行：三大类航线在节假日表现出很大差异化：国内航线保持相对稳定的增长态势；国际航线则增速明显放缓；港澳台市场则在复苏之路上缓慢前行。',
                                'h3_section': [
                                    {
                                        'img_title': '图8.2017年上半年节假日市场概况',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年上半年节假日市场概况.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图8所示，2017年春节长假依然是日均旅客量最多的假期，国内航线增长加快，同比增幅达到16%，超2016年同期13个百分点；除春节外的其他小长假，国内航线同样保持着相对稳定的增长态势。',
                                            '国际航线则出现明显的增速放缓态势，元旦、春节、五一小长假的日均旅客量同比增幅已放缓至10%以下，甚至在清明、端午小长假出现了负增长现象。',
                                            '港澳台航线在上半年前四个小长假表现欠佳，持续呈负增长趋势，且春节小长假的日均旅客量已下降至13%；然而在端午小长假中港澳台市场日均旅客量表现出利好的复苏迹象，同比上升7个百分点，但未来市场发展如何还需进一步观察。',
                                        ],
                                    }
                                ]
                            },
                            {
                                'h3': '“萨德”致中—韩航线失利：由于“萨德”事件影响，2017年3月3日，国家旅游局在官网发布《赴韩国旅游提示》后国内多家旅游企业全面下架韩国游产品。随后一周中，中-韩航线未来一个月航班预订量出现了大量的取消。',
                                'h3_section': [
                                    {
                                        'img_title': '图9.赴韩旅客量增长走势',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('赴韩旅客量增长走势.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图9所示，2015年MERS疫情使得赴韩旅客量断崖式下跌，以致2016年6-8月的旅客量呈爆发式增长，之后从9月开始，赴韩旅客量增长走势逐渐回归常态。',
                                            '2017年初随着“萨德”事件的推进及民众的强烈抗议，3月初中—韩航线再次迎来市场“寒冬”，赴韩旅客取消量倍增，3-6月赴韩旅客量同比下降45%。',
                                            '鉴于多种因素的影响，3月后中-韩航线各月运力投放同样出现了不同程度的缩减，3-6月运力投放同比下降36%。',
                                        ],
                                    }
                                ]
                            },
                            {
                                'h3': '中-澳旅游年助力民航市场：2017年为中-澳旅游年，宽松的对华签证政策为民航市场带来了新动力。多家航司加大运力投放力度，迎来旅客量高涨的同时客座率也明显上升。',
                                'h3_section': [
                                    {
                                        'img_title': '图10.中澳间执飞航线图',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('中澳间执飞航线图.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '2017年上半年共有7家国内航空公司运营中-澳航线，分别是国航、东航、南航、海航、厦航、川航和首都航空，其中涉及航线28条。',
                                            '执飞的28条航线中，国航、东航、南航三大航共占据六成以上的市场份额。开通中—澳航线的城市中广州是最多的也是唯一一个拥有5条不同航线的城市。',
                                        ],
                                    },
                                    {
                                        'img_title': '图11.上半年赴澳旅客量增长走势',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('上半年赴澳旅客量增长走势.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图11所示，自2016年中澳关系逐渐升温，旅客赴澳热情高涨，很大程度上推动了中-澳航线的运力投放力度，2017年1-6月月度运力增幅均超过25%。',
                                            '宽松利好的签证政策及大量的运力投放同时也一并带来了良好的市场反馈，2017年上半年赴澳旅客量平均同比增幅达到了27%。产投匹配度相一致，市场投放策略相对利好。',
                                        ],
                                    },
                                    {
                                        'img_title': '图12.2017上半年赴澳目的地分布情况',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017上半年赴澳目的地分布情况.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图12所示，2017上半年赴澳目的地中旅客量前5的澳大利亚城市依次为悉尼、墨尔本、布里斯班、珀斯和阿德莱德，其中去往悉尼和墨尔本的旅客量占到了市场总额的87%。',
                                            '2016年年底新开航线涉及的阿德莱德虽市场份额较少，但2017年上半年旅客量市场份额已接近老航线珀斯，市场潜力不可小觑。',
                                            '布里斯班毗邻黄金海岸市，近年来火热的海岛游需求也间接带动了布里斯班旅客量的逐年上涨，2017年上半年旅客量增长气势十足，同比增幅34%，已超过第一、二大城市的增长水平。',
                                        ],
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
                                            '国内航线暑运峰值期或将拉长，峰值区间相对平滑，整个暑运期间景气指数将维持在134以上；十一假期国内航线景气指数有望迎来5个百分点增长。',
                                            '国际航线下半年将又一次刷新峰值，景气指数将在8月初迎来峰值期，较2016年同期增幅有望达到14%。',
                                            '港澳台市场在下半年的两个波峰期尖点景气指数均有望达到120以上峰值，且在波谷期表现优于去年，淡季低点较去年略有提升。'
                                        ],
                                    },
                                    {
                                        'img_title': '图14.量价指数值预测走势图',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('量价指数值预测走势图.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '预计2017下半年市场运输量指数将维持在高位，国内航线运输量指数有望保持在180以上，国际航线运输量指数或将突破300到达350的新高度，港澳台航线运输量指数平稳维持在150—180之间。',
                                            '价格指数方面，国内航线价格指数十一假期之前尚能维持在90以上，假期过后则逐渐降至80左右。',
                                            '国际航线价格指数则整体低于国内航线，暑期过半价格指数开始逐渐走低，十一假期过后将在70以下浮动。'
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
                                            '如图15所示，国内航线运力投放稳定增长，同比2016年暑期增投20%。截止到六月底的预订量增幅暂（17%）低于运力投放增幅，但就2016年同期来说，预订量市场表现仍处于稳步上升趋势。',
                                            '国际航线较2016年增速相比出现增长乏力现象，运力投放同比2016年暑期增投6%。但其预订量却较2016年同期下降了3个百分点，供大于求的市场状态使得今年暑期的国际市场充满了悬念。',
                                            '港澳台航线暑期市场就目前展望而言表现欠佳，无论从运力投放或同期的预订水平都低于2016年同期。'
                                        ],
                                    },
                                    {
                                        'img_title': '图16.2017年暑运国内重点市场',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年暑运国内重点市场.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图16所示，国内市场暑期重点投放城市依然是上半年的热点城市，TOP10重点城市依次为北京、上海、广州、重庆、西安、成都、昆明、深圳、杭州、郑州。',
                                            '重点市场的暑期预订量除北京与昆明之外，其他城市均高于2016年同期，西安与郑州的预订增幅均优于国内航线整体水平，市场基础与增长潜力并存。',
                                            '重点市场今年投放座位量增幅最大的城市为重庆，增幅达到46%，而预订量增幅最大的城市为新晋十强的郑州，增幅可达40%。'
                                        ],
                                    },
                                    {
                                        'img_title': '图17.2017年暑运出入境重点航线',
                                        'img': InlineImage(word_tpl.tpl, word_tpl.get_img_file('2017年暑运出入境重点航线.png'),
                                                           width=Mm(160)),
                                        'explanation': [
                                            '如图17所示，2017年暑运出入境市场的运力投放排名中，越南同比增幅最高48%，预订量增长也遥遥领先其他航线，达到83%；“中澳旅游年”的开幕推动了中—澳航线运力投放新增长，同比增幅达46%。',
                                            '中—韩航线市场“寒冬”依旧持续，暑运期间运力投放同比下降42%，预订量同比下降64%。中-日及中-泰航线分别位列出入境航线运力投放的第一、二位，然而其运力投放增幅和预订量增幅有明显放缓趋势，甚至出现了负增长情况，市场需求将逐渐趋于稳定。',
                                            '港澳台市场方面，中国内地往返香港和台湾的航线无论从运力投放还是同期预订量均出现不同幅度下滑；中国内地-澳门航线运力投放略好于港台市场，但预订量也有小幅下滑。'
                                        ],
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
                                        'explanation': [
                                            '如图18所示，展望2017年十一黄金周旅客预订偏好，东南亚区域为当前最大的出入境热点，占据预订市场份额24%；日韩朝较去年同期相比失去了8%的市场份额。',
                                            '往返北美洲、港澳台和欧洲区域的预订需求份额相近；港澳台所占份额低于去年同期，市场需求动力不足。',
                                            '基于出入境整体市场的迅速扩张，中-美航线持续火热的市场需求仅使北美区域预订份额增长1个百分点；中东、西南太平洋区域要想抢占更多国际市场份额仍需更有吸引力的元素激发市场潜力。'
                                        ],
                                    },
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        'footer': {
            'title': '结语：',
            'paragraphs': [
                '随着“一带一路”的提出与推进，打造世界级城市群和机场群成为崛起经济全球化时代的显著特征，同时也给航空运输业的发展带来了新的机遇和新的挑战。随着城市群和机场群的发展，航空运输市场多样化趋势愈加明显，航空服务不断向价值链两端延伸，这也给民航业管理理念、经营模式以及政府监管方式带来了巨大挑战。在这样的发展过程中，能为政府机构、航空公司、机场以及处于民航产业链上各行各业，以精准的数据结合科学的研判方法，及时的洞悉市场变幻风云，提供更加直接高效的决策支撑，将是航指数不懈努力的方向。',
            ],
            'annotation': {
                'title': '注释：',
                'content': [
                    '[注1]景气指数：是一种综合性指标，综合考虑市场运输量规模、价格水平和行业投入产出比计算得到，以2011年100点作为基准。',
                    '[注2]运输量指数：反应行业市场规模变化，以客公里指标为基础的计算指标，以2011年100点作为基准。',
                    '[注3]价格指数：反应旅客支付价格变化，以客公里收益为基础的计算指标，以2011年100点作为基准。',
                    '[注4]客座率：反应行业的投入产出比指标，客座率=客公里/座公里',
                    '[注5]旅客规模：按旅客个体计算，通过证件唯一识别和确定民航旅客，多次乘坐飞机的旅客记为1个个体。',
                    '[注6]重复购买率：每个旅客购买机票的平均次数。',
                    '[注7]提前预订天数：旅客起飞日期与旅客PNR创建日期之差。',
                    '[注8]暑运：7月1日至8月31日。'
                ]
            }
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

