# 从两个字典中找相同

a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}

# 找相同的 key
print("#"*4 + " Section 1 " + "#"*4)
print(a.keys() & b.keys()) # 集合运算

# 找存在于 a 的 keys 而不存在于 b 的 keys
print("#"*4 + " Section 2 " + "#"*4)
print(a.keys() - b.keys())

# 寻找相同的键值对
print("#"*4 + " Section 3 " + "#"*4)
print(a.items() & b.items())

# 创建一个新的字典，其中只含有特定的键值对
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print("#"*4 + " Section 4 " + "#"*4)
print(c)