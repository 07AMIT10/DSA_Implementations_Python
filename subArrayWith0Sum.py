


def subsum(l):
    pre_sum = 0
    h = set()
    for i in range(len(l)):
        pre_sum+= l[i]
        if pre_sum==0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False


print(subsum([1,2,34,-34]))
