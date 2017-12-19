# 常用函数
print('--------------->', '# 常用函数')
myInt = int('3')
myFloat = float(1)
myStr = str(123)
myBool = bool('a')
myHex = hex(9)  # 将十进制的转成十六进制
print(myFloat)
print(myBool)
print(myHex)

# 定义函数
# 位置参数
print('--------------->', '# 常用函数（位置参数）')


def myfunction(x):
    if x < 10:
        print('This x is:', x)
        return x
    else:
        print('This x+10 is:', x + 10)
        return x + 10


print(myfunction(10))

# 默认参数
print('--------------->', '# 默认参数')


def power(x, n=2):
    s = 1
    while n > 1:
        n = n - 1
        s = s * x
    return s


print(power(2))
print(power(2, 4))

# 可变参数
print('--------------->', '# 可变参数')


def calc(*number):
    my_sum = 0
    for n in number:
        my_sum = my_sum + n * n
    return my_sum


print(calc(1, 2, 3, 4))
print(calc(*[1, 2, 3, 4, 5]))
print(calc(*(1, 2, 3, 4, 5, 6)))

# 关键字参数
print('--------------->', '# 关键字参数')


def person(name, age, **kw):
    print(name, age, kw)


person('张三', 11, city='北京')
person('张三', 12, city='北京', home='家里', love='电脑')
extra = {'city': 'beijing', 'job': 'coder'}
person('张三', 13, city=extra['city'])
person('张三', 14, **extra)


# 命名关键字参数
print('--------------->', '# 命名关键字参数')


def person_2(name, age, *, city, home):
    print(name, age, city, home)


def person_3(name, age, *, city='默认北京', home):
    print(name, age, city, home)


person_2('我没有很想要啦', 25, city='北京', home='家')
person_2('我没有很想要啦', 25, home='家', city='北京')
person_3('老婆别生气了', 26, home='上海家')
person_3('老婆别生气了', 26, home='上海家', city='上海')
person_3('老婆别生气了', 26, city='上海', home='上海家')


# 参数组合
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
print('--------------->', '# 参数组合：必选参数、默认参数、可变参数、命名关键字参数和关键字参数')


def f_1(a, b, c=3, *args, **kw):
    print(a, b, c, args, kw)


def f_2(a, b, c=3, *, d, **kw):
    print(a, b, c, d, kw)


f_1('A', 'B', 'C', *[1, 2, 3, 4], city='北京', home='房子')
f_2('AA', 'BB', 'CC', d='北京', city='北京')

# 递归函数
print('--------------->', '# 递归函数')


def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


print(fact(9))

