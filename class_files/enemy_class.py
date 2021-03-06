# define enemy class
class enemy:

  # define initial function
  def __init__(self):
    
    # define enemy stats
    self.health = int(random.randint(26, 68) * player.attackmulti)
    if self.health < (40 * player.attackmulti):
      self.size = 'small'
    else:
      self.size = 'large'
    self.attackmulti = player.attackmulti
    self.attackbonus = player.level
    self.ac = (4 + player.level)
    
    # define random variables
    self.type = random.choice(text.textenemy_type[player.location])
    self.duration = 0

    # define enemy invntory
    self.experience = (self.health * 40)
    self.gold = self.health

    # start fight
    player.fighting = True


  # define fire damage function
  def onfire(self):

    damage = d(4) + player.level
    self.health -= damage
    sprint(f"The {text.enemy_type} is on fire. It takes {damage} damage.")
    if self.health <= 0:
      sprint(f"The {text.enemy_type} died.")
      player.reward()
    self.duration -= 1
    
  
  # define enemy action function
  def action(self):

    global distance
    # creature is close

    # if creature is on fire
    if self.duration > 0:
      self.onfire()

    # creature movment
    # creature is far
    if distance == 2:
      if player.fighting:

        # creature gets closer or fight 
        if self.health > 8:
          if onein(6):
            sprint(f"The {text.enemy_type} lunges at you.")
            distance -= 1

        # creature flees for its life
        else:
          if onein(4):
            sprint(f"The {text.enemy_type}, close to death, flees off into the forest.")
            sprint("You do not get the bounty.")
            player.fighting = False

    # creature is close
    else:

      # creature retreats for its life
      if self.health < 8:
        if onein(2):
          sprint(f"The {text.enemy_type} slowly retreats from you.")
          distance += 1

    # creature attack
  
    if player.fighting:
      # creature gets bonus for being close
      if distance == 1:
        attack_chance = (d(20) + self.attackbonus)
      else:
        attack_chance = (d(20))

      if attack_chance > player.ac:
        damage = (d(20) + self.attackbonus)
        player.health -= damage
        if player.health <= 0:
          player.health = 0
          player.fighting = False
                    
        sprint((text.enemy_attack) + f" dealing {damage} damage. You are at {player.health} hp.")

        if not player.fighting:
          sprint("You got knockd unconscious.")
          sprint("You awake in the tavern with no bounty and a massive headache.")
          player.died()
          player.reward()
                      
      else:
        sprint(text.enemy_miss)

