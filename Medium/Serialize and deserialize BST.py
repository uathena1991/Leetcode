# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # pre-order traversal
        res = []
        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return ' '.join(map(str, res))




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = [int(x) for x in data.split()]
        if not nodes:
            return None

        def buildbst(minv, maxv):
            if nodes and minv < nodes[0] < maxv:
                val = nodes.pop(0)
                node = TreeNode(val)
                node.left = buildbst(minv, val)
                node.right = buildbst(val, maxv)
                return node

        return buildbst(-float('inf'), float('inf'))







# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))