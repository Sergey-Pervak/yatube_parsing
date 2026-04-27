import scrapy


class YatubeSpider(scrapy.Spider):
    name = "yatube"
    allowed_domains = ["158.160.177.221"]
    start_urls = ["http://158.160.212.51/"]

    def parse(self, response):
        pass
