
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
                                                            #DFS
        stack = [(cloned)]
        while stack:
            n = stack.pop()
            if n.val == target.val: return n
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)
                                                            #Recursive DFS
        if not original: return None
        if original is target: return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)