import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do: ") #create a label
input_box = sg.InputText(tooltip = "Enter todo", key = "todo")
add_button = sg.Button("Add")

window = sg.Window("My to-do App",
                   layout = [[label], [input_box, add_button]], #layout is a list, but if only one [] --> error
                   font = ("Helvetica", 16)) #tuple
# if change layout to = [[label, input_box]], the input will be on the same line --> one [] is one line, each row has to be its own list

while True:
    event, values = window.read() #can assign multiple variables to a list/tuple
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break
window.close()
