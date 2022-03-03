# import imoportant variables
import random, time



# define random variables
distance = 1

# define slow print function
def sprint(str):
    print(str)
    time.sleep(1)

# define one in chance function
def onein(int):
  return random.randint(1, int) == 1

# define dice roll function
def d(int):
  roll = random.randint(1, int)
  return roll

# import player class 
try:
  exec(open("class_files/player_class.py").read())
except:
  sprint("You do not have all neccisarry files needed downloaded.")
  sprint("File \"class_files/player_class.py\" is missing.")
  exit()

# import enemy class 
try:
  exec(open("class_files/enemy_class.py").read())
except:
  sprint("You do not have all neccisarry files needed downloaded.")
  sprint("File \"class_files/enmey_class.py\" is missing.")
  exit()




# game code 

# game intro scene
while True:
  player_name = input("Enter character name: ")
  if not player_name.isalpha():
    sprint("That name conatins invalid characters")
  else:
    break
file_name = player_name + "_DataFile.py"
player = player(file_name)


# import tavern class 
try:
  exec(open("class_files/tavern_class.py").read())
  tavern = tavern()
except:
  sprint("You do not have all neccisarry files needed downloaded.")
  sprint("File \"class_files/tavern_class.py\" is missing.")
  exit()


# game loop
while True:
  
  # tavern selection menu
  tavern_action = input("""--------------------
1) take a bounty
2) grab a drink
3) buy items
--------------------
 (4) map  (0) quit
""")

  # 1 take a bounty
  if tavern_action == ("1"):
    creature = tavern.bounty_board()
    if player.fighting:
      tavern.fight()

  # 2 grab a drink
  elif tavern_action == ("2"):
    tavern.barkeep()
    
  # 3 buy items
  if tavern_action == ("3"):
    tavern.shop()

  # 4 map
  if tavern_action == ("4"):
    tavern.map()
    
  # 0 quit
  elif tavern_action == ("0"):
    sprint("You step out of the tavern and take a deep breathe of fresh air after a long days work.")
    player.save()
    exit()
    
  # invalid input
  else:
    sprint("That is not an option.")
