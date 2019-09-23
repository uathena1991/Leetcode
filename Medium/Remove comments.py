class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        inblock = False
        res = []
        for line in source:
            c = 0
            if not inblock: # not blocked
                curr = []
            while c < len(line):
                if line[c:c+2] == '//' and not inblock:
                    break
                elif line[c:c+2] == '/*' and not inblock:
                    inblock = True
                    c += 1
                elif line[c:c+2] == '*/' and inblock:
                    inblock = False
                    c += 1
                elif not inblock:
                    curr.append(line[c])
                c += 1
            if not inblock and curr:
                res.append(''.join(curr))

        return res
