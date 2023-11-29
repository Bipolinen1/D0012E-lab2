def incremental(ls):

    nls = [float('inf'), float('inf'), float('inf')]

    for i in ls:
        if i < nls[0]:
            nls[1] = nls[0]
            nls[0] = i
        elif i < nls[1]:
            nls[2] = nls[1]
            nls[1] = i
        elif i < nls[2]:
            nls[2] = i

        return nls
