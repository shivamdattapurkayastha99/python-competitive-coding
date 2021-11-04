# gcd and lcm
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return a*b//gcd(a,b)
t=int(input())
while t:
    # a=int(input())
    # b=int(input())
    a,b=map(int,input().split(' '))
    print(f"gcd is {gcd(a,b)} and lcm is {lcm(a,b)}")
    t-=1