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
    # delivery_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=delivery&find_loc=.+[&ytp_st=.+&attrs=.+&start=\d+]?$'))
    # takeout_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=takeout&find_loc=.+[&ytp_st=.+&attrs=.+&start=\d+]?$'))
    # reservations_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=reservations&find_loc=.+[&ytp_st=.+&attrs=.+&start=\d+]?$'))
    # waitlist_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=waitlist&find_loc=.+[&start=\d+]?$'))
    # burgers_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=burgers&find_loc=.+[&start=\d+]?$'))
    # chinese_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=chinese&find_loc=.+[&start=\d+]?$'))
    # italian_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=italian&find_loc=.+[&start=\d+]?$'))
    # mexican_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=mexican&find_loc=.+[&start=\d+]?$'))
    # # -------------------------第三大类
    # # https://www.yelp.com/search?cflt=autorepair&find_loc=New+York%2C+NY
    # # https://www.yelp.com/search?cflt=autorepair&find_loc=New%20York%2C%20NY&start=10
    # autorepair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=autorepair&find_loc=.+[&start=\d+]?$'))
    # car_dealers_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=car_dealers&find_loc=.+[&start=\d+]?$'))
    # auto_detailing_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=auto_detailing&find_loc=.+[&start=\d+]?$'))
    # oilchange_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=oilchange&find_loc=.+[&start=\d+]?$'))
    # bodyshops_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=bodyshops&find_loc=.+[&start=\d+]?$'))
    # parking_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=parking&find_loc=.+[&start=\d+]?$'))
    # carwash_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=carwash&find_loc=.+[&start=\d+]?$'))
    # towing_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=towing&find_loc=.+[&start=\d+]?$'))
    # # -----------------------第四大类
    # dryclean_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=dryclean&find_loc=.+[&start=\d+]?$'))
    # hair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=hair&find_loc=.+[&start=\d+]?$'))
    # mobilephonerepair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=mobilephonerepair&find_loc=.+[&start=\d+]?$'))
    # gyms_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=gyms&find_loc=.+[&start=\d+]?$'))
    # bars_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=bars&find_loc=.+[&start=\d+]?$'))
    # massage_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=massage&find_loc=.+[&start=\d+]?$'))
    # nightlife_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=nightlife&find_loc=.+[&start=\d+]?$'))
    # shopping_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?cflt=shopping&find_loc=.+[&start=\d+]?$'))
    """
    33个分类：
    1、贷款公司Mortgage Company  2、保险公司Home Insurance 3、房产经纪公司Real Estate Broker 4、房屋检查Home inspectors
    5、房产过户中间公司Escrow Services 6、评估公司Real Estate Appraiser 7、产权保险公司Title Insurance Company
    8、律师事务所Legal Services 9、杀虫公司Pest Control Company 10、空调维修Hvac Maintenance 11.家用电器修理  Appliance Repair
    12、垃圾处理公司 Republic Service 13、园艺花圃 Landscaping 14、建筑装修 Construction Company
    15、窗帘安装公司 Curtains Installation Service 16、清洁服务 Cleaning Company
    17、地毯清洁 Carpet Cleaning Service 18、屋顶维修Roof Repair 19、贷款经纪 Mortgage Broker
    20、地板装簧 Flooring Company 21、安全防盗系统Security Systems 22、泳池清洁保养Pool Cleaners
    23、砍树服务公司Tree Cutting Service 24、搬运服务 Moving Company
    25、室内装修Interior Design 26、锁匠Locksmiths 27、电工Electricians 28、车库门维修 Garage Door Repair
    29、隐形围栏Decks & Railing/ Fence 30、遮阳棚 Awnings 
    31、饮水设备 Water Purifying Equipment Company 32、下水处理服务 Gutter Services
    33、儿童防护Childproofing
    """
    # 1、贷款公司Mortgage Company https://www.yelp.com/search?find_desc=Mortgage%20Company&find_loc=NY&start=10
    mortgage_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Mortgage%20Company&find_loc=.+[&start=\d+]?$'))
    # 2、保险公司Home Insurance https://www.yelp.com/search?find_desc=Home%20Insurance&find_loc=NY
    insurance_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Home%20Insurance&find_loc=.+[&start=\d+]?$'))
    # 3、房产经纪公司Real Estate Broker https://www.yelp.com/search?find_desc=Real%20Estate%20Broker&find_loc=NY
    estate_broker_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Real%20Estate%20Broker&find_loc=.+[&start=\d+]?$'))
    # 4、房屋检查Home inspectors https://www.yelp.com/search?find_desc=Home%20inspectors&find_loc=NY
    home_inspectors_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Home%20inspectors&find_loc=.+[&start=\d+]?$'))
    # 5、房产过户中间公司Escrow Services https://www.yelp.com/search?find_desc=Escrow%20Services&find_loc=NY
    escrow_services_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Escrow%20Services&find_loc=.+[&start=\d+]?$'))
    # 6、评估公司Real Estate Appraiser https://www.yelp.com/search?find_desc=Real%20Estate%20Appraiser&find_loc=NY
    real_estate_appraiser_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Real%20Estate%20Appraiser&find_loc=.+[&start=\d+]?$'))
    # 7、产权保险公司Title Insurance Company https://www.yelp.com/search?find_desc=Title%20Insurance%20Company&find_loc=NY
    title_insurance_company_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Title%20Insurance%20Company&find_loc=.+[&start=\d+]?$'))
    # 8、律师事务所Legal Services https://www.yelp.com/search?find_desc=Legal%20Services&find_loc=NY
    legal_services_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Legal%20Services&find_loc=.+[&start=\d+]?$'))
    # 9、杀虫公司Pest Control Company https://www.yelp.com/search?find_desc=Pest%20Control%20Company&find_loc=NY
    pest_control_company_services_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Pest%20Control%20Company&find_loc=.+[&start=\d+]?$'))
    # 10、空调维修Hvac Maintenance https://www.yelp.com/search?find_desc=Hvac%20Maintenance&find_loc=NY
    hvac_maintenance_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Hvac%20Maintenance&find_loc=.+[&start=\d+]?$'))
    # 11.家用电器修理  Appliance Repai https://www.yelp.com/search?find_desc=Appliance%20Repair&find_loc=NY
    appliance_repair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Appliance%20Repair&find_loc=.+[&start=\d+]?$'))
    # 12、垃圾处理公司 Republic Service https://www.yelp.com/search?find_desc=Republic%20Service&find_loc=NY
    republic_service_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Republic%20Service&find_loc=.+[&start=\d+]?$'))
    # 13、园艺花圃 Landscaping https://www.yelp.com/search?find_desc=Landscaping&find_loc=NY
    landscaping_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Landscaping&find_loc=.+[&start=\d+]?$'))
    # 14、建筑装修 Construction Company https://www.yelp.com/search?find_desc=Construction%20Company&find_loc=NY
    construction_company_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Construction%20Company&find_loc=.+[&start=\d+]?$'))
    # 15、窗帘安装公司 Curtains Installation Service https://www.yelp.com/search?find_desc=Curtains%20Installation%20Service&find_loc=NY
    curtains_installation_service_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Curtains%20Installation%20Service&find_loc=.+[&start=\d+]?$'))
    # 16、清洁服务 Cleaning Company https://www.yelp.com/search?find_desc=Cleaning%20Company&find_loc=NY
    cleaning_company_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Cleaning%20Company&find_loc=.+[&start=\d+]?$'))
    # 17、地毯清洁 Carpet Cleaning Service  https://www.yelp.com/search?find_desc=Carpet%20Cleaning%20Service%20&find_loc=NY
    carpet_cleaning_service_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Carpet%20Cleaning%20Service%20&find_loc=.+[&start=\d+]?$'))
    # 18、屋顶维修Roof Repair https://www.yelp.com/search?find_desc=Roof%20Repair&find_loc=NY
    roof_repair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Roof%20Repair&find_loc=.+[&start=\d+]?$'))
    # 19、贷款经纪 Mortgage Broker https://www.yelp.com/search?find_desc=Mortgage%20Broker&find_loc=NY
    mortgage_broker_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Mortgage%20Broker&find_loc=.+[&start=\d+]?$'))
    # 20、地板装簧 Flooring Company https://www.yelp.com/search?find_desc=Flooring%20Company&find_loc=NY
    flooring_company_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Flooring%20Company&find_loc=.+[&start=\d+]?$'))
    # 21、安全防盗系统Security Systems https://www.yelp.com/search?find_desc=Security%20Systems%20&find_loc=NY
    security_systems_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Security%20Systems%20&find_loc=.+[&start=\d+]?$'))
    # 22、泳池清洁保养Pool Cleaners https://www.yelp.com/search?find_desc=Pool%20Cleaners&find_loc=NY
    pool_cleaners_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=find_desc=Pool%20Cleaners&find_loc=.+[&start=\d+]?$'))
    # 23、砍树服务公司Tree Cutting Service https://www.yelp.com/search?find_desc=Tree%20Cutting%20Service&find_loc=NY
    tree_cutting_service_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Tree%20Cutting%20Service&find_loc=.+[&start=\d+]?$'))
    # 24、搬运服务 Moving Company https://www.yelp.com/search?find_desc=Moving%20Company&find_loc=NY
    moving_company_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Moving%20Company&find_loc=.+[&start=\d+]?$'))
    # 25、室内装修Interior Design https://www.yelp.com/search?find_desc=Interior%20Design&find_loc=NY
    interior_design_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Interior%20Design&find_loc=.+[&start=\d+]?$'))
    # 26、锁匠Locksmiths https://www.yelp.com/search?find_desc=Locksmiths&find_loc=NY
    locksmiths_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Locksmiths&find_loc=.+[&start=\d+]?$'))
    # 27、电工Electricians https://www.yelp.com/search?find_desc=Electricians&find_loc=NY
    electricians_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Electricians&find_loc=.+[&start=\d+]?$'))
    # 28、车库门维修 Garage Door Repair https://www.yelp.com/search?find_desc=Garage%20Door%20Repair&find_loc=NY
    garage_door_repair_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Garage%20Door%20Repair&find_loc=.+[&start=\d+]?$'))
    # 29、隐形围栏Decks & Railing/Fence https://www.yelp.com/search?find_desc=Decks%20%26%20Railing%2FFence&find_loc=NY
    decks_railing_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Decks%20%26%20Railing%2FFence&find_loc=.+[&start=\d+]?$'))
    # 30、遮阳棚 Awnings https://www.yelp.com/search?find_desc=Awnings&find_loc=NY
    awnings_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Awnings&find_loc=.+[&start=\d+]?$'))
    # 31、饮水设备 Water Purifying Equipment Company https://www.yelp.com/search?find_desc=Water%20Purifying%20Equipment%20Company&find_loc=NY
    water_purifying_equipment_company_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Water%20Purifying%20Equipment%20Company&find_loc=.+[&start=\d+]?$'))
    # 32、下水处理服务 Gutter Services https://www.yelp.com/search?find_desc=Gutter%20Services&find_loc=NY
    gutter_services_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Gutter%20Services&find_loc=.+[&start=\d+]?$'))
    # 33、儿童防护Childproofing https://www.yelp.com/search?find_desc=Childproofing&find_loc=NY
    childproofing_page_link = LinkExtractor(allow=(r'^https://www.yelp.com/search\?find_desc=Childproofing&find_loc=.+[&start=\d+]?$'))
    # 每页中的详情页 https://www.yelp.com/biz/ge-construction-group-washington-dc-2
    detail_link = LinkExtractor(allow=(r'^https://www.yelp.com/biz/.+'))
    rules = (
        Rule(mortgage_page_link, follow=True),
        Rule(insurance_page_link, follow=True),
        Rule(estate_broker_page_link, follow=True),
        Rule(home_inspectors_page_link, follow=True),
        Rule(escrow_services_page_link, follow=True),
        Rule(real_estate_appraiser_page_link, follow=True),
        Rule(title_insurance_company_page_link, follow=True),
        Rule(legal_services_page_link, follow=True),

        Rule(pest_control_company_services_page_link, follow=True),
        Rule(hvac_maintenance_page_link, follow=True),
        Rule(appliance_repair_page_link, follow=True),
        Rule(republic_service_page_link, follow=True),
        Rule(landscaping_page_link, follow=True),
        Rule(construction_company_page_link, follow=True),
        Rule(curtains_installation_service_page_link, follow=True),
        Rule(cleaning_company_page_link, follow=True),

        Rule(carpet_cleaning_service_page_link, follow=True),
        Rule(roof_repair_page_link, follow=True),
        Rule(mortgage_broker_page_link, follow=True),
        Rule(flooring_company_page_link, follow=True),
        Rule(security_systems_page_link, follow=True),
        Rule(pool_cleaners_page_link, follow=True),
        Rule(tree_cutting_service_page_link, follow=True),
        Rule(moving_company_page_link, follow=True),

        Rule(interior_design_page_link, follow=True),
        Rule(locksmiths_page_link, follow=True),
        Rule(electricians_page_link, follow=True),

        Rule(garage_door_repair_page_link, follow=True),
        Rule(decks_railing_page_link, follow=True),
        Rule(awnings_page_link, follow=True),
        Rule(water_purifying_equipment_company_page_link, follow=True),
        Rule(gutter_services_page_link, follow=True),
        Rule(childproofing_page_link, follow=True),
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