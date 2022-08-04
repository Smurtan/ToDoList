class Viewing:
    indent = ' ' * 4
    with open('todoList.txt', 'r+') as file:
        todolist = list(file.read())
    print('Your business for today:')
    for case in todolist:
        print(f'{indent}case')


class Add(Viewing):
    pass


class Delete(Viewing):
    pass


class Rename(Viewing):
    pass


class Do(Viewing):
    pass
