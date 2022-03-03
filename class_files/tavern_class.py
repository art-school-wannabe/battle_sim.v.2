# define tavern class
class tavern:

  # define initial function
  def __init__(self):
    taverns = {"Connyberry": "Tuligan", "Barstal": "Kem", "Ironstone": "Barthock", "Kelender": "Jameti"}
    self.keep = taverns[player.location]
    
  # define bounty board function
  def bounty_board(self):

    # define creature a
    creaturea = enemy()

    # define creature b
    creatureb = enemy()

    # define creature c
    creaturec = enemy()

    # bounty board selection menu
    sprint(f""" ______________    ______________    ______________
|  Creature A  |  |  Creature B  |  |  Creature C  |
|  size: {creaturea.size} |  |  size: {creatureb.size} |  |  size: {creaturec.size} |
|  exp: {creaturea.experience}   |  |  exp: {creatureb.experience}   |  |  exp: {creaturec.experience}   |
|    Reward    |  |    Reward    |  |    Reward    |
|   {creaturea.gold}  gold   |  |   {creatureb.gold}  gold   |  |   {creaturec.gold}  gold   |
 ______________    ______________    ______________ """)
    enemy_selection = input("Choose a bounty. ").lower()

    # leave bounty board
    if enemy_selection == "0":
      return

    # set creature a
    elif enemy_selection == "a":
      return creaturea

    # set creature b
    elif enemy_selection == "b":
      return creatureb

    # set creature c
    elif enemy_selection == "c":
      return creaturec

    # invalid input
    else:
      sprint("This is not an option.")
      return

  
  # define fight function
  def fight(self):
        
    # fight openning scene
    sprint(f"You step out onto the dirt trail outside the tavern and journey off deep into the forest ahead.")
    sprint(f"A short walk later, a {creature.size} creature has approached you. It appears hostile.")
    sprint("""------------------------
1) attack with sword
2) attack with crossbow
3) cast a spell
4) check inventory
5) move
------------------------""")

    # fight round loop
    while True:
      # action selection menu
      player_action = input("What do you do next? ")

      
      # controls info pannel (0)
      if player_action == "0":
        sprint("""------------------------
1) attack with sword
2) attack with bow
3) cast a spell
4) check inventory
5) move
------------------------""")
        continue

    
      # attack with sword (1)

      # player attack
      elif player_action == "1":
        player.sword()
        if not player.fighting:
          break

        # creature attack
        creature.action()
        if not player.fighting:
          break


      # attack with crossbow (2)

      # player attack
      elif player_action == "2":
        player.crossbow()
        if not player.fighting:
          break

        # creature attack
        creature.action()
        if not player.fighting:
          break


      # cast spell (3)

      # player attack
      elif player_action == "3":
                    
        # spell selection menu
        spell_cast = input(f"""------------------------
mp                  {player.mana}
------------------------
1) flame             10
2) lightening bolt   30
3) heal              20
------------------------
""")

        # cast flame spell
        if spell_cast == "1":
          player.flame()
          if not player.fighting:
            break

        # cast lightening bolt spell
        elif spell_cast == "2":
          player.lightening_bolt()
          if not player.fighting:
            break

        # cast heal spell
        elif spell_cast == "3":
          player.heal()
          if not player.fighting:
            break

        else:
          sprint("That is not an option.")
          

      # check inventory (4)

      elif player_action == "4":
        player.inventory()


      # move (5)
        
      elif player_action == "5":
        player.move()
        if not player.fighting:
          break


      # invalid input

      else:
        sprint("That wa not an option.")


  # define barkeep function
  def barkeep(self):
    
    if player.drink <= 2:
      sprint("\"Hunter, I see the monsters haven\'t gotten you yet. Can\'t say the same for all your peers.\"")
      player_action = input("\"I take it you want a drink?\" (y or n) ").lower()
      if player_action == "n":
        sprint("\"To early for some I guess\"")
        player_action = input("\"I take it you\'re here for the special bounty than?\" (y or n) ").lower()
        if player_action == "y":
          sprint("\"Ah, just head over the bounty board and choose the \"special\" one, but i warn you, its a tough one... be safe.\"")  
        else:
          sprint('\"Well I\'ll see you later. And be safe\"')
      elif player_action == 'y':
        sprint("\"Ah, one to have some fun in battle I see. I knew I liked you\"")
        if player.gold >= 5:
          player.gold -= 5
          health_from_potion = random.randint(8, 15)
          player.health += health_from_potion
          player.mana += 10
          player.drink += 1
          sprint(f"You gained {health_from_potion} hp.")
          sprint("\"Have fun, and remeber, be safe\"")
        else:
          sprint("\"If you dont got the funds then dont be asking\"")
          sprint("You do not have enough gold.")
    else:
      sprint("\"Careful, you gotta slow down before I gotta take that sword from you.\"")
      sprint("You can not have any more drinks right now.")


  # define shop function
  def shop(self):

    sprint("\"So you\'re looking for some provisions? I have some stuff under the bar.\"")
    print(f"""------------------------------
you have             {player.gold} gold
------------------------------
1 potion of health   30 gold
2 potion of mana     45 gold
3 arrows (4 count)   10 gold
     4 check inventory
------------------------------
     0 finish shopping""")
    while True:
      purchase = input("")

      # buy health potion
      if purchase == ("1"):
        if player.gold >= 30:
          player.gold -= 30
          player.health_potions += 1
          sprint('You purchased a health potion.')
          continue
        else:
          sprint('You do not have enough gold.')
          continue

      # buy mana potion
      elif purchase == ("2"):
        if player.gold >= 45:
          player.gold -= 45
          player.mana_potions += 1
          sprint("You purchased a potion of mana.")
          continue
        else:
          sprint("You do not have enough gold.")
          continue

      # buy arrows
      elif purchase == ("3"):
        if player.gold >= 10:
          player.gold -= 10
          player.arrows += 4
          sprint("You purchased a bundle of arrows.")
          continue
        else:
          sprint("You do not have enough gold.")
          continue

      # check inventory
      elif purchase == ("4"):
        print(f"""------------------------------
1) potion of health       {player.health_potions}
2)   potion of mana       {player.mana_potions}
3)           arrows       {player.arrows}
------------------------------""")

      # exit shop
      elif purchase == ("0"):
        sprint(f"{self.keep} puts the items back under the bar.")
        break

      # invalid input
      else:
        sprint("That is not an option.")
        continue


  # define map function
  def map(self):

    map_action = input(f"""-------------------------------------------
1)     Barstal    The Brass Flagon
2)  Connyberry    The Bard and The Badger
3)   Ironstone    Dead Man's Spirit
4)    Kelender    The Trader's Bounty
            0)    Exit Map
-------------------------------------------
     currently at {player.location}
-------------------------------------------
""")

    # travel to barstal
    if map_action == "1":
      if player.location != "Barstal":
        sprint("You look over the slope of the city to the sea. Boats in the docks and seagulls in the air.")
        sprint("You step through the doorway of The Brass Flagon. Most tables full. The smell strong.")
        player.location = "Barstal"
      else:
        sprint("You are already in Barstal.")

    # travel to connyberry
    if map_action == "2":
      if player.location != "Connyberry":
        sprint("The breeze blowing off Lake Bizarre is refreshing as you step into the town.")
        sprint("You step through the doorway of The Bard and The Badger. Tuliagn with a smile on his face.")
        player.location = "Connyberry"
      else:
        sprint("You are already in Connyberry.")

    # travel to ironstone
    if map_action == "3":
      if player.location != "Ironstone":
        sprint("You step of the boat onto Beford Island and make your way into the dark, wet alley ways of the city.")
        sprint("You step through the doorway of The Dead Man's Spirit. It is empty with only the barkeep asleep in the corner behind the bar.")
        player.location = "Ironstone"
      else:
        sprint("You are already in Ironstone.")

    # travel to kelender
    if map_action == "4":
      if player.location != "Kelender":
        sprint("Finally through the gates of the capital city. Through the hustle and bustle you find your way.")
        sprint("You step through the doorway of The Trader's Bounty. The crowd is rowdy.")
        player.location = "Kelender"
      else:
        sprint("You are already in Kelender.")
