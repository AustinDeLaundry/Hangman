#Made by Austin DeLauney
#Jan. 8, 2015
#Simple hangman game made in Python

import random

class Hangman:
	def __init__(self):
		dic = open("Dictionary.txt", "r")
		word  = self.chooseWord(dic)

	def chooseWord(self, dictionary):
		listofwords = []
		for line in dictionary.readlines():
			listofwords.append(line)
		return listofwords[random.randint(0, len(listofwords))].strip()

	def play(self):
		print("PLAYING!")

if(__name__ == "__main__"):
	playgame = ""
	while(playgame != "y" and playgame != "n"):
		playgame = input("Hello, woud you like to play a game of Hangman? (y/n)")

	if(playgame == "y"):
		game = Hangman()
		game.play()

	else:
		print("Aw :(")

	print("Thanks for playing!")
