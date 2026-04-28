import scrapy


class GroupSpider(scrapy.Spider):
    name = "group"
    allowed_domains = ["158.160.212.51"]
    start_urls = ["http://158.160.212.51/"]

    def parse(self, response):
        # all_groups = response.css('a[href^="/group/"]')
        all_groups = response.css('a.group_link::attr(href)')

        for group_link in all_groups:
            yield response.follow(group_link, callback=self.parse_group)

        next_page = response.xpath("//a[contains(., 'Следующая')]/@href").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_group(self, response):
        group_name = response.css('div.card-body h2::text').get().strip()
        description = response.css('li.list-group-item p.group_descr::text').get().strip()
        posts_count = int(response.css('div.h6.text-muted.posts_count::text').get('').replace('Записей:', '').strip())

        yield {
            'group_name': group_name,
            'description': description,
            'posts_count': posts_count,
        }

    # with open('groups.csv', encoding='utf-8') as file:
    #     content = file.read()
    #     print(len(content))
