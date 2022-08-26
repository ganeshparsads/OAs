
def solution(stationA, stationB, stationC, origin, dest):
	routeMap = {}

	for i in stationA:
		if i not in routeMap:
			routeMap[i] = "A"

	for i in stationB:
		if i not in routeMap:
			routeMap[i] = "B"

	for i in stationC:
		if i not in routeMap:
			routeMap[i] = "C"

	if origin not in routeMap or dest not in routeMap:
		return ""

	print(routeMap[origin], routeMap[dest])

	# import pdb
	# pdb.set_trace()

	if (routeMap[origin] == "A" and routeMap[dest] == "B") or (routeMap[origin] == "B" and routeMap[dest] == "A"):
		return "AB"

	if (routeMap[origin] == "A" and routeMap[dest] == "A") or (routeMap[origin] == "B" and routeMap[dest] == "B"):
		return "AB"

	if (routeMap[origin] == "B" and routeMap[dest] == "C") or (routeMap[origin] == "C" and routeMap[dest] == "B"):
		return "BC"

	if (routeMap[origin] == "C" and routeMap[dest] == "C"):
		return "BC"

	if (routeMap[origin] == "A" and routeMap[dest] == "C") or (routeMap[origin] == "C" and routeMap[dest] == "A"):
		return "ABC"

	return ""


stationA = ["Green Park", "Holdborn"]
stationB = ["Mile End", "Bow Road"]
stationC = ["Forest Hill", "Balham"]

# origin = "Forest Hill"

# dest = "Green Park"

origin = "Forest Hill1"

dest = "Green Park"

print(solution(stationA, stationB, stationC, origin, dest))
