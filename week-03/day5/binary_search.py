class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        print(f"{self.val} --> {self.left} --> {self.right}")

class Solution:
    def sortedArrayToBST(nums):
        def helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
    
print(Solution.sortedArrayToBST([-3, -1, 0, 5, 9]))