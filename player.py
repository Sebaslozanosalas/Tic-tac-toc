class Player:
    def __init__(self, id: str, name: str, mark: str):
        self.id = id
        self.name = name
        self.mark = mark
        self.win_count = 0
    
    def __str__(self):
        return self.name