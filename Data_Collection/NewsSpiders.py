import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from time import gmtime, strftime
from wrapper import goal_parser, espn_parser, sky_parser

class GoalSpider(CrawlSpider):
    name = 'goal'
    allowed_domains = ['www.goal.com']
    start_urls = ['http://www.goal.com/en/news/1']
    rules = [Rule(
        LinkExtractor(allow=['/news/.*']),
        callback='parse_item',
        follow=True
        )
    ]
    counter = 0
    def parse_item(self, response):

        result = dict()
        result['url'] = response.url
        html = response.body.decode(response.encoding)
        result['raw_content'] = goal_parser(html)
        result['timestamp_crawl'] = strftime("%Y-%m-%dT%H:%M:%S%Z", gmtime())
        self.counter+=1

        print response.url
        return result

class ESPNSpider(CrawlSpider):
    name = 'espn'
    allowed_domains = ['www.espn.com']
    start_urls = ['http://www.espn.com/soccer/league/_/name/eng.1']
    rules = [
    

        Rule(
            LinkExtractor(allow=['http://www.espn.com/soccer/.*/story/.*']), #http://www.espn.com/soccer/west-bromwich-albion/story/3408563/west-brom-owners-to-quiz-chief-executive-over-slump-reports
            callback='parse_item',
            follow=True
            ),
        Rule(
            LinkExtractor(allow=['http://www.espn.com/soccer/.*']), 
            callback='parse_item2',
            follow=True
            )            
            
    ]

    def parse_item(self, response):

        result = dict()
        result['url'] = response.url
        html = response.body.decode(response.encoding)   
        result['raw_content'] = espn_parser(html)
        result['timestamp_crawl'] = strftime("%Y-%m-%dT%H:%M:%S%Z", gmtime())
        print response.url
        return result

    def parse_item2(self, response):
        return

class SkySpider(CrawlSpider):
    name = 'sky'
    allowed_domains = ['www.skysports.com']
    start_urls = ['http://www.skysports.com/football/news']
    rules = [
    
        Rule(
            LinkExtractor(allow=['http://www.skysports.com/football/news/.*']), 
            callback='parse_item',
            follow=True
            )
    ]

    def parse_item(self, response):

        result = dict()
        result['url'] = response.url
        html = response.body.decode(response.encoding)
        result['raw_content'] = sky_parser(html)        
        result['timestamp_crawl'] = strftime("%Y-%m-%dT%H:%M:%S%Z", gmtime())

        print response.url
        return result

