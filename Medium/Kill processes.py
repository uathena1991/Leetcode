class Solution(object):
	def killProcess(self, pid, ppid, kill):
		"""
		:type pid: List[int]
		:type ppid: List[int]
		:type kill: int
		:rtype: List[int]
		"""
		import collections
		pp_dic = collections.defaultdict(set)
		for child, par in zip(pid, ppid):
			pp_dic[par].add(child)

		queue = [kill]
		# print pp_dic
		res = []
		while queue:
			# print queue
			curr = queue.pop()
			res.append(curr)
			[queue.append(x) for x in pp_dic[curr]]
		return res
A = Solution()
print A.killProcess([1,3,10,5], [3,0,5,3], 5)