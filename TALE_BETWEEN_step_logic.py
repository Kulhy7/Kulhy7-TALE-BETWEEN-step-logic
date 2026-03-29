# Made by Luboš Kulhan | alias: Adam Kaiser
# step = 8/16/32 pixels
# first 20 steps = 0 chance for spawn
# location = what scene player is in
# each location has different spawn rate

import random

def stepcount():
    step = int(0)
    min_value = 20
    max_value = 100
    no_one_came = random.randint(0,100)
    milestone_1 = random.randint(30,40)
    milestone_2 = random.randint(50,60)
    milestone_3 = random.randint(70,80)
    milestone_4 = random.randint(90,100)

    # debug
    cathedral = 0
    hollow_bourg = 20
    stillroot_wilds = -20
    oblitus_keep = 10
    capital = -10
    laboratory = 10
    citadel = 0
    basalrealm = 50
    potion_of_transparency = False  # exploration item
    potion_of_visibilty = False     # farm item

    # debug
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

    if no_one_came <= 5:
        min_value = max_value - 10
        RNG = random.randint(min_value,max_value)
        print("But no one came...") # debug print
    else:
        RNG = random.randint(min_value,max_value)

    print(RNG) # debug print

    while True:
        if RNG < step:
            print(f"\nBattle begins after {RNG} steps.\nMin Value = {min_value}\nMax Value = {max_value}")  # debug print
            break

        if no_one_came > 5:
            if step == milestone_1:
                sub = random.randint(5,10)
                min_value = milestone_1
                max_value -= sub
                if min_value < max_value:
                    RNG = random.randint(min_value,max_value)
                else:
                    max_value += sub
                print(f"You hear strange sounds, RNG = {RNG}") # debug print
            elif step == milestone_2:
                sub = random.randint(5,10)
                min_value = milestone_2
                max_value -= sub
                if min_value < max_value:
                    RNG = random.randint(min_value,max_value)
                else:
                    max_value += sub
                print(f"You feel something closing in , RNG = {RNG}") # debug print
            elif step == milestone_3:
                sub = random.randint(5,10)
                min_value = milestone_3
                max_value -= sub
                if min_value < max_value:
                    RNG = random.randint(min_value,max_value)
                else:
                    max_value += sub
                print(f"Its getting closer , RNG = {RNG}") # debug print
            elif step == milestone_4:
                sub = random.randint(5,10)
                min_value = milestone_4
                max_value -= sub
                if min_value < max_value:
                    RNG = random.randint(min_value,max_value)
                else:
                    max_value += sub
                print(f"You feel someone breathing down your neck , RNG = {RNG}") # debug print

        step += 1

stepcount()