# 拆解不定长的可迭代对象

# 使用 * 运算符
record = ('Dave', "Dave@example.com", '773-555-1212', '847-555-1212')
print("#### Section 1 ####")
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)  # 总是返回一个 list

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("\n#### Section 2 ####")
print(trailing)
print(current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

print("\n#### Section 3 ####")
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print("\n#### Section 4 ####")
print(uname)
print(homedir)
print(sh)

# * 运算符忽略一连串的元素
record = ['ACME', 50, 91.1, (2012, 12, 21)]
name, *_, (*_, year) = record
print("\n#### Section 5 ####")
print(name)
print(year)

# 使用 * 运算符对 list 进行操作
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print("\n#### Section 6 ####")
print(head)
print(tail)

# 使用 * 运算符进行递归操作
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print("\n#### Section 7 ####")
print(sum(items))
