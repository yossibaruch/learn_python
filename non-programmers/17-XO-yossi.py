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

    def make_move(self, player, place):
        self.board[place] = player.marker
        return self.is_winner(player.marker)

    def is_winner(self, marker):
        print(marker)
        winning_sets = [
            {0, 1, 2},
            {3, 4, 5},
            {6, 7, 8},
            {0, 3, 6},
            {1, 4, 7},
            {2, 5, 8},
            {0, 4, 8},
            {2, 4, 6}
        ]
        state = [i for i, val in enumerate(self.board) if val == marker]
        self.to_string()
        for i in winning_sets:
            if i.issubset(state):
                print(f'Player with {marker} has won')
                print(state)
                return True
        return False


yossi = Player("yossi", "X")
shoshy = Player("shoshy", "Y")
board = Board()
print(board.to_string())

board.make_move(yossi, 0)
board.make_move(shoshy, 1)
board.make_move(yossi, 3)
board.make_move(shoshy, 4)
board.make_move(yossi, 5)
board.make_move(shoshy, 2)
board.make_move(yossi, 6)
board.make_move(shoshy, 7)
board.make_move(yossi, 8)

