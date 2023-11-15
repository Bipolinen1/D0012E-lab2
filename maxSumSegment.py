
def maxSumSegment(ls):
    if len(ls) == 1:

        return ls[0], ls[0], 0, 0

    m = len(ls)//2
    l, lsum, lstart, lstop = maxSumSegment(ls[:m])
    r, rsum, rstart, rstop = maxSumSegment(ls[m:])
    lsum = 0
    rsum = 0
    for i in ls[lstart:m]:
        lsum += i
    for j in ls[m:m + rstop + 1]:
        rsum += j

    if l < 0 and r < 0:
        return lsum + rsum, lsum + rsum, lstart, m + rstop
    if l > 0 and r < 0:
        return l, lsum, lstart, lstop
    if l < 0 and r > 0:
        return r, rsum, m + rstart, m + rstop
    if l > 0 and r > 0:
        if (lsum + rsum) > l and (lsum + rsum) > r:
            return lsum + rsum, lsum + rsum, lstart, m + rstop
        else:
            if l > r:
                return l, lsum, lstart, lstop
            else:
                return r, rsum, m + rstart, m + rstop
        # if (lsum + rsum) > l and (lsum + rsum) < r:
        #     return r, rsum, m + rstart, m + rstop
        # else:
        #     return l, lsum, lstart, lstop

ls = [-2,3,-5,4]
print(maxSumSegment(ls))
