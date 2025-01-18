import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do: ") #create a label
input_box = sg.InputText(tooltip = "Enter todo: ")
add_button = sg.Button("Add")

window = sg.Window("My to-do App", layout = [[label], [input_box, add_button]]) #layout is a list
# if change to layout = [[label, input_box]], the input will be on the same line
window.read()
window.close()
