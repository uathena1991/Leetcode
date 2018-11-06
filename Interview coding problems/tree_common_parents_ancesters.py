from collections import defaultdict
class Solution():
	def __init__(self, edges):
		self.p_dict = defaultdict(list)
		for ll in edges:
			if ll[0] not in self.p_dict[ll[1]]:
				self.p_dict[ll[1]].append(ll[0])

	def parent01(self):
		res0, res1 = [], []
		for node in self.p_dict:
			if len(self.p_dict[node]) ==0:
				res0.append(node)
			if len(self.p_dict[node]) == 1:
				res1.append(node)
		return res0, res1



	def common_ancenster(self, na, nb):
		def get_all_ancenster(node, res):
			if not self.p_dict[node]:
				return
			else:
				for x in self.p_dict[node]:
					res.append(x)
					get_all_ancenster(x, res)


		res_a, res_b = [], []
		get_all_ancenster(na, res_a)
		get_all_ancenster(nb, res_b)
		if len(set(res_a).intersection(set(res_b))) > 0:
			return True
		else:
			return False


	def farthest_ancenster(self, node):
		def dfs(depth, node):
			""" DFS to get furthest ancenster"""

			parents = self.p_dict[node]
			if len(parents)  == 0:
				return 0, node
			else:
				for pa in parents:
					return dfs(depth, pa)[0] + 1, dfs(depth, pa)[1]

		max_depth, max_pa = 0, node
		for x in self.p_dict[node]:
			# print(max_pa, max_depth)
			tmp_depth = 1
			tmp_depth, tmp_node = dfs(tmp_depth, x)
			if tmp_depth > max_depth:
				max_depth, max_pa = tmp_depth, tmp_node
		return max_pa, max_depth

ltt = [[1,4], [1,5], [2,5], [3,6], [6,7], [7,8]]
nn = Solution(ltt)
print(nn)
print(nn.p_dict)
print(nn.parent01())

print(nn.common_ancenster(4,5))
print(nn.common_ancenster(4,7))
print(nn.common_ancenster(6,8))

print(nn.farthest_ancenster(8))











