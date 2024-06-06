


def distElements(arr):
    ele_map = {}
    for i in arr:
        if i in ele_map:
            ele_map[i]+=1
        else:
            ele_map[i] = 1
    return len(ele_map)

def distEle(l):
    s = set(l)
    return(len(s))

print(distElements([10,20,10,30,30,20]))

print(distEle([10,20,10,30,30,20]))