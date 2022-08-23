class ToDoList:
    def __init__(self):
        self.indent = ' ' * 4  # setting up the indentation
        self.gap = None  # to store the last deleted task
        self.index = None  # to store the number of the last deleted task
        with open('todoList.txt', 'r') as f:  # opening the file for reading
            self.todolist = f.read().split(', ')  # reading the contents into the list

    def __str__(self):
        print('--' * 70)  # separator
        print('Your business:')
        for index in range(len(self.todolist)):  # through the indexes of the list we output
            print('%s %i) %s' % (self.indent, index + 1, self.todolist[index]))  # the corresponding task and its number
        print('--' * 70)  # separator

    def add(self, other):
        other = other.replace('+', '')  # remove the "+" character
        if other[0] == ' ':  # removing the initial space
            other = other[1:]
        self.todolist.append(other)  # adding a task to the list
        print('Task "%s" successfully added.' % other)  # the line about the execution of the action

    def remove(self, index):
        self.index = int(index.replace('-', '').replace(' ', ''))  # getting rid of extra characters
        self.gap = self.todolist.pop(self.index - 1)  # memorizing a deleted task
        print('Task "%s" has been successfully deleted.' % self.gap)  # the line about the execution of the action
        print('To cancel the deletion, enter "с"(cancel).')

    def cancel(self):
        self.todolist.insert(self.index - 1, self.gap)
        print('Action canceled.')


if __name__ == '__main__':
    print('Instruction manual:\n'
          '- To add a task to the to-do list, type "+" before the task name.\n'
          '- If you want to delete a task, enter "-" indicating the number of the task you want to get rid of.\n'
          '- To see the entire task list, type "w"(watch).\n'
          '- To exit, enter "e"(exit).')
    user = ToDoList()  # A copy of the to-do list
    user.__str__()  # viewing existing tasks
    try:
        while True:  # Program cycle
            user.line = input('What do you want to do? --> ')  # The line in which the user interacts with the program

            try:
                if user.line[0] == '+':  # adding a task
                    user.add(user.line)

                elif user.line[0] == '-':  # deleting a task
                    user.remove(user.line)

                elif user.line[0] == 'w':  # view the to-do list
                    user.__str__()

                elif user.line[0] == 'e':  # exiting the application
                    raise KeyboardInterrupt

                elif user.line[0] == 'c':  # returning the last deleted task
                    user.cancel()

                elif user.line[0] == ' ':  # if there is an extra space at the beginning
                    print('Please remove the extra space at the beginning, and try again:')
            except IndexError:
                print('No action were specified.\n')
            except KeyboardInterrupt:
                print('Exiting the program...')
                break
    finally:
        print('Saving data...')
        with open('todoList.txt', 'w') as file:  # If for some reason the program was closed, then before exiting
            file.write(str(user.todolist)[1:-1].replace("'", ""))  # the entire file is overwritten with a line
        print('Changes saved.\n'
              'Star action! Good luck!')
