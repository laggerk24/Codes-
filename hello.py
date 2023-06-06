def odd_even(l):
    t = []
    o = []
    e = []
    for i in l:
        if i%2 ==0:
            e.append(i)
        else:
            o.append(i)
    t.append(o)
    t.append(e)
    return t

print(odd_even([1,2,3,4,5,6,7,8,9,10]))
