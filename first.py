def reverse_list(l):
    tempeorary = []
    i = len(l)-1
    while i>=0:
        tempeorary.append(l[i])
        i -= 1
    return tempeorary
print(reverse_list([1,2,4,5,6,7,8]))


