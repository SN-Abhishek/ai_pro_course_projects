# Let's start with an empty to-do list
my_tasks = []

print(f"Starting my day with tasks: {my_tasks}")
print(f"Number of tasks to do: {len(my_tasks)}")
print("---") # Just a separator line

# Now, let's add some tasks to our list using .append()
print("Adding some tasks...")
my_tasks.append("Lesson 6.6 - Finish script")
my_tasks.append("Record video")
my_tasks.append("Edit final cut")

print(f"My tasks now: {my_tasks}")
print(f"Number of tasks to do: {len(my_tasks)}")
print("---")

# Let's say I've just finished the first task.
# I can remove it from the list.
print("Completing a task...")
my_tasks.remove("Lesson 6.6 - Finish script")

print(f"My remaining tasks: {my_tasks}")
print(f"Number of tasks left: {len(my_tasks)}")
print("---")

# Finally, let's access and print just the very next task I need to do.
# Since counting starts at 0, the next task is at index 0.
next_task = my_tasks[0]
print(f"My very next task is: {next_task}")

