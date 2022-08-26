
# schedules = ["12:30", "14:00", "19:55"]

# time = "14:30"

# schedules = ["00:00", "14:00", "19:55"]

# time = "00:00"

schedules = ["12:30", "14:00", "19:55"]

time = "14:00"

converted_times = []

i = 0

for t in schedules:
	temp = t.split(':')
	hr = int(temp[0])
	minu = int(temp[1])

	total = hr*60 + minu

	converted_times.append(total)

target = time.split(':')

target_hr = int(target[0])
target_min = int(target[1])


targetTime = target_hr * 60 + target_min

reqTime = -1

for t in converted_times:
	if t >= targetTime:
		break
	reqTime = t

if reqTime == -1:
	# return -1
	print(-1)
else:
	print(targetTime - reqTime)

