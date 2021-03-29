L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)
'''
by_name函数要达到的目的是：将tuple的第一个元素，即名称字符串t[0]，用lower()函数做全部小写处理，并返回结果。
sorted()函数将by_name函数一一作用于L上的每个元祖上，并根据函数结果的顺序，对原L中原元素排序。
'''