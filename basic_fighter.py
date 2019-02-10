# Most basic fantasy combat simulator
import random

p_health = 5
g_health = 5
goblin_alive = True

def status():
    if g_health == 5:
        return "\nA menacing goblin stands before you..."
    elif g_health >= 3:
        return "\nThe goblin is looking a little tired, and is bleeding..."
    elif g_health >= 1:
        return "\nThe goblin is bleeding horribly and looks enraged..."

while goblin_alive:
    if g_health <= 0:
        goblin_alive = False
        print("\nCongrats you slayed the goblin!")
        again = input("Play again? Y/N: ")

        if again == 'y' or again == 'Y':
            goblin_alive = True
        elif again == 'N' or again == 'n':
            print("\nGoodbye")
            exit()
    if p_health <= 0:
        print("Oh dear you have died horribly and the goblin cuts your head off for a trophy...")
        again = input("Play again? Y/N: ")

        if again == 'y' or again == 'Y':
            p_health = 5
            g_heath = 5
            goblin_alive = True
        elif again == 'N' or again == 'n':
            print("\nGoodbye")
            exit()
            
    desc = status()
    print(desc)
    print("You have " + str(p_health) + ' hit points.')

    attack = input("Press enter to attack: ")
    if attack == '':
        print("\nYou swing your sword fiercely at the goblin!")
        hit_type = random.randint(1, 2)
        if hit_type == 1:
            damage = random.randint(1, 3)
            print("You deal a fierce blow for " + str(damage) + " damage to the goblin.")
            g_health = g_health - damage
        elif hit_type == 2:
            damage = random.randint(1, 3)
            print("The goblin slashes you for " + str(damage) + " damage, uh oh...")
            p_health = p_health - damage
    else:
        print("\nYou better do something...")
