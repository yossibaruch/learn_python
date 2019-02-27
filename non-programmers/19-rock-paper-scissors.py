print("""
1. rock > paper > scissors > rock
2. best of 1 (original) - 5 (max)
    * we ask this after first game won
    * we don't ask this at start
3. classes?
""")


class Player:
    def __init__(self, name):
        self.name = name
        self.play = ''


class Game:
    def __init__(self, player1, player2):
        self.players = [Player(player1), Player(player2)]
        self.playing = False
        self.turns = 1
        self.extended = False
        self.winning = [0, 0]
        self.to_win = 1

    def add_turns(self):
        X = int(input("Please enter a number, 2-5 for extra turns, anything else to quit:"))
        if X in range(2, 5):
            self.turns = X
            self.to_win = round(X/2)
            self.extended = True
            return True
        else:
            print("Don't want to add more turns, that's OK. Bye...")
            return False

    def select_winner(self, playerL, playerR):
        print([playerL.play, playerR.play])
        winning_left = [["r", "p"], ["p", "s"], ["s", "r"]]
        winning_right = [["p", "r"], ["s", "p"], ["r", "s"]]
        print(self.to_win, self.winning)
        if [playerL.play, playerR.play] in winning_left:
            self.winning = [self.winning[0]+1, self.winning[1]]
            if self.winning[0] == self.to_win:
                return "LEFT"
            else:
                return "left"
        if [playerL.play, playerR.play] in winning_right:
            self.winning = [self.winning[0], self.winning[1]+1]
            if self.winning[1] == self.to_win:
                return "RIGHT"
            else:
                return "right"
        return

    def play(self):
        while True:
            current_player = self.players[int(self.playing)]
            current_player.play = input(f'{current_player.name} please write r[ock], p[aper], s[cissors]')
            self.playing = not self.playing
            next_player = self.players[int(self.playing)]
            next_player.play = input(f'{next_player.name} please write r[ock], p[aper], s[cissors]')
            self.playing = not self.playing
            who_won = self.select_winner(current_player, next_player)
            if who_won == "left":
                continue
            if who_won == "right":
                continue
            if who_won == "LEFT":
                print(f'{current_player.name} has won the game, {self.winning[0]}:{self.winning[1]}')
                if not self.extended:
                    if self.add_turns():
                        continue
                break
            if who_won == "RIGHT" and not self.extended:
                print(f'{next_player.name} has won the game, {self.winning[0]}:{self.winning[1]}')
                if not self.extended:
                    if self.add_turns():
                        continue
                break


game = Game("Yossi", "Shoshy")
game.play()
