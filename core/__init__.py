import os
from docxtpl import DocxTemplate
from wordmarker.contexts import WordMarkerContext
from wordmarker.templates import CsvTemplate, PdbcTemplate, WordTemplate
from core.text import text

csv_tpl: CsvTemplate
pdbc_tpl: PdbcTemplate
word_tpl: WordTemplate
tpl: DocxTemplate


def init_context(ctx):
    global csv_tpl, pdbc_tpl, word_tpl, tpl
    WordMarkerContext(os.path.abspath(ctx))
    csv_tpl = CsvTemplate()
    pdbc_tpl = PdbcTemplate()
    word_tpl = WordTemplate()
    tpl = word_tpl.tpl
