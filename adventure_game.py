# Very Basic Text Based Game

def die():
    print("You are dead, so sorry")
    exit()

def end():
    print("Goodbye")
    exit()


print("Welcome to the great story game")

player_name = input("Enter in your name please: ")
print("Hello, " + player_name + " you are a brave knight")

print("Your great adventure starts, as you enter a cave you are faced with a choice, also you have no weapons")

door_not = True
door_pick = False
sword = False
cup = False
while door_not:
    door_choice = input("\nDo you pick the red door or blue door? Type in 'red' or 'blue'")
    if door_choice == 'red':
        door1 = 'red'
        door_pick = True
    elif door_choice == 'blue':
        door1 = 'blue'
        door_pick = True
    else:
        dor_not = True

    if door_pick:
        if door1 == 'red':
            fight = input("\nIn front of you is a fierce red dragon? Fight Y/N?")
            if fight == 'Y' or fight == "y":
                if cup == True:
                    print("Because you drank from the Holy Grail you are immortal")
                    print("The flames do nothing")
                    print("The dragon gets annoyed and wanders away leaving all it's treasure")
                    print("You win the game!")
                    end()
                if sword == True:
                    print("\nBecause of your awesome sword you can slay the fierce dragon")
                    print("You win!")
                    end()
                elif sword == False or cup == False:
                    print("\nBecause you have no weapons you die horribly from dragon fire")
                    die()
            elif fight == 'N' or fight == 'n':
                print("\nYou are very smart and return to the first room")
                door_not = True
        elif door1 == 'blue':
            print("\nAs you enter into the room with the blue door you see the following:")
            if sword == False and cup == False:
                print("You see a table with a sword and a cup.")
                object_choice = input("What will you pick up the cup or the sword? ")
                if object_choice == 'sword':
                    print("\nYou pick up the sword and feel more powerful")
                    sword = True
                elif object_choice == 'cup':
                    cup = True
                    print("\nThe cup fills with a strange potion that you drink")
                    print("You feel immortal")
            elif sword == True or cup == True:
                print("You see an empty table, go try the red door")
                

    
