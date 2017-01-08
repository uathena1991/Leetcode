class Solution(object):
    def evalRPN(self, tokens):
        """
            :type tokens: List[str]
            :rtype: int
            """
        operators = ['+','-','*','/']
        l = []
        for elem in tokens:
            if elem in operators:
                a = l.pop()
                b = l.pop()
                if elem == '+':
                    l.append(b+a)
                elif elem == '-':
                    l.append(b-a)
                elif elem == '*':
                    l.append(b*a)
                elif elem == '/':
                    l.append(int(b/(a*1.0)))
            else:
                l.append(int(elem))
        return l[0]


