class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = ''
        if n <= 11 or n >= 2**31 - 1:
            return -1
        str_n = str(n)
        to_sort = [int(str_n[-1])]
        # to_sort = []
        for i in range(len(str_n)-2, -1, -1):
            if str_n[i] >= str_n[i+1]:
                to_sort.append(int(str_n[i]))
                continue
            else:
                break
        if i == 0 and len(to_sort) == len(str_n):
            return -1
        # print(to_sort)
        to_switch = int(str_n[i])
        res += str_n[:i]
        for x in range(len(to_sort)):
            if to_switch < to_sort[x]:
                res += str(to_sort[x])
                to_sort[x] = to_switch
                break
        to_sort.sort()
        # print(to_sort)
        res += ''.join([str(x) for x in to_sort])

        return int(res) if 0< int(res) < 2**31-1 else -1


