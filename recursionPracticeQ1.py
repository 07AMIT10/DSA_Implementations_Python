def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    print(n)

# fun(3)

def fun2(n):
    if n==0:
        return
    fun2(n-1)
    print(n)
    fun2(n-1)

# fun2(3)


def fun3(n):
    if n<=1:
        return 0
    else:
        return 1+fun3(n//2)
    
# print(fun3(16))

# recursive function to find the binary of a decimal (base 10) number
def fun4(n):
    if n==0:
        return
    fun4(n//2)
    print(n%2)

fun4(13)
