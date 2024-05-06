from _datetime import datetime

from modules.functions import Functions

todo_function = Functions()
now = datetime.now()
formatted_date = now.strftime("%B %d, %Y")
print(f'It is {formatted_date}')
while True:
    user_action = input('Type add, show, edit, delete or exit: ')
    user_action = user_action.strip()
    if user_action == 'add':
        todo_function.add_todo()
    elif user_action == 'delete':
        todo_function.delete_todo()
    elif user_action == 'show':
        todo_function.show_todos()
    elif user_action == 'edit':
        todo_function.edit_todo()
    elif user_action == 'exit':
        exit()
    else:
        print('Please type correct action')
