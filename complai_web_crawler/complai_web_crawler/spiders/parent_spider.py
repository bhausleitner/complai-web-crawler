from itertools import product

from scrapy import Request
from scrapy import Spider


class ParentSpider(Spider):
    def __init__(
        self, search_terms, years, type_of_acts, go_to_next_page=False, *args, **kwargs
    ):
        super(ParentSpider, self).__init__(*args, **kwargs)

        self.search_terms = search_terms
        self.years = years
        self.type_of_acts = type_of_acts
        self.go_to_next_page = go_to_next_page

    def get_start_url(self, search_term, year, type_of_act):
        raise NotImplementedError()

    def start_requests(self):
        for search_term, year, type_of_act in product(
            self.search_terms, self.years, self.type_of_acts
        ):
            start_url = self.get_start_url(search_term, year, type_of_act)
            yield Request(
                url=start_url,
                cb_kwargs={"search_term": search_term, "type_of_act": type_of_act},
            )

    def parse(self, response, **cb_kwargs):
        raise NotImplementedError()
