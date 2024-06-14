def merge(a,b):
    res = []
    m = len(a)
    n = len(b)
    i =0
    j =0
    while (i<m and j<n):
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        
        else:
            res.append(b[j])
            j+=1

    while i<m:
        res.append(a[i])
        i+=1
    while j<n:
        res.append(b[j])
        j+=1
    return res


def mergeSort(arr, l, r):
    if r>l:
        m = (r+l)//2
        mergeSort(arr, l, m)
        mergeSort(arr ,m+1, r)
        merge(arr, l, m, r)

    return arr


l = [90,80,90,25]

l1 = [10,820,220,25]

print(mergeSort(l, 2,2))