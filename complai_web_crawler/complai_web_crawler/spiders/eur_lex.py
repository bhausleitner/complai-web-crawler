from complai_web_crawler.item_loader import EurLexLoader
from complai_web_crawler.items import EurLexItem
from complai_web_crawler.spiders.parent_spider import ParentSpider


class EurLexSpider(ParentSpider):
    name = "eur_lex"
    allowed_domains = ["eur-lex.europa.eu"]

    custom_settings = {
        "ITEM_PIPELINES": {
            "complai_web_crawler.pipelines.MetaDataPipeline": 300,
            "complai_web_crawler.pipelines.MongoPipeline": 400,
        },
        "MONGO_DATABASE": name,
    }

    def __init__(
        self,
        search_terms=("lebensmittel",),
        years=("2020",),
        type_of_acts=("regulation", "directive", "decision"),
        go_to_next_page=False,
        *args,
        **kwargs,
    ):
        super(EurLexSpider, self).__init__(
            search_terms, years, type_of_acts, go_to_next_page, *args, **kwargs
        )

    def get_start_url(self, search_term, year, type_of_act):
        start_url = (
            "https://eur-lex.europa.eu/search.html?"
            "textScope0=ti-te"
            "&DTA=2020"
            "&VV=true"
            f"&DB_TYPE_OF_ACT={type_of_act}"
            f"&DTA={year}"
            f"&typeOfActStatus={type_of_act}"
            "&type=advanced"
            "&lang=de"
            f"&andText0={search_term}"
            "&SUBDOM_INIT=LEGISLATION"
            "&DTS_SUBDOM=LEGISLATION"
            "&locale=de"
        )
        return start_url

    def parse(self, response, **cb_kwargs):
        self.logger.info(f"A response from {response.url} just arrived!")

        for idx, search_result in enumerate(response.css("div.SearchResult")):
            item_loader = EurLexLoader(
                item=EurLexItem(), selector=search_result, response=response
            )

            item_loader.add_value(
                field_name="search_term", value=response.cb_kwargs["search_term"]
            )
            item_loader.add_value(
                field_name="type_of_act", value=response.cb_kwargs["type_of_act"]
            )
            item_loader.add_css(field_name="title", css="h2 a.title::text")
            item_loader.add_css(
                field_name="meta_data",
                css=".CollapsePanel-sm .SearchResultData .row .col-sm-6 dl dt, dd",
            )
            item_loader.add_css(
                field_name="pdf_url",
                css=".CollapsePanel-sm .SearchResultData .row .col-sm-6 ul.SearchResultDoc li a::attr(href)",  # noqa: E501
            )

            yield item_loader.load_item()

        if self.go_to_next_page:
            next_page = (
                response.css(".ResultsTools .PaginationGroup a ")
                .re(r".*Next Page.*")[0]
                .split('"')[1]
                .replace("&amp;", "&")
            )
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
