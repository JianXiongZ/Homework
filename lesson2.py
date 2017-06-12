# enconding: utf-8
print('二分查找')
key = int(input('Please input a number: '))
l = [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 15]
low = 0
high = len(l)
while True:
    mid = (high + low) // 2
    if key == l[mid]:
        print (mid)
        break
    elif key > l[mid]:
        low = mid + 1
    else:
        high = mid - 1
    if high < low:
        print('没找到')
        break


print('插入排序')
l = [6, 5, 3, 1, 8, 7, 2, 4]
for i in list(range(1, len(l))):
    for j in list(range(i, 0, -1)):
        if l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
print (l)

# 冒泡排序
print('冒泡排序')
list_test = [1, 3, 5, 4, 7, 8, 0, 9]
for i in range(len(list_test) - 1):
    for j in range(len(list_test) - 1):
        if list_test[j] > list_test[j + 1]:
            list_test[j], list_test[j + 1] = list_test[j + 1], list_test[j]
print (list_test)
