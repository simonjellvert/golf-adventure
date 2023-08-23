import sys
import time
import os
import gspread
from google.oauth2.service_account import Credentials
from blessed import Terminal


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('results_golf-adventure')


def clear_terminal():
    """
    Clears terminal for better UX
    Code retrieved from Stack Overflow
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def logotype():
    """
    Prints logotype at welcome message
    """
    file_path = 'text_files/logotype.txt'
    with open(file_path, 'r') as file:
        content_logo = file.read()
    print(term.green + content_logo + term.normal)


def print_slow(words):
    """
    Function for printing text slow.
    Printing each letter set to 0.03s
    Code retrieved from Stack Overflow
    """
    for letter in words:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


term = Terminal()   # Code from CI mentor Alexsei Konovalov

PLAYER_NAME = None


def get_PLAYER_NAME():
    """
    # Asks player for name
    """

    global PLAYER_NAME

    if PLAYER_NAME is None:
        while True:
            name = input(term.green + "\nEnter your name: " + term.normal)
            if valid_name(name):
                clear_terminal()
                print_slow(
                    term.green + f"\nThank you {name}, "
                    "great to meet you!\n" + term.normal
                    )
                PLAYER_NAME = name
                break


def valid_name(name):
    """
    # Checks if the name contains only letters (no numbers or symbols)
    """
    if name.isalpha():  # Check if the name contains only alphabetic characters
        return True
    else:
        print(term.red + "Invalid name. Try again!.\n" + term.normal)
        return False


def menu():
    """
    Gives the player options of play game, see the leaderboard,
    see the rules or quit game"
    """
    while True:
        print_slow(
            "\nWe are now at the Clubhouse, what would you like to do?\n"
            )
        print(
            "---------------------------------------------------------\n"
            "\n* Start game? Press 1\n"
            "\n* Check out the leaderboard? Press 2\n"
            "\n* Check out the rule book of Random Golf? Press 3\n"
            "\n* Do you want to come back later? Press 4\n"
            )
        menu_choice = input(term.green + "Enter here: " + term.normal).strip()

        try:
            index = int(menu_choice)
            if index == 1:  # Sends player to the play hole function
                clear_terminal()
                print("\nLaunching game...\n")
                time.sleep(1.0)
                clear_terminal()
                play_hole()
                break
            elif index == 2:    # Sends player to the leaderboard function
                clear_terminal()
                print("\nLoading leaderboard...\n")
                time.sleep(1.0)
                clear_terminal()
                check_leaderboard()
                break
            elif index == 3:    # Sends player to read the rule book
                clear_terminal()
                print("\nLoading rule book...\n")
                time.sleep(1.0)
                clear_terminal()
                rule_book()
                break
            elif index == 4:    # Exits game and sends player welcome message
                clear_terminal()
                print_slow(
                    "\nThank you for visiting, welcome back another time!"
                    )
                exit()
            else:   # Sends error message to player
                clear_terminal()
                print(
                    term.red + "\nInvalid choice. Try again!\n" + term.normal
                    )
        except ValueError:  # Sends error message to player
            clear_terminal()
            print(
                term.red + "\nInvalid choice. Try again!\n" + term.normal
                )


def rule_book():
    """
    Explains the rule of the game for the player.
    With options to return to "clubhouse"
    """
    file_path = 'text_files/rule_book.txt'
    with open(file_path, 'r') as file:
        content = file.read()

    clear_terminal()
    print(content)
    clubhouse()


def clubhouse():
    """
    Function within rule_book and leaderboard
    to let the player return to the menu
    """
    print(term.green + "\nPress 1 to return to Clubhouse" + term.normal)
    to_clubhouse = input("")
    try:
        index = int(to_clubhouse)
        if index == 1:  # Sends player back to the clubhouse
            clear_terminal()
            print("\nHeading back to the Clubhouse...\n")
            time.sleep(1.0)
            clear_terminal()
            menu()
        else:   # Error message if invalid input, asks player to try again
            clear_terminal()
            print(
                term.red + "\nInvalid choice. Try again!\n" + term.normal
                )
            clubhouse()
    except ValueError:  # Error message if invalid input, try again
        clear_terminal()
        print(
            term.red + "\nInvalid choice. Try again!\n" + term.normal
            )
        clubhouse()


def update_leaderboard(score):
    """
    Function to update leaderboard. Linked to
    Google sheet for score keeping
    """

    sheet = SHEET.get_worksheet(0)
    row_data = [PLAYER_NAME, int(score)]
    sheet.append_row(row_data)


def check_leaderboard():
    """
    Function to let the player see the leaderboard.
    Linked to Google Sheet, which is updated through
    update_leaderboard funktion.
    """

    sheet = SHEET.get_worksheet(0)
    leaderboard = sheet.get_all_records()

    if not leaderboard:     # If leaderboard is empty, print message
        print_slow("The leaderboard is empty.\n")
        clubhouse()
        return

    aggregated_scores = {}

    for entry in leaderboard:
        name = entry['Name']
        score_str = entry['Score']
        try:
            score = int(score_str)
            if name in aggregated_scores:
                aggregated_scores[name] += score
            else:
                aggregated_scores[name] = score
        except ValueError:
            print_slow(
                "Unable to convert score "
                f"value for {name} to int: {score_str}")
            continue

    sorted_leaderboard = sorted(aggregated_scores.items(), key=lambda x: x[1])

    print_slow(term.green + "\nLeaderboard\n" + term.normal)
    for i, (name, score) in enumerate(sorted_leaderboard[:5], start=1):
        print(f"\n{i}. {name} - Score: {score}")    # Prints sorted leaderboard
    clubhouse()


def play_hole():
    """
    Function that starts the game and first shot option.
    """

    print_slow(
        "\nFeeling warmed up? Perfect! Let's get this round started\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nThis is the Random Golf hole, it's a 350 meters long par 4.\n"
        "\nThe left side is out of bounce, which means if you hit "
        "it there \nyou are going to need to hit your 3rd "
        "shot from the tee box.\n"
        "On the right side there's a grove, "
        "if you hit it there you might have to \njust lay up.\n"
        "\nYou can either choose to hit a driver, with the risk "
        "of ending up \nin one of the hazards. Or you can choose "
        "the play a safe shot, \nwhich is a long iron.\n"
        )

    while True:
        first_shot = get_choice(
            "\nPress 1 for driver.\n"
            "Press 2 for iron.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
            )

        if first_shot == 1:     # Driver
            clear_terminal()
            play_driver_shot()
        elif first_shot == 2:   # Iron
            clear_terminal()
            play_iron_shot()
        elif first_shot == 0:   # Exit game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def get_choice(prompt):
    """
    Function to try the players choice on each shot
    """
    print_slow(prompt)
    try:    # Checks for valid input
        index = int(input())
        return index
    except ValueError:  # Checks for invalid input
        print(term.red + "Invalid choice. Try again!" + term.normal)
        return get_choice(prompt)


def play_driver_shot():
    """
    - Tells the player the result of the  first choice,
    - Asks the player to choose next shot,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nNice shot, you avoided the out of bounce and ended up "
        "in the rough on the right hand side.\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nYou're now 125 meters away from the hole. \nThere's a bunker "
        "on the back side of the green and on the left side, \nthe "
        "left one is really steep and is hard to get out of.\n"
        "\nYou normally play your 7 iron from this distance, "
        "\nbut maybe it's better to play the 8 iron, "
        "which goes shorter?\n"
        )

    while True:
        driver_choice = get_choice(
            "\nPress 7 for 7 iron.\n"
            "Press 8 for 8 iron.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
            )

        if driver_choice == 7:      # 7 iron
            clear_terminal()
            play_7_iron_shot()
        elif driver_choice == 8:    # 8 iron
            clear_terminal()
            play_8iron_shot()
        elif driver_choice == 0:    # Exit game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_7_iron_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot,
    - Runs the choice through get_choice function and return
    next function
    """
    print_slow(
        "\nHere's your 7 iron. Good luck!\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nYou hit that really well, but it looked like it went a bit far.\n"
        "Let's go check where it ended up.\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nOh, you're in the bunker on the back of the green.\n"
        "The hole is in the center of the green, but after the hole "
        "it will run away, \nso it's better to be a bit short.\n"
        )
    print_slow(
        "\nDo you want to hit it short or do you want to go for the hole?\n"
        )

    while True:
        driver_7iron_choice = get_choice(
            "\nPress 1 to aim for the hole.\n"
            "Press 2 for the shorter shot."
            "\nPress 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
            )
        if driver_7iron_choice == 1:    # Aim for the hole
            clear_terminal()
            play_driver_7iron_hole_shot()
        elif driver_7iron_choice == 2:  # Hit a short shot
            clear_terminal()
            play_driver_7iron_short_shot()
        elif driver_7iron_choice == 0:  # Exit
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_driver_7iron_hole_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nWOW! You managed to get it to stop just one meter from the hole, "
        "well done!\n"
        "\nBut there's still work to do, "
        "these putts are sometimes the hardest.\n"
        "Concentrate, and put it in the hole.\n"
        )

    while True:
        driver_7iron_hole_choice = get_choice(
            "\nPress 1 to submit score of par and head back to Clubhouse.\n"
            "Press 2 to end game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
            )
        if driver_7iron_hole_choice == 1:   # Submit score and show clubhouse
            update_leaderboard(0)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif driver_7iron_hole_choice == 2:     # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "I will not submit your score, since you didn't complete "
                "the round. Welcome back another time!"
                )
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_driver_7iron_short_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nOh no, it's a little too short and got stuck on the fringe...\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nNow, if you choose to chip there is a possibility that you \n"
        "hit it too far and roll of the green, but on the other hand "
        "- if you \nhit it well you avoid undulations ahead of the hole.\n"
        "If you choose to put, you need to read the line carefully.\n")

    while True:
        driver_7iron_short_choice = get_choice(
            "\nPress 1 to chip the ball.\n"
            "Press 2 to putt the ball.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if driver_7iron_short_choice == 1:  # Chip the ball
            clear_terminal()
            play_driver_7iron_short_chip_shot()
        elif driver_7iron_short_choice == 2:    # Putt the ball
            clear_terminal()
            play_driver_7iron_short_putt_shot()
        elif driver_7iron_short_choice == 0:    # Exit game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_driver_7iron_short_chip_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nOps...it's a duff...\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nBut it rolled out a bit but it's too far off the hole.\n"
        "I'll set you up for a 2-putt and a score of 6, "
        "on a par 4 that means +2.\n"
        )

    while True:
        play_driver_7iron_short_chip_choice = get_choice(
            "\nPress 1 to submit score and head back to Clubhouse.\n"
            "Press 2 to end game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_driver_7iron_short_chip_choice == 1:    # Submit score
            update_leaderboard(2)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_driver_7iron_short_chip_choice == 2:  # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!")
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_driver_7iron_short_putt_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nNice putt , that's a tap in for a 5. "
        "On a par 4 that means your score in +1.\n")
    while True:
        play_driver_7iron_short_putt_choice = get_choice(
            "\nPress 1 to submit score of +1 and head back to Clubhouse.\n"
            "Press 2 to end game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_driver_7iron_short_putt_choice == 1:    # Enter score
            update_leaderboard(1)
            print_slow("\nUpdating leaderboard...")
            clear_terminal()
            clubhouse()
        elif play_driver_7iron_short_putt_choice == 2:  # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "I will not submit your score, since you didn't complete "
                "the round. Welcome back another time!")
            time.sleep(3.0)
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_8iron_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nNice shot! That ball came out smooth from the rough!\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nYou're pin high on the right side of the green, on the fringe.\n"
        "If you chip the ball you avoid undulations ahead of the hole \n"
        "but risk hitting it short or long.\n"
        "If you choose to putt, you need to read the green carefully\n"
        )

    while True:
        driver_8iron_choice = get_choice(
            "\nPress 1 to chip the ball.\n"
            "Press 2 to putt.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
            )

        if driver_8iron_choice == 1:    # Chip ball
            clear_terminal()
            play_driver_8iron_chip_shot()
        elif driver_8iron_choice == 2:  # Putt ball
            clear_terminal()
            play_driver_8iron_putt_shot()
        elif driver_8iron_choice == 0:  # Leave game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_driver_8iron_chip_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nOH! You chipped right in the hole!!\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nThat's a birdie! I'll put a 3 on the scorecard, "
        "on a par 4 that means -1.\n"
        )

    while True:
        driver_8iron_chip_choice = get_choice(
            "\nPress 1 to submit score of -1 and head back to Clubhouse.\n"
            "Press 2 to end game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if driver_8iron_chip_choice == 1:   # Enter Score
            update_leaderboard(-1)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif driver_8iron_chip_choice == 2:     # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!")
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_driver_8iron_putt_shot():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nNice putt, that was very close!\n"
        "That's just a tap in for par, well done!\n"
        )

    while True:
        play_driver_8iron_putt_choice = get_choice(
            "\nPress 1 to submit score of par and head back to Clubhouse.\n"
            "Press 2 to exit game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_driver_8iron_putt_choice == 1:  # Enter score
            update_leaderboard(0)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_driver_8iron_putt_choice == 2:    # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "I will not submit your score, since you didn't complete "
                "the round. Welcome back another time!")
            time.sleep(3)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_shot():
    """
    - Tells the player the result of the first choice,
    - Asks the player to choose next shot,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nReally nice iron shot, "
        "that went straight down the middle of the fairway!\n"
        "\nNow you have 180 meters to the green, that's quite long.\n"
        "\nOn the left side of the green there is a steep bunker, "
        "and there's \nanother one on the back side of the green.\n"
        "\nYou can either choose to play a fairway wood that should "
        "take you \nto the green but risks ending up in one of the bunkers.\n"
        "Or you can play it safe and lay up for a chip shot.\n"
        )

    while True:
        play_iron_choice = get_choice(
            "\nPress 1 to hit a fairway wood.\n"
            "Press 2 to lay up.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_choice == 1:   # Fairway wood
            clear_terminal()
            play_iron_wood()
        elif play_iron_choice == 2:     # Lay up
            clear_terminal()
            play_iron_layup()
        elif play_iron_choice == 0:     # Leave game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nOh no, wind is taking it to the left...\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nUnfortunately it looks like you're in the steep bunker.\n"
        "\nThis bunker is really hard to get out of. If you aim for "
        "the hole \nand hit it well, you might just be able to get up.\n"
        "You're other option, which is a safer one, "
        "is to aim for the fringe \nto your right side.\n"
        )

    while True:
        play_iron_wood_choice = get_choice(
            "\nPress 1 to aim for the green.\n"
            "Press 2 to aim for the fringe.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_choice == 1:  # Aim for the green
            clear_terminal()
            play_iron_wood_green()
        elif play_iron_wood_choice == 2:    # Aim for the fringe
            clear_terminal()
            play_iron_wood_fringe()
        elif play_iron_wood_choice == 0:    # Leave game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_green():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nOps.. It was close but it didn't reach all the way up. "
        "Good effort!\n"
        "\nDo you want to try again or do you want to play the safer shot?\n"
        )

    while True:
        play_iron_wood_green_choice = get_choice(
            "\nPress 1 to try again.\n"
            "Press 2 to aim for the fringe.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_green_choice == 1:    # Another try
            clear_terminal()
            play_iron_wood_green_again()
        elif play_iron_wood_green_choice == 2:  # Aim for the fringe
            clear_terminal()
            play_iron_wood_green_fringe()
        elif play_iron_wood_green_choice == 0:  # Leave game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_green_again():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nWell done, you managed to get out of there, "
        "it's on the green \nbut far away from the hole.\n"
        "\nI'll set you up for a 2-putt and a score of 6, "
        "on a par 4 that means +2\n"
        )

    while True:
        play_iron_wood_green_again_choice = get_choice(
            "\nPress 1 to submit score of +2 and head back to Clubhouse.\n"
            "Press 2 to exit game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_green_again_choice == 1:  # Submit score
            update_leaderboard(2)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_iron_wood_green_again_choice == 2:    # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!"
                )
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_green_fringe():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nGood choice!\n"
        "\nSo, now your about 50 meters from the hole.\n"
        "If you're short it will come back to you because "
        "of the green's slope \nso it's better to be a bit long.\n"
        "\nWould you like to chip with a wedge or "
        'hit a "bump and run" with your 7 iron?\n'
        )

    while True:
        play_iron_wood_green_fringe_choice = get_choice(
            "\nPress 1 for wedge.\n"
            "Press 7 for 7 iron.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_green_fringe_choice == 1:     # Play wedge
            clear_terminal()
            play_iron_wood_green_fringe_chip()
        elif play_iron_wood_green_fringe_choice == 7:   # Bump and run
            clear_terminal()
            play_iron_wood_green_fringe_7iron()
        elif play_iron_wood_green_fringe_choice == 0:   # Leave game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_green_fringe_chip():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nYou got the perfect amount of length and spin on that shot!\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nIt ended up just 1 meter from the hole on the backside of it.\n"
        "But there's still work to do, these putts "
        "are sometimes the hardest.\n"
        "\nConcentrate, and put it in the hole.\n"
        )
    time.sleep(1.0)

    while True:
        play_iron_wood_green_fringe_chip_choice = get_choice(
            "\nPress 1 to submit score of +2 and head back to Clubhouse.\n"
            "Press 2 to exit game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_green_fringe_chip_choice == 1:    # Submit score
            update_leaderboard(2)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_iron_wood_green_fringe_chip_choice == 2:  # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!"
                )
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_green_fringe_7iron():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nWell done! That's just a tap in for a bogey.\n"
        "That means your score is +1.\n"
        )

    while True:
        play_iron_wood_green_fringe_7iron_choice = get_choice(
            "\nPress 1 to submit score of +1 and head back to Clubhouse.\n"
            "Press 2 to exit game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_green_fringe_7iron_choice == 1:   # Submit
            update_leaderboard(1)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_iron_wood_green_fringe_7iron_choice == 2:     # Leave
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!"
                )
            time.sleep(3.0)
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_fringe():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to choose next shot or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nGood choice!\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nSo, now your about 50 meters from the hole.\n"
        "\nIf you're short it will come back to you because of it's "
        "slope \nso it's better to be a bit long.\n"
        "\nWould you like to chip with a wedge or hit a "
        '"bump and run" with your 7 iron?\n'
        )

    while True:
        play_iron_wood_fringe_choice = get_choice(
            "\nPress 1 for wedge.\n"
            "Press 7 for iron.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_fringe_choice == 1:   # Play wedge
            clear_terminal()
            play_iron_wood_fringe_wedge()
        elif play_iron_wood_fringe_choice == 7:     # Bump and run
            clear_terminal()
            play_iron_wood_fringe_7iron()
        elif play_iron_wood_fringe_choice == 0:     # Leave
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_fringe_wedge():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nYou got a little bit to much spin on that one, "
        "and it rolled back a bit.\n"
        "\nIt's a bit far off the hole, I'll set you up for a 2-putt, "
        "which means you shot 6, on a par 4 that means +2.\n"
        )

    while True:
        play_iron_wood_fringe_wedge_choice = get_choice(
            "\nPress 1 to submit score of +2 and head back to Clubhouse.\n"
            "Press 2 to end game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_fringe_wedge_choice == 1:     # Submits score
            update_leaderboard(2)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_iron_wood_fringe_wedge_choice == 2:   # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!"
                )
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_wood_fringe_7iron():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nWell done! That's just a tap in for a bogey.\n"
        "That means your score is +1.\n"
        )

    while True:
        play_iron_wood_fringe_7iron_choice = get_choice(
            "\nPress 1 to submit your score of +1 "
            "and head back to Clubhouse.\n"
            "Press 2 to exit game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_wood_fringe_7iron_choice == 1:     # Submit
            update_leaderboard(1)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_iron_wood_fringe_7iron_choice == 2:   # Leave
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!")
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_layup():
    """
    - Tells the player the result of the previous choice,
    - Asks the player make another choice,
    - Runs the choice through get_choice function and return
    next function
    """
    print_slow(
        "\nGood choice.\n"
        )
    time.sleep(1.0)
    print_slow(
        "\nThat went further than I thought it would, you're on the fringe!\n"
        "\nYou can choose to chip this ball or putt, but the green is "
        "sloping \nback towards you so you can't be short.\n"
        )

    while True:
        play_iron_layup_choice = get_choice(
            "\nPress 1 to chip the ball.\n"
            "Press 2 to putt.\n"
            "Press 0 to exit game.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_layup_choice == 1:     # Chip ball
            clear_terminal()
            play_iron_layup_chip()
        elif play_iron_layup_choice == 2:   # Putt ball
            clear_terminal()
            play_iron_layup_putt()
        elif play_iron_layup_choice == 0:   # Leave game
            clear_terminal()
            print("Thank you for your visit, welcome back another time!")
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_layup_chip():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """

    print_slow(
        "\nGood chip, it stayed just one meter from the hole!\n"
        "\nBut there's still work to do, "
        "these putts are sometimes the hardest.\n"
        "Concentrate, and put it in the hole.\n"
        )
    time.sleep(1.0)

    while True:
        play_iron_layup_chip_choice = get_choice(
            "\nPress 1 to submit your score par and head back to Clubhouse.\n"
            "Press 2 to exit game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_layup_chip_choice == 1:    # Submit
            update_leaderboard(0)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_iron_layup_chip_choice == 2:  # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!")
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def play_iron_layup_putt():
    """
    - Tells the player the result of the previous shot,
    - Asks the player to submit score or leave the game,
    - Runs the choice through get_choice function and return
    next function
    """
    print_slow(
        "\nThat's how it's done! Right in the hole for BIRDIE!\n"
        "\nWell played, safe and sound from tee to hole. True pro!\n"
        )

    while True:
        play_iron_layup_putt_choice = get_choice(
            "\nPress 1 to submit your score of -1 and "
            "head back to Clubhouse.\n"
            "Press 2 to exit game without submitting your score.\n"
            + term.green + "\nEnter here: " + term.normal
        )

        if play_iron_layup_putt_choice == 1:    # Submit
            update_leaderboard(-1)
            print_slow("\nUpdating leaderboard...")
            time.sleep(1.0)
            clear_terminal()
            clubhouse()
        elif play_iron_layup_putt_choice == 2:  # Leave game
            clear_terminal()
            print(
                "\nThank you for giving me the chance to caddie for you. "
                "Welcome back another time!")
            time.sleep(3.0)
            exit()
        else:
            print(term.red + "Invalid choice. Try again!" + term.normal)


def main():
    """
    Runs the game
    """
    get_PLAYER_NAME()

    menu()
    rule_book()
    check_leaderboard()
    play_hole()


print_slow(     # Part 1 welcome message
    term.green + "Welcome to this little game called "
    "Random Round of Golf!\n" + term.normal
    )
logotype()      # Runs logotype in welcome message
time.sleep(1.0)
print_slow(     # Part 2 Welcome message
    "\nI'm Billy, your caddie for the day.\n"
    )
print_slow(
    "\nBefore we tee off, what name should I put in the scorecard?\n"
    + term.red + "(Make sure you only use letters, "
    "no whitespaces, when entering your name)\n" + term.normal
    )
main()
