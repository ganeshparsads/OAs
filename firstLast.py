class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            if nums[low] <= nums[high]:
                return nums[0]
            
            mid = low + (high-low)//2
            
            if (mid == 0 || nums[mid - 1] >= nums[mid]) and (mid == len(nums) - 1 or  nums[high] >= nums[mid]):
                return nums[mid]
            
            
            if nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
