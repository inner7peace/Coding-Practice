‘’‘有一楼梯共m级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第m级，共有多少走法？
注：规定从一级到一级有0种走法。

输入数据首先包含一个整数n(1<=n<=100)，表示测试实例的个数，然后是n行数据，每行包含一个整数m，（1<=m<=40), 表示楼梯的级数。’‘’


def jump(n):
  if n <= 3:
    return n-1
  else: 
    return jump(n-1) + jump(n-2)
    
num = int(raw_input())
for i in range(num):
  n = int(raw_input())
  print jump(n)
