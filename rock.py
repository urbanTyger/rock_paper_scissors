
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.their_move = random.choice(moves)
        self.my_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class randomPlayer(Player):
    def move(self):
        self.my_move = random.choice(moves)
        print(f"Opponent will play: {self.my_move.upper()}")
        return self.my_move


class reflectPlayer(Player):
    def move(self):
        print(f"Opponent will play: {self.their_move.upper()}")
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class cyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            self.my_move = 'paper'
        elif self.my_move == 'paper':
            self.my_move = 'scissors'
        elif self.my_move == 'scissors':
            self.my_move = 'rock'
        print(f"Opponent will play: {self.my_move.upper()}")
        return self.my_move

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class humanPlayer(Player):
    def move(self):
        x = ""
        while x not in moves:
            print("What would you like to play")
            x = input("  Rock, Paper, or Scissors? > ").lower()
        print(f"You played: {x.upper()}")
        return x


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1wins = 0
        self.p2wins = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if beats(move1, move2):
            self.p1wins += 1
            print("\t§- PLAYER ONE WINS +1 point -§")
        elif beats(move2, move1):
            print("\t§- PLAYER TWO WINS +1 point -§")
            self.p2wins += 1
        else:
            print("\t§- PLAYERS TIE no points -§")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: Player One {self.p1wins},  Player Two {self.p2wins}\n")
        time.sleep(1)

    def announce_winner(self, player1, player2):
        if player1 > player2:
            print(f"Player One has defeated Player Two by {player1-player2}!")
        elif player2 > player1:
            print(f"Player Two has defeated Player One by {player2-player1}!")
        else:
            print("There is no winner due to a TIE!")
        print(f"\nFinal Score:\n")
        print(f"  Player One: {player1}")
        print(f"  Player Two: {player2}\n")
        x = input("Would you like to CONTINUE playing? (yes or?) ").lower()
        if 'yes' in x or x == 'y':
            game.play_game()
        else:
            print("\nGame over!")

    def play_game(self):
        print("Game start!\n")
        games = input("How many rounds of play? (Choose between 3 - 12) ")
        try:
            games = int(games)
        except ValueError:
            games = random.randint(3, 12)
            print(f"Unknown or incorrect imput, you will play {games} rounds")
        if games < 3:
            games = 3
            print("Your choice was too low, you will play 3 rounds")
        elif games > 12:
            games = 12
            print("Your choice was too high, you will play 12 rounds")
        for round in range(games):
            print(f"Round {round+1} ~~")
            self.play_round()
        self.announce_winner(self.p1wins, self.p2wins)


if __name__ == '__main__':
    game = Game(humanPlayer(), randomPlayer())
    game.play_game()
