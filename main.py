def to_do_list():
    tasks = []
    while True:
        print("1. add tasks: ")
        print("2. remove tasks: ")
        print("3. show tasks: ")
        print("4. quit: ")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
        elif choice == "2":
            task = input("Enter your task for remove: ")
            if task in tasks:
                tasks.remove(task)
                print("task removed successfully")
            else:
                print("task not found")
        elif choice == "3":
            print("tasks list: ")
            for task in tasks:
                print("-" + task)
        elif choice == "4":
            print("quit")
            break
to_do_list()
