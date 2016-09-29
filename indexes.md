# Chapter 1

## 1.1
- 将**可迭代**的对象，拆解到变量中，适用于 list, tuple, 字符串
- 使用 `_` 忽略拆解过程中不需要的值

## 1.2
- `*` 运算符截取从可迭代对象中的多个变量
- `*_` 忽略从可迭代对象中截取的多个值
- `*` 运算符实现递归操作

## 1.3
- 保存最后的 N 项元素
- 生成器 Generator 的使用，`yield` 关键字
- 文件操作，使用 `with...as...` 的便利
- 队列的操作 `dequeue`

## 1.4
- 寻找最大或最小的 N 个元素
- 实际上是用的是堆的算法
- `heapq.nlargest` 和 `heapq.nsmallest` 方法适用于寻找数目相对较少的项
- 只想寻找单一的最小或最大元素，使用 `min()` 或 `max()` 更佳
- 若寻找的数目 N 与可迭代集合的大小相差无几，更好的是
	1. 将集合进行排序操作 sort
	2. 对排序后的集合进行截取 sorted(items)[:N], sorted(items)[-N:]
- 实际上，`heapq.nlargest` 和 `heapq.nsmallest` 会根据调用行为来决定使用哪种策略

## 1.5
- 实现优先队列
- 使用堆
- 所用函数

```py
import heapq

# 添加元素到堆，并维持最小堆的性质
heapq.heappush(<heap>, <item>)

# 获得并移除最小的元素，并维持最小堆的性质
heapq.headppop(<heap>)

# 重写类方法
__str__(self) # 可读性较强的描述方法，str() 时调用
__repr__(self) # 多用与 debug 时的描述方法，repr() 时调用

acsii() # 使用 ascii 码打印，并转义非 acsii 码

# 格式化字符串
"<a string format {0}{1}>".format(<variable1>, <variable2>)
```

- tuple 的自动比较
