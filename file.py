#檔案物件=open(檔案路徑,mode=開啟模式)  讀取模式-R 寫入模式-w 讀雪模式-r+
#一次讀取一行
#for 變數 in 檔案物件:  從檔案依序讀取每行文字到變數中

#儲存檔案
# file=open("data.txt",mode="w",encoding="utf-8")#開啟 #utf-8編碼--除英文外都需要utf-8
# file.write("中文\n小")#操作
# file.close()#關閉
# with open("data.txt",mode="w",encoding="utf-8")as file:#mode w =write
#     file.write("5\n3")
# #讀取檔案
# with open("data.txt",mode="r",encoding="utf=8")as file:
#     data=file.read()
#     print(data)
#把檔案中的數字資料,一行一行的讀取出來,並計算總合
# sum=0
# with open("data.txt",mode="r",encoding="utf-8")as file:
#     for line in file:
#         sum+=int(line)
# print(sum)


#使用 JSON格式讀取、複寫檔案
import json
#從檔案中讀取 JSON 資料,放入變數data裡面
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data)#data 是一個字典資料
data["name"]="New Name"#修改變數中資料
#把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file)

# print('name',data["name"])
# print("version",data["version"])


      
