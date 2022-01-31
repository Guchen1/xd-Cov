from logging import exception
import requests
import json
import os
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',"Referer":"https://xxcapp.xidian.edu.cn/site/ncov/xidiandailyup"}
data={"szcs":"","szgj":"","zgfxdq":"0","mjry":"0","csmjry":"0","tw":"3","sfcxtz":"0","sfjcbh":"0","sfcxzysx":"0","qksm":"","sfyyjc":"0","jcjgqr":"0","remark":"","address":"\u6c5f\u82cf\u7701\u5357\u901a\u5e02\u5d07\u5ddd\u533a\u5510\u95f8\u9547\u8857\u9053\u6c38\u548c\u8def\u5c1a\u6d77\u57ce","geo_api_info":"{\"type\":\"complete\",\"position\":{\"Q\":32.053842773438,\"R\":120.86325981987898,\"lng\":120.86326,\"lat\":32.053843},\"location_type\":\"html5\",\"message\":\"Get geolocation success.Convert Success.Get address success.\",\"accuracy\":40,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"0513\",\"adcode\":\"320613\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"\u6c38\u548c\u8def\",\"streetNumber\":\"573\u53f7\",\"country\":\"\u4e2d\u56fd\",\"province\":\"\u6c5f\u82cf\u7701\",\"city\":\"\u5357\u901a\u5e02\",\"district\":\"\u5d07\u5ddd\u533a\",\"towncode\":\"320613017000\",\"township\":\"\u5510\u95f8\u9547\u8857\u9053\"},\"formattedAddress\":\"\u6c5f\u82cf\u7701\u5357\u901a\u5e02\u5d07\u5ddd\u533a\u5510\u95f8\u9547\u8857\u9053\u6c38\u548c\u8def\u5c1a\u6d77\u57ce\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","area":"\u6c5f\u82cf\u7701 \u5357\u901a\u5e02 \u5d07\u5ddd\u533a","province":"\u6c5f\u82cf\u7701","city":"\u5357\u901a\u5e02","sfzx":"0","sfjcwhry":"0","sfjchbry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","bztcyy":"","sftjhb":"0","sftjwh":"0","sfjcjwry":"0","jcjg":"","date":"20220130","uid":"445135","created":1643505589,"jcqzrq":"","sfjcqz":"","szsqsfybl":"0","sfsqhzjkk":0,"sqhzjkkys":"","sfygtjzzfj":0,"gtjzzfjsj":"","ismoved":"0","created_uid":0,"id":11135344}
username=os.environ["username"]
password=os.environ["password"]
url="https://xxcapp.xidian.edu.cn/uc/wap/login/check"
p1=requests.Session()
p2=p1.post(url,headers = headers,data={"username":username,"password":password},timeout=10)
if(p2.status_code!=200):
    raise Exception('不明原因失败');
p2=p1.post("https://xxcapp.xidian.edu.cn/ncov/wap/default/index",headers=headers,data=data,timeout=10)
if(p2.status_code!=200):
    raise Exception('不明原因失败');
try:
    a=json.loads(p2.text)
    print(a['m'])
except Exception:
    print("不明原因失败")

