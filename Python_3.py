# 切片
print('--------------->', '# 切片')

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = list(range(100))
print('L[1:4]--->', L[1:4])
print('L[:4]--->', L[:4])
print('L[-2:]--->', L[-2:])
print('L[-2:-1]--->', L[-2:-1])
print('L[-2:4]--->', L[-2:4])
print('L[:20:2]--->', L[:20:2])
print('L[:]--->', L[:])

print('(0, 1, 2, 3, 4, 5)[:3]--->', (0, 1, 2, 3, 4, 5)[:3])

print("'abcdefg'[:3]", 'abcdefg'[:3])


# 迭代
print()
print('--------------->', '# 迭代')

print('for key in my_Map:')
my_Map = {'a': 1, 'b': 2, 'c': 3}
for key in my_Map:
    print(key)

print()
print('for key, value in my_Map.items():')
my_Map = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_Map.items():
    print(key, value)

print()
print('for value in my_Map.values():')
for value in my_Map.values():
    print(value)

print()
print('for ch in \'abcdefg\':')
for ch in 'abcdefg':
    print(ch)


print()
from collections import Iterable
print('isinstance(\'abc\', Iterable):', isinstance('abc', Iterable))
print('isinstance([1, 2, 3], Iterable):', isinstance([1, 2, 3], Iterable))
print('isinstance(123, Iterable):', isinstance(123, Iterable))

print()
print('enumerate函数可以把一个list变成索引-元素对:')
print('''for i, value in enumerate(['a', 'b', 'c', 'd']):''')
for i, value in enumerate(['a', 'b', 'c', 'd']):
    print(i, value)

print()
print('for循环里，同时引用了两个变量:')
print('''for x, y in [(1, 2), (2, 3), (3, 4)]:''')
for x, y in [(1, 2), (2, 3), (3, 4)]:
    print(x, y)

# 列表生成器 List Comprehensions
print()
print('--------------->', '# 列表生成器 List Comprehensions')
print('''[x * x for x in range(1, 11)]''')
L_1 = [x * x for x in range(1, 11)]
print(L_1)

print()
print('''[x * x for x in range(1, 11) if x % 3 == 0]''')
L_2 = [x * x for x in range(1, 11) if x % 3 == 0]
print(L_2)

map_2 = {'x': 'A', 'y': 'B', 'z': 'C'}
L_3 = [k + ' = ' + v for k, v in map_2.items()]
print()
print('''[k + ' = ' + v for k, v in map_2.items()]''')
print(L_3)

print()
L_4 = ['hello', 'yourBody', 'i love you']
L_4_n = [st.upper() for st in L_4]
print('[st.upper() for st in L_4]')
print(L_4_n)

# 生成器
print()
print('--------------->', '# 生成器')

g = (x * x for x in range(10))
print('g is:', g)
print('g.__next__():', g.__next__())
for n in g:
    print(n)


print()
print('生成器函数：')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print()
print('循环无return的生成器')
f = fib(6)
f_1 = fib(6)
for fs in f:
    print('f:', fs)

print()
print('循环有return的生成器')
while True:
    try:
        x = next(f_1)
        print('f_1:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


print()
print('生成器函数：')


def test_yield():
    print('step 1!')
    yield('1111')
    print('step 2!')
    yield('22222')
    print('step 3!')
    yield('33333')



test_y = test_yield()
test_y.__next__()
next(test_y)
next(test_y)
