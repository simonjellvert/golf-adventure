import gspread
from google.oauth2.service_account import Credentials
import time
import os

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
    os.system('clear')


player_name = None


def get_player_name():
    """
    # Asks user for name
    """

    global player_name

    if player_name is None:
        while True:   
            name = input("Enter your name: ")

            if valid_name(name):
                clear_terminal()
                print(f"\nThank you {name}, great to meet you!\n") # Make text green
                player_name = name
                break


def valid_name(name):
    """
    # Checks if the name contains only letters (no numbers or symbols)
    """
    if name.isalpha():  # Check if the name contains only alphabetic characters
        return True
    else:
        print("Invalid name. Try again!.\n") # Make text red
        return False


def menu():
    """
    Gives the user options of play game, see the leaderboard, see the rules or quit game"
    """
    while True:
        print("We are now at the Clubhouse, what would you like to do?\n")
        print("Start game? Press 1")
        print("Check out the leaderboard? Press 2")
        print("Check out the rule book of Random Golf? Press 3")
        print("Do you want to come back later? Press 4")
        menu_choice = input("").strip()

        try:
            index = int(menu_choice)
            if index == 1:
                #clear_terminal()
                print("\nLaunching game...\n")
                play_hole()
                break
            elif index == 2:
                #clear_terminal()
                print("\nLoading leaderboard...\n")
                check_leaderboard()
                break
            elif index == 3:
                #clear_terminal()
                print("\nLoading rule book...\n")
                rule_book()
                break
            elif index == 4:
                #clear_terminal()
                print("\nThank you for visiting, welcome back another time!")
                exit()
            else:
                print("\nInvalid choice. Try again!\n")
        except ValueError:
            print("\nInvalid choice. Try again!\n")


def rule_book():
    """
    Explains the rule of the game for the user. With options to return to "club house"
    """
    file_path = 'text_files/rule_book.txt'
    with open(file_path, 'r') as file:
        content = file.read()

    #clear_terminal()
    print(content)
    clubhouse()


def clubhouse():
    """
    Function to let the user return to the menu
    """
    print("\nPress 1 to return to Clubhouse")
    to_clubhouse = input("")
    try:
        index = int(to_clubhouse)
        if index == 1:
            clear_terminal()
            print("\nHeading back to the Clubhouse...\n")
            menu()
        else:
            print("\nInvalid choice. Try again!\n")
            clubhouse()
    except ValueError:
        print("\nInvalid choice. Try again!\n")
        clubhouse()


def update_leaderboard(score):
    """
    Function to update leaderboard
    """
    sheet = SHEET.get_worksheet(0)
    row_data = [player_name, str(score)]
    sheet.append_row(row_data)


def check_leaderboard():
    sheet = SHEET.get_worksheet(0)
    leaderboard = sheet.get_all_records()
    if not leaderboard:
        print("The leaderboard is empty.\n")
    else:
        aggregated_scores = {}
        for entry in leaderboard:
            name = entry['Name']
            score = int(entry['Score'])
            if name in aggregated_scores:
                aggregated_scores[name] += score
            else:
                aggregated_scores[name] = score

        sorted_leaderboard = sorted(aggregated_scores.items(), key=lambda x: x[1])

        print("\nLeaderboard\n")
        for i, (name, score) in enumerate(sorted_leaderboard, start=1):
            print(f"{i}. {name} - Score: {score}")
        print()


def play_hole():
    """
    Function that starts the game.
    """
    print(f"Feeling warmed up? Perfect! Let's get this round started\n")
    print("This is our first hole, it's a 350 meters long par 4.\n")
    print("The left side is out of bounce, which means if you hit it there you are going to need to hit your 3rd shot from the tee box.\n")
    print("On the right side there's a grove, if you hit it there you might have to just lay up.\n")
    print("You can either choose to hit a driver, with the risk of ending up in one of the hazards. Or you can choose the play a safe shot, which is a long iron.\n")

    first_shot = get_choice("Press 1 for driver.\nPress 2 for iron.\nPress 0 to exit game.\n")

    if first_shot == 1:     # Driver
        clear_terminal()
        play_driver_shot()
    elif first_shot == 2:   # Iron
        clear_terminal()
        play_iron_shot()
    elif first_shot == 0:   # Exit game
        exit()


def get_choice(prompt):
    try:
        index = int(input(prompt))
        return index
    except ValueError:
        print("Invalid choice. Try again!")
        return get_choice(prompt)


def play_driver_shot():
    print("Nice shot, you avoided the out of bounce and ended up in the rough on the right hand side.\n")
    print("You're now 125 meters away from the hole. There's a bunker on the back side of the green and on the left side, the left one is really steep and is hard to get out of.")
    print("You normally play your 7 iron from this distance, but maybe it's better to play the 8 iron, which goes shorter?\n")

    driver_choice = get_choice("Press 7 for 7 iron.\nPress 8 for 8 iron.\nPress 0 to exit game.\n")

    if driver_choice == 7:
        clear_terminal()
        play_7_iron_shot()
    elif driver_choice == 8:
        clear_terminal()
        play_8iron_shot()
    elif driver_choice == 0:
        exit()


def play_7_iron_shot():
    print("Here's your 7 iron. Good luck!\n")
    print("You hit that really well, but it looked like it went a bit far. Let's go check where it ended up.\n")
    print("Oh, you're in the bunker on the back of the green. The hole is in the center of the green, but after the hole it will run away, so it's better to be a bit short.")
    print("Do you want to hit it short or do you want to go for the hole?\n")

    driver_7iron_choice = get_choice("Press 1 to aim for the hole.\nPress 2 for the shorter shot.\nPress 0 to exit game.\n")
    
    if driver_7iron_choice == 1:
        clear_terminal()
        play_driver_7iron_hole_shot()
    elif driver_7iron_choice == 2:
        clear_terminal()
        play_driver_7iron_short_shot()
    elif driver_7iron_choice == 0:
        clear_terminal()
        exit()


def play_driver_7iron_hole_shot():
    print("WOW! You managed to get it to stop just one meter from the hole, well done!\n")
    print("But there's still work to do, theese putts are sometimes the hardest.")
    print("Concentrate, and put it in the hole.\n")

    driver_7iron_hole_choice = get_choice(
        "Press 1 to submit score of par and head back to Clubhouse.\nPress 2 to end game without submitting your score.\n"
        )
    
    if driver_7iron_hole_choice == 1:
        update_leaderboard(0)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif driver_7iron_hole_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. I will not submit your score, since you didn't complete the round. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_driver_7iron_short_shot():
    print("Oh no, it's a little too short and got stuck on the fringe...\n")
    print("Now, if you choose to chip there is a possibility that you hit it too far and roll of the green, but on the other hand - if you hit it well you avoid undulations ahead of the hole.")
    print("If you choose to put, you need to read the line carefully.\n")

    driver_7iron_short_choice = get_choice(
        "Press 1 to chip the ball.\nPress 2 to putt the ball.\nPress 0 to exit game.\n"
    )

    if driver_7iron_short_choice == 1:
        clear_terminal()
        play_driver_7iron_short_chip_shot()
    elif driver_7iron_short_choice == 2:
        clear_terminal()
        play_driver_7iron_short_putt_shot()
    elif driver_7iron_short_choice == 0:
        exit()


def play_driver_7iron_short_chip_shot():
    print("Ops...it's a duff...\n")
    print("But it rolled out a bit but it's too far off the hole.")
    print("I'll set you up for a 2-putt and a score of 6, on a par 4 that means +2.\n")

    play_driver_7iron_short_chip_choice = get_choice(
        "Press 1 to submit score and head back to Clubhouse.\nPress 2 to end game without submitting your score.\n"
    )

    if play_driver_7iron_short_chip_choice == 1:
        update_leaderboard(2)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_driver_7iron_short_chip_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_driver_7iron_short_putt_shot():
    print(f"Nice putt , that's a tap in for a 5. On a par 4 that means your score in +1.")
    
    play_driver_7iron_short_putt_choice = get_choice(
        "Press 1 to submit score of +1 and head back to Clubhouse.\nPress 2 to end game without submitting your score.\n"
    )

    if play_driver_7iron_short_putt_choice == 1:
        update_leaderboard(1)
        print("\nUpdating leaderboard...")
        clear_terminal()
        clubhouse()
    elif play_driver_7iron_short_putt_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. I will not submit your score, since you didn't complete the round. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_8iron_shot():
    print("Nice shot! That ball came out smooth from the rough!\n")
    print("You're pin high on the right side of the green, on the fringe.")
    print("If you chip the ball you avoid undulations ahead of the hole but risk hitting it short or long.")
    print("If you choose to putt, you need to read the green carefully\n")

    driver_8iron_choice = get_choice("Press 1 to chip the ball.\nPress 2 to putt.\nPress 0 to exit game.\n")

    if driver_8iron_choice == 1:
        clear_terminal()
        play_driver_8iron_chip_shot()
    elif driver_8iron_choice == 2:
        clear_terminal()
        play_driver_8iron_putt_shot()
    elif driver_8iron_choice == 0:
        exit()


def play_driver_8iron_chip_shot():
    print("OH! You chipped right in the hole!!\n")
    print("That's a birdie! I'll put a 3 on the scorecard, on a par 4 that means -1.\n")

    driver_8iron_chip_choice = get_choice(
        "Press 1 to submit score of -1 and head back to Clubhouse.\nPress 2 to end game without submitting your score.\n"
    )

    if driver_8iron_chip_choice == 1:
        update_leaderboard(-1)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif driver_8iron_chip_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_driver_8iron_putt_shot():
    print("Nice putt, that was very close!")
    print("That's just a tap in for par.\n")

    play_driver_8iron_putt_choice = get_choice(
        "Press 1 to submit score of par and head back to Clubhouse.\nPress 2 to exit game without submitting your score.\n"
    )

    if play_driver_8iron_putt_choice == 1:
        update_leaderboard(0)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_driver_8iron_putt_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. I will not submit your score, since you didn't complete the round. Welcome back another time!")
        time.sleep(3)
        exit()


def play_iron_shot():
    print(f"Really nice iron shot, that went straight down the middle of the fairway!\n")
    print("Now you have 180 meters to the green, that's quite long.")
    print("On the left side of the green there is a steep bunker, and there's another one on the back side of the green.")
    print("You can either choose to play a fairway wood that should take you to the green but risks ending up in one of the bunkers.")
    print("Or you can play it safe and lay up for a chip shot.\n")

    play_iron_choice = get_choice(
        "Press 1 to hit a fairway wood.\nPress 2 to lay up.\nPress 0 to exit game.\n"
    )

    if play_iron_choice == 1:
        clear_terminal()
        play_iron_wood()
    elif play_iron_choice == 2:
        clear_terminal()
        play_iron_layup()
    elif play_iron_choice == 0:
        exit()


def play_iron_wood():
    print("Oh no, wind is taking it to the left...\n")
    print("Unfortunately it looks like you're in the steep bunker.")
    print("This bunker is really hard to get out of. If you aim for the hole and hit it well, you might just be able to get up.")
    print("You're other option, which is a safer one, is to aim for the fringe to your right side.\n")

    play_iron_wood_choice = get_choice(
        "Press 1 to aim for the green.\nPress 2 to aim for the fringe.\nPress 0 to exit game.\n"
    )

    if play_iron_wood_choice == 1:
        clear_terminal()
        play_iron_wood_green()
    elif play_iron_wood_choice == 2:
        clear_terminal()
        play_iron_wood_fringe()
    elif play_iron_wood_choice == 0:
        exit()


def play_iron_wood_green():
    print("Ops.. It was close but it didn't reach all the way up. Good effort!\n")
    print("Do you want to try again or do you want to play the safer shot?")

    play_iron_wood_green_choice = get_choice(
        "Press 1 to try again.\nPress 2 to aim for the fringe.\nPress 0 to exit game.\n"
    )

    if play_iron_wood_green_choice == 1:
        clear_terminal()
        play_iron_wood_green_again()
    elif play_iron_wood_green_choice == 2:
        clear_terminal()
        play_iron_wood_green_fringe()
    elif play_iron_wood_green_choice == 0:
        exit()


def play_iron_wood_green_again():
    print("Well done, you managed to get out of there, it's on the green but far away from the hole.")
    print("I'll set you up for a 2-putt and a score of 6, on a par 4 that means +2\n")

    play_iron_wood_green_again_choice = get_choice(
        "Press 1 to submit score of +2 and head back to Clubhouse.\nPress 2 to exit game without submitting your score.\n"
    )

    if play_iron_wood_green_again_choice == 1:
        update_leaderboard(2)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_iron_wood_green_again_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_iron_wood_green_fringe():
    print("Good choice!\n")
    print("So, now your about 50 meters from the hole. If you're short it will come back to you because of it's slope so it's better to be a bit long.")
    print("Would you like to chip with a wedge or hit a 'bump and run' with your 7 iron?")

    play_iron_wood_green_fringe_choice = get_choice(
        "Press 1 for wedge.\nPress 7 for 7 iron.\nPress 0 to exit game.\n"
    )

    if play_iron_wood_green_fringe_choice == 1:
        clear_terminal()
        play_iron_wood_green_fringe_chip()
    elif play_iron_wood_green_fringe_choice == 7:
        clear_terminal()
        play_iron_wood_green_fringe_7iron()
    elif play_iron_wood_green_fringe_choice == 0:
        exit()


def play_iron_wood_green_fringe_chip():
    print("You got the perfect amount of length and spin on that shot!")
    print("It ended up just 1 meter from the hole on the backside of it.\n")
    print("But there's still work to do, theese putts are sometimes the hardest.")
    print("Concentrate, and put it in the hole.\n")

    play_iron_wood_green_fringe_chip_choice = get_choice(
        "Press 1 to submit score of +2 and head back to Clubhouse.\nPress 2 to exit game without submitting your score.\n"
    )

    if play_iron_wood_green_fringe_chip_choice == 1:
        update_leaderboard(2)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_iron_wood_green_fringe_chip_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_iron_wood_green_fringe_7iron():
    print(f"Well done! That's just a tap in for a bogey. that means your score is +1.\n")

    play_iron_wood_green_fringe_7iron_choice = get_choice(
        "Press 1 to submit score of +1 and head back to Clubhouse.\nPress 2 to exit game without submitting your score.\n"
    )

    if play_iron_wood_green_fringe_7iron_choice == 1:
        update_leaderboard(1)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_iron_wood_green_fringe_7iron_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_iron_wood_fringe():
    print(f"Good choice!")
    print("So, now your about 50 meters from the hole. If you're short it will come back to you because of it's slope so it's better to be a bit long.")
    print("Would you like to chip with a wedge or hit a 'bump and run' with your 7 iron?")

    play_iron_wood_fringe_choice = get_choice(
        "Press 1 for wedge.\nPress 7 for iron.\nPress 0 to exit game.\n"
    )

    if play_iron_wood_fringe_choice == 1:
        clear_terminal()
        play_iron_wood_fringe_wedge()
    elif play_iron_wood_fringe_choice == 2:
        clear_terminal()
        play_iron_wood_fringe_7iron()
    elif play_iron_wood_fringe_choice == 0:
        exit()


def play_iron_wood_fringe_wedge():
    print("You got a little bit to much spin on that one, and it rolled back a bit.")
    print("It's a bit far off the hole, I'll set you up for a 2-putt.")
    print("which means you shot 6, on a par 4 that means +2.")

    play_iron_wood_fringe_wedge_choice = get_choice(
        "Press 1 to submit score of +2 and head back to Clubhouse.\nPress 2 to end game.\n"
    )

    if play_iron_wood_fringe_wedge_choice == 1:
        update_leaderboard(2)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_iron_wood_fringe_wedge_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_iron_wood_fringe_7iron():
    print(f"Well done! That's just a tap in for a bogey. that means your score is +1.\n")

    play_iron_wood_fringe_7iron_choice = get_choice(
        "Press 1 to submit your score of +1 and head back to Clubhouse.\nPress 2 to exit game without submitting your score.\n"
    )

    if play_iron_wood_fringe_7iron_choice == 1:
        update_leaderboard(1)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_iron_wood_fringe_7iron_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_iron_layup():
    print(f"Good choice.\n")
    print("That went further than I thought it would, you're on the fringe!")
    print("You can choose to chip this ball or putt, but the green is sloping back towards you so you can't be short.\n")

    play_iron_layup_choice = get_choice(
        "Press 1 to chip the ball.\nPress 2 to putt.\nPress 0 to exit game.\n"
    )

    if play_iron_layup_choice == 1:
        clear_terminal()
        play_iron_layup_chip()
    elif play_iron_layup_choice == 2:
        clear_terminal()
        play_iron_layup_putt()
    elif play_iron_layup_choice == 0:
        exit()


def play_iron_layup_chip():
    print("Good chip, it stayed just one meter from the hole!\n")
    print("But there's still work to do, theese putts are sometimes the hardest.")
    print("Concentrate, and put it in the hole.\n")

    play_iron_layup_chip_choice = get_choice(
        "Press 1 to submit your score par and head back to Clubhouse.\nPress 2 to exit game without submitting your score.\n"
    )

    if play_iron_layup_chip_choice == 1:
        update_leaderboard(0)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_iron_layup_chip_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def play_iron_layup_putt():
    print("That's how it's done! Right in the hole for BIRDIE!")
    print(f"Well played, safe and sound from tee to hole. True pro!\n")
    print("Press 1 to submit score.")
    print("Press 2 to end game.")

    play_iron_layup_putt_choice = get_choice(
        "Press 1 to submit your score of -1 and head back to Clubhouse.\nPress 2 to exit game without submitting your score.\n"
    )

    if play_iron_layup_putt_choice == 1:
        update_leaderboard(-1)
        print("\nUpdating leaderboard...")
        time.sleep(1.0)
        clear_terminal()
        clubhouse()
    elif play_iron_layup_putt_choice == 2:
        clear_terminal()
        print(f"\nThank you for giving me the chance to caddie for you. Welcome back another time!")
        time.sleep(3.0)
        exit()


def main():
    """
    Runs the game
    """
    get_player_name()

    menu()
    rule_book()
    play_hole()


print("Welcome to this little game called Random Round of Golf!\n")
print("I'm Billy, your caddie for the day.\n")
print("Before we tee off, what name should I put in the scorecard?")
print("(Make sure you only use letters, no whitespaces, when entering your name)\n")
main()
