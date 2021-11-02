#break 的 簡易範例
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)#印出迴圈中的n 
#     n+=1
# print("最後的n:",n)#印出迴圈結束後的n

#continue
# n=0
# for x in range(5):
#     if x%2==0: #x是偶數
#         continue
#     print(x)
#     n+=1
# print("lastN:",n)
# print("x改:",x)

#else 的簡易範例
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum)

#綜合範例:找出整數平方根
n=int(input("請輸入數字:"))
for i in range(n+1): #x從0~n
    if i**2==n:
        print("整數平方根:",i)
        break#用break強制結束迴圈時,不會執行else區塊
else :
    print("無整數迴圈")