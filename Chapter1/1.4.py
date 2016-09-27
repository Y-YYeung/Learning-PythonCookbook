# 寻找最大或最小的 N 个元素


import heapq

# 普通玩法
print("#"*4 + "Section 1" + "#"*4)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 进阶玩法，对于复杂的数据结构，自定义排序依据
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 最后一个参数 key，为一个函数，用来指定用于排序的 key
# 而不是传统意义上一个返回 -1, 0, 1 的函数
print("\n" + "#"*4 + "Section 2" + "#"*4)
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)

# 对 list 进行建堆操作
print("\n" + "#"*4 + "Section 3" + "#"*4)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)  # 最小堆
heapq.heapify(heap)
print(heap)

# 弹堆，寻找最小元素
print(heapq.heappop(heap))  # 弹出来之后，就不在堆里面了
print(heap)
