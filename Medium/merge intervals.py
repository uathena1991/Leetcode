class Solution:
	def merge_intervals(self, intervals):
		op = []
		for interval in sorted(intervals, key=lambda i: i.start):
			if op and interval.start <= op[-1].end:
				op[-1].end = max(interval.end, op[-1].end)
			else: op.append(interval)
		return op

	def gap(self, intervals):
		op = self.merge_intervals(intervals)
		res = []
		if op[0][0] != 0:
			res.append([0, op[0][0]])
		pre_end = op[0][1]
		for start, end in op[1:]:
			res.append([pre_end, start])
			pre_end = end
		if end < 2400:
			res.append([end, 2400])
		return res