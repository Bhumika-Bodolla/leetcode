class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        closest = float('inf')
        n = len(nums)
        if sum(nums[:3])>target:
            return sum(nums[:3])
        if sum(nums[-3:])<target:
            return sum(nums[-3:])
            
        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum-target) < abs(closest-target):
                    closest = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest