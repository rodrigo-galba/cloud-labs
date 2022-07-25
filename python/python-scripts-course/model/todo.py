class Todo:

    """
    A task to be done
    """

    statuses = {False: 'Incomplete', True: 'Complete'}

    def __init__(self, name, description, points, completed=False) -> None:
        self.name = name
        self.description = description
        self.points = points
        self.completed = completed

    def __repr__(self) -> str:
        return f"{self.name} ({self.statuses[self.completed]} - {self.points} points): {self.description}"
