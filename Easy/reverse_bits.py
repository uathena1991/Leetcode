class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str_n = bin(n)[2:]
        str_n_32 = '0' * (32-len(str_n)) + str_n
        reverse_str = str_n_32[::-1]
        return int(reverse_str, 2)