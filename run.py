import gspread
from google.oauth2.service_account import Credentials

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
            print(f"Thank you {name}!\n") #Make text green

            break

    return name.upper()

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
    print("Here are a few options for you:\n")
    print("Start game? Press 1")
    print("Check out the leaderboard? Press 2")
    print("Official rule book of Random Golf? Press 3")
    print("Do you want to come back later? Press 4")
    start_game = input(" ")
    check_leaderborad = input(" ")
    check_rules = input(" ")
    quit_game = input(" ")
    if start_game == '1':
        print("Game loading...\n")
        run_game()
    elif check_leaderborad == '2':
        print("Leaderboard loading...\n")
        show_leaderboard()
    elif check_rules == '3':
        print("Rule book loading...")
        rule_book()
    else:
        print("Thank you for visiting, welcome back another time!")

def main():
    """
    Runs the game
    """
    name = player_name()
    menu()

print("Welcome to this little game called Random Round of Golf!\n")
print("I'm Billy, your caddie for the day.\n")
print("Before we tee off, what name should I put in the scorecard?.")
print("(Make sure you only use letters when entering your name)\n")
main()
