class Solution(object):
	def subdomainVisits(self, cpdomains):
		"""
		:type cpdomains: List[str]
		:rtype: List[str]
		"""
		from collections import defaultdict
		res = defaultdict(int)
		for dm in cpdomains:
			click = cpdomains[dm]
			subs = dm.split('.')
			for i in range(len(subs)):
				csb = '.'.join(subs[i:])
				res[csb] += click
		return res

	def longest_continuous_common_history(self, his1, his2):
		"""
		user0 = [ "/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html" ]
		user2 = [ "/nine.html", "/two.html", "/three.html", "/four.html", "/six.html", "/seven.html" ]
		user1 = [ "/one.html", "/two.html", "/three.html", "/four.html", "/six.html" ]
		user3 = [ "/three.html", "/eight.html" ]. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴

		Sample output:

		(user0, user2):
		   /four.html
		   /six.html
		   /seven.html

		(user1, user2):. visit 1point3acres.com for more.
		   /two.html
		   /three.html
		   /four.html
		   /six.html

		(user0, user3):
		   None. 鍥磋鎴戜滑@1point 3 acres

		(user1, user3):
		   /three.htmlint3acres

		:param his1:
		:param his2:
		:return:
		"""
		dp = [[0 for _ in range(len(his2) + 1)] for _ in range(len(his1) + 1)]
		max_len, last_idx = 0, 0
		for i1 in range(len(his1)):
			for i2 in range(len(his2)):
				if his1[i1] == his2[i2]:
					dp[i1 + 1][i2 + 1] = dp[i1][i2] + 1
					if max_len < dp[i1 + 1][i2 + 1]:
						max_len = dp[i1 + 1][i2 + 1]
						last_idx = i1 + 1
		return max_len, his1[last_idx - max_len:last_idx]
