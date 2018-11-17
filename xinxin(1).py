from bs4 import BeautifulSoup
import requests
import csv
import re
from time import sleep
def gethtml(url):
    try:
        headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        rr=requests.get(url,headers=headers)
        rr.raise_for_status()
        rr.encoding=rr.apparent_encoding
        return rr.text
    except:
        return url

def output(html,csv_writer):
    html_doc = BeautifulSoup(html,"html.parser")
    h_list = html_doc.select(".list  li")
    for h_item in h_list:
        h_desc =  h_item.select("h2")[0].string
        h_url = h_item.select("a")[0]["href"]
        h_url = "http:%s"%h_url
        headers = {"User-Agent" : "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        #rr=requests.get(h_url,headers=headers)
        #rr.encoding=rr.apparent_encoding
       # ma=re.findall(r'____json4fe.lon.+\'',rr.text)
        #mt=re.findall(r'____json4fe.lat.+\'',rr.text)
        #mz=re.findall(r'\d+.\d+',str(ma))
        #mx=re.findall(r'\d+.\d+',str(mt))
        h_info_list = h_desc.split()
        h_loc = h_info_list[1]
        h_money =  h_item.select(".money")[0].select("b")[0].string
        csv_writer.writerow([h_desc, h_loc, h_money, h_url])
        #sleep(6)


def main():
    file_name = 'rrrr.csv'
    with open(file_name, 'w', newline='',encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for i in range(1,10):
            url="http://bj.58.com/pinpaigongyu/pn/{}/?PGTID=0d3111f6-0000-1f5b-1512-447e5e45fb76&ClickID=1".format(i)
            html=gethtml(url)
            output(html,csv_writer)


main()




