from core.game import Game
from core.gui import GUI


def main(terminal_mode=True):

    if terminal_mode:
        game = Game()
        game.play()
    else:
        gui = GUI()
        gui.run()


if __name__ == "__main__":
    main()