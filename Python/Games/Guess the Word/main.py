import random
name = input("aapka naam kya hai ? ")
print("sabbas ! ", name)
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("characters socho !")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("aap jitgaye")
        print("The word is: ", word)
        break
    print()
    guess = input("ek character socho :")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Galat")
        print("Aapke paas", + turns, 'turns hai sochne k liye')
        if turns == 0:
            print("aap hargaye")
