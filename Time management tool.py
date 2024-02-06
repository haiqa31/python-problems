tasks = ["coding", "reading", "exercise"]
durations = [2, 1, 0.5]  

total_time_per_task = {task: duration for task, duration in zip(tasks, durations)}
print("Total time spent on each task:")
for task, duration in total_time_per_task.items():
    print(task, duration, "hours")

max_time_task = max(total_time_per_task.values())
improvement_areas = [task for task, duration in total_time_per_task.items() if duration < max_time_task and task != "coding"]
print("Areas for improvement (to maximize coding time):")
for area in improvement_areas:
    print(area)