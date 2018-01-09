# 给一个int的array，输出数字的最高出现频率。比如, input:  [1, 2, 2, 2, 4, 4, 5], output: 3.
def max_fre(l):
	d = dict()
	max_freq = min(len(l), 1)
	for i in l:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1

	for i in d:
		max_freq = max(max_freq, d[i])

	return max_freq


# 第二题是给一个int的array，其中只有一个数字在array中只出现一次，其他数字都是成对出现的（一个数字出现两次），输出这个单一的数字。比如，input: [1, 1, 2, 2, 3, 5, 5, 9, 9], output: 3

def single_int(l):
	tmp_set = []
	for i in l:
		if i not in tmp_set:
			tmp_set.append(i)
		else:
			tmp_set.remove(i)
	return tmp_set

# log(n) dichotomy

def single_int(l):
	if len(l) <= 1:
		return l
	low = 0
	high = len(l)
	mid =  (low + high)/2
	while low < high:
		if l[mid] == l[mid-1]:
			if (mid - 1) % 2 == 0:
				low = mid
				mid = (low + high)/2
			else:
				high = mid
				mid = (low + high)/2
		elif l[mid] == l[mid + 1]:
			if mid % 2 == 0:
				low = mid
				mid = (low + high)/2
			else:
				high = mid
				mid = (low + high)/2
		else:
			return l[mid]



