# Made by Luboš Kulhan | alias: Adam Kaiser

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

    if no_one_came <= 5:
        min_value = max_value - 10
        RNG = random.randint(min_value,max_value)
    else:
        RNG = random.randint(min_value,max_value)

    while True:
        if RNG < step:
            print("Loading battle.tscn") # placeholder - change correspondingly
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
            elif step == milestone_2:
                sub = random.randint(5,10)
                min_value = milestone_2
                max_value -= sub
                if min_value < max_value:
                    RNG = random.randint(min_value,max_value)
                else:
                    max_value += sub
            elif step == milestone_3:
                sub = random.randint(5,10)
                min_value = milestone_3
                max_value -= sub
                if min_value < max_value:
                    RNG = random.randint(min_value,max_value)
                else:
                    max_value += sub
            elif step == milestone_4:
                sub = random.randint(5,10)
                min_value = milestone_4
                max_value -= sub
                if min_value < max_value:
                    RNG = random.randint(min_value,max_value)
                else:
                    max_value += sub
        step += 1