class Player:

    def __init__(self, id):
        self.id = id
        self.get_name()

    def get_name(self):
        self.name = input(f'{self.id} enter your name: ').title()
    
    def get_mark(self):
        user_input = None
        while user_input not in ['X', 'O']:
            user_input = input(f'{self.name}: X or O?\n').upper() 
        self.mark = user_input
        return user_input 

    def __str__(self):
        return f'{self.name} plays {self.mark}'
