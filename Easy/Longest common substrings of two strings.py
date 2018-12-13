class Solution():
	def find_common(self, s1, s2):
		len1, len2 = len(s1), len(s2)
		m = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
		max_len = 0
		last_idx = 0
		for i in range(len1):
			for j in range(len2):
				if s1[i] == s2[j]:
					m[i+1][j+1] = m[i][j] + 1
					if m[i+1][j+1] > max_len:
						max_len = m[i+1][j+1]
						last_idx = i + 1
		return s1[last_idx - max_len: last_idx], max_len
