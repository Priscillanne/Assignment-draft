# Iteration 2: Continuation of Iteration 1 with new features
# New features: Due dates, Priority levels, and Categories

import datetime

def add_task():
    task_name = input("Enter the task: ")

    # Validate due date format
    while True:
        due_date = input("Enter the due date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Incorrect date format. Please enter as YYYY-MM-DD.")

    # Validate priority input
    while True:
        priority = input("Enter the priority (High/Medium/Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Invalid priority. Please enter High, Medium, or Low.")

    category = input("Enter the category (e.g., School, Work, Personal): ")

    task = {
        "name": task_name,
        "status": "Pending",
        "due_date": due_date,
        "priority": priority,
        "category": category
    }
    print(f'Task "{task.get("name")}" has been added.')
    task_list.append(task)


def view_all_task():
    if not task_list:
        raise ValueError("List is empty")
    print("All Tasks:")
    for i, reference_task in enumerate(task_list, start=1):
        print(f"{i}. {reference_task['name']} - {reference_task['status']} | Due: {reference_task['due_date']} | Priority: {reference_task['priority']} | Category: {reference_task['category']}")


def delete_task():
    user_input = input("Task number to delete: ")
    try:
        delete = int(user_input)
    except:
        raise ValueError("Enter a number")

    if delete <= 0 or delete > len(task_list):
        raise ValueError("That task does not exist")
    deleted_task = task_list[delete - 1]
    print(f'Task {delete}: "{deleted_task.get("name")}" has been deleted')
    del task_list[delete - 1]


def mark_done():
    user_input = input("Task number to edit status: ")
    try:
        edit_task = int(user_input)
    except:
        raise ValueError("Enter a number")
    if edit_task <= 0 or edit_task > len(task_list):
        raise ValueError("That task does not exist")

    edit_task_status = input("Status of task: ")
    reference_task = task_list[edit_task - 1]
    reference_task["status"] = edit_task_status
    print(f'Task {edit_task}: "{reference_task.get("name")}" has been marked {reference_task.get("status")}')


def view_status_task():
    status_choice = input("Which status of tasks would you like to view?: ")
    print(f"{status_choice} tasks:")
    task_count = 0
    for i, reference_task in enumerate(task_list, start=1):
        if reference_task.get("status") == status_choice:
            print(f"{i}. {reference_task['name']} - {reference_task['status']} | Due: {reference_task['due_date']} | Priority: {reference_task['priority']} | Category: {reference_task['category']}")
            task_count += 1
    if task_count == 0:
        print("No tasks with that status")
