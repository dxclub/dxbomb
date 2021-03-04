import time, sys, time, os, gspread
from ascii_art import congrats, boom
from time import sleep
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

# This DxClub Cybersecurity Challenge was a part of numerous routine 
# challenges the club would do during the first 10 minutes of a meeting.
# The goal of this challenge is to not only teach members about the fundamentals
# of cryptography but also to learn it in a fun way! 

# Most of this code was made by Luis Plascencia, any code taken from outside sources will
# be linked in a comment next to its corresponding place! This challenge took place 
# on February 3, 2021.

def main():
    # Configurations for connecting to the Google Sheets/Drive API 
    scope = ["https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets", 
            "https://www.googleapis.com/auth/drive.file", 
            "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("ENTERGOOGLESHEETSNAMEHERE").sheet1
    
    # Prints all the instructions for the challenge
    type_writer("Hello there... I have placed a bomb in this zoom meeting! Disarm me before things get messy...\n", 0.05)
    time.sleep(1)
    type_writer('------------------------------------------------------\n', 0.01)
    type_writer("VIGENERE CIPHER: JOAYSPCANPOEUWQ\n", 0.05)
    type_writer("KEY: BOOM\n", 0.05)
    type_writer('------------------------------------------------------\n', 0.01)
    type_writer("ROT13 CIPHER: OBBZTBRFGURQLANZVGR\n", 0.05)
    type_writer('------------------------------------------------------\n', 0.01)
    type_writer("MORSE CODE: -... .. - .-.-.- .-.. -.-- -..-. ...-- - ----. ...- .--. -- -\n", 0.05)
    type_writer('------------------------------------------------------\n', 0.01)
    time.sleep(3)
    progress("Arming the bomb...")
    print("\n")

    # Keeps track of challenge completions
    solved = [False, False, False]

    # Timer: 600 seconds for 10 mins
    for i in range(600, 0, -1):
        mins = i // 60
        sec = i % 60
        print(f"Countdown: {mins:02d}:{sec:02d} mins", end = '\r')
        sleep(1)
        data = sheet.get_all_records()

        # Constantly checks google sheets for any of the answers being inputted by a team.
        for i in range(len(data)):

            team = data[i]['Team Name']
            answer = data[i]["Answer"]

            # If the answer for vigenere cipher is found
            if("IAMMRBOOMBASTIC" in answer.upper() and solved[0] == False):
                print(f"\r{team} solved the cipher! The vigenere cipher was: IAMMRBOOMBASTIC\n")
                sheet.update_cell(i+2, 3, "VIGENERE_WINNER")
                solved[0] = True

            # If the answer for the rot13 cipher is found
            elif("BOOMGOESTHEDYNAMITE" in answer.upper() and solved[1] == False):
                print(f"\r{team} solved the cipher! The rot13 cipher was: BOOMGOESTHEDYNAMITE\n")
                sheet.update_cell(i+2, 3, "ROT13_WINNER")
                solved[1] = True

            # If the answer for the morse code is found
            elif("bit.ly/3t9vpmt" in answer.lower() and solved[2] == False):
                print(f"""\r{team} solved the cipher! The morse code cipher was: bit.ly/3t9vpmt | Check the link out!\n""")
                sheet.update_cell(i+2, 3, "MORSE_WINNER")
                solved[2] = True

            # If the answer for the morse code is found (assuming person clicked the bitly link)
            elif("RICKROLLED" in answer.upper() or "NEVERGONNAGIVEYOUUP" in answer.upper() and solved[2] == False):
                print(f"\r{team} got Rick Rolled! The morse code cipher was: bit.ly/3t9vpmt | Other possible answers: RICKROLLED or NEVERGONNAGIVEYOUUP\n")
                sheet.update_cell(i+2, 3, "MORSE_WINNER")
                solved[2] = True

            # If all challenges are solved
            if(solved.count(True) == 3):
                type_writer("CONGRATULATIONS! YOU HAVE SOLVED THE DXCLUB CYBER CHALLENGE!", 0.05)
                type_writer(congrats(), 0.005)
                return("")
    
    # Competitors did not solve the challenge
    print("\r")
    type_writer(boom(), 0.005)
    type_writer("\nBOOOOOOOOOOOM!", 0.05)
    type_writer("\nBetter luck next time...", 0.05)
    type_writer("\nThe vigenere cipher was: IAMMRBOOMBASTIC", 0.05)
    type_writer("\nThe rot13 cipher was: BOOMGOESTHEDYNAMITE", 0.05)
    type_writer("\nThe morse code cipher was: bit.ly/3t9vpmt | Other possible answers: RICKROLLED or NEVERGONNAGIVEYOUUP", 0.05)

# Source: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# Continously prints the progress characters to create a download/upload progress bar animation
def progress(process):
    items = list(range(0, 30))
    ls = len(items)
    progress_settings(0, ls, prefix=process, suffix='Complete', length=50)
    for i, item in enumerate(items):
        time.sleep(0.1)
        progress_settings(i + 1, ls, prefix=process, suffix='Complete', length=50)

# Creates the chars for the progress bar in the console
def progress_settings(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=print_end)
    if iteration == total:
        print()

# Source: https://stackoverflow.com/questions/20302331/typing-effect-in-python
# Type writer animation for the console!
def type_writer(message, speed):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


if __name__ == '__main__':
    main()