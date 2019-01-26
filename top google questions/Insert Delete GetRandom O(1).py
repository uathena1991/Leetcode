import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num2idx = dict()
        self.idx2num = dict()
        self.len = 0


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.num2idx:
            self.num2idx[val] = self.len
            self.idx2num[self.len] = val
            self.len += 1
            # print('add', val)
            # print(self.idx2num)
            # print(self.num2idx)
            # print(self.len)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.num2idx:
            olast_num = self.idx2num[self.len - 1]
            orem_idx = self.num2idx[val]
            self.num2idx[olast_num] = orem_idx
            self.idx2num.pop(orem_idx)
            self.idx2num[orem_idx] = olast_num
            self.num2idx.pop(val)
            self.len -= 1
            # print("remove", val)
            # print(self.idx2num)
            # print(self.num2idx)
            # print(self.len)
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.idx2num[random.randint(0, self.len-1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()