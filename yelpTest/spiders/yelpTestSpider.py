# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from yelpTest.items import YelpspiderItem
from yelpTest.optutil import OptUtil
import json


class YelpTestSpider(RedisCrawlSpider):
    name = 'yelp_test'
    # 增加redis_keys
    redis_key = 'yelpTestSpider:start_urls'
    # allowed_domains = ['yelp.com']
    # start_urls = ['https://www.yelp.com/search?find_desc=Mortgage+Company&find_loc=New+York%2C+NY&ns=1']
    # 搜索条件 https://www.yelp.com/search?find_desc=&find_loc=New%20York%2C%20NY
    # search_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=&find_loc=.+[&start=\d+]?$'))
    # search_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=&find_loc=.+$'))
    # 8类分类
    # https://www.yelp.com/search?cflt=contractors&find_loc=Washington%2C%20DC
    # contractors_link = LinkExtractor(allow=(r"^https://www.yelp.com/search?cflt=contractors&find_loc=.+$"))
    # ----------------------------第二个大类
    # contractors_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=contractors&find_loc=.+[&start=\d+]?$'))
    # landscaping_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=landscaping&find_loc=.+[&start=\d+]?$'))
    # electricians_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=electricians&find_loc=.+[&start=\d+]?$'))
    # locksmiths_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=locksmiths&find_loc=.+[&start=\d+]?$'))
    # homecleaning_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=homecleaning&find_loc=.+[&start=\d+]?$'))
    # movers_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=movers&find_loc=.+[&start=\d+]?$'))
    # hvac_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=hvac&find_loc=.+[&start=\d+]?$'))
    # plumbing_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=plumbing&find_loc=.+[&start=\d+]?$'))
    # ---------------------------第一个大类
    delivery_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=delivery&find_loc=.+[&ytp_st=.+&attrs=.+&start=\d+]?$'))
    takeout_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=takeout&find_loc=.+[&ytp_st=.+&attrs=.+&start=\d+]?$'))
    reservations_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=reservations&find_loc=.+[&ytp_st=.+&attrs=.+&start=\d+]?$'))
    waitlist_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=waitlist&find_loc=.+[&start=\d+]?$'))
    burgers_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=burgers&find_loc=.+[&start=\d+]?$'))
    chinese_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=chinese&find_loc=.+[&start=\d+]?$'))
    italian_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=italian&find_loc=.+[&start=\d+]?$'))
    mexican_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=mexican&find_loc=.+[&start=\d+]?$'))
    # -------------------------第三大类
    # https://www.yelp.com/search?cflt=autorepair&find_loc=New+York%2C+NY
    # https://www.yelp.com/search?cflt=autorepair&find_loc=New%20York%2C%20NY&start=10
    autorepair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=autorepair&find_loc=.+[&start=\d+]?$'))
    car_dealers_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=car_dealers&find_loc=.+[&start=\d+]?$'))
    auto_detailing_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=auto_detailing&find_loc=.+[&start=\d+]?$'))
    oilchange_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=oilchange&find_loc=.+[&start=\d+]?$'))
    bodyshops_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=bodyshops&find_loc=.+[&start=\d+]?$'))
    parking_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=parking&find_loc=.+[&start=\d+]?$'))
    carwash_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=carwash&find_loc=.+[&start=\d+]?$'))
    towing_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=towing&find_loc=.+[&start=\d+]?$'))
    # -----------------------第四大类
    dryclean_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=dryclean&find_loc=.+[&start=\d+]?$'))
    hair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=hair&find_loc=.+[&start=\d+]?$'))
    mobilephonerepair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=mobilephonerepair&find_loc=.+[&start=\d+]?$'))
    gyms_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=gyms&find_loc=.+[&start=\d+]?$'))
    bars_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=bars&find_loc=.+[&start=\d+]?$'))
    massage_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=massage&find_loc=.+[&start=\d+]?$'))
    nightlife_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=nightlife&find_loc=.+[&start=\d+]?$'))
    shopping_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=shopping&find_loc=.+[&start=\d+]?$'))

    # 每页中的详情页 https://www.yelp.com/biz/ge-construction-group-washington-dc-2
    detail_link = LinkExtractor(allow=(r'^https://www.yelp.com/biz/\w+-\w+-.+$'))
    rules = (
        Rule(delivery_page_link, follow=True),
        Rule(takeout_page_link, follow=True),
        Rule(reservations_page_link, follow=True),
        Rule(waitlist_page_link, follow=True),
        Rule(burgers_page_link, follow=True),
        Rule(chinese_page_link, follow=True),
        Rule(italian_page_link, follow=True),
        Rule(mexican_page_link, follow=True),

        Rule(autorepair_page_link, follow=True),
        Rule(car_dealers_page_link, follow=True),
        Rule(auto_detailing_page_link, follow=True),
        Rule(oilchange_page_link, follow=True),
        Rule(bodyshops_page_link, follow=True),
        Rule(parking_page_link, follow=True),
        Rule(carwash_page_link, follow=True),
        Rule(towing_page_link, follow=True),

        Rule(dryclean_page_link, follow=True),
        Rule(hair_page_link, follow=True),
        Rule(mobilephonerepair_page_link, follow=True),
        Rule(gyms_page_link, follow=True),
        Rule(bars_page_link, follow=True),
        Rule(massage_page_link, follow=True),
        Rule(nightlife_page_link, follow=True),
        Rule(shopping_page_link, follow=True),
        Rule(detail_link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = YelpspiderItem()
        item['referer'] = response.request.headers['Referer'].decode(encoding='utf-8')
        item['detail_page_url'] = response.url
        # item['logo'] = response.meta['_logo']
        # item['city'] = self.get_city(response)
        # 公司名
        item['company'] = self.get_company(response)
        item['address'] = self.get_address(response)
        # category
        item['category'] = self.get_category(response)
        # 手机号
        item['phone'] = self.get_phone(response)
        # 公司链接
        item['websiteurl'] = self.get_websiteurl(response)
        # 公司图片,多张以逗号分隔
        item['img_url'] = self.get_img_url(response)
        # 描述
        item['content'] = self.get_content(response)
        # bussiness_content
        item['business_content'] = self.get_bussiness_content(response)
        # 经纬度
        item['latitude'] = self.get_latitude(response)
        item['longitude'] = self.get_longitude(response)
        yield item

    def get_city(self, response):
        city = response.xpath('//span/input[@id="dropperText_Mast"]/@value').extract()
        return city[0] if city else ""


    def get_company(self, response):
        company = response.xpath('//div[@class="top-shelf"]//h1/text()').extract()
        if company:
            return ' '.join(company)
        else:
            return ''

    def get_address(self, response):
        address = response.xpath('//div[@class="top-shelf"]//div[@class="mapbox"]//address/text()').extract()
        if address:
            return address[0].strip()
        else:
            return ''

    def get_category(self, response):
        category = response.xpath('//div[@class="price-category"]/span[@class="category-str-list"]/a[contains(@href, "/c/")]/text()').extract()
        if category:
            if len(category) > 1:
                return ",".join(category).strip()
            else:
                return category[0].strip()
        else:
            return ''

    def get_phone(self, response):
        phone = response.xpath('//div[@class="top-shelf"]//span[@class="biz-phone"]/text()').extract()
        if phone:
            return phone[0].strip()
        else:
            return ''

    def get_websiteurl(self, response):
        websiteurl = response.xpath('//div[@class="top-shelf"]//span/a[contains(@href, "biz_redir")]/@href').extract()
        if websiteurl:
            websiteurl = websiteurl[0]
            return OptUtil.urlDecoder(websiteurl[websiteurl.index("=") + 1:websiteurl.index("&")])
        else:
            return ''

    def get_img_url(self, response):
        img_url = response.xpath('//a[contains(@href, "/biz_photos")]/img/@src').extract()
        if img_url:
            referer = response.request.headers['Referer'].decode(encoding='utf-8')
            detail_url = response.url
            pics = ','.join(img_url)
            print("referer: %s------detail_url: %s-----pics: %s" % (referer, detail_url, pics))
            return pics
        else:
            return ''

    def get_content(self, response):
        content = response.xpath(
            '//div[contains(@class, "island")]/div[@class="from-biz-owner-content"]/p[position()<=3]').extract()
        if content:
            return ''.join(content).replace("<p>", "").replace("</p>", "").replace("\n", "")\
                .replace("\xa0", "").replace("<br>", "").replace("\n", "").strip()
        else:
            return ''

    def get_bussiness_content(self, response):
        business_content = response.xpath(
            '//div[contains(@class, "island")]/div[@class="from-biz-owner-content"]/p[position()>3]').extract()
        if business_content:
            return ''.join(business_content).replace("<p>", "").replace("</p>", "").replace("\n", "")\
                .replace("\xa0", "").replace("<br>", "").strip()
        else:
            return ''

    def get_location(self, response):
        data_map_state = response.xpath('//div[@class="mapbox-map"]/div/@data-map-state').extract()
        json_result = json.loads(data_map_state[0]) if data_map_state else {}
        markers = json_result.get('markers')[1] if json_result and json_result.get('markers') and len(
            json_result.get('markers')) >= 2 else {}
        if markers and markers.get('location'):
            return markers.get('location')
        else:
            return {}

    def get_latitude(self, response):
        location = self.get_location(response)
        if location and location.get('latitude'):
            return location.get('latitude')
        else:
            return ''

    def get_longitude(self, response):
        location = self.get_location(response)
        if location and location.get('longitude'):
            return location.get('longitude')
        else:
            return ''
