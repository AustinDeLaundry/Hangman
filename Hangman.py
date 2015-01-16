#Made by Austin DeLauney
#Jan. 8, 2015
#Simple hangman game made in Python

import random

class Hangman:
	def __init__(self):
		dic = open("Dictionary.txt", "r")
		self.word  = self.choose_word(dic)
		self.blank_word = "_" * len(self.word)
		self.MAX_INCORRECT = 5
		self.incorrect = 0

	def choose_word(self, dictionary):
		list_of_words = []
		for line in dictionary.readlines():
			list_of_words.append(line)
		return list_of_words[random.randint(0, len(list_of_words))].strip()

	def subsitute_blanks(self, guess):
		guess = guess.lower()
		correct_guess = False
		new_blank = ""
		for i in range(0,len(self.word)):
			if(guess == self.word[i]):
				correct_guess = True
				new_blank += guess
			else:
				new_blank += self.blank_word[i]
		self.blank_word = new_blank
		return correct_guess

	def play(self):
		win = False
		while(not win):
			print(self.blank_word)
			guess = input("Please give me your guess: ")

			if(len(guess) == 1):
				if(self.subsitute_blanks(guess)):
					print("Congrats! You've got a letter!")
				else:
					print("Nope! Try again!")
					self.incorrect += 1

			else:
				if(guess == self.word):
					self.blank_word = self.word
				else:
					print("Nope! Try again!")
					self.incorrect += 1

			if(self.blank_word == self.word):
				print("Congrats! You won!!!")
				win = True

			elif(self.incorrect == self.MAX_INCORRECT):
				print("Sorry! You ran out of guesses! The correct answer was " + self.word)
				win = True
			else:
				print("You have " + str(self.incorrect) + " guesses out of " + str(self.MAX_INCORRECT) + " guesses.")

if(__name__ == "__main__"):
	play_game = ""
	while(play_game != "y" and play_game != "n"):
		play_game = input("Hello, woud you like to play a game of Hangman? (y/n)")

	if(play_game == "y"):
		more = True
		while(more):
			game = Hangman()
			game.play()

			while(more != "y" and more != "n"):
				more = input("Hello, woud you like to play another game of Hangman? (y/n)")

			if(more == "y"):
				more = True
			else:
				more = False



	else:
		print("Aw :(")

	print("Thanks for playing!")
