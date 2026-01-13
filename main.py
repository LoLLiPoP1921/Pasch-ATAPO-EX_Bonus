from player import player_gen, player_dice, show_winner, win
from constant import DICE_VALUE
from checks import exit_game
import os

def main():
    os.system("clear")
    print("Press CTRL+C to quite the game")
    players = {}

    try:
        while True:
            while True:
                players = player_gen()
                if not players:
                    print("Player amount needs to be a number above 1")
                else:
                    break      
      
            players = player_dice(players)
            players = win(players)
            os.system("clear")
            for player in players:
                print(f"{player} has rolled {players[player]["dice"]} and scored {players[player]["points"]} points")
                input("press ENTER to show next player...")
                os.system("clear")

            show_winner(players)


            if not exit_game():
                break

    except KeyboardInterrupt:
        print("\nPasch stopped.")

if __name__ == "__main__":
    main()
