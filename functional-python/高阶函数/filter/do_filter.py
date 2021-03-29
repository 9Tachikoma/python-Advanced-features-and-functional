def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()
"""
2. python的and 返回值

>>> 'a' and 'b'
'b'
>>> '' and 'b'
''
>>> 'b' and ''
''
>>> 'a' and 'b' and 'c'
'c'
>>> '' and None and 'c'
''

在布尔上下文中从左到右演算表达式的值，如果布尔上下文中的所有值都为真，那么 and 返回最后一个值。

如果布尔上下文中的某个值为假，则 and 返回第一个假值。
"""
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))