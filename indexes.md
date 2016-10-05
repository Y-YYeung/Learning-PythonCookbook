# Python Cookbook

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

## 1.6
- 映射多个值到字典中，类似字典中包含数组的样子
- 给字典中不存在的 key 赋值，会抛出 `KeyError` 异常。通常需要检测字典中是否存在一个 key，然后再进行操作。然而，这可以简化
- 所用方法

```py
from collections import defaultdict

# 创建一个字典，默认其 value 为 list/set
d = defaultdict(list/set)

# 只需要专注于添加元素，不必考虑是否存在 key
[<defaultdict>][<aKey>].append(<aValue>)
```

## 1.7
- 有序字典
- 所用方法

```py
from collections import OrderedDict

# 创建一个有序字典
d = OrderedDict()

# 按照普通的方法添加元素即可

import json

# 通过字典生成 json，其实这叫 序列化
str = json.dumps(d) # 生成 json 的字符串
dump([<{}>]) # 生成 file-like object，需要文件操作

# 反序列化
json.loads()
json.load()
``` 

- 注意
	- [<OrderDict>] 维护一个 list 来记录字典的元素的添加顺序
	- 添加后，对现存 key 的修改并不会改变其添加顺序
	- OrderedDict 实例空间大小是一般字典的2倍或有多，需要兼顾性能考虑是否采用


## 1.8
- 字典计算
- 使用场景之一
	- 使用字典中的 value 作为排序依据，而不是默认的 key'
- 所用方法

```py
# 接受多个可迭代对象，进行合并
# 合并方法：将每个可迭代对象的相同位置的元素合并成一个 tuple，通过 yield 返回
zip(* iterables)

# 这两个方法可以使用可选参数 key 来指定用于排序的依据
min()
max()
```

- [`zip()` 实现](https://docs.python.org/3/library/functions.html?highlight=zip#zip)

## 1.9
- 从两个字典中找相同
- 集合(set) 运算

- 所用方法


```py
# 返回一个 key-view 对象
# 该对象支持一般的集合运算：unions, intersections, differences 
[<dictionary>].keys()

# 返回一个 items-view 对象，包含键值对
# 支持一般的集合操作，支持字典间键值对的比较
[<dictionary>].items()

# 不支持集合操作，有需要时，可手动将结果转换为集合
[<dictionary>].values()
```

## 1.10
- 移除序列中重复的元素，并维持顺序
- 使用一个临时变量集合(set)来剔除重复元素
- 分两种类型
	- 序列中的元素是 hashable
		- **可以直接**将元素添加到 set 中
	- 序列中的元素是 unhashable
		- **不可直接**将元素添加到 set 中
		- 从 unhashable 的元素中寻找其 hashable 的属性来当作特征，放到 set 中用于剔除
- `yield` 语句
	- 中途返回
	- 其中一个好处：调用普通函数时，在函数中的创建的临时变量，并不可以在作用域（函数体）外使用，函数执行完成之后便销毁。但使用 `yield` 语句时，函数体中的临时变量，可看作超越了这一限制。如在 1.10.py 中，通过 dedup2 函数创建一个 list，创建的过程便是不断地通过 `yield` 语句实现。`yield` 语句生成返回一个结果给 list 创建的过程，而函数执行过程中的临时变量 seen 并没有被销毁，而是保留下来。

