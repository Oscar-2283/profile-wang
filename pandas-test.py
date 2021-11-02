import pandas as pd
data = pd.Series([20, 10, 15])

# print(data)

# print("Max:", data.max())
# print("Median:", data.median())
# data = data*2
# print(data)

# data=data == 20
# print(data)

# 建立 DataFrame
data = pd.DataFrame({
    "name": ["Amy", "Jimmy", "Jack"],
    "salary": [30000, 40000, 50000]
})
print(data["name"])
print("==================")
# 取得特定的列
print(data.iloc[0])  # 印出第一列
