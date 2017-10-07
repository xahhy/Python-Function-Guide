class Animal:
    weight = 10

    def __init__(self, weight:int):
        self.weight = 100

    def __int__(self):
        return str(self.weight)
