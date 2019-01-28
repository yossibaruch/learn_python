print("""
# Adjectives are classes, Adverbs are methods
# Board, to_string as Adverbs 
# Players, have name and marker as Adjectives
# Game
""")


class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker


class Board:
    def __init__(self):
        # self.board = [str(_) + str(__) for _ in range(0, 3) for __ in range(0, 3)]
        self.board = [" " for _ in range(0, 3) for __ in range(0, 3)]

    def to_string(self):
        print("{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n".format(*self.board))


yossi = Player("yossi", "X")
board = Board()
print(board.to_string())
