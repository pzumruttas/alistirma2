def fibonacci(n):
    
    #case base
    if n==0 or n==1:
        return n
    #recursion
    else:
        return fibonacci(n-2)+fibonacci(n-1)

for i in range(1,31):
    print(fibonacci(i), end=" ")
