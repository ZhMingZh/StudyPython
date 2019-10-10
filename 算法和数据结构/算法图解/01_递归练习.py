# 编写一个递归函数来计算列表包含的元素数
def length(array):
    if len(array) == 0:
        return 0
    return 1 + length(array[1:])


# test length()
array = list(range(10))
assert length(array) == 10


# 请编写sum 函数的代码。
def add(array):
    if len(array) == 0:
        return 0
    return array[0] + add(array[1:])


# test add()
assert add(array) == 45


# 找出列表中最大的数字

