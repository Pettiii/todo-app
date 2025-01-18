#todos = [] not the reality, you don't know what you want

#from functions import get_todos, write_todos --> get_todos()
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() #.strip() make "add " == "add", removes the white space

    #match can only check if one value is equal to another but faster, if-else conditionals check more complex conditions (<=>)
    if user_action.startswith("add") or user_action.startswith("new") or user_action.startswith("more"): #changed from match to if with in user_action, select lines and shift+tab to move forward indent
        #todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:] #start after add

        #use the with function below is better, don't need to close the file
        #file = open("todos.txt", "r") #read first, make sure the user inputs are stored
        #todos = file.readlines() #readlines() gives a list, read() gives a single str
        #after file.read(), cursor is at the end of the file, if read again, blank space will be shown
        #list is created here
        #file.close()

        #with open("todos.txt", "r") as file: #by default it's r mode(can neglect r), but w has to be written
            #todos = file.readlines()
        todos = functions.get_todos() #global value

        todos.append(todo + "\n") #a list

        #file = open("todos.txt", "w") #w-write r-read/print things out
        #file.writelines(todos)

        #with open("todos.txt", "w") as file:
            #todos = file.writelines(todos)
        functions.write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("display"): #use | for or in match (match "add" | "display":)
        #file = open("todos.txt", "r")
        #todos = file.readlines()
        #file.close()

        todos = functions.get_todos()

        new_todos = [] #another way: new_todos = [item.strip("\n") for item in todos] (no need to declare this new empty list)

        for item in todos:
            new_item = item.strip("\n") #remove the \n in printing todos list
            new_todos.append(new_item)
        #print(new_todos)

        for index, item in enumerate(todos):
            item = item.strip() #remove the \n in show, simpler than the above two ways
            row = f"{index + 1}-{item}" #f-string
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) #user input number is a str type, convert to int
            print(number)
            number = number - 1 #matches the actual number sequence

            todos = functions.get_todos()
            print("Here is todos existing:", todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n" #str is immutable, no item assignment
            print("Here is how it will be:", todos)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is invalid.")
            #user_action = input("Type add, show, edit, complete or exit: ") repeat codes are not optimise
            #user_action = user_action.strip()
            continue #ignore everything underneath, go back to the start of the while loop

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n") #remove the break line
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There's no item with this number.")
            continue

    elif "exit" in user_action:
        break

    else:
        print("Command invalid.")

    #don't need to define the variable whatever, use a string is ok as well
    #case whatever:
        #print("You entered an unknown command.")

print("Bye!")
