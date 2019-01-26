class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        split_emails = [tuple(x.split("@")) for x in emails]
        res  = set()
        for loc, dom in split_emails:
            new = loc.replace(".", "").split("+")[0]
            res.add((new, dom))
        return len(res)


        