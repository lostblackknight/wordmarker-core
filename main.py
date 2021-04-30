from wordmarker.contexts import WordMarkerContext
import core

if __name__ == '__main__':
    WordMarkerContext('config.yaml')
    core.init()
    # data_base()  # 运行一次即可
    core.generate()
    core.build('2017年航指数半年白皮书—发布版（新）.docx')
