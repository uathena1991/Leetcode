class KeyNode():
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = None
        self.prev = None


class FreqNode():
    def __init__(self, freq):
        self.freq = freq
        self.next = None
        self.first = None
        self.last = None


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        if capacity < 1:
            return -1
        self.cap = capacity
        self.kdict = dict() # key_val: keyNode
        self.fdict = dict() # freq_val: freqNode
        self.fdict[0] = FreqNode(0)
        self.min_freq = self.fdict[0] # min_freq None

    def del_from_freqNode(self, freq_n, key_n):
        """
        delete a keyNode from freqNode
        including deleting from fdict, update min_freq
        not including deleting from kdict
        """
        if freq_n.first == freq_n.last: # only one element
            if key_n != freq_n.first:
                print("The KeyNode is not in current FreqNode")
                return
            else:
                if self.min_freq == freq_n:
                    self.min_freq = freq_n.next
                del self.fdict[freq_n.freq]
                return
        else: # > one element
            if key_n == freq_n.first:
                key_n.next.prev = None
                freq_n.first = key_n.next
            elif key_n == freq_n.last:
                freq_n.last = key_n.prev
                key_n.prev.next = None
            else:
                key_n.prev.next = key_n.next
            return




    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print('\n get', key)
        if key in self.kdict:
            # update freq in kdict
            key_n = self.kdict[key]
            old_freq_n = self.fdict[key_n.freq]
            key_n.freq += 1
            # update in FreqNode
            # delete from old FreqNode
            print(old_freq_n.freq, key_n.val, key_n.freq, old_freq_n.next)
            self.del_from_freqNode(old_freq_n, key_n)
            # print(old_freq_n.freq, key_n.val, key_n.freq, )
            print("get, after del", self.min_freq)
            # add to the new freqNode
            if key_n.freq not in self.fdict: # new freq not exist
                new_freq_n = FreqNode(key_n.freq)
                if old_freq_n:
                    old_freq_n.next = new_freq_n
                    print("old, new", old_freq_n.freq, new_freq_n.freq)
                else:
                    # update new min_freq
                    self.min_freq = new_freq_n
                new_freq_n.first, new_freq_n.last = key_n, key_n
                self.fdict[key_n.freq] = new_freq_n
            else:
                new_freq_n = self.fdict[key_n.freq]
                if old_freq_n:
                    old_freq_n.next = new_freq_n
                key_n.prev = new_freq_n.last
                key_n.next = None
                new_freq_n.last.next = key_n
                new_freq_n.last = key_n
            print(self.kdict.keys())
            print(self.fdict.keys())
            if self.min_freq and self.min_freq.first and self.min_freq.last:
                print(self.min_freq.freq, self.min_freq.first.val, self.min_freq.last.val)
            return key_n.val

        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        print("\n put", key, value)
        if key not in self.kdict: # insert
            # check capacity
            print("before", self.min_freq.freq, self.min_freq.first, self.min_freq.last)
            if len(self.kdict) >= self.cap: # delete from min_freq (may need to update min_freq)
                del self.kdict[self.min_freq.first.val]
                self.del_from_freqNode(self.min_freq, self.min_freq.first)

            # put new key
            self.kdict[key] = KeyNode(key, value, 0)
            if self.min_freq.first and self.min_freq.last:
                print("after1",  self.min_freq.freq, self.min_freq.first.val, self.min_freq.last.val)
            # add new keyNode to freqNode
            if 0 not in self.fdict:
                self.fdict[0] = FreqNode(0)
                self.min_freq = self.fdict[0]
            freq_n = self.fdict[0]
            if not freq_n.first:
                freq_n.first = self.kdict[key]
                freq_n.last = self.kdict[key]
            else:
                self.kdict[key].prev = freq_n.last
                freq_n.last.next = self.kdict[key]
                freq_n.last = self.kdict[key]
            if self.min_freq.first and self.min_freq.last:
                print("after2",  self.min_freq.freq, self.min_freq.first.val, self.min_freq.last.val)
            print(freq_n.first.val, freq_n.last.val)


        else: # key already in
            key_n = self.kdict[key]
            key_n.val = value
            print("after2",  self.min_freq.freq, self.min_freq.first, self.min_freq.last)


        print(self.kdict.keys())
        print(self.fdict.keys())
        print(self.min_freq.freq, self.min_freq.first, self.min_freq.last)






# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)