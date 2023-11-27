import re

boxList = [
	"ykc 82 01",
	"eo first qpx",
	"09z cat hamster",
	"06f 12 25 6", 
	"az0 first qpx", 
	"236 cat dog rabbit snake"
]

my_sortLambdaLst = [lambda x,y:cmp(x[0], y[0]), lambda x,y:cmp(x[1], y[1])]
def multi_attribute_sort(x,y):
    r = 0
    for l in my_sortLambdaLst:
        r = l(x,y)
        if r!=0: return r #keep looping till you see a difference
    return r

def sol(boxList):
	# s.matches(".*[a-zA-Z]+.*")
	new_list = []
	old_list = []


	for token in boxList:
		version = token.split(" ", 1)[1]
		print(version)
		if re.search('[a-zA-Z]', version):
			tup = (version, token)
			old_list.append(tup)
		else:
			new_list.append(token)

	old_list.sort(lambda x,y:multi_attribute_sort(x,y))

	new_old_list = []
	for rec in old_list:
		new_old_list.append(rec[1])

	return new_old_list + new_list

print(sol(boxList))
