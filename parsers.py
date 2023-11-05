import streamlit as st
import functions

tasklist = functions.get_tasklist()
def add_newtask():
    newtask = st.session_state['key1'] + '\n'
    tasklist.append(newtask)
    functions.write_tasklist(tasklist)

st.title('My To-Do App')
st.subheader("My Tasklist")

for x, y in enumerate(tasklist):
    checkbox = st.checkbox(y, key=y)
    if checkbox:
        tasklist.pop(x)
        functions.write_tasklist(tasklist)
        del st.session_state[y]
        st.rerun()

st.text('Checkmark your completed tasks to remove.')

st.text_input(label='', placeholder='Add a new task...',
              on_change=add_newtask, key='key1')


print('hello')
