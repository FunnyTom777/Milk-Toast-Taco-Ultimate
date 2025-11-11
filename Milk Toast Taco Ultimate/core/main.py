import time
import readchar # type: ignore

nooptioncount = 0
generalstoreopen = False
day = "Wednesday"
time1 = 12.00

def playmtt():
    start3()

def configbarkengine():
    print("lol")

def lol():
    print("lol")

def thisisaveryinportantfunctionthatshoulddosomthing():
    print("This is a very important function that should do somthing but probabbly dosent, either because you have reached a point in the game that i dident think was possibal considering the -100 people who would in there right mind play this game, or that i just completly forgot that this funtion exsisted in this game! (for real tho, if this pops up and you think it should do somthing, leave a message in the discord!)")


def start():
    print("BarkEngine Booting...")
    print("HEHE booting thats funny :D")
    time.sleep(2)
    print("Done Booting! hehehe")
    print("What Would You Like To do?")
    print("1 - Play MTT")
    print("2 - Configure BarkEngine")
    print("3 - Quit because you are too scared...")
    start2()

def openmainmenu():
    thisisaveryinportantfunctionthatshoulddosomthing()

def start2():
    global nooptioncount
    choice = input("What Would You Like to Do? ")

    if choice == "1":
        print("Ok! here you go!!!!")
        time.sleep(0.5)
        playmtt()

    elif choice == "2":
        print("OK! Here You GO!")
        time.sleep(0.5)
        configbarkengine()

    elif choice == "3":
        print("Ok Here You GO!")
        time.sleep(0.5)
        quit()

    else:
        if nooptioncount > 5:
            print("What is wrong with you???? CHOSE AN OPTION!!!!")
        else:
            print("BRO THAT ISN'T EVEN AN OPTION >:C")
            nooptioncount += 1
        print(" ")
        start2()







def start3():
    print(" ")
    username = input("Please Pick a username!: ")
    print("Welcome to the world of Milk Toast Taco " + username)
    print("We suggest you buckle up, get some pillows, maybe some medical advice, and be ready for the crazy, buggy, slightly minacle mess that is MTT!! :D")
    print("You can press space to advance thru dialouge, press Tab to open the main menu, Good luck!")

    while True:
        key = readchar.readkey()
        if key == ' ':
            start4()
            break
        elif key == '\t':
            openmainmenu()
            break

def start4():
    print(" ")
    print("You have just moved to a small town called snowland in the state of NorthMoor, all you have is a $500 loan, and a old rusty pickup truck...")
    print("Your currently staying at a carpark on the outskirts of town, you sleep in your truck")
    print("The border officer on the way here said you should go past the general store in town...")
    print("1 - Go to the general Store")
    print("2 - Explore Town")
    print("3 - Go to the police station")
    print("4 - Inspect the truck")

    input3 = input("What do you do?: ")
    if input3 == "1":
        start5()
    elif input3 == "2":
        start6()
    elif input3 == "3":
        start7()
    elif input3 == "4":
        start8()
    
    else:
        print("please Pick a option...")
        start4()


def start5(): # Go to the general store
    print("You Drive to the general store...")
    print(" ")
    global generalstoreopen
    if generalstoreopen == True:
        print("the general store was open...")
    elif generalstoreopen == False:
        print("You tug on the front door, but its locked...")
        print("You look at the opening times sign...")
        print(" ")
        print("'Monday - open 9:00AM till 8:00PM'")
        print("'Tuseday - open 9:00AM till 8:00PM'")
        print("'Closed Wednesday'")
        print("'Thursday - open 9:00AM till 8:00PM'")
        print("'Friday - open 9:00AM till 8:00PM'")
        print("'Closed Saturday'")
        print("'Closed Sunday'")
        print(" ")
        global day
        print("Its " + day + " today, must be closed...")
        print(" ")
        print("Tip!: Press Q to see what day/time it is!")


def start6(): # Explore Town
    print("still working on this bit...")

def start7(): # Go To the Police Station
    print("")
    
def start8(): # Inspect the truck
    print("")


start()