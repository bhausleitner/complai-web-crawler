import logging
from pprint import pformat

import click
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.argument(
    "spider_names",
    nargs=-1,
    required=True,
    type=click.Choice(["eur_lex", "offenegesetze"]),
)
@click.option(
    "--search_terms",
    "-s",
    multiple=True,
    default=("lebensmittel",),
    show_default=True,
    help="Search terms for website to crawl",
    type=str,
)
@click.option(
    "--years",
    "-y",
    multiple=True,
    default=("2020",),
    show_default=True,
    help="Years for search results",
    type=str,
)
def main(spider_names, **kwargs):
    logger.info(f"spider_names: {spider_names}\nkwargs:\n\t{pformat(kwargs)}")
    process = CrawlerProcess(get_project_settings())

    for spider_name in spider_names:
        logger.info(f"Spider {spider_name} running")
        process.crawl(crawler_or_spidercls=spider_name, **kwargs)
        logger.info(f"Spider {spider_name} finished")

    process.start()  # the script will block here until the crawling is finished


if __name__ == "__main__":
    main()
