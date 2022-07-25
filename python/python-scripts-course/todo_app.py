from model.todo import Todo
from model.todo_list import TodoList

def start_app():
    todo1 = Todo('Task 1', 'sample task', 100, True)
    todo2 = Todo('Task 2', 'important task', 10)
    todo3 = Todo('Task 3', 'optional task', 101)

    todo_list = TodoList([todo1, todo2, todo3])
    print(f"Average points: {todo_list.average_points()}")
    print(f"Completed tasks: {todo_list.completed()}")
    print(f"Incomplete tasks: {todo_list.incomplete()}")

if __name__ == '__main__':
    start_app()