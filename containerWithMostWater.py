class Solution:
    def maxArea(self, height):
        # BRUTE FORCE
        res =0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r-l)* min(height[l], height[r])
                res = max(res, area)

        return res
    

    def omaxArea(self, height):
        # OPTIMAL SOLUTION
        res =0
        l, r = 0, len(height)-1

        while l<r:
            area = (r-l)*min(height[l], height[r])
            res = max(res, area)
            if height[l]< height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                r-=1
        return res
    

a = Solution()
print(a.omaxArea([1,2,3,3,4,53,23,23,34]))