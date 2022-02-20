from logging import exception
import requests
import json
import datetime
import os
now = datetime.datetime.now()
now=now+datetime.timedelta(hours=8)
time=now.strftime('%Y%m%d')
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',"Referer":"https://xxcapp.xidian.edu.cn/site/ncov/xidiandailyup"}
data={"szcs":"","szgj":"","zgfxdq":"0","mjry":"0","csmjry":"0","tw":"3","sfcxtz":"0","sfjcbh":"0","sfcxzysx":"0","qksm":"","sfyyjc":"0","jcjgqr":"0","remark":"","address":"江苏省南通市通州区新三十里居平潮镇平东卫生院","geo_api_info":"{\"type\":\"complete\",\"position\":{\"Q\":32.053842773438,\"R\":120.86325981987898,\"lng\":120.86326,\"lat\":32.053843},\"location_type\":\"html5\",\"message\":\"Get geolocation success.Convert Success.Get address success.\",\"accuracy\":40,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"0513\",\"adcode\":\"320683\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"新三十里居\",\"streetNumber\":\"105号\",\"country\":\"中国\",\"province\":\"江苏省\",\"city\":\"南通市\",\"district\":\"通州区\",\"towncode\":\"320683017000\",\"township\":\"平潮镇\"},\"formattedAddress\":\"江苏省南通市通州区平潮镇平东卫生院\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","area":"江苏省 南通市 通州区","province":"江苏省","city":"南通市","sfzx":"0","sfjcwhry":"0","sfjchbry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","bztcyy":"","sftjhb":"0","sftjwh":"0","sfjcjwry":"0","jcjg":"","date":time,"uid":"445135","created":1643505589,"jcqzrq":"","sfjcqz":"","szsqsfybl":"0","sfsqhzjkk":0,"sqhzjkkys":"","sfygtjzzfj":0,"gtjzzfjsj":"","ismoved":"0","created_uid":0,"id":11135344}
username=os.environ['username']
password=os.environ['password']
data['date']=time
url="https://xxcapp.xidian.edu.cn/uc/wap/login/check"
p1=requests.Session()
p2=p1.post(url,headers = headers,data={"username":username,"password":password},timeout=10)
if(p2.status_code!=200):
    raise Exception('不明原因失败');
p2=p1.post("https://xxcapp.xidian.edu.cn/ncov/wap/default/save",headers=headers,data=data,timeout=10)
if(p2.status_code!=200):
    raise Exception('不明原因失败');
try:
    a=json.loads(p2.text)
    print(a['m'])
except Exception:
    print(p2.text)
    print("不明原因失败")


