import core
import scripts

if __name__ == '__main__':
    core.init_context("config.yaml")
    # scripts.init_data_base(core.csv_tpl, core.pdbc_tpl)  # 数据库脚本
    # scripts.generate_word(core.word_tpl, "2017年航指数半年白皮书—发布版（新）.docx")  # 生成文档
    c = scripts.TextConverter(core.word_tpl)
    d = c.convert_to_dict()
    print(d)
