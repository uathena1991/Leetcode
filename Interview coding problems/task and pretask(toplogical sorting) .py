"""
算task和pretask輸出task by level的那題. Just calculate indegree, bfs
是像這樣
input = {
{"cook", "eat"},   // do "cook" before "eat"
{"study", "eat"},
{"sleep", "study"}}

output (steps of a workflow):
{{"sleep", "cook"},.
{"study"},
{"eat"}}

"""
from collections import defaultdict
import pdb


class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edges(self, u, v):
		if v not in self.graph[u]:
			self.graph[u].append(v)



def topological_sort_DFS(inputs):
	def visit(node):
		visited[node] = True
		for xx in G.graph[node]:
			if not visited[xx]:
				visit(xx)
		res.append(node)

	# create graph
	G = Graph()
	visited = dict()
	v_list = []
	for i1, i2 in inputs:
		G.add_edges(i1, i2)
		visited[i1] = False
		visited[i2] = False
		if i1 not in v_list:
			v_list.append(i1)
		if i2 not in v_list:
			v_list.append(i2)

	# topological sorting
	res = []
	for vv in v_list:
		if not visited[vv]:
			visit(vv)
	return res


def topological_sort_task_by_level(inputs):

	# create graph
	G = Graph()
	v_list = []
	for i1, i2 in inputs:
		G.add_edges(i1, i2)
		if i1 not in v_list:
			v_list.append(i1)
		if i2 not in v_list:
			v_list.append(i2)

	to_visit = dict((i, False) for i in v_list)
	indegree = dict((u, 0) for u in v_list)
	for i1, i2 in inputs:
		indegree[i2] += 1

	queues = [u for u in v_list if indegree[u] == 0]
	res = [[queues]]

	while sum([to_visit[x] == False for x in to_visit]) > 0:
		next_queue = []
		for uu in queues:
			to_visit[uu] = True
			for vv in G.graph[uu]:
				indegree[vv] -= 1
				if indegree[vv] == 0:
					next_queue.append(vv)
		queues = next_queue
		if len(queues) > 0:
			res.append(next_queue)
	return res







"""
	  sleep
cook  study 
eat"""
inputs1 = [['cook', 'eat'], ["study", "eat"], ["sleep", "study"]]
print(topological_sort_DFS(inputs1))
print(topological_sort_task_by_level(inputs1))

inputs2 = [[5,0], [4,0], [4,1], [5,2], [2,3], [3,1]]

print(topological_sort_DFS(inputs2))
print(topological_sort_task_by_level(inputs2))



