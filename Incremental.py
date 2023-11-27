def incremental(ls):
    if len(ls) <= 3:
        return sorted(ls)
    left = incremental(ls[:3])
    right = incremental(ls[3:])
    li = 0
    ri = 0
    c = 0

    while c < 3:
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

    return tuple([x, y, z])


ls = [2, 3, 4, 6, 1, 7, 9, 8, 10, 4, 3, 1]
print(incremental(ls))
