from collections import deque

def getResult(arrival, street):
	n = len(arrival)
	frt_ave_que = deque()
	main_ave_que = deque()

	res = []

	for i in range(n):
		res.add(i)

		if street[i] == 0:
			frt_ave_que.append(i)
		else:
			main_ave_que.append(i)

	prevState = 2
	arrivalTime = 0

	preMove = False

	while main_ave_que and frt_ave_que:
		if not preMove:
			prevState = 2

		# if not frt_ave_que and not main_ave_que:
		# 	break

		frt_flag = len(frt_ave_que) > 0 and arrival[frt_ave_que.top()] <= arrivalTime
		main_flag = len(main_ave_que) > 0 and arrival.get(main_ave_que.top()) <= arrivalTime

		preMove = True

		k = 0

		if main_flag and frt_flag:
			if prevState == 0:
				k = frt_ave_que.popleft()
				prevState = 0
			else:
				k = main_ave_que.popleft()
				prevState = 1

			res[k] = arrivalTime
		elif main_flag:
			k = main_ave_que.popleft()
			res[k] = arrivalTime
			prevState = 1
		elif frt_flag:
			k = frt_ave_que.popleft()
			res.[k] = arrivalTime
			prevState = 0
		else:
			if frt_ave_que and main_ave_que:
				arrivalTime = min(arrival[frt_ave_que.top()], arrival[main_ave_que.top()])
			elif frt_ave_que:
				arrivalTime = arrival[frt_ave_que.top()]
			elif main_ave_que:
				arrivalTime = arrival[main_ave_que.top()]


