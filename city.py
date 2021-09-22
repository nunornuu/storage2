citys = ['北京', '上海', '广州']
other_citys = ['天津', '重庆', '郑州', '武汉', '石家庄', '哈尔滨']
GDP = [36710.36, 35427.10, 29863.23, 29667.39, 27665.36, 27650.45, 27620.38, 25369.20]
# GDP总和--a      平均GDP--b
a = 0
b = 0

for city in other_citys:
    citys.append(city)
print(citys)
for n in range(len(citys)):
    if citys[n] == '上海':

        citys.remove('广州')
        citys.insert(n, '广州')
        break
print(citys)
a = sum(GDP)
b = a/len(GDP)
print(f'总和{a} \n平均{b}')
