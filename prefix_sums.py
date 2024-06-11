# given an array of values, design a data structure that can query the sum of a subarray of the values


class PrefixSum:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total+=n
            self.prefix.append(total)
        

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left-1] if left>0 else 0
        return (preRight-preLeft)
    

a = PrefixSum([1,2,3,4,5,6,7,8])
print(a.rangeSum(2,5))