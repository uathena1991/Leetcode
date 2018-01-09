class Solution(object):
	def sent_similar(self, word1, word2, pairs):
		if len(word1) != len(word2):
			return False
		for i in range(len(word1)):
			if [word1[i], word2[i]] in pairs or [word2[i], word1[i]] in pairs:
				continue
			else:
				return False
		return True
