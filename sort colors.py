class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """


# quicksort     
    def sortColors(self, nums):
        # write your code here
        start, end = 0 , len(nums)-1 
        
        self.quicksort(nums,0,2,start,end)
        return nums
        
    
    
    
    
    def quicksort(self,nums, j, k, start,end ):
        if j== k or start > end:
            return 
        left, right = start, end 
        
        pivot = (j+k)//2 
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left+=1
                
            while left <= right and nums[right] > pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1 
                right -= 1 
                
            
        self.quicksort(nums, j, pivot, start, left )
        self.quicksort(nums, pivot+1, k, right, end )



#scan 

    def sortColors(self, A):
            left, index, right = 0, 0, len(A) - 1

            # be careful, index < right is not correct
            while index <= right:
                if A[index] == 0:
                    A[left], A[index] = A[index], A[left]
                    left += 1
                    index += 1
                elif A[index] == 1:
                     index += 1
                else:
                    A[right], A[index] = A[index], A[right]
                    right -= 1