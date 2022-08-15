class Viewing:
    def __init__(self):
        self.indent = ' ' * 4
        with open('todoList.txt', 'r') as file:
            self.todolist = file.read().split(', ')

    def __str__(self):
        print('Your business for today:')
        for case in self.todolist:
            print(self.indent + case)
        print()


class Add(Viewing):
    pass


class Delete(Viewing):
    pass


class Rename(Viewing):
    pass


class Do(Viewing):
    pass


if __name__ == '__main__':
    user = Viewing()  # A copy of the to-do list
    user.__str__()  # viewing existing tasks
    try:
        while True:  # Program cycle
            user.line = input(
                'Если Вы хотите добавить задачу, введите "+" перед ней \n--> '
            )  # The line in which the user interacts with the program

            try:
                if user.line[0] == '+' or user.line[1] == '+':  # adding a task
                    user.line = user.line.replace('+', '')  # remove the "+" character
                    if user.line[0] == ' ':  # removing the initial space
                        user.line = user.line[1:]
                    user.todolist.append(user.line)  # adding a task to the list
                    print('Вы добавили задачу: %s' % user.line)
            except IndexError:
                pass
    finally:
        with open('todoList.txt', 'w') as file:
            file.write(str(user.todolist)[1:-1].replace("'", ""))
            user.__str__()
