import requests

#payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
#r=requests.get("https://www.baidu.com/",params=payload)
#r.encoding='utf-8'
#r.text
#print(r.text)
#print(r.url)
headers = {
        "Host": "youpin.mi.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://youpin.mi.com/",  # 必须带这个参数，不然会报错
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
             }
url = "https://youpin.mi.com/app/shopv3/pipe"
form_data = {"data": '{"result": {"model": "Homepage", "action": "BuildClass", "parameters": {"id": -6}}}'}
results = requests.post(url, data=form_data, headers=headers).text
print(results)