"""
no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, “01:34”, “12:09” are all valid. “1:34”, “12:9” are all invalid.

Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller
than the input time numerically.

Solution:
go from the last digit, find the smallest one > it, if valid, return, else, set it as min, go the the left one, repeat...
"""

def next_closest_time(time):
	def isValid(t):
		return int(t[:2]) <= 23 and int(t[2:])<= 59 and int(t[0]) != 0
	libs = sorted([int(x) for x in time[:2] + time[3:]])
	for x in range(3,-1,-1):
		for y in libs:
			if y > time[x]:
				ntime = str[:x] + y + str[x+1:4]
				if isValid(ntime):
					return ntime[:2] + ':' + ntime[2:]
	return libs[0] + libs[0] + ':' + libs[0] + libs[0]


