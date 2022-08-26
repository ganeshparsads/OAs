
from colletions import deque

class Operation:
	def __init__(self, opName, opValue):
		self.opName = opName
		self.opValue = opValue


def Solution(strs):
	n = len(strs)

	stringBuilder = ""

	result = ["" for i in range(n)]

	for idx, cmd in enumerate(strs):
		strArr = cmd.split(" ")
		if len(strArr) == 1:
			if "UNDO" == cmd:
				if stack:
					opName, opValue = stack.pop()
					if opName == "INSERT":
						l = len(opValue)
						size = len(stringBuilder)
						stringBuilder = stringBuilder[:-l]
					elif opName == "BACKSPACE":
						stringBuilder.append(opValue)
		elif cmd == "BACKSPACE":
			if stringBuilder:
				ch = stringBuilder[-1]
				stringBuilder = stringBuilder[:-1]
				stack.push("BACKSPACE", ch)
		else:
			stringBuilder += strArr[1]
			stack.push("INSERT", strArr[1])

		result.append(stringBuilder)

	return result
