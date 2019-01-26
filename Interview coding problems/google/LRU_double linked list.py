class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap  = capacity
        self.head, self.tail = None, None
        self.curr_len = 0
        self.dict = {}
        if self.cap <= 0:
            return print('Error, capacity is not positive')

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print('get', key, self.dict.keys())
        if key in self.dict:
            cnode = self.dict[key]
            # update in the linke list
            if self.cap == 1:
                return cnode.val
            if cnode == self.head:
                return cnode.val
            if cnode == self.tail:
                self.tail = cnode.next
            if cnode.prev:
                cnode.prev.next = cnode.next
            cnode.next.prev = cnode.prev
            self.head.next = cnode
            cnode.prev = self.head
            cnode.next = None
            self.head = cnode
            # print('head', 'tail', self.head.key if self.head else 'None', self.tail.key if self.tail else 'None')
            # print('\n')
            return cnode.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print('put', key, value)
        if key in self.dict:
            cnode = self.dict[key]
            cnode.val = value
            # update in the linke list
            if self.cap == 1 or cnode == self.head:
                return
            if cnode == self.tail:
                self.tail = cnode.next
            if cnode.prev:
                cnode.prev.next = cnode.next
            cnode.next.prev = cnode.prev
            self.head.next = cnode
            cnode.prev = self.head
            cnode.next = None
            self.head = cnode
            return
        self.dict[key] = Node(key, value)
        if self.curr_len < self.cap:
            self.curr_len += 1
            if self.curr_len == 1:
                self.head, self.tail = self.dict[key], self.dict[key]
            else:
                self.head.next = self.dict[key]
                self.dict[key].prev = self.head
                self.head = self.head.next
        else:
            # remove the tail
            del self.dict[self.tail.key]
            self.tail = self.tail.next
            if self.tail:
                self.tail.prev = None
            self.curr_len -= 1
            # add new element
            if self.curr_len == 0:
                self.head, self.tail = self.dict[key], self.dict[key]
            else:
                self.head.next = self.dict[key]
                self.dict[key].prev = self.head
                self.head = self.head.next
            self.curr_len += 1
#         print('head', 'tail', self.head.key if self.head else 'None', self.tail.key if self.tail else 'None')
#         print(self.dict.keys())
#         print('\n')







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)