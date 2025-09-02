import random

words = ["apple", "banana", "cherry", "grape", "orange"]

word = random.choice(words).strip().lower()

guessed = ['_'] * len(word)
attempts = 6
guessed_letters = []

print("-------- Welcome to hangame -----------")

while attempts > 0 and "_" in guessed:

    print("Word:", " ".join(guessed))
    print("Attempts left :", attempts)
    guess = input("Guess a letter : ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter")
        continue

        guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess")

    else:
        print("Wrong guess")
        attempts -= 1

if "_" not in guessed:
    print(f"Congratulation You guessed it right. And the word is {word}")
else:
    print(f"Game Over.The word was {word}")

