class Functions:
    FILEPATH = 'todo.txt'

    def read_file(self):
        """function to read a file and return contents"""
        try:
            with open(self.FILEPATH) as todo_file:
                contents = todo_file.readlines()
                return contents
        except FileNotFoundError:
            print("Couldn't find file")

    def write_file(self, todo):
        """Function to write a file and doesn't return anything"""
        try:
            with open(self.FILEPATH, 'w') as todo_file:
                todo_file.writelines(todo)
        except FileNotFoundError:
            print("Couldn't find file")

    def add_todo(self, new_todo):
        """A single to-do item is added to a file"""
        contents = self.read_file()
        new_todo = input('Enter a todo: ') + '\n'
        contents.append(new_todo)
        self.write_file(contents)

    def show_todos(self):
        contents = self.read_file()
        for index, item in enumerate(contents):
            item = item.strip('\n')
            print(f'{index + 1}-{item}')

    def edit_todo(self):
        self.show_todos()
        try:
            todo_num = input('please type in number of the todo: ')
            todo_num = int(todo_num) - 1
            contents = self.read_file()

            contents[todo_num] = ''

            new_todo = input('Type in new todo: ') + '\n'
            contents[todo_num] = new_todo

            self.write_file(contents)
        except IndexError:
            print('Please select number corresponds to todos')

    def delete_todo(self):
        self.show_todos()
        try:
            contents = self.read_file()
            user_selection = input('please type in number of the todo: ')
            user_selection = int(user_selection) - 1
            removed_todo = contents.pop(user_selection).strip('\n')
            print(f'"{removed_todo}" was removed from the todo list ')
            self.write_file(contents)
        except IndexError:
            print('Please select number corresponds to todos')
