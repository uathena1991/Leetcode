"""
Leetcode 224: Basic calculator and others (several conditions)

"""


class Solution():


	def next_num(self, s, idx):
		res = ''
		while idx < len(s) and s[idx] not in ['+', '-', '*', '/', '(', ')', '[', ']', '{', '}']:
			res += s[idx]
			idx += 1
		return (res, idx)

	def basic_calculator_pm(self, s):
		"""
		only contains plus and minus
		"""
		s = list(s.replace(' ', '')[::-1])
		res, sign, num = 0, 1, ''
		while len(s) > 0:
			cc = s.pop()
			if cc == '+' or cc == '-':
				sign = 1 if cc == '+' else -1
			else:
				num += cc
				while len(s) > 0:
					cc = s.pop()
					if cc not in ['+', '-']:
						num += cc
					else:
						s.append(cc)
						break
				res += sign * int(num)
				num = ''
		# print("num: %s, cc: %s, res: %d" %(num, cc, res))
		return res

	def calculate_pm_par(self, s):
		"""
		include: + - ( )
		:type s: str
		:rtype: int
		"""

		def cal_recursive(s):
			res = 0
			num_s = ''
			sign = 1
			while len(s) > 0:
				char = s.pop()
				if char in ['+', '-', '(', ')']:
					if char in ['+', '-']:
						sign = 1 if char == '+' else -1
					elif char == '(':
						res += sign * cal_recursive(s)
					else:
						return res
				else:
					num_s += char
					while len(s) > 0:
						char = s.pop()
						if char not in ['+', '-', '(', ')']:
							num_s += char
						else:
							s.append(char)
							break
					res += sign * int(num_s)
					num_s = ''
			return res

		l = list(s.replace(" ", "")[::-1])
		return cal_recursive(l)

	def calculate_pmmd(self, s):
		"""
		include + - * /
		The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
		The integer division should truncate toward zero.

		:param s:
		:return:
		"""
		s = s.replace(' ', '')
		num, idx  = self.next_num(s, 0)
		stack= [int(num)]
		while idx < len(s):
			char = s[idx]
			num, idx = self.next_num(s, idx+1)
			if char == '+':
				stack.append(int(num))
			elif char == '-':
				stack.append(int(num)*(-1))
			elif char == "*":
				stack[-1] *= int(num)
			elif char == '/':
				stack[-1] = int(stack[-1]/int(num))
			else:
				raise Exception('ERROR!!%s %d' %(char, int(num)))

		return sum(stack)

	def calculate_pmmd_par_stack(self, s):
		"""
		The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces .
		The integer division should truncate toward zero.

		+ -, * /: calculate_pmmd
		(): recursive (as calculate_pm_par)
		:param s:
		:return:
		"""
		def find_parathesis(s, start_idx):
			end_idx = start_idx + 1
			count = 1
			while end_idx < len(s):
				if s[end_idx] == '(':
					count += 1
				elif s[end_idx] == ')':
					count -= 1
				end_idx += 1
				if count == 0:
					return end_idx
			return -1

		s = s.replace(" ", "")

		stack, idx, num, sign = [], 0, 0, "+"
		# num, idx = self.next_num(s, 0)
		# stack.append(num)
		s = s.replace(" ", "")
		while idx < len(s):
			curr = s[idx]
			if curr.isdigit():
				num = num * 10 + int(curr)
			if curr == '(': # recursion
				# find right ")"
				new_idx2 = find_parathesis(s, idx)
				num = self.calculate_pmmd_par_stack(s[idx+1:new_idx2-1])
				idx = new_idx2
			if idx == len(s) - 1 or curr in ["+", "-", "*", "/"]:
				if sign == '+':
					stack.append(num)
				elif sign == '-':
					stack.append(-1 * num)
				elif sign == '*':
					stack[-1] = stack[-1] * num
				elif sign == '/':
					stack[-1] = int(stack[-1] / num)
				num = 0
				sign = curr
			idx += 1


		return sum(stack)

	def calculate_pmmd_par_nostack(self, s):
		"""
		The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces .
		The integer division should truncate toward zero.

		+ -, * /: calculate_pmmd
		(): recursive (as calculate_pm_par)
		:param s:
		:return:
		"""
		ll = s.replace(" ", "")
		res, curr_res, idx, num = 0, 0, 0, 0
		while idx < len(ll):
			char = ll[idx]
			if char.isdigit():
				num = num*10 + int(char)
			elif char == '(':
				count = 1
				old_idx = idx
				while idx < len(ll):
					idx += 1
					if ll[idx] == '(':
						count += 1
					if ll[idx] == ')':
						count -= 1
					if count == 0:
						break
				num = self.calculate_pmmd_par_nostack(s[old_idx+1:idx-1])
			elif char == '+':
				curr_res += num
			elif char == '-':
				curr_res -= num
			elif char == '*':
				curr_res *= num
			elif char == '/':
				curr_res = int(res/num)
			if char == '+' or char == '-' or idx == len(ll) - 1:
				res += curr_res




		return res

	def calculate_pm_par_var(self, s, str_map):
		"""
		with expression, and + , -, (, )
		:param s:
		:return:
		"""
		s = s.replace(" ", "")
		for x in str_map:
			simple_s = s.replace(x, str_map[x])
		stack, num, sum, sign, idx, new_str = [], 0, 0, 1, 0, ''
		while idx < len(simple_s):
			char = simple_s[idx]
			if char.isdigit():
				num = num*10 + int(char)
				idx += 1
			elif char == '+' or char == '-':
				sum += num * sign
				sign = 1 if char == '+' else -1
				num = 0
				idx += 1
			elif char not in "()*/+-0123456789":
				if sign == 1:
					new_str += '+'
				if sign == -1:
					new_str += '-'
				while idx < len(simple_s) and char not in "()*/+-0123456789":
					new_str += char
					idx += 1
					char = simple_s[idx]
			elif char in '()':
				if char == '(':
					stack.append((sum, sign, new_str))
					sum, sign, new_str = 0, 1, ''
					idx += 1
				elif char == ')':
					prev = stack.pop()
					sum += sign*num
					t = prev[0] * prev[1]
					num = 0
					sum = prev[0] + t





# s1 = '3+4-5+6-8 +12'
# print(Solution().basic_calculator_pm(s1))
#
# s2 = '2 - (3 + ((1+2)  - (4- (3-5)))) - (4 - 10)'
s2 = '2+((8+2)+(3-999))'
# # s = "2147483647"
print(Solution().calculate_pm_par(s2))

# s3 = "3+2/4"

# print(s3, "\n", Solution().calculate_pmmd(s3))

s4 = "(2+6* 3+5- (3*14/7+2)*5)+3"
s4 = "5- (3*14/7+2)*5"
print(s4, "\n", Solution().calculate_pmmd_par_stack(s4))


