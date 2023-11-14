
def divAndConc(ls):

    if len(ls) <= 3:
        return tuple(ls.sort())

    m = len(ls)//2
    left = divAndConc(ls[:m])
    right = divAndConc(ls[m:])

    if left[0] < right[0]:
        x = left[0]
    else:
        x = right[0]
    if left[1] < right[1]:
        y = left[1]
    else:
        y = right[1]
    if left[2] < right[2]:
        z = left[2]
    else:
        z = right[2]

    return tuple([x,y,z])