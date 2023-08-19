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

    return name

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


def menu()


def main():
    """
    Runs the game
    """
    name = player_name()

print("Welcome to this little game called Random Round of Golf!\n")
print("I'm Billy, your caddie for the day.\n")
print("Before we tee off, what name should I put in the scorecard?.")
print("(Make sure you only use letters when entering your name)\n")
main()
