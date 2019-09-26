from time import sleep
import os
abc = "abcdefghijklmnopqrstuvwxyz"
translator = {"a":"._","b":"_...","c":"_._.","d":"_..","e":".","f":".._.","g":"__.","h":"....","i":"..","j":".___","k":"_._","l":"._..","m":"__","n":"_.","o":"___","p":".__.","q":"__._","r":"._.","s":"...","t":"_","u":".._","v":"..._","w":".__","x":"_.._","y":"_.__","z":"__..","1":".____","2":"..___","3":"...__","4":"...._","5":"....","6":"_....","7":"__...","8":"___..","9":"____."}
def play(char):
    os.system('play -q -V0 ./sounds/' + char + '.ogg' )
def abc_order():
    os.system("clear")
    print('You have chosen to practice the morse alphabet in order')
    print('You will the morse encoding of a letter and you will have to write it in dot-dash format e.g: ._.')
    print("We have three learning paths available:")
    print("1. From a-z")
    print("2. From a-m")
    print("3. From n-z")
    try:
        val = int(input())
    except e:
        print("Select a valid option!")
    else:
        if val == 1:
            score = 0
            for letter in abc:
                print("The letter " + letter + ":") 
                sleep(1)
                play(letter)
                code = input()
                if code == translator[letter]:
                    print("Correct!")
                    score = score + 1
                else:
                    print("Not very good")
            print("You were right " + str(score) + " of out 26 times") 
        elif val == 2:
            score = 0
            for letter in abc[:14]:
                print("The letter " + letter + ":") 
                sleep(1)
                play(letter)
                code = input()
                if code == translator[letter]:
                    print("Correct!")
                    score = score + 1
                else:
                    print("Not very good")
            print("You were right " + str(score) + " of out 13 times") 
        else:
            score = 0
            for letter in abc[14:]:
                print("The letter " + letter + ":") 
                sleep(1)
                play(letter)
                code = input()
                if code == translator[letter]:
                    print("Correct!")
                    score = score + 1
                else:
                    print("Not very good")
            print("You were right " + str(score) + " of out 13 times") 
def abc_random():
    pass
def decode_words():
    pass
def decode_phrases():
    pass
def menu():
    os.system("clear")
    print("Hello! I am your Morse Code Trainer")
    print("Please select one of the activities from the menu below!")
    print("1. In order abc training")
    print("2. Random abc training")
    print("3. Decode Words")
    print("4. Decode phrases!")
def process_input():
    choices = [1,2,3,4]
    func = [abc_order,abc_random,decode_words,decode_phrases]
    val = input()
    try:
        val = int(val)
        if val not in choices:
            raise Exception("heh")            
    except(e):
        print("Input a number from 1 to 4!")
    else:
        f =  func[val-1]()
menu()
process_input()
#word = input()
#for char in word:
#       if char != " ": 
#         os.system('play -q -V0 ./sounds/' + char + '.ogg' )
#       else:
#         sleep(1)