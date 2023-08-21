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


def update_leaderboard(score):
    """
    Function to update leaderboard
    """
    sheet = SHEET.get_worksheet(0)
    row_data = [player_name, int(score)]
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
            score_str = entry['Score']
            print(f"Raw Score value for {name}: {score_str}")
            try:
                score = int(score_str)
                if name in aggregated_scores:
                    aggregated_scores[name] += score
                else:
                    aggregated_scores[name] = score
            except ValueError:
                print(f"Unable to convert score value for {name} to int: {score_str}")
                continue

            # if name in aggregated_scores:
                # aggregated_scores[name] += score
            # else:
                # aggregated_scores[name] = score

        sorted_leaderboard = sorted(aggregated_scores.items(), key=lambda x: x[1])

        print("\nLeaderboard\n")
        for i, (name, score) in enumerate(sorted_leaderboard, start=1):
            print(f"{i}. {name} - Score: {score}")
        print()


check_leaderboard() 



