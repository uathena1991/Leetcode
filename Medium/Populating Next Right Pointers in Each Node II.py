

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


# recursion, but not constant space...
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or (not root.left and not root.right):
            return
        if root.left and root.right:
            root.left.next = root.right
        next_node = self.find_next(root.next)
        if root.right:
            root.right.next = next_node
        else:
            root.left.next = next_node
        self.connect(root.right)
        self.connect(root.left)

    def find_next(self,root): # find the next root to expand: DFS
        if not root:
            return None
        if not root.left and not root.right:
            return self.find_next(root.next)
        if root.left:
            return root.left
        if root.right:
            return root.right



## BSF: didn't pass all cases: 36/61 passed...
# wrong case:
# input:{3,9,20,#,#,15,7}
# output: {3,#,9,20,#,15,#}
# expected: {3,#,9,20,#,15,7,#}
# why....?????????????

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        pre_level = root
        curr_level = None
        while pre_level.left or pre_level.right:
            curr_level = pre_level
            tmp_pre = []
            idx = 0 # whether current node is the left-est of current level
            while curr_level:
                # inner connect
                if curr_level.left and curr_level.right:
                    curr_level.left.next =  curr_level.right
                    tmp_pre = curr_level.right
                    idx = 1
                elif curr_level.left:
                    tmp_pre = curr_level.left
                    idx = 1
                elif curr_level.right:
                    tmp_pre = curr_level.right
                    idx = 1
                if curr_level.next and tmp_pre:
                    if curr_level.next.left:
                        tmp_pre.next = curr_level.next.left
                    elif curr_level.next.right:
                        tmp_pre.next = curr_level.next.right
                curr_level = curr_level.next
                if idx == 0:
                    pre_level = curr_level
            pre_level = pre_level.left if pre_level.left else pre_level.right


## passed copy
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
        :param root:
        :return:
        """
        if not root:
            return
        head_next = root
        while head_next:
            curr = head_next # nodes in current level
            pre_next = [] # previous node in next level
            head_next = []  # most left node in the next level
            while curr:
                # left child
                if curr.left:
                    if pre_next:
                        pre_next.next = curr.left
                    else:
                        head_next = curr.left
                    pre_next = curr.left
                # right child
                if curr.right:
                    if pre_next:
                        pre_next.next = curr.right
                    else:
                        head_next = curr.right
                    pre_next = curr.right
                curr = curr.next



a = Solution()
import leetcode_tool_lib as ltl
tree_list = ltl.List2Tree().list2node([1,2,3,[],4,[],5,[],[],6,7])
root = ltl.List2Tree().from_level_list(tree_list)
a.connect(root)
print ltl.PrintTree().level_traversal(root)
