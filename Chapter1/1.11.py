# 对分片进行命名

record = "11111111111111111111111111111111111111"

# 记录分片范围
SHARES = slice(2, 10)
PRICE = slice(20, 29)

result = int(record[SHARES]) + int(record[PRICE])
print("#"*4 + " Section 1 " + "#"*4)
print(result)

# Discussion
items = [0, 1, 2, 3, 4, 5, 6]
slice1 = slice(2, 4)
print("#"*4 + " Section 2 " + "#"*4)
print(items[2:4])
print(items[slice1])

# 利用分片替换
items[slice1] = [10, 11]
print(items)

# 利用分片删除
del items[slice1]
print(items)

print("#"*4 + " Section 3 " + "#"*4)

# 控制 slice 的属性 start, stop, step
slice2 = slice(5, 50, 2)
print(slice2.start)
print(slice2.stop)
print(slice2.step)

print("#"*4 + " Section 4 " + "#"*4)

s = 'HelloWorld'
slice3 = slice2.indices(len(s))
print(slice3)

# range 中的 * 号将 tuple 中的数据全部带出来，并对照 range 的参数传递
for i in range(*slice2.indices(len(s))):
    print(s[i])