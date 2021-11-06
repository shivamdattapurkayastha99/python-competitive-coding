# all divisors of a number
from math import sqrt
t=int(input())
def fun1(n):
    div1=[]
    for i in range(1,n+1):
        if n%i==0:
            div1.append(i)
    return div1
def fun2(n):
    div1=[]
    for i in range(1,int(sqrt(n+1))):
        if n%i==0:
            div1.append(i)
    return div1
while t:
    n=int(input())
    div1=fun1(n)
    print(*div1)
    div2=fun1(n)
    print(*div2)
    t-=1
