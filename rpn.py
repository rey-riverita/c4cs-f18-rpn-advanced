#!/usr/bin/env python3
import operator
import colored 

op = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.floordiv,
	'^': operator.pow
	}

def calculate(arg):
	# stack for calculator
	stack = arg.split()

	# process tokens
	while len(stack) > 1:
		token = stack.pop()
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			val2 = int(stack.pop())
			val1 = int(stack.pop())
			# Look up function in table
			func = op[token]
			result = func(val1, val2)

			stack.append(str(result))
	return int(stack[0])

def main():
	while True:
		result = calculate(input('rpn calc> ')) 
		print('%s%s ' + str(result) + ' %s' % (colored.fg('white'), colored.bg('yellow'), colored.attr('reset')))


if __name__ == '__main__':
	main()