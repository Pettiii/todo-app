FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """
    Read a text file and return a list of to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local #if no return statement, None will be returned

def write_todos(todos_arg, filepath = FILEPATH): #more like a procedure(modify the file), no return
    #put the non-default parameter(todos_arg) before the default(filepath), otherwise error
    """
    Write the to-do items list in the text file
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())