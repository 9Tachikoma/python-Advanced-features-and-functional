def is_palindrome(n):
  return str(n)==str(n)[::-1]  #字符串取倒叙
#>>> 'abcdefghijklm'[2:10:3]  # start at 2, go upto 10, count by 3
#'cfi'
#>>> 'abcdefghijklm'[10:2:-1] # start at 10, go downto 2, count down by 1
#'kjihgfed'
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')