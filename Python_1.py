# List和Tuple
print('--------------->', '# List和Tuple')
myList = [1, 2, 3, 4]
print(myList)
print(myList[3])
print(myList[-1])
print(len(myList))
myList.append(6)
myList.insert(2, 5)
print(myList)
print(len(myList))
myList.pop()

myTuple = (1, 2, 3, 4)
print('myTuple:', myTuple)


'''
块注释
'''

# if语句，检测输入
print('--------------->', '# if语句，检测输入')
# s = input('brithYear:')
s = 2000
brith = int(s)
if brith > 2000:
    print(2000, '后面')
else:
    print(2000, '前面')

# 循环
print('--------------->', '# 循环')
sum = 0
for a in (range(10)):
    sum = sum + a
print(sum)

# dict和set
print('--------------->', '# dict和set')
myDict = {'a': 100, 'b': 200, 'c': 300}
myDict['d'] = 400
print(myDict['d'])
print(myDict.get('e'))
print(myDict.get('e', 'The key is not in dict'))

s1 = set([1, 2, 3, 3])
print(s1)
s1.add(4)
s1.add(5)
s1.remove(5)
print(s)
s2 = set([3, 4, 5])
print('s1 & s2:', s1 & s2)
print('s1 | s2:', s1 | s2)
