"""
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
Newton's Method
https://en.wikipedia.org/wiki/Newton's_method#Square_root_of_a_number
x_{n+1} = (x_{n}+x/x_{n})/2
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        # Newton's method #
        x_guess = x/10.0
        epsion = 1
        error = abs(x_guess*x_guess-x)
        while (error) >= epsion:
            x_guess = (x_guess+float(x)/x_guess)/2
            error = abs(x_guess*x_guess-x)
        return int(x_guess)


a = Solution()
print a.mySqrt(3)