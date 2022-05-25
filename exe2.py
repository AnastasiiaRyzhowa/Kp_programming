def filter_even(li):
    a=list(filter(lambda x: x%2==0, li))
    return a

li=map(int,input().split())
print(filter_even(li))
li=[11,22,33,44,55,88,99,66]
print(filter_even(li))
