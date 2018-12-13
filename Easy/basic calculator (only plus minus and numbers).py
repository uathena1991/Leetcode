class Solution():
	def plus_minus(self, s1):
		"""
		where input is only plus and minus and numbers
		:param str:
		:return:
		"""
		num_list = s1.replace(' ', '').replace('+', 't').replace('-', 't').split('t')
		num_list = num_list[::-1]
		res = int(num_list.pop())
		for c in s1:
			if c == '+':
				res += int(num_list.pop())
			elif c == '-':
				res -= int(num_list.pop())

		return res

	def plus_minus_multi_div(self, s1):
		"""
		include + - * /
		:param s1:
		:return:
		"""
		num_list = s1.replace(' ', '').replace('+', 't').replace('-', 't').replace('*', 't').replace('/', 't').split('t')
		num_list = num_list[::-1]
		stack = [int(num_list.pop())]
		for c in s1:
			if c == '+':
				stack.append(int(num_list.pop()))
			elif c == '-':
				stack.append(int(num_list.pop())*(-1))
			elif c == '*':
				stack[-1] *= int(num_list.pop())
			elif c == '/':
				stack[-1] /= int(num_list.pop())
		return sum(stack)


	def plus_minus_parentheses(self, s1):
		"""
		+ - * / and ()
		:param s1:
		:return:
		"""
		def cal_para(stack):
			res, num = 0, stack.pop()
			if not stack: return num
			op = stack.pop()
			if op == '(': return num
			while stack:
				if op == '+':
					res += num
				elif op == '-':
					res -= num
				num = int(stack.pop())
				op = stack.pop()
				if op == '(':
					return res + num
		pstack = []
		res = 0
		s1 = s1.replace(' ', '')
		for c in s1: