# 将序列，对所有可迭代的对象有效，拆解到变量中

p = (4, 5)

# 逐一赋值
x, y = p
print("#### Section 1 ####")
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("\n#### Section 2 ####")
print(name)
print(date)

# 对序列中的 tuple，也可以将其赋值到一个 tuple 变量中
name, shares, price, (year, month, day) = data
print("\n#### Section 3 ####")
print(name)
print(year)
print(month)
print(day)

# 拆解字符串
s = 'Hello'
a, b, c, d, e = s
print("\n#### Section 4 ####")
print(a)
print(b)
print(c)

# 拆解过程中，可忽略一些值
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print("\n#### Section 5 ####")
print(shares)
print(price)
