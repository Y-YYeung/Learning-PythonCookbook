
# 保存最后的 N 项元素

from collections import deque

# history 设置了默认值
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # 由于 yield，变成了 Generator 生成器了
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    print("\n#### Section 1 ####")
    with open('./1.3testfile.txt') as f:
        for line, previouseLines in search(f, 'python', 5):
            for pline in previouseLines:
                print("previous line: " + pline)
            print("current line: " + line)
            print('-'*20)


# 使用 dequeue
print("\n#### Section 2 ####")
q = deque(maxlen=3)  # 创建固定长度的 dequeue
q.append(1)
q.append(2)
q.append(3)
print(q)

# 超过 dequeue 固定的长度后，将会移除最旧的元素
print("\n#### Section 3 ####")
q.append(4)
q.append(5)
q.append(6)
print(q)

# 创建没有长度限制的 dequeue，不指定 maxlen
print("\n#### Section 4 ####")
qq = deque()
qq.append(10)
qq.append(20)
qq.append(30)
print(qq)

# 花式添加元素
print("\n#### Section 5 ####")
qq.appendleft(40)
print(qq)

# 移除元素
print("\n#### Section 6 ####")
qq.pop()
print(qq)

# 花式移除元素
print("\n#### Section 7 ####")
qq.popleft()
print(qq)






