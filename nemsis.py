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
                  'http://www.nemsis.org/supportv3/stateProgressReports/Alaska.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Arizona.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Arkansas.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/California.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Colorado.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Connecticut.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Delaware.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Florida.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Georgia.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Hawaii.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Idaho.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Illinois.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Indiana.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Iowa.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Kansas.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Kentucky.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Louisiana.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Maine.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Maryland.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Massachusetts.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Michigan.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Minnesota.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Mississippi.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Missouri.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Montana.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Nebraska.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Nevada.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/NewHampshire.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/NewJersey.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/NewMexico.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/NewYork.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/NorthCarolina.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/NorthDakota.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Ohio.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Oklahoma.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Oregon.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Pennsylvania.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/RhodeIsland.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/SouthCarolina.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/SouthDakota.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Tennessee.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Texas.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Utah.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Vermont.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Virginia.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Washington.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/WestVirginia.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Wisconsin.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/Wyoming.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/americanSamoa.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/guam.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/marianaIslands.html',
                  'http://www.nemsis.org/supportv3/stateProgressReports/puertoRico.html',
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

