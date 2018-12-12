def Solution:
	def wordPatternMatch(self, pattern, str):
		def recursive(pattern, p, str, r, map):
			if p == len(pattern) and r == len(str):
				return True
			if p == len(pattern) or r == len(str):
				return False
			c = pattern[p]
			for i in range(r, len(str)):
				t = str[r:i+1]
				if map[c] == t:
					if recursive(pattern, p+1, str, i + 1, map):
						return True
				elif c not in map and t not in map.values():
					map[c] = t
					if recursive(pattern, p+1, str, i+1, map):
						return True
					del map[c]
				else: # map[c] != t or t has been assigned to some pattern
					return False
			return False
		map = dict()
		return recursive(pattern, 0, str, 0, map)





