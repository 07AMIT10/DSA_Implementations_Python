
def sum_of_nums(n):
    return ((n*(n+1))/2)

# print(sum_of_nums(10))

# recursive function to print n to 1 using recursion

def rec_printNTo1(n):
    if n<=0:
        return
    print(n)
    rec_printNTo1(n-1)

# def rec_print(n):
#     if n<=0:
#         return 1
#     print(n, end = " ")
#     return(n-rec_print(n-1))

# rec_printNTo1(5)
        


def print1ToN(n):
    if n<=0:
        return 
    print1ToN(n-1)
    print(n, end=" ")

print1ToN(5)

