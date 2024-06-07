

def rec_sum(n):
    if n<10:
        return n
    return rec_sum(n//10)+n%10
# sum = 0
print(rec_sum(253))