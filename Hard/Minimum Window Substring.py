class Solution():
	def minWindow(self, s, t):
		from collections import Counter
		def helper(dict_t, curr_counts):
			for dt in dict_t:
				if dict_t[dt] > curr_counts[dt]:
					return False
			return True
		left, right  = 0, 0
		curr_window = s[left:right+1]
		min_len = len(s)
		rest_start = 0
		dict_t = Counter(t)
		curr_counts = Counter(curr_window)
		while 0 <= left <= right < len(s):
			# expand window
			while right < len(s) and not helper(dict_t, curr_counts):
				right += 1
				curr_counts.update(s[right])
			# contract the window
			while left >=0 and helper(dict_t, curr_counts):
				left -= 1
				curr_counts -= Counter(s[left])
			curr_len = right - left + 1
			res_start = left if curr_len < min_len else rest_start
			min_len = curr_len if curr_len < min_len else min_len
		return s[res_start: res_start + min_len + 1]