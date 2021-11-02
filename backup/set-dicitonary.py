#集合的運算
#s1={3,4,5}
#print(1 not in s1)
#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2 #交集: 取兩個集合中.相同的資料
#s3=s1|s2 #聯集:取兩個集合中所有資料.但不重複
#s3=s1-s2#差集:從S1中,減去和S2重疊的地方
#s3=s1^s2 #反交集:取兩個集合中,不重疊的地方
#print(s3)
#s=set("hello")#把字串中字母拆解成集合#set(字串)
#print("h" in s)
#字典的運算: key-value 配對
#dic={"apple":"蘋果","bug":"蟲子"}
#dic["apple"]="小哪吒"
#print(dic["apple"])
#dic={"apple":"蘋果","bug":"蟲子"}
#print("jimmy" not in dic)#判斷 Key是否存在
#print(dic)
#del dic["apple"] #刪除字典中的鍵值對(Key-value pair)
#print(dic)
dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)
