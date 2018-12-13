from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_len = capacity
        self.dict = OrderedDict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.dict:
            self.dict.move_to_end(key, last = True)
            return self.dict[key]
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dict:
            while len(self.dict) >= self.max_len:
                self.dict.popitem(last = False)
            self.dict[key] = value
        else:
            self.dict[key] = value
            self.dict.move_to_end(key, last = True)






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)