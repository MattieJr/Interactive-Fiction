# The Forest
# Interactive Fiction
# Reagan Barrington

# Setup

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
enemy_troll = "defeated"
stranger = ["hello," "goodbye"]

 
# Introduction
name = raw_input("What is your name, adventurer? ")
race = raw_input("Are you an elf, human, orc, or hafling? ")

import weapons
from weapons import weapon

print("Greetings, " + name + " the " + race +". Let us go on a quest! ")
print("You find yourself on the edge of a dark forest. ")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = raw_input("Would you like to step into the forest?  yes/no \n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are a coward and a disgrace to " + race +"s everywhere, " + name + ". Come back when you develop a worthy sense of adventure. Goodbye.")
        quit()
    else: 
        print("I didn't understand that.\n")


 
# Part 1: First direction
response = ""
while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = raw_input("What direction do you move?\nleft/right/forward/backward\n")
# bear storyline
    if response == "left":
        # paste import here if doesnt work
        print("The bear lifts its gaze. \n")
        if weapon == "sword":
            print("You slowly unsheath your sword, watching the bear carefully. It stares for a minute, then turns and runs. You take a sigh of relief, happy to let the animal go, and return your sword to its place on your side. \n")
        elif weapon == "bow":
            print("You've armed yourself with your bow. Plenty of arrows, too. You watch the bear carefully. It stares for a minute, then turns and runs. You take a sigh of relief, happy to let the animal go. \n")
        elif weapon == "knife":
            print("You've only remembered your knife. Not the best weapon against a bear, but you trust in your training. The bear stares at you for a minute, then turns and runs. You take a sigh of relief, happy to let the animal go, and return your knife to its place in your boot. \n")
        elif weapon == "axe":
            print("Your favorite weapon: the axe.... The bear stares at you for a minute, then turns and runs. You take a sigh of relief, happy to let the animal go, and return your axe to its place on your belt. \n")
        else:
            print("I didn't understand that.")
            response = ""

  
    elif response == "right":
      weapon_type = "none"
      print("You head deeper into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")


# ENEMY: Troll
import enemy as en
foe=en.Enemy("troll","great axe")
print("You meet a " + foe.enemy + " wielding a " + foe.weapon)
print("You reach for your " + weapon + ", knowing you won't avoid a fight this time. He swings at you but misses.")
# main enemy loop
while True:
   
    print("Type the a key and then RETURN to attack.")

    action=raw_input()

    if action.lower() == "a":
        foe.fight(foe)

    if foe.alive == False:
        print("You have won...this time. \n")
        break
    

# Part 2: Meet a Stranger
response = ""
while response not in stranger:
  print("You continue walking in the forest. You recognize a stream you pass. They call it the halfling stream of Normoon. \n")
  break

import enemy as en
foe=en.Enemy("deer","")
print("You see a " + foe.enemy)
print("You reach for your " + weapon + ", feeling your stomach rumble.")
# main enemy loop
while True:
   
    print("Type the a key and then RETURN to attack.")

    action=raw_input()

    if action.lower() == "a":
        foe.fight(foe)

    if foe.alive == False:
        print("You take down the deer...thankful to have dinner. \n")
        break


  
