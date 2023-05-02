import scrapy


# got help from  "Coding Web Crawler in Python with Scrapy" - by NeuralNine
# https://www.youtube.com/watch?v=m_3gjHGxIJc

class KaubamajaSpider(scrapy.Spider):
    name = 'kaubamaja'
    start_urls = ['https://www.kaubamaja.ee/kodu/vannituba']

    def parse(self, response, **kwargs):
        for item in response.css('.products-grid__link'):
            yield {
                'Title': item.xpath('@title').get(),
                'Price': item.css('.price::text').get().replace('\xa0', ' '),
                'Picture href': item.css('.products-grid__image img:nth-child(2)::attr(src)').get(),
            }
        # 1 page under category
        # next_page = response.css('.pagination__link.pagination__link--next a::attr(href)').get()

        # ALL pages under category
        next_page = response.css('.pagination__link.pagination__link--next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
