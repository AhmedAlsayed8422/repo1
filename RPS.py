#!/usr/bin/env python3
import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
       self.score=0
       self.my_move = Player.move(self)
       self.their_move = Player.move(self)

    def move(self):
            return moves[0]

    def learn(self, my_move, their_move):
            self.my_move = my_move
            self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        usermove = input("enter rock, paper, or scissors")
        while usermove not in moves:
            print("try again")
            usermove = input("enter rock, paper, or scissors")
        return usermove


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is moves[0]:
            self.my_move = moves[1]
        elif self.my_move is moves[1]:
            self.my_move = moves[2]
        elif self.my_move is moves[2]:
            self.my_move = moves[0]
        return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
                    (one == 'scissors' and two == 'paper') or
                    (one == 'paper' and two == 'rock'))



class RepeaterPlayer(Player):
	def move(self):
		return moves[0]



class Game:
    def __init__(self, p1, p2):
        self.score = 0
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print (f"Player 1: {move1} Player 2: {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print('Player 1 win!')
        elif beats(move2, move1):
            self.p2.score += 1
            print('Player 2 win!')
        else:
            print("It\'s a draw.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(f"""Player 1 (human Won!)
            Final score:Player 1: {self.p1.score} | Player 2 {self.p2.score}
			Game Over.""")
        elif self.p2.score > self.p1.score:
            print(f"""Player 2 (computer won!)
            Final Score: Player 1: {self.p1.score} | Player 2 {self.p2.score}
            Game Over.""")
        else:
            print(f"""It\'s a draw!
            Final Score: Player1 = {self.p1.score} | Player2= {self.p2.score}
            Game Over""")

def start_game():
    if __name__ == '__main__':
        print('Welcome to Rock, Paper, Scissors.')
        playerlist = int(input("enter number random(1),cycler(2), repeater(3), or reflector(4) or press (0) to quit the game"))
        if playerlist == 4:
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game()
        if playerlist == 1:
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
        if playerlist == 2:
            game = Game(HumanPlayer(), CyclePlayer())
            game.play_game()
        if playerlist == 3:
            game = Game(HumanPlayer(), RepeaterPlayer())
            game.play_game()
        if playerlist == 0:            print('thanks for playing.')            exit()
#except Keybord Interrupt:
            game.play_game()

start_game()
