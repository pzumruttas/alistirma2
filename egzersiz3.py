def faktoryel(n):
    #case base
    if n==1:
        return 1
    #recursion
    else:
        return n*faktoryel(n-1)
