import os

def is_a_number(str):
    if str.isdigit():
        str = int(str) 
    else:
        return False

    if str <= 1:
        return False
    
    return True

def exit_game():
    while True:
        play_again = input("Do you want to play again (Y/N)")
        if play_again.upper() == "N":
            print("good bye")
            return False
        elif play_again.upper() == "Y":
            print("here we go again")
            return True
        else:
            print("Need to be Y/N")

        