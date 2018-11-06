from collections import defaultdict
class Solution():
	def check_exit(self, records):
		res = []
		res_dict = defaultdict(list)
		for r in records:
			res_dict[r[0]].append(r[1])
		for p in res_dict:
			stat = 0
			for rr in res_dict[p]:
				if rr == 'enter':
					stat += 1
				if rr == 'exit':
					stat -= 1
				if stat not in [1, -1 , 0]:
					res.append(p)
					break
		return res

	def check_enter(self, records):


