import gspread
from google.oauth2.service_account import Credentials
from itertools import islice

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('results_golf-adventure')

# scores = SHEET.worksheet('result')

# data = scores.get_all_values()

def player_name():
    """
    Asks user for name
    """
    while True:   
        name = input("Enter your name: ")

        if valid_name(name):
            print(f"Thank you {name}, great to meet you!\n") #Make text green

            break

    return name.upper

def valid_name(name):
    """
    Checks if the name contains only letters (no numbers or symbols)
    """
    if name.isalpha():  # Check if the name contains only alphabetic characters
        return True
    else:
        print("Invalid name. Try again!.\n") #Make text red
        return False

    return True 


def menu():
    """
    Gives the user options of play game, see the leaderboard, see the rules or quit game"
    """
    print("We are now at the club house, what would you like to do?\n")
    print("Start game? Press 1")
    print("Check out the leaderboard? Press 2")
    print("Check out the rule book of Random Golf? Press 3")
    print("Do you want to come back later? Press 4")
    menu_choice = input("")
    try:
        index = int(menu_choice)
        if index == 1:
            print("\nLaunching game...\n")
            play_hole()
        elif index == 2:
            print("\nLoading leaderboard...\n")
            check_leaderboard()
        elif index == 3:
            print("\nLoading rule book...\n")
            rule_book()
        elif index == 4:
            print("\nThank you for visiting, welcome back another time!")
        else:
            print("\nInvalid choice. Try again!\n")
            menu()
    except ValueError:
        print("\nInvalid choice. Try again!\n")
        menu()           

def rule_book():
    """
    Explains the rule of the game for the user. With options to return to "club house"
    """
    file_path = 'text_files/rule_book.txt'
    with open(file_path, 'r') as file:
        content = file.read()
    
    print(content)
    clubhouse()
    
def clubhouse():
    """
    Function to let the user return to the menu
    """
    print("\nPress 1 to return to clubhouse")
    to_clubhouse = input("")
    try:
        index = int(to_clubhouse)
        if index == 1:
            print("\nHeading back to the clubhouse...\n")
            menu()
        else:
            print("\nInvalid choice. Try again!\n")
            clubhouse()
    except ValueError:
        print("\nInvalid choice. Try again!\n")
        clubhouse()


def play_hole():
    """
    Function that holds the 1st hole game
    """
    file_path = 'text_files/first_hole.txt'
    with open(file_path, 'r') as file:
        content_1 = file.read()
    
    print(content_1)
    
    first_shot = input("")
    try:
        index = int(first_shot)
        if index == 1:
            print("\nBrave choice. Remember, the left side is not where we want to be.\n")
            print(f"Nice shot {name}, you avoided the out of bounce and ended up in the rough on the right hand side")
            print("You're now 150 meters away from the hole. There's a bunker on the back side of the green and on the left side, the left one is really steep and is hard to get out of.")
            print("You normally play your 6 iron from this distance, but maybe it's better to play the 7 iron, which is shorter?")
            print("Press 6 for 6 iron")
            print("Press 7 for 7 iron")
            first_driver_second_choice = input("")
            try:
                index =int(first_driver_second_choice)
                if index == 1:
                    print("\nHere's your 6 iron. Good luck!\n")
                    print("You hit that really well, but it looked like it went a bit far. Let's go check where it ended up.\n")#Waiting time
                    print("Unlucky, you're in the bunker on the back of the green. The hole is in the center of the green, but after the hole it will run away, so it's better to be a bit short.")
                    print("Do you want to hit it short or do you want to go for the hole?")
                    print("Press 1 for short")
                    print("Press 2 for hole")
                    first_driver_third_choice = input("") 
                    try:
                        index =int(first_driver_second_choice)
                if index == 1:
                    print("\nHere's your 6 iron. Good luck!\n")
                    print("You hit that really well, but it looked like it went a bit far. Let's go check where it ended up.\n")#Waiting time
                    print("Unlucky, you're in the bunker on the back of the green. The hole is in the center of the green, but after the hole it will run away, so it's better to be a bit short.")
                    print("Do you want to hit it short or do you want to go for the hole?")
                    print("Press 1 for short")
                    print("Press 2 for hole")
                    first_driver_third_choice = input("") 
        elif:
            print("\nInvalid choice. Try again!\n")
            clubhouse()
    except ValueError:
        print("\nInvalid choice. Try again!\n")
        clubhouse()


def main():
    """
    Runs the game
    """
    name = player_name()
    menu()

print("Welcome to this little game called Random Round of Golf!\n")
print("I'm Billy, your caddie for the day.\n")
print("Before we tee off, what name should I put in the scorecard?")
print("(Make sure you only use letters when entering your name)\n")
main()
