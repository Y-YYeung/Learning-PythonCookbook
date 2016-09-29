# 实现优先队列

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 添加元素到堆，并维持最小堆的性质
        # 堆 默认为最小堆，-priority 是一个构建最大堆的 trick
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 获得并移除最小的元素，并维持最小堆的性质
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return "Item({!r}) from __str__".format(self.name)

    # 多用于 debug
    # 若重写 __repr__ 却没有重写 __str__, 则会调用已重写的 __repr__
    def __repr__(self):
        # !r 指示调用 repr() -> __repr__
        # !s 指示调用 str() -> __str__
        # !a 指示调用 acsii() -> 使用 ascii 码打印，并转义非 ascii 码
        return "Item({!r})".format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print("#"*4 + "Section 1" + "#"*4)
print(q.pop())

print("#"*4 + "Section 2" + "#"*4)
print(q.pop())

print("#"*4 + "Section 3" + "#"*4)
print(q.pop())

print("#"*4 + "Section 4" + "#"*4)
print(q.pop())

print("#"*4 + "Section 5" + "#"*4)
# tuple 中的数字/字符可以用作比较
# 只有当作比较的数字/字符串不相同是才通过，否则抛异常
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a<b)
print(a<c)
