class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None #  1
        self.right = None # 0


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode(0)
        # build a Trie
        for num in nums:
            node = root
            for i in range(32)[::-1]:
                cbits = num >> i & 1
                if cbits == 0:
                    if not node.right:
                        node.right = TrieNode(0)
                    node = node.right
                elif cbits == 1:
                    if not node.left:
                        node.left = TrieNode(1)
                    node = node.left
                else:
                    print("Error!!!", cbits)
            node.val = num
        trueroot = root
        max_bits = 31
        while trueroot.val == 0 and (trueroot.right and not trueroot.left):
            trueroot = trueroot.right
            max_bits -= 1
        # print(trueroot.val, trueroot.left.val, trueroot.right.val)


        # calculate the max distance
        res = 0
        for num in nums:
            node = trueroot
            for i in range(max_bits + 1)[::-1]:
                cbits = num >> i & 1
                if node.left and node.right:
                    node = node.right if cbits == 1 else node.left
                else:
                    node = node.left if node.left else node.right
            # print(num, node.val)
            res = max(num^node.val, res)
        return res

