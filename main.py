print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
wait = (
    "the old man fucks you,you realise you have found your ultimate treasure and give up"
)
swim = (
    "you reach the shore you almost get fucked by the crocadile but you manage to fuck him instead"
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input(
    "you have encountered a lake in front you , you see the treasure island \na boat with a sus old man is coming towards you do you wish to wait or swim to the island\n"
).lower()
if choice1 == "swim":
    print(swim)
    choice2 = input(
        "you see a house on the island with no lights you assume there was a powercut\n "
        "you go in with a torch u had bought\n"
        "you come across three colour doors red blue and yellow which one do u choose to go in\n"
    ).lower()
    if choice2 == "blue":
        print("congrats you are not ded yet")
        choice3 = input(
            "you get in a room u see a ghost give you three options\n "
            "to die by hanging on an electric chair or let his pet crocodile eat you\n"
        ).lower()
        print("LMAOOOO bitch thought the ghost ends up raping you \n"
              "yea thats how you die feeling the pleasure u have never felt,"
              "\n finally realising what the real treasure was")

    elif choice2 == "yellow":
        print("you died, yea no reason u just dead jackass")
    elif choice2 == "red":
        print("u get fucked by a charizad")
    else:
        print("wrong input smartass")

else:
    print(wait)
