import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from bs4 import BeautifulSoup


class ScrapedItems(Item):
    url = Field()
    title = Field()
    summary = Field()
    details = Field()
    msds = Field()
    category = Field()

class V3crawlerSpider(CrawlSpider):
    name = "bowers1"

    prefix = 'http://products.bowersindustrial.com'
    rules = (Rule(LinkExtractor(canonicalize=True, unique=True), callback='parse_items', follow=True),)
    domain = "products.bowersindustrial.com"
    allowed_domains = ["products.bowersindustrial.com"]
    start_urls = [
        prefix
    ]

    def parse_items(self, response):

        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        title = hxs.select('//*[@id="ContentPlaceHolder1_Panel1"]/div[3]/h4').extract()
        sourcestring = ''.join(title)
        title = sourcestring.encode('ascii', 'ignore')
        summary = hxs.select('//*[@id="ContentPlaceHolder1_Panel1"]/div[4]/div[1]/p').extract()
        sourcestring = ''.join(summary)
        summary = sourcestring.encode('ascii', 'ignore')
        details = hxs.select('//*[@id="ContentPlaceHolder1_Panel1"]/div[5]/table').extract()
        sourcestring = ''.join(details)
        details = sourcestring.encode('ascii', 'ignore')
        # msds = (hxs.select('//*[@id="ContentPlaceHolder1_Panel1"]/div[4]/div[2]/div/table/tbody/tr/td/a/@href').extract())
        #safestring = sourcestring.encode('ascii', 'ignore')
        #cleanmsds = BeautifulSoup(safestring)
        category = hxs.select('//*[@id="content_area"]/table/tbody/tr/td/a[2]').extract()
        sourcestring = ''.join(category)
        category = sourcestring.encode('ascii', 'ignore')


        item['url'] = response.url
        item['title'] = title
        item['summary'] = summary
        item['details'] = details
        # item['msds'] = cleanmsds.get_text()
        item['category'] = category
        return item
