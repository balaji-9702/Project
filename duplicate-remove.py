dup_list = [3,5,4,5,6,3,10,12,10,5]


for x in dup_list:
    count = dup_list.count(x)
    print(count)
    if count > 1:
        dup_list.remove(x)
print (dup_list)        