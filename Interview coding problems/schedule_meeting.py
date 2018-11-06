class Solution():
	def meeting_scedule(self, list, query):
		for l1, l2 in list:
			if query[0] <= l1 and l2 <= query[1]:
				return False
			if l1 <=query[0] and l2 >= query[1]:
				return False
			if query[0] <= l1 <= query[1] and l2 > query[1]:
				return False
			if l1 <= query[0] and  query[0] <= l2 <=query[1]:
				return False
		return True

