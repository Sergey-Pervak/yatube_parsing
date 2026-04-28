import scrapy
from yatube_parsing.items import YatubeParsingItem


class YatubeSpider(scrapy.Spider):
    name = "yatube"
    # allowed_domains = ["158.160.177.221"]
    allowed_domains = ["158.160.212.51"]
    start_urls = ["http://158.160.212.51/"]

    def parse(self, response):
        for card in response.css('div.card-body'):
            author = card.css('strong.d-block::text').get()
            # full_text = ''.join(card.css('p.card-text::text').getall()).strip()
            full_text = ' '.join(
                t.strip() for t in card.css('p::text').getall()
            ).strip()
            date = card.css('small.text-muted::text').get()
            # group = card.css('a.group_link::text').get()
            # yield {
            #     'author': author,
            #     'text': full_text,
            #     'date': date
            # }

            data = {
                'author': author,
                'text': full_text,
                'date': date
            }
            yield YatubeParsingItem(data)

        # next_page = response.css('li.page-item a.page-link:contains("Следующая »")::attr(href)').get()
        next_page = response.xpath("//a[contains(., 'Следующая')]/@href").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)
