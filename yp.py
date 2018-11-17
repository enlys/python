import requests
import json
import re
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36;"}
rr=requests.get("https://www.ximalaya.com/revision/play/album?albumId=16046207&pageNum=1&pageSize=30",headers=headers)
ret=rr.content.decode()

di=json.loads(ret)
lists=di['data']['tracksAudioPlay']
for i in lists:
    src=i['src']
    name=i['trackName']
    print(src,name)
    with open('{}.m4a'.format(name),'ab') as f:
        music=requests.get(src,headers=headers)
        f.write(music.content)