import random, time, sys

health = 100
money = 0
food = 10
role = ''

print("Welcome to the Oregon Trail")
time.sleep(1)
def getName():
  print("Enter your name:")
  name = input()
  return name

def setRole():
  while True:
    print("Who do you want to be: 1 for Doctor, 2 for Banker")
    role = input()
    if role == '1':
      role = 'Doctor'
      health = 125
      money = 100
      break
    elif role == '2':
      role = 'Banker'
      health = 100
      money = 150
      break
    else:
      print('Please enter something valid')
  return role, health, money

def hunt():
  global food
  huntedFood = random.randint(1, 200)
  food += huntedFood
  print('Hunting')
  return food

def rest(days):
  global health
  health = health + (days * 3)
  print('Resting')
  return health

def randomSick():
  global health
  sickChoice = random.randint(1, 3)
  if sickChoice == 1:
    print("Fever")
    health -= 10
    print(f"Health is now {health}")
  elif sickChoice == 2:
    print("Cold")
    health -= 20
    print(f"Health is now {health}")
  else:
    print("Cholera")
    health -= 30
    print(f"Health is now {health}")
  return health

def update(distance, pace, destination):
  while distance > 0:
    print(f"{distance} miles to go")
    time.sleep(1)
    event()
    distance -= 3 * pace
  return print(f"Arrived at {destination}")

def event():
  global food
  something = random.randint(1, 4)
  if something == 1:
    rest(2)
  elif something == 2:
    hunt()
  elif something == 3:
    randomSick
  else:
    pass
  
def lowFood():
  global food
  if food < 50:
    huntQ = input("Low food, hunt? ")
    if huntQ.lower() == 'y' or huntQ.lower() == 'yes':
      hunt()
    else:
      print(food)
      
def lowHealth():
  global health
  if health < 50:
    restQ = input("Low health, rest? ")
    if restQ.lower() == 'y' or restQ.lower() == 'yes':
      daysQ = input("How many days? ")
      rest(int(daysQ))
    else:
      print(health)

# name = getName()
# print(f"Welcome, {name}, to the adventure!")

# (role, health, money) = setRole()
# print(f"Role: {role}, Health: {health}, Money: {money}")

update(20, 2, 'Charlotte')
