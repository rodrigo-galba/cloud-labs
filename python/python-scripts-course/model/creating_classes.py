class Car:
    """
    Docstring for this class
    """

    def __init__(self, engine, tires) -> None:
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires.")
    
    def f(self):
        return 'car class'
