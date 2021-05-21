import copy
import ast
from wordmarker.templates import WordTemplate
from jinja2 import Template, Environment, meta
from wordmarker.utils import YamlUtils
from abc import ABCMeta


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
