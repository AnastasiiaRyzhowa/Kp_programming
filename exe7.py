def substring_slice(path2file_1,path2file_2):
    f1=path2file_1.readlines()
    f2=path2file_2.readlines()
    str_1, str_2='', ''
    x=0
    z=0
    zn_1, zn_2, res='', '', ''
    for i in f1:#проходим по элементам 1 файла
        str_1+=i
    for j in f2:#проходим по элементам 2 файла
        str_2+=j
    str_1, str_2=str_1.split(), str_2.split()
    while x+1<len(str_2):
        zn_1=int(str_2[x])#1 значение
        zn_2=int(str_2[x+1])+1#последнее
        x=x+2
        for i in range(len(f1)):
            if z==i:
                n=f1[i]
                for w in range(len(n)):
                    res=res+n[zn_1:zn_2]+' '
                    break
        z+=1
    return res
f1=open('test_import_file_2_1.txt')
f2=open('test_import_file_2_2.txt')
print(substring_slice(f1,f2))

