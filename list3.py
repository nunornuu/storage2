list1 = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
list2 = []

a = 0
# 获取唯一元素的集合
for x in list1:
    if x not in list2:
        list2.append(x)
print(list2)

while a < len(list2):
    b = 0
    for x in list1:
        if list2[a] == x:
            b += 1

    print(f'{list2[a]} 出现次数为{b}')
    a = a + 1
