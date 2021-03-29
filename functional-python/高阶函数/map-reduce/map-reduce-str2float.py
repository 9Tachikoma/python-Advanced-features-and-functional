from functools import reduce

def str2float(s):

    def fn(x,y):#转换成整数

        return x*10+y

    def char2num(s): #字符串转换成list

        digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}

        return digits[s]

    pointnum=s.count('.')    #计算小数点的个数

    if pointnum ==0:        

        return reduce(fn,map(char2num,s))+0.0

    elif pointnum==1:

        L1=s.split('.')[0]  #按小数点分割字符串得到一个包含两个字符串的list

        L2=s.split('.')[1]  #小数点部分在后面除以10^得到

        length=len(L2)      #计算小数点位数

        return reduce(fn,map(char2num,L1))+reduce(fn,map(char2num,L2))/10**length

    else:

        return f'输入的字符串：\'{s}\'无法换成浮点数'

print(str2float('192.168.12.22'))

print(str2float('23333'))

print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:

    print('测试成功!')

else:

    print('测试失败!')