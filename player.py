from checks import is_a_number
import random
from constant import DICE_VALUE

def player_gen():
    amount = input("Set player amount: ")   
    if not is_a_number(amount):
        return False 
    amount = int(amount)
    
    players = {f"p{i}": {"dice": None, "points": None} for i in range(1, amount + 1)}
    return players

def player_dice(dict):
    for key in dict:
        dice = (random.randint(1, 6), random.randint(1, 6))
        dict[key]["dice"] = tuple(sorted(dice ,reverse=True))
    return dict

def win(dict):
    players = dict
    for player in players:
        players[player]["points"] = DICE_VALUE[players[player]["dice"]]

    return players
 

