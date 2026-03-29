# Made by Luboš Kulhan | alias: Adam Kaiser
# step = 16 pixels
# first 20 steps = 0 chance for spawn
# location = what scene player is in
# each location will have different spawn rate

import random

def stepcount():
    step = 1
    min_value = 20
    max_value = 100

    cathedral = 0
    hollow_bourg = 20
    stillroot_wilds = -20
    oblitus_keep = 10
    capital = -10
    laboratory = 10
    citadel = 0
    basalrealm = 50

    potion_of_transparency = False  # exploration item
    potion_of_visibilty = True     # farm item

    # debug decision
    location = int(input("cathedral = 1\nhollow_bourg = 2\nstillroot_wilds = 3\noblitus_keep = 4\ncapital = 5\nlaboratory = 6\ncitadel = 7\nbasalrealm = 8\nupperealm = 9\nInput number: "))

    match location:
        case 1:
            max_value += cathedral
        case 2:
            max_value += hollow_bourg
        case 3:
            max_value += stillroot_wilds
        case 4:
            max_value += oblitus_keep
        case 5:
            max_value += capital
        case 6:
            max_value += laboratory
        case 7:
            max_value += citadel
        case 8:
            max_value += basalrealm
        case 9:
            print("Only one foe is present...")
            exit()
    
    if potion_of_transparency:
        min_value += 10
        max_value += 25
    elif potion_of_visibilty:
        min_value -= 10
        max_value -= 25

    RNG = random.randint(min_value,max_value)
    while True:
        if RNG < step:
            print(f"\nBattle begins after {RNG} steps.\nMin Value = {min_value}\nMax Value = {max_value}")
            break

        step += 1
        if step == 30:
            RNG -= 5
            print("You hear strange sounds") # debug print
        elif step == 50:
            RNG -= 5
            print("You feel something closing in") # debug print
        elif step == 70:
            RNG -= 5
            print("Its getting closer") # debug print
        elif step == 90:
            RNG -= 5
            print("You feel someone breathing down your neck") # debug print

stepcount()