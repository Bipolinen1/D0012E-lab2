
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




    # if (lcurr_max > 0 and lend == len(l) - 1) and (rcurr_max > 0 and rstart == 0):
    #     return ls, lstart, len(l) + rend , lcurr_max + rcurr_max, total_sum
    # if lcurr_max > 0 and rcurr_max < 0:
    #     return ls, lstart, lend, lcurr_max, total_sum
    # if lcurr_max < 0 and rcurr_max > 0:
    #     return ls, len(l) + rstart,len(l) + rend, rcurr_max, total_sum
    # if lcurr_max < 0 and rcurr_max <0:
    #     return ls, rstart, rend, rcurr_max, total_sum
    # if lend != len(l) - 1 or rstart > len(r)-1:
    #     if total_sum > lcurr_max and total_sum > rcurr_max:
    #         return ls,lstart, len(l) + rend, total_sum, total_sum
    #     if lcurr_max >= rcurr_max:
    #         return ls, lstart, lend, lcurr_max, total_sum
    #     else:
    #         return ls,len(l) + rstart, len(l) + rend, rcurr_max, total_sum








ls = [-2,3,-5,4]
print(maxSumSegment(ls))
