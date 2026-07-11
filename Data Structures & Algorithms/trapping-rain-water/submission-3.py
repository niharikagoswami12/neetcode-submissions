class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        n=len(height)-1
        left=0
        right=n
        leftMax=height[left]
        rightMax=height[right]
        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax=max(leftMax, height[left])
                res+=leftMax-height[left]
            else:
                right-=1
                rightMax=max(rightMax, height[right])
                res+=rightMax-height[right]
        return res


        