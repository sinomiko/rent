#-*- coding:utf-8 -*-
#!/usr/bin/python
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv
#url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"
url = "http://sh.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"
#ÒÍ³ɵÄ³ÊÐºţ¬³õª0
page = 0
csv_file = open("rent_sh.csv","wb") 
csv_writer = csv.writer(csv_file, delimiter=',')
while True:
    page += 1
    print "fetch: ", url.format(page=page)
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text)
    house_list = html.select(".list > li")
    # ѭ»·Ô¶r»µ½Ðµķ¿Դʱ½á
    if not house_list:
        break
    for house in house_list:
        house_title = house.select("h2")[0].string.encode("utf8")
        house_url = urljoin(url, house.select("a")[0]["href"])
        house_info_list = house_title.split()
        # È¹ûÁÊ¹«ԢÃÔȡµÚ»Á×ΪµØ·
        if "¹«Ԣ" in house_info_list[1] or "ÇÄÉÇ" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]
        house_money = house.select(".money")[0].select("b")[0].string.encode("utf8")
        csv_writer.writerow([house_title, house_location, house_money, house_url])
csv_file.close()
