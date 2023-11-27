arr = [[1,3,2], [2,5,3], [5,6,2]]

def prob(arr):
    h_map = {}
    task_map = {}
    task_period_map = {}

    for idx, ele in enumerate(arr):
        task_map[idx+1] = []
        task_period_map[idx+1] = ele[2]
        for interval in range(ele[0], ele[1]+1):
            task_map[idx+1].append(interval)
            if interval not in h_map:
                h_map[interval] = []
            h_map[interval].append(idx+1)

    print("h_map: ", h_map)
    print("task_map: ", task_map)
    print("task_period_map: ", task_period_map)
    tasks_order = []

    for idx, ele in enumerate(arr):
        diff = ele[1]+1 - ele[0]
        tasks_order.append([diff*ele[2], idx+1])

    tasks_order.sort()

    real_order = []

    for ele in tasks_order:
        real_order.append(ele[1])

    print("RealOrder: ", real_order)


    final = []
    for each_task in real_order:
        picked_array = []
        # get elements order
        for ele in task_map[each_task]:
            picked_array.append((len(h_map[ele]), ele))

        picked_array.sort(reverse=True)

        pick_eles = []

        for pick in picked_array:
            pick_eles.append(pick[1])

        print(pick_eles)

        if each_task in task_period_map:
            for interval_range in range(task_period_map[each_task]):
                picked_ele = pick_eles[interval_range]
                final.append(picked_ele)
                reserved_tasks = h_map[picked_ele]

                # clear tasks
                for task in reserved_tasks:
                    if task in task_period_map:
                        task_period_map[task] -= 1
                        if task_period_map[task] == 0:
                            task_period_map.pop(task, None)

    print("Final: ", final)
    return len(final)


prob(arr)
