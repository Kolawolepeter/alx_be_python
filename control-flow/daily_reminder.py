# Prompt the user to input a task description and save it into a task variable
task = input("Enter your task: ")

# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes or no) and save it into a time_bound variable
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(f"Reminder: {reminder}")
