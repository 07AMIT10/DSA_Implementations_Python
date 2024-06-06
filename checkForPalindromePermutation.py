from collections import Counter

def isPalPer(s):
    cut = Counter(s)
    odd = 0
    for freq in cut.values():
        if freq%2!=0:
            odd+=1
            if odd>1:
                return False
    return True



print(isPalPer('abaaacc'))