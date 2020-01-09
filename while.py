guesses = 1
while guesses <= 5:
    print('*' * guesses)
    guesses = guesses + 1
print("Done")

number = 9
guesses = 0
guess_limit = 3
while guesses < guess_limit:
    guess = int(input('Guess: '))
    guesses += 1
    if guess == number:
      print('correct guess')
      break
    else:
        print("wrong guess")