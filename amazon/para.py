from collections import deque

texts = [
	["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and align", "to center"]
]

width = 16

start = '*' * width

end = '*' * width

stringBuilder = ""

stringBuilder = start + "\n"

for portion  in texts:
	newString = ""
	for idx, j in enumerate(portion):
		if idx <= 





		if len(newString + j) <= width:
			newString += 
		else:
			# justify
			# even
			len_new = len(newString)
			delta = (width - len_new)
			if delta % 2 == 0:
				len_new = delta/2
				for i in range(len_new):
					newString.append(" ")
					newString.apendleft(" ")
			else:
				len_new = delta // 2

				for i in range(len_new):
					newString.append(" ")
					newString.apendleft(" ")
				newString.append(" ")

		newString.append("*")
		stringBuilder.append("".join(newString))

			# secondString = j
			# second = deque()

			# len_new = len(secondString)
			# delta = (width - len_new)
			# if delta % 2 == 0:
			# 	len_new = delta/2
			# 	for i in range(len_new):
			# 		second.append(" ")
			# 		second.apendleft(" ")
			# else:
			# 	len_new = delta // 2

			# 	for i in range(len_new):
			# 		second.append(" ")
			# 		second.apendleft(" ")
			# 	newString.append(" ")

print(stringBuilder)
