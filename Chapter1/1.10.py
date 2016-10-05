# 移除序列中重复的元素，并维持顺序

# For hashable, 只适用于 hashable 的元素
# 当元素为 字典 等类型时，不可用
print("#"*4 + " Section 1 " + "#"*4)
def dedupe1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

test1 = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe1(test1)))

# For unhashable
# 用一个 set 来存储检查重复性的 key
def dedupe2(items, hashKey=None):
    seen = set()
    for item in items:
        val = item if hashKey is None else hashKey(item)
        if val not in seen:
            yield item
            seen.add(val)

    print("Content of seen: ")
    print(seen)

print("#"*4 + " Section 2 " + "#"*4)
test2 = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

# hashKey 这里为一个匿名函数，目的用于提供一个特征，用于剔除重复元素
print(list(dedupe2(test2, hashKey=lambda d: (d['x'], d['y']))))


print("#"*4 + " Section 3 " + "#"*4)
print(list(dedupe2(test2, hashKey=lambda d: d['x'])))

# testTuple = (1, 2, 4)
# testSet = set(1, 2, 10, 11)

# print(testTuple in testSet)