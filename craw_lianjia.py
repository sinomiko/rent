#-*- coding:utf-8 -*-
#!/usr/bin/python
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import string
import csv
#url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"
#url = "http://sh.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"
url = "http://sh.lianjia.com/ershoufang/b150to250d{page}"
#ÒÍ³ɵÄ³ÊÐºţ¬³õª0
page = 0
csv_file = open("rent_sh_lianjia_150_250_wan.csv","wb") 
csv_writer = csv.writer(csv_file, delimiter=',')
while True:
	page += 1
	print "fetch: ", url.format(page=page)
	response = requests.get(url.format(page=page))
	html = BeautifulSoup(response.text)
	house_list = html.select(".house-lst > li")
	if page ==101:
                break
	for house in house_list:
		house_title = house.select("a")
                #for item in house_title:
		#   print item.get_text()
                   #itemtitle =itemtitle.join(item.get_text())
		house_url = urljoin(url, house.select("a")[0]["href"])
		#print house_url
		house_location =  house.select(".nameEllipsis")[0].string.encode("utf8") #nameEllipsis
                #print house_location
                house_money = house.select(".num")[0].string.encode("utf8")
                #print house_money,house_location
                hs_title = house_title[1].string.encode("utf8")
               # print hs_title
                csv_writer.writerow([hs_title, house_location, house_money, house_url])
csv_file.close()
