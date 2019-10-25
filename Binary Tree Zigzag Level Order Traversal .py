"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
            
        queue = deque([])
        queue.append(root)
        output = []
        
        while queue:
            temp =[]
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            output.append(temp)
            
        for i, out in enumerate(output):
            if i%2 ==1:
                out.reverse()
                output[i] = out
            else:
                continue
            
            
        return output