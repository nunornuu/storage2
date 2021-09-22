list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表反转函数list.reverse()
# list1.reverse()
# print(list1)
#
list1_len = len(list1)
# 冒泡
for x in range(1, list1_len):
    for y in range(list1_len-x):
        if list1[y] < list1[y+1]:
            a = list1[y]
            list1[y] = list1[y+1]
            list1[y+1] = a

print(list1)


