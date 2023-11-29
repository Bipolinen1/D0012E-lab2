

def incremental2(ls):

    t = [float('inf'),float('inf'),float('inf')]

    for i in ls:
        if i < t[0]:
            t[1] = t[0]
            t[0] = i

        elif i < t[1]:
            t[2] = t[1]
            t[1] = i
        elif i < t[2]:
            t[2] = i
    return t


ls = [10, 5, 6, 4, 2, 5, 3]

print(incremental2(ls))

