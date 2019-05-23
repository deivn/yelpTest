#! /usr/bin/env python  
# -*- coding:utf-8 -*-
import json
import redis
import MySQLdb
from  datetime import datetime
def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.139.101', port=6379, db=0)
    # 指定mysql数据库
    mysqlcli = MySQLdb.connect(host='184.181.11.233', user='ebuyhouse', passwd='ebuyhouse135', db='crawl_data', port=3306, use_unicode=True, charset='utf8')

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["yelp_test:items"])
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语
            if not item['referer']:
                item['referer'] = ' '
            if not item['detail_page_url']:
                item['detail_page_url'] = ' '
            if not item['company']:
                item['company'] = ' '
            if not item['category']:
                item['category'] = ' '
            if not item['img_url']:
                item['img_url'] = ' '
            if not item['business_content']:
                item['business_content'] = ' '
            if not item['latitude']:
                item['latitude'] = ' '
            if not item['longitude']:
                item['longitude'] = ' '
            if not item['content']:
                item['content'] = ' '
            if item['phone']:
                today = datetime.now()
                current_time = '{}-{}-{} {}:{}:{}'.format(today.year, today.month, today.day, today.hour, today.minute,today.second)
                cur.execute("INSERT INTO washington (referer, detail_page_url, logo, company, address, category, phone, websiteurl, img_url, content, business_content, latitude, longitude, date_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [item['referer'], item['detail_page_url'], ' ', item['company'], item['address'], item['category'], item['phone'], item['websiteurl'], item['img_url'], item['content'], item['business_content'], item['latitude'], item['longitude'], current_time])
                # 提交sql事务
                mysqlcli.commit()
                #关闭本次操作
                cur.close()
                print("inserted %s" % item['detail_page_url'])
        except MySQLdb.Error as e:
            print("Mysql Error  %s" % e)


if __name__ == '__main__':
    main()