class character:
    def __init__(self, name, hp, arm, termwnds, coin, srcy, strn, inte,
                 crg, srdmp, arch, attk, arr, food, flu):
        self.name=name
        self.health=hp
        self.armour=arm
        self.terminal_wounds=termwnds
        self.coin=coin
        self.sorcery=srcy
        self.strength=strn
        self.intelligence=inte
        self.courage=crg
        self.swordsmanship=srdmp
        self.archery=arch
        self.attack=attk
        self.arrows=arr
        self.food=food
        self.fluid=flu
from random import randint
armour_dictionary={"iron horned helm":0.75, "cloth shirt":0.5, "padded torso armour":1.5, "marching boots":0.5,
        "padded gloves":0.5, "chainmail chestpiece":2.5, "oak buckler":1}
armour_list=["iron horned helm", "cloth shirt", "padded torso armour", "marching boots", "padded gloves",
        "chainmail chestpiece", "oak buckler"]
melee_weapon_dictionary={"iron arming sword":2,"small dagger":1}
melee_weapon_list=["iron arming sword","small dagger"]
ranged_weapon_dictionary={"elm bow":2, "slingshot":1}
range_weapon_list=["elm bow", "slingshot"]
coin_dictionary={"2 coin":2, "15 coin":15}
coin_list=["2 coin", "15 coin"]
arrows_dictionary={"3 arrows":3,"10 arrows":10}
arrows_list=["3 arrows", "10 arrows"]
food_dictionary={"saltfish":1, "coconut flesh":0.5, "crab meat":1.5}
food_list=["saltfish", "coconut flesh", "crab meat"]
fluid_dictionary={"bottle of wine":1.5, "full waterskin":2}
fluid_list=("bottle of wine", "full waterskin")
chest1=["iron horned helmet", "elm bow", "3 arrows", "10 arrows", "2 coin", "15 coin", "iron arming sword",
        "padded torso armour", "saltfish", "small dagger", "marching boots", "empty waterskin",
        "bottle of wine", "padded gloves", "chainmail chestpiece", "oak buckler", "coconut flesh", "crab meat",
        "slingshot"]
races=['h','d','a','r']
giant_crab=character("giant crab", 5, 2.5, 0, 0, 0, 2, 0.25, 2, 1, 0, 1, 0, 0, 0)

hname=input("Welcome Hero to the island of White-Fern, please choose your Hero's name to continue.\n\n")
hname=character(hname, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0)
hinventory=["cloth shirt"]
print("You awaken on a sandy shore, your back propped against a large rock several feet from the water's edge.") 
print("The last thing you remember was the storm that struck in the night as you were travelling on the Felicity Rose")
print("The ship was carrying war prisoners from the West to the East along the Living Sea.")
decision0=input("Type any key and hit enter to continue\n")
print("Eastwards, towards the sunset, you see a long beach spanning for miles with a jungle clinging to it's border.")
print("To the West you see a shipwreck; birds and wildlife feeding on the departed.")
print("Before moving off, you need to customise your character")
race=input("First select your race. Type,\n'h' for Human\n'd' for Dweefa\n"
"'a' for Aelf\n'r' for Arecapai\n")
if race not in races:
    race="h"
if race=="h":
    print("You are a human, you have an average strength and intelligence among races, and your sword skills are already somewhat honed.")
    hname.strength=hname.strength+3
    hname.intelligence=hname.intelligence+3
    hname.armour=hname.armour+1
    hname.courage=hname.courage+3
    hname.swordsmanship=hname.swordsmanship+2
    hname.archery=hname.archery+1
elif race=="d":
    print("You are a Dweefa, a man of the caves, you are a brute and courageous warrior, with an adept knowledge of combat.")
    hname.strength=hname.strength+4
    hname.armour=hname.armour+1
    hname.courage=hname.courage+4
    hname.swordsmanship=hname.swordsmanship+3
    hname.health=hname.health+1
elif race=="a":
    print("You are an Aelf, one of the ancient races of the land, you are brave and cunning, and an expert in archery.")
    hname.strength=hname.strength+2
    hname.intelligence=hname.intelligence+4
    hname.armour=hname.armour+1
    hname.courage=hname.courage+3
    hname.swordsmanship=hname.swordsmanship+1
    hname.archery=hname.archery+3
    hname.health=hname.health-1
elif race=="r":
    print("You are an Arecapai, a sorcerous bird race from the Western lands, you are mysterious yet dextrous, a feared opponent to many.")
    hname.strength=hname.strength+3
    hname.intelligence=hname.intelligence+2
    hname.armour=hname.armour+1
    hname.courage=hname.courage+2
    hname.sorcery=hname.sorcery+3
    hname.health=hname.health+2
    hname.attack=hname.attack+2
decision1set=['e','w']
decision1=input("Your legs are bruised but you can move, which way do you travel?\n 'e' for East, 'w' for West.\n")
if decision1=='e':
    print("You stand and move slowly down the Eastern shore, the Sun setting in the distance over the water is cooling.")
    print("You find a chest washed up on the shore several hundred yards on, it's wood is water-logged, the locks rusted away.")
elif decision1=='w':
    print("You stand and move slowly Westwards, with the evening breeze spilling over you as the final splash of sunset warms your back.")
    print("You arrive at the shipwrech, only fragments of what it was only day's earlier remain, you find a chest among the rubble.")
elif decision1 not in decision1set:
    print("You try to stand but pass out from exhaustion instantly. You rest for a few more countless hours before awakening again.")
    print("It's the evening now, the sky is dark, you hear a person calling from the shipwreck, you move to investigate.")
    print("On arriving you find the corpses of people, none who you recoginse, and a gull mocking you from a high up part of the wreck.")
    print("As you try and climb to get the gull you fall and injure yourself, landing on an old, sodden chest.")
    hname.health=hname.health-2
    print("You lose -2hp Your new health is "+str(hname.health))
continue1=input("Press any key to coninue\n")

action=input("A giant crab emerges from the wet sand to defend the chest! Type 'p' to fight or 'x' to run away.\n")
modified_giant_crab_health=giant_crab.health
turns=2
while hname.health>=hname.courage:
    if action=="x":
             print("You flee the fight, but will live to tell the tale.")
             break
    if action=="p":
        print("You have the courage to fight!")
        putin=input("Type any key to roll to hit\n")
        dice_roll=randint(0,3)
        print("You roll "+str(dice_roll+1)+" + your attack modifier of "+str(hname.swordsmanship+hname.sorcery))
        modified_roll=dice_roll+hname.sorcery+hname.swordsmanship
        if modified_roll>giant_crab.armour:
            print("You hit the "+str(giant_crab.name))
            action=input("Now roll again for damage. Press 'p'\n")
            if action=="p":
                dice_roll=randint(0,3)
                print("You roll "+str(dice_roll+1)+" + your damage modifier of "+str(hname.attack))
                modified_roll=dice_roll+hname.attack
                modified_giant_crab_health=giant_crab.health-modified_roll
                if modified_giant_crab_health<=0:
                    print("You kill the "+str(giant_crab.name)+". Victory is your!")
                    print("You move the crab's giant body aside and break back the lid of the chest and find several items inside")
                    turns=turns-turns
                    break
                elif modified_giant_crab_health>0:
                    print("You hurt the creature but it fights on.")
                    turns=turns-1
                    action3=input("Type any key to continue\n")
                    break
        elif modified_roll<=giant_crab.armour:
             print("You miss and now the giant crab moves to strike back.")
             turns=turns-1
             break
while hname.health<hname.courage:
    if action=="x":
        break
    print("You lack the courage to fight on...")
    break
while modified_giant_crab_health>=giant_crab.courage:
    if action=="x":
        break
    print("The crab has the courage to fight")
    putin=input("Type any key to continue\n")
    dice_roll=randint(0,3)
    modified_roll=dice_roll+giant_crab.swordsmanship
    if modified_roll>hname.armour:
        print("The giant crab hits you!")
        dice_roll=randint(0,3)
        modified_roll=dice_roll+giant_crab.attack
        hname.health=hname.health-modified_roll
        if hname.health<=0:
            print("You die, the giant crab has defeated you.")
            break
        elif hname.health>0:
            print("You are hurt but will survive")
            break
    elif modified_roll<=hname.armour:
        print("The giant crab misses with it's strike and you can attack again")
        break
while hname.health>=hname.courage:
    if modified_giant_crab_health<giant_crab.courage:
        print("The crab flees back to the ocean.")
        print("You break back the lid of the chest and find several items inside")
        break
    if action=="x":
             print("You flee the fight, but will live to tell the tale.")
             break
    elif action=="p":
        print("You have the courage to fight!")
        putin=input("Type any key to roll to hit\n")
        dice_roll=randint(0,3)
        print("You roll "+str(dice_roll+1)+" + your attack modifier of "+str(hname.swordsmanship+hname.sorcery))
        modified_roll=hname.sorcery+hname.swordsmanship+dice_roll
        if modified_roll>giant_crab.armour:
            print("You hit the "+str(giant_crab.name))
            action=input("Now roll again for damage. Press 'p'\n")
            if action=="p":
                dice_roll=randint(0,3)
                print("You roll "+str(dice_roll+1)+" + your damage modifier of "+str(hname.attack))
                modified_roll=dice_roll+hname.attack
                modified_giant_crab_health=modified_giant_crab_health-modified_roll
                if modified_giant_crab_health<=0:
                    print("You kill the "+str(giant_crab.name)+". Victory is your!")
                    print("You move the crab's giant body aside and break back the lid of the chest and find several items inside")
                    turns=turns-turns
                    break
                elif modified_giant_crab_health>0:
                    print("You hurt the creature but it fights on.")
                    turns=turns-1
                    action3=input("Type any key to continue\n")
                    break
        elif modified_roll<=giant_crab.armour:
             print("You miss and now the giant crab moves to strike back.")
             turns=turns-1
             break
while hname.health<hname.courage:
    if action=="x":
        break
    print("You lack the courage to fight on...")
    break
while modified_giant_crab_health>=giant_crab.courage:
    if action=="x":
        break
    print("The crab has the courage to fight")
    putin=input("Type any key to continue\n")
    dice_roll=randint(0,3)
    modified_roll=dice_roll+giant_crab.swordsmanship
    if modified_roll>hname.armour:
        print("The giant crab hits you!")
        dice_roll=randint(0,3)
        modified_roll=dice_roll+giant_crab.attack
        hname.health=hname.health-modified_roll
        if hname.health<=0:
            print("You die, the giant crab has defeated you.")
            putin=input("Type any key to continue\n")
            break
        elif hname.health>0:
            print("You are hurt but will survive")
            putin=input("Type any key to continue\n")
            break
    elif modified_roll<=hname.armour:
        print("The giant crab misses with it's strike and you can attack again")           
        break
while hname.health>=hname.courage:
    if modified_giant_crab_health<giant_crab.courage:
        break
    if action=="x":
             print("You flee the fight, but will live to tell the tale.")
             break
    elif action=="p":
        print("You have the courage to fight!")
        putin=input("Type any key to roll to hit\n")
        dice_roll=randint(0,3)
        print("You roll "+str(dice_roll+1)+" + your attack modifier of "+str(hname.swordsmanship+hname.sorcery))
        modified_roll=hname.sorcery+hname.swordsmanship+dice_roll
        if modified_roll>giant_crab.armour:
            print("You hit the "+str(giant_crab.name))
            action=input("Now roll again for damage. Press 'p'\n")
            if action=="p":
                dice_roll=randint(0,3)
                print("You roll "+str(dice_roll+1)+" + your damage modifier of "+str(hname.attack))
                modified_roll=dice_roll+hname.attack
                modified_giant_crab_health=modified_giant_crab_health-modified_roll
                if modified_giant_crab_health<=0:
                    print("You kill the "+str(giant_crab.name)+". Victory is your!")
                    print("You move the crab's giant body aside and break back the lid of the chest and find several items inside")
                    turns=turns-turns
                    break
                elif modified_giant_crab_health>0:
                    print("You hurt the creature but it fights on.")
                    turns=turns-1
                    action3=input("Type any key to continue\n")
                    break
        elif modified_roll<=giant_crab.armour:
             print("You miss and now the giant crab moves to strike back.")
             turns=turns-1
             break
while modified_giant_crab_health>=giant_crab.courage:
    if action=="x":
        break
    print("The crab has the courage to fight")
    putin=input("Type any key to continue\n")
    dice_roll=randint(0,3)
    modified_roll=dice_roll+giant_crab.swordsmanship
    if modified_roll>hname.armour:
        print("The giant crab hits you!")
        dice_roll=randint(0,3)
        modified_roll=dice_roll+giant_crab.attack
        hname.health=hname.health-modified_roll
        if hname.health<=0:
            print("You die, the giant crab has defeated you.")
            putin=input("Type any key to continue\n")
            break
        elif hname.health>0:
            print("You are hurt but will survive")
            putin=input("Type any key to continue\n")
            break
    elif modified_roll<=hname.armour:
        print("The giant crab misses with it's strike and you can attack again")           
        break
if turns==0:
    print("The crab tires of this fight and retreats to the ocean")
    
type_of_dice=18
amount_of_dice=5
rolls_taken=0
rolls=[]
while int(rolls_taken)<int(amount_of_dice):
    action=input("Type 'f' to find objects in the chest. ")
    if action=="f":    
        dice_roll=randint(0,int(type_of_dice))
        if dice_roll in rolls:
            print("Your item breaks apart...")
            continue
        rolls.append(int(dice_roll))
        print("You find "+str(chest1[int(dice_roll)]))
        hinventory.append(str(chest1[int(dice_roll)]))
        if str(chest1[int(dice_roll)]) in armour_list:
            hname.armour=hname.armour+(armour_dictionary.get(str(chest1[int(dice_roll)])))
        elif str(chest1[int(dice_roll)]) in melee_weapon_list:
            hname.attack=hname.attack+(melee_weapon_dictionary.get(chest1[int(dice_roll)]))
        elif str(chest1[int(dice_roll)]) in coin_list:
            hname.coin=hname.coin+(coin_dictionary.get(chest1[int(dice_roll)]))
        elif str(chest1[int(dice_roll)]) in arrows_list:
            hname.arrows=hname.arrows+(arrows_dictionary.get(chest1[int(dice_roll)]))
        elif str(chest1[int(dice_roll)]) in food_list:
            hname.food=hname.food+(food_dictionary.get(chest1[int(dice_roll)]))
        elif str(chest1[int(dice_roll)]) in fluid_list:
            hname.fluid=hname.fluid+(fluid_dictionary.get(chest1[int(dice_roll)]))
        rolls_taken=rolls_taken+1
        continue
    elif action!="f":
        print("Your items breaks into mush...")
        rolls_taken=rolls_taken+1
        continue
print("\n"+str(hname.name))
print("Your stats are currently "+"\nHealth "+str(hname.health)+"\nArmour "+str(hname.armour)+"\nStrength "+str(hname.strength))
print("Intelligence "+str(hname.intelligence)+"\nCourage "+str(hname.courage)+"\nSorcery "+str(hname.sorcery))
print("Swordsmanship "+str(hname.swordsmanship)+"\nArchery "+str(hname.archery)+"\nAttack "+str(hname.attack))
print("Coin "+str(hname.coin)+"\nArrows "+str(hname.arrows)+"\nFood "+str(hname.food)+"\nFluid "+str(hname.fluid))
continue2=input("press 'i' to view inventory or any key to coninue. ")
if continue2=="i":
    print("Your inventory now includes: ")
    print(hinventory)
print("At any time you can use these shortcuts to view certain stats:\n'i' will display inventory"
      "\n'a' will display armour\n't' will display attack\n'h' will display health"
      "\n'c' will display coin\n's' will display all stats")
print("The story continues.")



                
    
    