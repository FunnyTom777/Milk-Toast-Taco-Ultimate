import random
import time

devmode = True
arrested = False
player_money = 500
player_inventory = []
player_location = "outside"



inventory = {}


# Fishing Stuff:
fishs1 = ["pike", "carp", "Coral Trout", "Dufish", "Salmon", "King Gourge Whiting", "Break Sea Cod", "Blue Spotted Emporer", "Squid", "Puffer Fish", "Old Shoe", "Tuna", "Minuture shark!"]
illigalfish = ["pufferfish", "sealion", "Barry...", "John", "CRAIG!!!!!"] # add some more lmaoooooo


prices = {
    "pike": 10,
    "carp": 5,
    "Coral Trout": 15,
    "Dufish": 8,
    "Salmon": 12,
    "King Gourge Whiting": 40,
    "Break Sea Cod": 25,
    "Blue Spotted Emporer": 30,
    "Squid": 7,
    "Puffer Fish": 18,
    "Old Shoe": 1,
    "Tuna": 22,
    "Minuture shark!": 50
}

# Terrain Stuff



# Laws should be dynamically loaded from stuff/laws.yaml eventually... but knowing me it will probbbably never happen :D
laws = {
    "speeding": {"severity": 3, "fine": 100, "arrest": False, "impoundvehicle": False},
    "illegal_mod": {"severity": 6, "fine": 500, "arrest": False, "impoundvehicle": True},
    "assault": {"severity": 9, "fine": 1000, "arrest": True, "impoundvehicle": False},
    "fishing_without_license": {"severity": 2, "fine": 50, "arrest": False, "impoundvehicle": False},
    "driving_without_license": {"severity": 4, "fine": 300, "arrest": False, "impoundvehicle": False}
}

# Police function
def policenew(offense):
    global arrested
    if offense not in laws:
        print("This offense doesn't exist!")
        print("Me probbably screwed up some code...")
        return
    
    print("🚨 The Police Show Up!! 🚨")
    decision = input("Surrender (Y) Or Run (N)?: ").upper()
    offense_data = laws[offense]

    if decision == "Y":
        # Surrender
        if offense_data["arrest"]:
            print("You are Arrested by the police!")
            togglearrest()
        else:
            fine = offense_data["fine"]
            print(f"You Surrender And Get Fined ${fine}")
            fineplayer(fine, f"Player Was Fined For: {offense}")
            if devmode:
                print(f"[DEV MODE] Player fined for: {offense}")

        # Handle vehicle impound
        if offense_data["impoundvehicle"]:
            print("Your vehicle has been impounded!")

    elif decision == "N":
        # Attempt to run
        escape = random.randint(0, 100)
        if escape < 50:
            print("You managed to escape the police!")
        else:
            print("The police caught you!")
            if offense_data["arrest"]:
                togglearrest()
            else:
                fine = offense_data["fine"]
                print(f"You still get fined ${fine} for the offense.")
                fineplayer(fine, f"Player Was Fined For: {offense}")
    else:
        print("Invalid input! The police are confused by your decision, and get angry and arrest you...")
        togglearrest()


def start():
    global player_money
    print("Welcome To MTT!")
    print(f"You currently have ${player_money}")

def error(errorreason, fatal):
    if fatal == True:
        print(f"Fatal Error: {errorreason}")
    elif fatal == False:
        print(f"Error: {errorreason}")
    


def event1():
    event = random.randint(0, 5)  # returns 0–5 inclusive
    if event == 1:
        print("Event 1 Happens!")
    elif event == 2:
        print("Event 2 Happens")
    elif event == 3:
        print("Event 3 Happens")
    elif event == 4:
        print("Event 4 Happens")
    elif event == 5:
        print("Event 5 Happens!")
    elif event == 0:
        print("Event 0 Happens!")
    else:
        error("Event did not match set peramaters!", False)
        
def togglearrest():
    global arrested # this is needed for some reason for it to work, if this is not here it errors lol
    arrested = not arrested


# VVVVVVVVVVV--- OLDDDDDD OLLDDD OLDDD OLLLDDD ---VVVVVVVVVV Use policenew instead!!!
def police(fine, offense, arrest):
    global arrested
    print("The Police Show Up!!")
    decision = input("Surrender (Y) Or Run (N)?: ").upper()
    if decision == "Y":
        # Surrender
        if arrest == True:
            # Arrest
            print("You are Arrested by the police!")
            togglearrest()
        elif arrest == False:
            # No arrest (Fine only)
            print(f"You Surrender And Get Fined ${fine}")
            fineplayer(fine, f"Player Was Fined By Police For Offence: {offense}")
            global devmode
            if devmode == True:
                print(f"Player Was Fined By Police For Offence: {offense}")
    elif decision == "N":
        escape = random.randint(0, 100)
        if escape < 50:
            print("You managed to escape the police!")
        else:
            print("The police caught you anyway!")
            togglearrest()





def fisheriesshowup(): # idk why i have this, i just thought it would be cool to be able to have more than 1 officer hehe
    Fisherie_officers_count = random.randint(1,2)
    if Fisherie_officers_count == 1:
        print("A Fisheries Officer Shows Up!")
        fisheries()
    elif Fisherie_officers_count == 2:
        print("2 Fisheries Officers Show Up!")
        fisheries()
    else:
        print("the code ded... call the emergency department, the code is dieing!!!")
        fisheries()




def fisheries():
    """Check the player's inventory for illegal fish or fish requiring a license."""
    global arrested, inventory, player_money

    illegal_caught = [fish for fish in inventory if fish in illigalfish]
    licensed_caught = [fish for fish in inventory if fish in ["King Gourge Whiting", "Break Sea Cod", "Blue Spotted Emporer"]]

    if illegal_caught:
        print("🚨 Fisheries Alert! 🚨")
        for fish in illegal_caught:
            print(f"You have an illegal fish: {fish}!")
            # 50% chance to get caught and fined/arrested
            if random.random() < 0.5:
                print(f"Fisheries catch you trying to sell {fish}!")
                fine_amount = 500  # arbitrary fine, can be dynamic
                print(f"You are fined ${fine_amount} for possessing illegal fish.")
                fineplayer(fine_amount, f"Illegal fish caught: {fish}")
                # Chance of arrest for repeated offenses
                if random.random() < 0.3:
                    print("You are arrested for illegal fishing activities!")
                    togglearrest()
            else:
                print(f"You manage to hide {fish} from Fisheries officers... for now.")

    if licensed_caught:
        print("⚠️ Some fish require a license to sell:")
        for fish in licensed_caught:
            print(f" - {fish}")
        print("Selling these without a license may alert Fisheries!")






def fishing():
    print("Fishing...")
    chance = random.randint(0, 100)
    time.sleep(random.randint(2, 5))
    if chance < 70:
        global fishs1
        caught_fish = random.choice(fishs1)
        print(f"You Caught a {caught_fish}!")
        add_item(inventory, caught_fish, 1)
    else:
        print("Dident Catch Anything...")



def phone():
    print("working on this hehehehe >:D")



def sellitems():
    global player_money
    if not inventory:
        print("Your inventory is empty! 🛒")
        return

    display_inventory(inventory)
    itemtosell = input("What would you like to sell?: ")

    if itemtosell not in inventory:
        print(f"You don't have any {itemtosell} to sell!")
        return

    quantity_available = inventory[itemtosell]

    try:
        howmanytosell = int(input(f"How many {itemtosell} would you like to sell? (You have {quantity_available}): "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if howmanytosell <= 0 or howmanytosell > quantity_available:
        print("Invalid quantity!")
        return

    # Check if the fish is illegal before selling
    if itemtosell in illigalfish or itemtosell in ["King Gourge Whiting", "Break Sea Cod", "Blue Spotted Emporer"]:
        fisheriesshowup()

    # Determine sale price
    price_per_item = prices.get(itemtosell, 1)
    total_price = howmanytosell * price_per_item

    # Update inventory and money
    remove_item(inventory, itemtosell, howmanytosell)
    player_money += total_price

    print(f"You sold {howmanytosell} x {itemtosell} for ${total_price}!")
    print(f"You now have ${player_money}")


def sell_all():
    global player_money
    if not inventory:
        print("Nothing to sell!")
        return
    total_earned = 0
    for item, qty in list(inventory.items()):
        price = get_price(item)
        total_price = price * qty
        total_earned += total_price
        remove_item(inventory, item, qty)
        print(f"Sold {qty} x {item} for ${total_price}")
    player_money += total_earned
    print(f"Total money earned: ${total_earned}")
    print(f"Current balance: ${player_money}")




### PLAYER INVENTORY SYSTEM: (Confusing!):
def add_item(inv: dict, name: str, qty: int = 1) -> None:
    """Add `qty` of `name` to the inventory."""
    if qty <= 0:
        raise ValueError("qty must be positive")
    inv[name] = inv.get(name, 0) + qty

def remove_item(inv: dict, name: str, qty: int = 1) -> None:
    """Remove `qty` of `name`. Raises if you try to remove more than you have."""
    if name not in inv:
        raise KeyError(f"No {name} in inventory")
    if qty <= 0:
        raise ValueError("qty must be positive")
    if inv[name] < qty:
        raise ValueError(f"Not enough {name} to remove")
    inv[name] -= qty
    if inv[name] == 0:
        del inv[name]  # tidy up empty slots

def get_quantity(inv: dict, name: str) -> int:
    """Return how many of `name` the player has (0 if none)."""
    return inv.get(name, 0)

def display_inventory(inv: dict) -> None:
    """Print a quick, human‑readable view of the inventory."""
    if not inv:
        print("🛒 Inventory is empty.")
        return
    print("🛒 Inventory:")
    for name, qty in inv.items():
        print(f"   {name}: {qty}")

        


def fineplayer(finevalue, reason):
    global player_money
    player_money -= finevalue
    # Should log reason to a log.txt or somthing...
    global devmode
    if devmode == True:
        print(f"Money Updated: {player_money}")


def bank():
    print("You Went to the bank...")
    print(f"You have ${player_money}!")






# Map strings to functions
functions = {
    "togglearrest": togglearrest,
    "event": event1

}

def runfunction():
    input50 = input("What Function To Run?: ")
    if input50 in functions:
        functions[input50]()  # call the function
    else:
        print("No such function!")


