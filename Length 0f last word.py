class Solution(object):
def lengthOfLastWord(self, s):
"""
:type s: str
:rtype: int
"""
length = 0
ind = 0
for char in s[::-1]:
if char != ' ':
ind = 1
length+=1
elif ind == 1:
break
else:
continue
return length
