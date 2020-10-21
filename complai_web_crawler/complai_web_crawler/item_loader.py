import re

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from w3lib.html import remove_tags


def filter_pdf_url(url):
    if re.match(pattern=r".*/PDF/.*", string=url):
        return url


def urljoin(url, loader_context):
    response = loader_context["response"]
    return response.urljoin(url)


class EurLexLoader(ItemLoader):
    default_output_processor = TakeFirst()

    meta_data_in = MapCompose(remove_tags)
    meta_data_out = Identity()

    pdf_url_in = MapCompose(filter_pdf_url, urljoin)
