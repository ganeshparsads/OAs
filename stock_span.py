
def stock_span(arr):
	result = []

	stack = []

	for idx, i in enumerate(arr):

		while stack and stack[-1][0] > i:
			stack.pop()

		