import json

from complai_web_crawler.items import OffenegesetzeItem
from complai_web_crawler.spiders.parent_spider import ParentSpider


class OffenegesetzeSpider(ParentSpider):
    name = "offenegesetze"
    allowed_domains = ["api.offenegesetze.de"]

    custom_settings = {"MONGO_DATABASE": name}

    def __init__(
        self,
        search_terms=("lebensmittel",),
        years=("2020",),
        type_of_acts=("bgbl1", "bgbl2"),
        *args,
        **kwargs,
    ):
        super(OffenegesetzeSpider, self).__init__(
            search_terms, years, type_of_acts, *args, **kwargs
        )

    def get_start_url(self, search_term, year, type_of_act):
        start_url = (
            "https://api.offenegesetze.de/v1/veroeffentlichung/?"
            "format=json"
            f"&kind={type_of_act}"
            f"&q={search_term}"
            f"&year={year}"
        )
        return start_url

    def parse(self, response, **cb_kwargs):
        self.logger.info(f"A response from {response.url} just arrived!")

        data = json.loads(response.text)

        for result in data["results"]:
            item = OffenegesetzeItem(result)
            item["search_term"] = response.cb_kwargs["search_term"]
            item["type_of_act"] = response.cb_kwargs["type_of_act"]

            yield item
