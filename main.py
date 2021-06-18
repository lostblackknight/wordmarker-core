import core
import scripts
from core.data import Data

if __name__ == '__main__':
    core.init_context("config.yaml")
    # scripts.init_data_base(core.csv_tpl, core.pdbc_tpl)  # 数据库脚本
    text = scripts.TextConverter(core.word_tpl, Data({
        '城市数据': core.pdbc_tpl.query_table("t_city_data"),
        '市场数据': core.pdbc_tpl.query_table("t_market_data"),
        '景气指数': core.pdbc_tpl.query_table("t_prosperity_index"),
        '量价指数': core.pdbc_tpl.query_table("t_volume_price_index"),
        '旅客规模': core.pdbc_tpl.query_table("t_passenger_size"),
        '旅客特征': core.pdbc_tpl.query_table("t_passenger_characteristics"),
        '日均旅客量': core.pdbc_tpl.query_table("t_average_daily_passenger_volume"),
    }))
    scripts.generate_word(core.word_tpl, "2017年航指数半年白皮书—发布版.docx", text)
