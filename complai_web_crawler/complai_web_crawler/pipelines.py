import pymongo
from scrapy.exceptions import DropItem


class MetaDataPipeline:
    def process_item(self, item, spider):

        meta_data_list = item.get("meta_data")

        meta_data_dict = {}
        celex_number_found = False
        authors_found = False
        date_of_document_found = False

        for i, meta_data in enumerate(meta_data_list[::2]):
            value_idx = i * 2 + 1
            value = meta_data_list[value_idx]

            if meta_data == "CELEX-Nummer: ":
                meta_data_dict["celex_number"] = value
                celex_number_found = True

            elif meta_data == "Autor: ":
                meta_data_dict["authors"] = value.split(", ")
                authors_found = True

            elif meta_data == "Datum des Dokuments: ":
                meta_data_dict["date_of_document"] = value
                date_of_document_found = True

            else:
                spider.logger.info(f"Additional meta data: {meta_data}")

        if celex_number_found and authors_found and date_of_document_found:
            item["meta_data"] = meta_data_dict
            spider.logger.info("Processed meta data of item")
            return item
        else:
            raise DropItem(f"Not all necessary metadata found: {meta_data_list}")


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
            collection_name=crawler.settings.get("COLLECTION_NAME"),
        )

    def open_spider(self, spider):
        mongo_dict = {
            "mongo_uri": self.mongo_uri,
            "mongo_db": self.mongo_db,
            "collection_name": self.collection_name,
        }

        spider.logger.info(f"mongo_dict: {mongo_dict}")
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        spider.logger.info("Inserted item in database")
        return item
