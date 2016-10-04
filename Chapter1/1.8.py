# 字典计算

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75   
}

print("#"*4 + " Section 1 " + "#"*4)
# 使用 zip 产生的数据(实际上是 tuple)，只能使用一次，因为这个 tuple 实质是用 yield 返回的结果
#  这里通过对 values 数组与 keys 数组进行 zip，形成一个假象：value 与 key 的位置交换，实际上是一个 tuple
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

print("#"*4 + " Section 2 " + "#"*4)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
print(max_price)

print("#"*4 + " Section 3 " + "#"*4)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print("#"*4 + " Section 4 " + "#"*4)
print(min(prices))
print(max(prices))

print("#"*4 + " Section 5 " + "#"*4)
min_key = min(prices, key=lambda k: prices[k]) #  key: 指定用于排序的依据
print(min_key)