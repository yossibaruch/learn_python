print("""
# Adjectives are classes, Adverbs are methods
# Board, to_string as Adverbs 
# Players, have name and marker as Adjectives
# Game
""")


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [Player(player1, "X"), Player(player2, "Y")]
        self.turn = False

    def play(self):
        while True:
            current_player = self.players[int(self.turn)]
            self.turn = not self.turn
            print(self.board.to_string)
            move = int(input(f'Please write down your move player {current_player.name}:'))
            print(move)
            is_winner = self.board.make_move(current_player, move)
            if is_winner:
                print(f'We have a winner, {current_player.name} has won!!!')
            empty_spaces = [i for i, val in enumerate(self.board.board) if val == ' ']
            if not empty_spaces:
                print("No one has won, fuck off!!!")
                break


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
        while self.board[place] != ' ':
            place = int(input(f'Place {place} not empty, please select another:'))
        print(player.name, player.marker, place)
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


game = Game("yossi", "shoshy")
game.play()
