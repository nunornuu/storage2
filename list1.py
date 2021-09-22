a = [1, 5, 21, 30, 15, 9, 30, 24]
sum1 = 0
for num in a:
    if num != 0:
        if num % 5 == 0:
            sum1 += num

print(f'5的倍数总和 {sum1}')
