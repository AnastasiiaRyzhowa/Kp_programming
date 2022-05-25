def bin_search(li, element):
    low=0
    high=len(li)-1#хранятся границы части списка, в которой выполняется поиск
    while low<=high:#пока эта часть не сократиться
        mid=(low+high)//2#находим средний элемент и проверяем его
        chislo=li[mid]
        if chislo==element:
            return mid
        if chislo>element:#много
            high=mid-1
        else:
            low=mid+1#мало
    return -1

a=sorted([3,1,9,5,2,7])
b=-1
print(bin_search(a, b))

a=sorted([3,1,9,5,2,7])
b=9
print(bin_search(a, b))

print(bin_search( [2,5,7,9,11,17,222], 12))

print(bin_search( [2,5,7,9,11,17,222], 11))
