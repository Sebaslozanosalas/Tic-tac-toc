class Player:
    def __init__(self, id, mark):
        self.id = id
        self.mark = mark
        self.win_count = 0
    
    def __str__(self):
        return f'{self.id} ({self.mark})'
    
