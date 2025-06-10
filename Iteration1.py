#get name of task and add to array list of tasks
def add_task():

    #define each task as an object with default status: pending
    task = {
        "name" : input("Enter the task: "),
        "status" : "Pending"
    }
    print("Task \"{0}\" has been added.".format(task.get("name")))
    #add task object to list
    task_list.append(task)

#for length of array, print all task objects
def view_all_task():
    if (task_list == []):
        raise ValueError("List is empty")
    print("All Tasks:")
    for i in range (1,len(task_list)+1):
        reference_task = task_list[i-1]
        print("{0}. {1} - {2}".format(i, reference_task.get("name"), reference_task.get("status")))
&dk 
#remove object from list
def delete_task():
        user_input = input("Task number to delete: ")
        try:
            delete = int(user_input)
        except:
            raise ValueError("Enter a number")

        #check if task number exists, raise error if not
        if (delete <= 0) or (delete > len(task_list)):
            raise ValueError("That task does not exist")
        deleted_task = task_list[delete - 1]
        print("Task {0}: \"{1}\" has been deleted".format(delete, deleted_task.get("name")))
        del task_list[delete-1]

#change status description
def mark_done():

        #obtain task to be editted
        user_input = input("Task number to edit description: ")
        try:
            edit_task = int(user_input)
        except:
            raise ValueError("Enter a number")
        if (edit_task <= 0) or (edit_task > len(task_list)):
            raise ValueError("That task does not exist")

        #obtain new status
        edit_task_status = input("Status of task: ")

        #access correct list item
        reference_task = task_list[edit_task - 1]

        #set new status to object
        reference_task["status"] = edit_task_status
        print("Task {0}: \"{1}\" has been marked {2}".format(edit_task, reference_task.get("name"),reference_task.get("status")))
        

#view list of tasks with specific status
def view_status_task():
        status_choice = input("Which status of tasks would you like to view?: ")

        print("{0} tasks:".format(status_choice))
        task_count = 0
        for i in range (1,len(task_list)+1):
            reference_task = task_list[i-1]

            #print only tasks with specified status
            if (reference_task.get("status") == status_choice):
                print("{0}. {1} - {2}".format(i,reference_task.get("name"),reference_task.get("status")))
                task_count += 1
        #if tasks with that status dont exist, show list empty
        if (task_count == 0):
            print("No tasks with that status")
            
 

print("To-Do List Menu")
print()

#print to-do list options
print(
    "1. Add Task\n"
    "2. View All Tasks\n"
    "3. Delete Task\n"
    "4. Mark Task as Done\n"
    "5. View Done/Pending Tasks\n"
    "6. Exit"
)
#define array for tasks
task_list = []

#repeat questions until option 6(exit)
while True:
    print()

    #try to execute code unless error occurs, then print error
    try:
        user_input = input("Enter your choice (1-6): ")

        #test if input is integer, raise error if not
        try:
            choice = int(user_input)
        except:
            raise ValueError("Enter a number")

        #test in input is in range of available choices, raise error if not
        if (choice <= 0) or (choice > 6):
            raise ValueError("Choose a number 1-6")

        #execute function based on inputted choice
        if (choice == 1): 
            add_task()
    
        elif (choice == 2):
            view_all_task()
            
        elif (choice == 3):
            delete_task()
    
        elif (choice == 4):
            mark_done()
    
        elif (choice == 5):
            view_status_task()
    
        elif(choice == 6):
            print("Thank you")
            break

        #incase of uncaught error
        else:
            print("Invalid choice, please try again.")

    #raise error message if code crashes
    except ValueError as e:
        print("Error: " + str(e))
        
