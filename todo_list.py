tasks=[]

def to_do_list():
    while True:
        print("/n To-Do List")
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Exit")

        choice=input("Enter a Choice to perform(1/2/3/4)")
        if choice == "1":
            task=input("Enter a Task: ")
            tasks.append(task)
            print("Task Added")
        elif choice == "2":
            if tasks:
                print("Tasks:")
                for i in enumerate(tasks,1):
                    print(f"{i}")
            else:
                print("No Tasks!")
        elif choice == "3":
            if tasks:
                for i in enumerate(tasks,1):
                    print(f"{i}")
                task_num=int(input("Enter task number to remove:"))
                if 1 <= task_num <= len(tasks):
                    tasks.pop(task_num-1)
                    print("Task Removed....")
                else:
                    print("Invalid task")
            else:
                print("No Task To Remove!")
        elif choice == "4":
            break
        else:
            print("Invalid Choice")
to_do_list()




