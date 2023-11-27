# songs = ["notion:180","voyage:185", "sample:180"]

# animation = ["circles:360", "squares:180", "lines:37"]

songs = ["songone:150", "songtwo:150", "songthree:150", "songfour:150"]

animation = ["first:150", "second:75", "third:10"]

# op = ["squares:1", "lines:5", "sqaures:1"]

formatted_songs = []

for i in songs:
	formatted_songs.append(int(i.split(":")[1]))

formatted_ani = []

for j in animation:
	formatted_ani.append((int(j.split(":")[1]), j.split(":")[0]))

formatted_ani.sort()

final_result = []

for i in formatted_songs:
	result = -1
	result_str = ""
	for j in formatted_ani:
		if i < j[0]:
			break
		elif i == j[0]:
			result = 1
			result_str = j[1]
			break
		elif i >= j[0] and i % j[0] == 0:
			div = i//j[0]
			if div > result:
				result = div
				result_str = j[1]

	final_result.append(result_str + ":" + str(result))

# return final_result
print(final_result)