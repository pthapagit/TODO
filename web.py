import streamlit as st
from modules.functions import Functions

todo_function = Functions()
st.title('_My To-do App_ :heavy_check_mark:')
my_todos = todo_function.read_file()
print(my_todos)


def add_todo():
    todo = st.session_state["new_todo"]
    st.session_state["new_todo"] = ""
    my_todos.append(todo + '\n')
    todo_function.write_file(my_todos)


def delete_todo(to_remove_index):
    my_todos.pop(to_remove_index)
    todo_function.write_file(my_todos)


for index, item in enumerate(my_todos):
    value = st.checkbox(item.strip('\n'), key=item)
    if value:
        delete_todo(index)
        del st.session_state[item]
        st.rerun()

text_input = st.text_input(
    "Enter Your To-do 👇",
    placeholder='Pick up Groceries',
    on_change=add_todo,
    key='new_todo',

)


st.session_state
