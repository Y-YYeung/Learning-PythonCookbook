# 映射多个值到字典中

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(4)

print("#"*4 + " Section 1 " + "#"*4)
print(d)

print("#"*4 + " Section 2 " + "#"*4)
print(d2)