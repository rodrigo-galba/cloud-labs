class TodoList:
    def __init__(self, todos) -> None:
        self.todos = todos

    def average_points(self):
        total = 0
        for todo in self.todos:
            total += todo.points
        return total / len(self.todos)

    def completed(self):
        # doctest and other methods omitted

        results = []
        for todo in self.todos:
            if todo.completed:
                results.append(todo)
        return results

    def incomplete(self):
        results = []
        for todo in self.todos:
            if not todo.completed:
                results.append(todo)
        return results
