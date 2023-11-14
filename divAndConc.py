
def divAndConc(ls):

    if len(ls) <= 3:
        return tuple(sorted(ls))

    m = len(ls)//2
    left = list(divAndConc(ls[:m]))
    right = list(divAndConc(ls[m:]))

    li = 0
    ri = 0
    c = 0

    while li < len(left) and ri < len(right) and c < 3:
        if left[li] <= right[ri]:
            if c == 0:
                x = left[li]
            elif c == 1:
                y = left[li]
            elif c == 2:
                z = left[li]
            li += 1
            c += 1
        elif right[ri] <= left[li]:
            if c == 0:
                x = right[ri]
            elif c == 1:
                y = right[ri]
            elif c == 2:
                z = right[ri]
            ri += 1
            c += 1

    return tuple([x,y,z])

ls = [1,2,8,3,13,15,4,1,2,3,5,3]
print(divAndConc(ls))
