import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
import hashlib

class ScrapedItems(Item):
    url = Field()
    source = Field()

class V3crawlerSpider(CrawlSpider):
    name = "v3crawler"
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def __init__(self, domain='nemsis.org', *args, **kwargs):
        super(V3crawlerSpider, self).__init__(*args, **kwargs)
        self.domain = domain
        self.allowed_domains = ["nemsis.org"]
        self.start_urls = ['http://www.nemsis.org/supportv3/stateProgressReports/Alabama.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/virginIslands.html']

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        source = hxs.select('//*[@id="subPageContainer"]').extract()
        sourcestring = ','.join(source)
        safestring = sourcestring.encode('ascii', 'ignore')
        print(response.url)
        print(safestring)
        item['url'] = response.url
        item['source'] = safestring
        return item

