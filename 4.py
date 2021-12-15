# prime numbers
def approach1(n):
    divcnt=0
    for i in range(1,n+1):
        if n%i==0:
            divcnt+=1
    if divcnt==2:
        return True
    else:
        return False







def approach2(n):
    pass


t=int(input())
while t:
    n=int(input())
    print(approach1(n))
    # print(approach2(n))
    t-=1