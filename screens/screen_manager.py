class ScreenManager:

    def __init__(self):
        self.screens = {}
        self.current_screen = None


    def add_screen(self, name, screen):
        self.screens[name] = screen


    def set_screen(self, name):
        self.current_screen = self.screens.get(name)


    def handle_events(self, event):
        if self.current_screen:
            self.current_screen.handle_events(event)


    def update(self):
        if self.current_screen:
            self.current_screen.update()


    def draw(self, surface):
        if self.current_screen:
            self.current_screen.draw(surface)

