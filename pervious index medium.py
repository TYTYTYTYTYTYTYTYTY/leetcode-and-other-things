class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        index = 1 
        
        for i in range(len(A)):
            count = 0 
            
            factor  =  1 
            for j in range(i+1,len(A)):
                if A[j] < A[i]:
                    count += 1 
                    
            for k in range(1, len(A) -i):
                factor *= k 
                
            index += factor*count 
            
        return index