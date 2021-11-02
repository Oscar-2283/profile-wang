#網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw//"
# with request.urlopen(src) as respone:
#     data=respone.read().decode("utf-8")#取得網站的原始碼
# print(data)

#串接
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as respone:
    data=json.load(respone)#利用 json模組處理json
clist=data["result"]["results"] 
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")