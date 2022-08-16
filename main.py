class Viewing:
    def __init__(self):
        self.indent = ' ' * 4  # setting up the indentation
        with open('todoList.txt', 'r') as f:  # opening the file for reading
            self.todolist = f.read().split(', ')  # reading the contents into the list

    def __str__(self):
        print('--' * 70)  # separator
        print('Your business for today:')
        for index in range(len(self.todolist)):  # through the indexes of the list we output
            print('%s %i) %s' % (self.indent, index + 1, self.todolist[index]))  # the corresponding task and its number
        print('--' * 70)  # separator

    def add(self, other):
        other = other.replace('+', '')  # remove the "+" character
        if other[0] == ' ':  # removing the initial space
            other = other[1:]
        self.todolist.append(other)  # adding a task to the list
        print('Задача "%s" успешно добавлена.' % other)  # the line about the execution of the action

    def remove(self, index):
        index = index.replace('-', '').replace(' ', '')  # getting rid of extra characters
        gap = self.todolist.pop(int(index) - 1)  # memorizing a deleted task
        print('Задача "%s" успешно удалена.' % gap)  # the line about the execution of the action


if __name__ == '__main__':
    print('Инструкция:\n'
          'Чтобы добавить задачу в список дел, введите "+" перед названием задачи.\n'
          'Если вы хотите удалить задачу, введите "-" с указанием номера задачи, от которой необходимо избавиться.\n'
          'Чтобы увидеть весь список задач введите "w"(watch).\n'
          'Для выхода введите "e"(exit).')
    user = Viewing()  # A copy of the to-do list
    user.__str__()  # viewing existing tasks
    try:
        while True:  # Program cycle
            user.line = input('Что Вы хотите сделать? --> ')  # The line in which the user interacts with the program

            try:
                if user.line[0] == '+':  # adding a task
                    user.add(user.line)

                elif user.line[0] == '-':  # deleting a task
                    user.remove(user.line)

                elif user.line[0] == 'w':  # view the to-do list
                    user.__str__()

                elif user.line[0] == 'e':  # exiting the application
                    user.__str__()

                elif user.line[0] == ' ':  # if there is an extra space at the beginning
                    print('Пожалуйста, уберите лишний пробел в начале, и попробуйте снова:')
            except IndexError:
                print('Небыло указано никаких действий.\n')
    finally:
        with open('todoList.txt', 'w') as file:  # If for some reason the program was closed, then before exiting
            file.write(str(user.todolist)[1:-1].replace("'", ""))  # the entire file is overwritten with a line
