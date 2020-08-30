import random

with open("word_list.txt") as f:
	word_list = f.read().splitlines()

word_list = [x for x in word_list if len(x)>6]

def get_word():
	word = random.choice(word_list)
	return word.upper()


def play(word):
	word_completion = "_" * len(word)
	guessed = False
	guessed_letters = []
	guessed_words = []
	tries = 6

	name = input("What is your name?\n")
	print("Let's play hangman!")
	print(display_hangman(tries))
	print(word_completion)
	print("\n")
	while not guessed and tries > 0:
		guess = input("Please guess a letter or word: ").upper()
		if len(guess) == 1 and guess.isalpha():
			
			if guess in guessed_letters:
				print("You already guessed the letter", guess)
			
			elif guess not in word:
				print(guess, "Guess is not in word.")
				tries -= 1
				guessed_letters.append(guess)
			
			else:
				print("Good job,", guess, "is the correct answer!")
				guessed_letters.append(guess)
				word_as_list = list(word_completion)
				
				indices = [i for i, letter in enumerate(word) if letter == guess]
				for index in indices:
					word_as_list[index] = guess
				word_completion = "".join(word_as_list)
				
				if "_" not in word_completion:
					guessed = True
		elif len(guess) == len(word) and guess.isalpha():

			if guess == guessed_words:
				print("You already guessed the word", guess)

			elif guess != word: 
				print(guess, "is not the word")
				tries -= 1
				guessed_words.append(guess)
			else:
				guessed = True
				word_completion = word
		else:
			print("Guess is invalid.")
		print(display_hangman(tries))
		print(word_completion)
		print("\n")

	if guessed:
		print("Congratulations " + name + "! You win!")

	else:
		print("Sorry " + name + ", you ran out of tries. The word was " + word + ".")


def display_hangman(tries):
		stages = [	"""
					--------
					|      |
					|      0
					|     \\|/
					|      |
					|     / \\
					_
					""",
					"""
					--------
					|      |
					|      0
					|     \\|/
					|      |
					|     / 
					_
					""",
					"""
					--------
					|      |
					|      0
					|     \\|/
					|      |
					|     
					_
					""",
					"""
					--------
					|      |
					|      0
					|     \\|
					|      |
					|     
					_
					""",
					"""
					--------
					|      |
					|      0
					|      |
					|      |
					|     
					_
					""",
					"""
					--------
					|      |
					|      0
					|      
					|      
					|     
					_
					""",
					"""
					--------
					|      |
					|      
					|     
					|      
					|     
					_
					"""
	 		]
		return stages[tries]

def main():
	word = get_word()
	play(word)
	while input("Play again (Y/N)").upper() == "Y":
		word = get_word()
		play(word)


if __name__ == "__main__":
	main()








