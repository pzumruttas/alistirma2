def toplam(n):
    #case base
    if n==1:
        return 1
    #recursion
    else:
        return n+toplam(n-1)
