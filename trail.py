import random, time, sys

health = 100
money = 0
food = 1
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

def hunt(food):
  huntedFood = random.randint(1, 200)
  food += huntedFood
  return food

def rest(days):
  global health
  health = health + (days * 3)
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


# name = getName()
# print(f"Welcome, {name}, to the adventure!")

# (role, health, money) = setRole()
# print(f"Role: {role}, Health: {health}, Money: {money}")

newFood = hunt(food)
print(newFood)
