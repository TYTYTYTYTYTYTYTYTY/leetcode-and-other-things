class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        x ,y  = len(matrix)-1 ,0 
        count = 0 
        if not matrix or not matrix[0]:
            return 0 
            
        while x >=0 and y < len(matrix[0]):
            if matrix[x][y] == target:
              x -= 1
              y += 1 
              count += 1 
            elif matrix[x][y] < target:
                y += 1 
            else:
                x-=1
        
        
        return count