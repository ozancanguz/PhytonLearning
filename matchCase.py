todos=[]
while True:

    userAction=input("Type add or show: ")
    match userAction:
        case 'add':
            todo=input("Enter your todo: ")
            todos.append(todo)
        case 'show':
            for i in todos:
                print(i)
        case 'exit':
            break