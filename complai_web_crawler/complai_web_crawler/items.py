from scrapy import Field
from scrapy import Item


class ParentItem(Item):
    search_term = Field()
    type_of_act = Field()
    title = Field()


class EurLexItem(ParentItem):
    meta_data = Field()
    pdf_url = Field()


class OffenegesetzeItem(ParentItem):
    api_url = Field()
    content__highlight = Field()
    date = Field()
    document_url = Field()
    id = Field()
    kind = Field()
    law_date = Field()
    num_pages = Field()
    number = Field()
    order = Field()
    page = Field()
    pdf_page = Field()
    score = Field()
    title__highlight = Field()
    url = Field()
    year = Field()
