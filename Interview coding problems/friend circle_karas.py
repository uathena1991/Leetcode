"""
1st Question: 输出所有的employee的friendlist -> 就是用一个map存起来然后打印就好了（这个是无向图，e.g: 1和2是朋友，2的列表里也要有1）
2nd Question: 输出每个department里有多少人的朋友是其他部门的 ->也就是遍历一遍就好了
3rd Question: 输出是否所有employee都在一个社交圈 -> 我当时想的就是随便找一个点，用DFS遍历一遍，如果所有点都被遍历到就return true，不然就是false. 1point 3acres 璁哄潧

"""
from collections import defaultdict
class Person(object):
	def __init__(self, input):
		self.name = input[0]
		self.department = input[1]
		self.friends = []

	def add_friend(self, p1):
		""" p1, p2 are two nodes"""
		if p1 not in self.friends:
			self.friends.append(p1)

class Solution():
	def friend_map(self, lists):
		res = defaultdict()
		for l1,l2 in lists:
			p1 = Person(l1)
			p2 = Person(l2)
			p1.add_friend(p2)
			p2.add_friend(p1)
			if p2 not in res[p1]:
				res[p1].append(p2)
		return res

	def different_department(self, fmap):
		"""
		:param fmap: friend maps
		:return:
		"""
		toselect = list(fmap.keys())
		res = defaultdict() # key: department, value: Person
		while len(toselect) > 0:
			curr = toselect.pop()
			for ff in fmap[curr]:
				if ff.deparment != curr.deparment:
					if curr not in res[curr.deparment]:
						res[curr.deparment].append(curr)
					if ff not in res[ff.deparment]:
						res[ff.deparment].append(ff)
					toselect.pop(ff)
		return res

	def same_friend_circle(self, p_list, fmap):
		all_friends = []
		for x in p_list:
			all_friends += fmap[x]
			
		return len(p_list) == len(set(all_friends))

