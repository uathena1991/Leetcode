from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = defaultdict(int)
        for cc in cpdomains:
            ct, doms = cc.split(" ")
            counts[doms] += int(ct)
            idx = 0
            while idx < len(doms):
                if doms[idx] == '.':
                    counts[doms[idx+1:]] += int(ct)
                idx += 1


        res = []
        for cc in counts:
            res.append(str(counts[cc]) + " " + cc)

        return res


