import random


def input_choice(q: str, a: list[str]) -> str: #Aufgabenteil (a)
    pos = ""
    for i in a:
        if i == a[0]:
            pos += "[" + i + "|"
        elif i == a[-1]:
            pos += i + "]"
        else:
            pos += i + "|"
    print(q, pos)
    ans = input()
    if ans in a:
        return ans
    else:
        print("Invalid answer. Try again.")


def shape(word: str, guesses: str): #Aufgabenteil (b)
    real_guess = ""
    list(guesses)
    for i in range(len(word)):
        if word[i] in guesses:
            real_guess += word[i]
        else:
            real_guess += "_"
    return real_guess + ";"


def hangman(word: str, max_fails: int): #Aufgabenteil (c)
    guesses = ""
    a = ""
    while max_fails > 0 and a != word:
        print(shape(word, guesses), max_fails, " mistakes left; ", end="")
        a = input("make a guess: ")
        if a in word:
            guesses += a
        else:
            max_fails -= 1
    n = shape(word, guesses)
    if word + ";" == n:
        word = "'"+word+"!'"
        print("You won! The word was", word, "You're the best! Everyone loves you!")


words = ['apple', 'tree', 'python', 'bench', 'float']
max_fails = int(input("Number of allowed mistakes: "))
while input_choice("Wanna play a game?", ['yes', 'no']) == 'yes':
    word = random.choice(words)
    hangman(word, max_fails)
