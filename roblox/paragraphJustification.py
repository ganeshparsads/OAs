

para = [
	["hello", "world"],
	["how", "areYou", "doing"],
	["Please look", "and align", "to center"]
]

width = 16

final_result = []

def justify_word(sentence, width):
	n = width - len(sentence)

	# spaces are equal
	if n%2 == 0:
		lSpace = n//2
		rSpace = lSpace
	else:
		lSpace = n//2
		rSpace = lSpace + 1

	sentence = " "*lSpace + sentence + " "*rSpace

	return sentence


for each in para:
	temp_result = ""
	for word in each:
		if len(temp_result) + len(word) <= width-1:
			temp_result = temp_result + " " + word
		else:
			temp_result = justify_word(temp_result, width)
			final_result.append(temp_result)
			temp_result = word

	temp_result = justify_word(temp_result, width)
	final_result.append(temp_result)

print(final_result)
