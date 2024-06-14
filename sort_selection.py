

def select_sort(l):
    n = len(l)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1, n):
            if l[j]<l[min_ind]:
                min_ind = j
        l[min_ind], l[i] = l[i], l[min_ind]
    return l


l = [90,80,90,25]
print(select_sort(l))