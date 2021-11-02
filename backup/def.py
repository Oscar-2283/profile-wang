# #定義一個印出hello的函式
# def sayhello(msg="hello"):
#     print(msg)
# #呼叫上方定義的函式
# sayhello()
# sayhello("UUURRRY")
# # def say(a):
#     print(a)
# say("UUURRRY")
# say("KONODIODA!")

#函式回傳 n1+n2的結果
# def add(n1,n2):
#     result=n1+n2
#     return  result

# #呼叫函式,取得回傳值
# value=add(3,4)
# print(value)#印出7

#定義一個可以做加法的函式
# def divide(n1,n2):
#     result=n1/n2
#     print(result)
# divide(2,4)#印出0.5
# divide(n2=2,n1=4)#印出2

#函式接受無限參數*
def say(*msgs):
    for msg in msgs:
        print(msg)
say("hello","arbirtrary","arguments")