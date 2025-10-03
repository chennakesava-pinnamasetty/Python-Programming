task = []

while True:
    print("1. Add task\n")
    print("2.View task")

    choice = input("Enter your task (1-2) :")

    if choice == "1":
     n = input("Enter a new task :")
     task.append(n)
     print(f"{n} task is added")

    elif choice == "2":
     if not task:
       print("no tasks")
     else:
       print("\n your task :")
       for i,t in enumerate(task, start =1):
         print(f"{i}.{t}")

