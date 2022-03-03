# define the player class
class player:

  # define initial function
  def __init__(self, file_name):

    while True:
      # import player data from existing file
      try:
        exec(open(file_name).read())
        sprint("Welcome back to the tavern fine traveller.")
        break

      # import starting player data into a new file
      except:
        sprint("This character does not exist.")
        if (input("Would you like to start a new charecter by this name? (y or n) ").lower()) == "y":
          file = open(file_name, "w+")
          stat_block = f"""
# define player stats
self.level = 1
self.health = 48
self.mana = 40
self.attackmulti = ((self.level / 10) + 1)
self.attackbonus = (2 + self.level)
self.ac = (4 + self.level)

# define random variables
self.drink = 1
self.location = 'Connyberry'
self.fighting = False

# define player inventory
self.experience = 0
self.gold = 80
self.health_potions = random.randint(0,3)
self.mana_potions = random.randint(0,3)
self.arrows = random.randint(12,16)
"""
          file.write(stat_block)
          file.close()

          # import player data from new file
          exec(open(file_name).read())
          sprint("And so your journey begins.")
          break
        else:
          file_name = input("Enter a valid character name: ") + "_DataFile.py"
          continue


  # define save function
  def save(self):
    global file_name
    file = open(file_name, "w+")
    stat_block = f"""
# define player stats
self.level = {self.level}
self.health = {player.health}
self.mana = {self.mana}
self.attackmulti = ((self.level / 10) + 1)
self.attackbonus = (2 + self.level)
self.ac = (4 + self.level)

# define random variables
self.drink = {self.drink}
self.location = '{self.location}'
self.fighting = False

# define player inventory
self.experience = {self.experience}
self.gold = {self.gold}
self.health_potions = {self.health_potions}
self.mana_potions = {self.mana_potions}
self.arrows = {self.arrows}
"""
    file.write(stat_block)
    file.close()
          

  # define reward function
  def reward(self):

    global distance
    if creature.health == 0:
      # reward variables
      arrows = random.randint(6, 8)
      potions = random.randint(0, 2)
      item_list = ['a tattered pelt', 'a broken arrow']
      item = (random.choice(item_list))
      
      # reward alert and inventory update
      sprint(f"You got {creature.gold} gold, {arrows} arrows, {potions} health potions, and {creature.experience} experience.")
      self.mana += 20
      self.health_potions += potions
      self.arrows += arrows
      self.gold += creature.gold
      self.experience += creature.experience

      # level up
      if self.experience >= ((3000 * player.attackmulti) * self.level):
        self.level += 1
        self.attackmulti = (self.level / 10 + 1)
        self.attackbonus = (2 + self.level)
        self.ac = (4 + self.level)
        sprint(f"You leveled up. You are now at level {self.level}.")

    distance = 1
    self.drink = 1
    enemy.duration = 0
    self.save()
    sprint("You return to the tavern.")
    self.fighting = False


  # define death fucntion
  def died(self):
    
    self.health = d(6)
    self.health_potions = 0
    self.mana_potions = 0
    self.arrows = d(3)
    self.gold -= int(self.gold / 2)


  # define attack with sword function
  def sword(self):

    global distance
    if distance == 1:
      attack_chance = (d(20) + self.attackbonus)
      if attack_chance > creature.ac:
        attack = (d(12) + self.attackbonus)
        
        creature.health -= attack
        if creature.health < 0:
          creature.health = 0
        sprint(f"You swung you sword at the creature dealing {attack} damage. The creature is at {creature.health} hp.")
        
        if creature.health == 0:
          sprint('The creature died.')
          self.reward()
                            
      else:
        sprint('You missed the attack.')
    else:
      sprint('You are to far from the creature.')

      
  # define attack with crossbow function
  def crossbow(self):

    global distance
    if self.arrows > 0:
      self.arrows -= 1
      
      if distance == 1:
        attack_chance = (d(20) - (6 + self.attackbonus))
      else:
        attack_chance = (d(20) + self.attackbonus)
        
      if attack_chance > creature.ac:
        attack = d(12) + self.attackbonus
        creature.health -= attack
        if creature.health < 0:
          creature.health = 0
        sprint(f"You shot the creature with your bow doing {attack} damage. The creature is at {creature.health} hp.")
        if creature.health == 0:
          sprint("The creature died.")
          self.reward()
            
      else:
        sprint("You missed the attack.")

    else:
      sprint("You are out of arrows.")


  # define flame spell function
  def flame(self):

    # player attack
        
    if self.mana >= 10:
      self.mana -= 10
          
      attack_chance = (d(20) + self.attackbonus)
      if attack_chance > creature.ac:
        attack = (d(12) + self.attackbonus)
        creature.health -= attack
        if creature.health < 0:
          creature.health = 0
        sprint(f"You cast flame dealing {attack} damage. The creature is at {creature.health} hp.")
        if creature.health == 0:
          sprint("The creature died.")
          self.reward()
        creature.duration = random.randint(2, 3)
      else:
        sprint("You missed the spell.")

    # creature attack
    if self.fighting:
      creature.action()


  # define lightening bolt spell function
  def lightening_bolt(self):

    # player attack
    if self.mana >= 30:
      self.mana -= 30
      attack_chance = (d(20) + self.attackbonus)
      if attack_chance > creature.ac:
        attack = (d(12) + self.attackbonus)
        creature.health -= attack
        if creature.health < 0:
          creature.health = 0
        sprint(f"You cast lightening bolt dealing {attack} damage. The creature is at {creature.health} hp.")
        sprint("The creature is temporarily paralyzed. It does not attack.")
        if creature.health == 0:
          sprint("The creature died.")
          self.rewrad()

      # enemy attack
      else:
        sprint("You missed the spell.")
        creature.action()
    
    else:
      sprint("You do not have enough mana.")
                  
        
  # define heal spell function
  def heal(self):
    if self.mana >= 20:
      self.mana -= 20
      self.health += 10
      sprint(f"You cast heal. You recovered 10 hp. You are at {self.health} hp.")
    else:
      sprint("You do not have enough mana.")

      
  # define check inventory function
  def inventory(self):
    
    print(f"""-------------------------------
1) potion of health       {self.health_potions}
2)   potion of mana       {self.mana_potions}
3)           arrows       {self.arrows}
4)             gold       {self.gold}
   {self.mana} mana   {self.experience} experience
-------------------------------
  (5) check bounty  (0) exit""")

    # inventory repeat
    while True:
      inventory_action = input("")

      # exit inventory
      if inventory_action == "0":
        break

      # use health potion
      elif inventory_action == "1":
        if self.health_potions > 0:
          health_from_potion = d(20)
          self.health += health_from_potion
          self.health_potions -= 1
          sprint(f"You took a potion of health. You recovered {health_from_potion} hp. You are at {player.health} hp. You have {self.health_potions} potions left.")
          continue
        else:
          sprint("You are out of health potions.")
          continue

      # use mana potion
      elif inventory_action == "2":
        if self.mana_potions > 0:
          self.mana += 20
          self.mana_potions -= 1
          sprint(f"You took a potion of mana. You recovered 20 mp. You are at {self.mana} mp. You have {self.mana_potions} potions left.")
          continue
        else:
          sprint("You are out of potions of mana.")
          continue

      # check bounty
      elif inventory_action == "5":
        sprint(f""" ______________
|   Creature   |
|  size: {creature.size} |
|  exp: {creature.experience}   |
|    Reward    |
|   {creature.gold}  gold   |
 ______________""")
        continue

       # use nonusable item
      else:
        sprint("This item is not usable.")
        continue

      

  # define move function
  def move(self):

    global distance
    move_action = input("""------------------------
1) step forward
2) step back
3) run away
------------------------
""")

    # step forward
    if move_action == "1":
      if distance == 1:
        sprint("You cant step any closer to the creature.")
      else:
        distance -= 1
        sprint("You stepped toward the creature.")

    # step backward
    elif move_action == "2":
      if distance == 1:
        distance += 1
        sprint("You stepped from the creature.")
      else:
        move_action = input("You are already stepped away from the creature. Do you want to run away? (y or n) ").lower()
        if move_action == "y":
          sprint("You ran away.")
          self.rewrad()
        else:
          time.sleep(1)
          
    # run away
    elif move_action == "3":
      sprint("You ran away.")
      self.reward()

    # invalid input
    else:
      sprint("That was not an option.")
                  
