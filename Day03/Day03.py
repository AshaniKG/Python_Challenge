myTask = []
add = 1
remove = 2
view = 3
exit = 4
i = 1
step = 1

print ("MAIN MENU:\n  1.Add task\n  2.Remove task\n  3.View task\n  4.Exit\n")

choice = int (input ("What do you want to do (Enter the menu number): "))

while choice != exit:

    if choice == add:
        myTask.append(input (f"{i})")) 
        i += 1

    elif choice == remove:
        i = int (input("Enter the task number you want to remove: "))
        myTask.pop(i-1)

    elif choice == view:
        i = 1
        for x in myTask:
            print(f"{i}){x}")
            i += 1

    choice = int (input ("What do you want to do (Enter the menu number): ")) 