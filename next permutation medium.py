class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        
        if len(nums) <=1:
            return nums
            
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1,i,-1):
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        nums[i+1:] = sorted(nums[i+1:])
                        
                        break 
                break
            
            
            else:   
                if i ==0:
                    nums.reverse()
                
                
                
                
        return nums        
