#定義函式
# def multiply(n1,n2):
#     return n1*n2
# #呼叫函式
# value=multiply(3,4)+multiply(5,5) #(3*4)+(5*5)
# print(value)

#函式可用來做程式的包裝:同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum+=n
    print(sum)

import sys as s
print(s.path)

 
calculate(10)
calculate(20)




