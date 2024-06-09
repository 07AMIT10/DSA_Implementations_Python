class Solution:
    def zigZag(self, n, arr):
        for i in range(n-1):
            if arr[i]> arr[i+1] and i%2==0:
                arr[i], arr[i+1]= arr[i+1], arr[i]
            if arr[i]< arr[i+1] and i%2!=0:
                arr[i], arr[i+1]= arr[i+1], arr[i]
        return arr


a = Solution()
print(a.zigZag(5, [1,32,2,4,6]))