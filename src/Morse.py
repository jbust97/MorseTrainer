from time import sleep
import os
abc = "abcdefghijklmnopqrstuvwxyz"
translator = {"a":"._","b":"_...","c":"_._.","d":"_..","e":".","f":".._.","g":"__.","h":"....","i":"..","j":".___","k":"_._","l":"._..","m":"__","n":"_.","o":"___","p":".__.","q":"__._","r":"._.","s":"...","t":"_","u":".._","v":"..._","w":".__","x":"_.._","y":"_.__","z":"__..","1":".____","2":"..___","3":"...__","4":"...._","5":"....","6":"_....","7":"__...","8":"___..","9":"____."}
def play(char):
    os.system('play -q -V0 ../sounds/' + char + '.ogg' )

def validate_input_range(v,l,r):
    if v not in range(l,r+1):
        raise Exception("Out of range option")

def validate_input_integer(v):
    try:
        v =int(v)
        return v
    except e:
        raise Exception("Not an integer")  

def abc_order_inner(l,r):
    score = 0
    for letter in abc[l:r+1]:
        print("The letter " + letter + ":") 
        sleep(1)
        play(letter)
        code = input()
        if code == translator[letter]:
            print("Correct!")
            score = score + 1
        else:
            print("Not very good")
    print("You were right " + str(score) + " of out " + str(r-l + 1) + " times")
def abc_order():
    valid = False
    os.system("clear")
    while not valid:
        valid = True
        print('You have chosen to practice the morse alphabet in order')
        print('You will the morse encoding of a letter and you will have to write it in dot-dash format e.g: ._.')
        print("We have three learning paths available:")
        print("1. From a-z")
        print("2. From a-m")
        print("3. From n-z")
        val = input()
        try:
            val = validate_input_integer(val)
            validate_input_range(val,1,3)
        except:
            print("Select a valid option!")
            valid = False


    if val == 1:
         abc_order_inner(0,25)
    elif val == 2:
         abc_order_inner(0,12)
    else:
        abc_order_inner(13,25)
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
        val = validate_input_integer(val)
        validate_input_range(val,1,4)          
    except:
        print("Input a number from 1 to 4!")
        return False
    else:
        f =  func[val-1]()
        return True
valid = False
while not valid:
    menu()
    valid = process_input()
