# even odd using bitwise operator 
def evenodd(n):
    if n&1==1:
        print("odd")
    else:
        print("even")
def mul(x,y):
    return x<<y
def div(x,y):
    return x>>y

t=int(input())
while t:
    # n=int(input())
    x,y=map(int,input().split())
    print(mul(x,y))
    print(div(x,y))

    
    t=t-1
