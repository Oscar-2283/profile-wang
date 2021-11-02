#有序可變動列表 List
#grade=[12,60,15,70,90]
#grade[0]=55#打55放到列表中第一個位置
#grade[1:4]=[] #連續刪除列編號從1到編號4(不包括)的資料
#grade=grade+[12,33]
#length=len(grade) #取得列表長度len
#print(length) #0=列表中第一個編號
data=[[3,4,5],[6,7,8]]
data[0][1]=500,20
print(data[0])
#有序不可變動列表
#data=(3,4,5)
#data[0]=5 #錯誤 Tuple的資料不可變動
#print(data[0:2])