# define enemy class
class enemy:

  # define initial function
  def __init__(self):
    
    # define enemy stats
    self.health = int(player.attackmulti * random.randint(26, 68))
    if self.health < player.health:
      self.size = 'small'
    else:
      self.size = 'large'
    self.attack_bonus = player.level
    self.attackmulti = player.attackmulti
    self.attackbonus = player.level
    self.ac = (4 + player.level)
    
    # define random variables
    self.duration = 0

    # define enemy invntory
    self.experience = (self.health * 40)
    self.gold = self.health

    # start fight
    player.fighting = True

  
  # define enemy action function
  def action(self):

    global distance
    # creature is close

    # if creature is on fire
    if self.duration > 0:
      damage = d(4)
      self.health -= damage
      sprint(f"The creature is on fire. It takes {damage} damage.")
      if self.health < 0:
        self.health = 0
      self.duration -= 1

    # creature movment
    # creature is far
    if distance == 2:

      # creature gets closer or fight 
      if self.health > 8:
        if onein(6):
          sprint("The creature lunges at you.")
          distance -= 1

      # creature flees for its life
      else:
        if onein(4):
          sprint("The creature, close to death, flees off into the forest.")
          sprint("You do not get the bounty.")
          distance = 3

    # creature is close
    else:

      # creature retreats for its life
      if self.health < 8:
        if onein(2):
          sprint("The creature slowly retreats from you.")
          distance += 1

    # creature attack
  
    if distance < 3:
      # creature gets bonus for being close
      if distance == 1:
        attack_chance = (d(20) + self.attackbonus)
      else:
        attack_chance = (d(20))

      if attack_chance > player.ac:
        damage = (d(20) + self.attackbonus)
        player.health -= damage
        if player.health < 0:
          player.health = 0
                    
        sprint(f"The creature attacked dealing {damage} damage. You are at {player.health} hp.")
        if player.health == 0:
          sprint("You got knockd unconscious.")
          sprint("You awake in the tavern with no bounty and a massive headache.")
          player.died()
          player.reward()
                      
      else:
        sprint("The creature missed the attack.")

