import streamlit as st
import functions as f

st.title("My Todo App")
st.subheader("Application to manage Todo")
st.write("You can manage your daily Todo")
todos = f.read_todo()


def add_todo():
    todo1 = st.session_state["newTodo"] + "\n"
    # print(todo1)
    todos.append(todo1)
    f.write_todo(todos)
    st.session_state["newTodo"] = ""


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Type a todo", key="newTodo", on_change=add_todo)
