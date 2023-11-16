import time
import random
# def maxSumSegment(ls):
#     if len(ls) == 1:
#
#         return ls[0], ls[0], 0, 0
#
#     m = len(ls)//2
#     l, lsum, lstart, lstop = maxSumSegment(ls[:m])
#     r, rsum, rstart, rstop = maxSumSegment(ls[m:])
#     lsum = 0
#     rsum = 0
#     for i in ls[lstart:m]:
#         lsum += i
#     for j in ls[m:m + rstop + 1]:
#         rsum += j
#
#     if l < 0 and r < 0:
#         return lsum + rsum, lsum + rsum, lstart, m + rstop
#     if l > 0 and r < 0:
#         return l, lsum, lstart, lstop
#     if l < 0 and r > 0:
#         return r, rsum, m + rstart, m + rstop
#     if l > 0 and r > 0:
#         if (lsum + rsum) > l and (lsum + rsum) > r:
#             return lsum + rsum, lsum + rsum, lstart, m + rstop
#         else:
#             if l > r:
#                 return l, lsum, lstart, lstop
#             else:
#                 return r, rsum, m + rstart, m + rstop
#         # if (lsum + rsum) > l and (lsum + rsum) < r:
#         #     return r, rsum, m + rstart, m + rstop
#         # else:
#         #     return l, lsum, lstart, lstop

def maxSumSegment(ls):
    if len(ls) == 1:

        return ls[0], ls[0], ls[0], ls[0]

    m = len(ls)//2
    lmax, l_left_sum, l_right_sum, l_tot = maxSumSegment(ls[:m])
    rmax, r_left_sum, r_right_sum, r_tot = maxSumSegment(ls[m:])

    if lmax <= 0 and rmax <= 0:
        return 0,l_tot, l_tot, l_tot + r_tot
    if lmax > 0 and rmax < 0:
        return lmax, l_left_sum, lmax + r_tot, l_tot + r_tot
    if lmax < 0 and rmax > 0:
        return rmax, rmax + l_tot, r_left_sum, l_tot + r_tot
    if lmax > 0 and rmax > 0:
        if (l_right_sum + r_left_sum) > lmax and (l_right_sum + r_left_sum) > rmax:
            new_max = l_right_sum + r_left_sum
            return new_max, l_tot + r_left_sum, r_tot + l_right_sum , l_tot + r_tot
        else:
            if lmax > rmax:
                return lmax, l_left_sum, lmax + r_tot, l_tot + r_tot
            elif rmax > lmax:
                return rmax, rmax + l_tot, r_left_sum, l_tot + r_tot

"""Pseudocode:
    1. Base case: if the length of array is 1 we return the element
    2. Divide list into sub-lists
"""
ls = [-1,4,-1,3]
print(maxSumSegment2(ls))