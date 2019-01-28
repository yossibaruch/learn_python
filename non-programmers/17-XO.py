print("""
# Adjectives are classes, Adverbs are methods
# Board
# Players
# Game
""")


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = False

    def play(self):
        while True:
            current_player = self.players[int(self.turn)]

            print(self.board.to_string())
            move = int(input(f'This is the current board, {current_player.name} make a move 0-8.\n'))

            while True:
                try:
                    is_winner = self.board.make_move(current_player, move)
                    break
                except (ValueError, IndexError):
                    move = int(input('Illegal move, please try again.'))
            if is_winner or self.board.is_draw():
                break

            self.turn = not self.turn
        if is_winner:
            print(f'{current_player.name} has won!!!')
        else:
            print("it's a draw!!!")
        print(self.board.to_string())


class Board:
    def __init__(self):
        self.board = [' '] * 9

    def to_string(self):
        return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}'.format(*self.board)

    def make_move(self, player, place):
        if self.board[place] != ' ':
            raise ValueError(f'place {place} is already taken')
        self.board[place] = player.marker
        return self.is_winner(player.marker)

    def is_winner(self, marker):
        winning_position = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        return any([all([self.board[x] == marker for x in pos]) for pos in winning_position])

    def is_draw(self):
        return ' ' not in self.board


class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

Game(Player('yossi', 'X'), Player('baruch', 'O')).play()