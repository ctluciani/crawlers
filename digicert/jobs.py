import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class ScrapedItems(Item):
    url = Field()
    title = Field()
    content = Field()


class V3crawlerSpider(CrawlSpider):
    name = "digicrawler"
    rules = (Rule(LinkExtractor(), callback='parse', follow=False),)

    def __init__(self, domain='digicert.com', *args, **kwargs):
        super(V3crawlerSpider, self).__init__(*args, **kwargs)
        prefix = 'https://www.digicert.com'
        self.domain = domain
        self.allowed_domains = ["digicert.com"]
        self.start_urls = [
            prefix + '/news/jobs/business-validation-intern.htm',
            prefix + '/news/jobs/business-validation.htm',
            prefix + '/news/jobs/customer-relations-intern.htm',
            prefix + '/news/jobs/manager-sales-operations.htm',
            prefix + '/news/jobs/senior-software-quality-engineer.htm',
            prefix + '/news/jobs/software-engineer.htm',
            prefix + '/news/jobs/technical-support.htm',
            prefix + '/news/software-quality-engineer.htm'
        ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        title = hxs.select('/html/body/h1').extract()
        content = hxs.select('//*[@id="mainContent"]/div[1]').extract()
        item['url'] = response.url
        item['title'] = title
        item['content'] = content
        return item
