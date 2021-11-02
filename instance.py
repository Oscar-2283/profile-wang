# Point 實體物件的設計:平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5
# p=Point(3,4)
# p.show()
# result=p.distance(0,0)#r計算座標3,4 和座標0,0之間的距離
# print(result)
#FullName 實體物件的設計: 分開紀錄性、名資料的全名
# class FullName:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# name1=FullName("C.W.","Peng")
# print(name1.first,name1.last)
# name2=FullName("DE","Wang")
# print(name2.first,name2.last)


#File 實體物件的設計:包裝檔案讀取的程式
class File:
    def __init__(self,name):
        self.name=name
        self.file=None #尚未開啟檔案 :初始是 None
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=File("data.txt")
f1.open()
data=f1.read()
print(data)

    
