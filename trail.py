import random, time

health = 0
money = 0
food = 50
role = ''

# break_program = False
# def on_press(key):
#     global break_program
#     print (key)
#     if key == keyboard.Key.esc:
#         print ('end pressed')
#         break_program = True
#         return False

# with keyboard.Listener(on_press=on_press) as listener:
#     while break_program == False:
#         print ('program running')
#         time.sleep(5)
#     listener.join()

class Destination:
  def __init__(self, name, miles):
    self.name = name
    self.miles = miles

durham = Destination("Durham", 300)
charlotte = Destination("Charlotte", 450)

print("Welcome to the Oregon Trail")
time.sleep(1)

def getName():
  name = input("Enter your name: ")
  print(f"Welcome, {name}, to the adventure!")
  return name

def setRole():
  while True:
    role = input("Who do you want to be: 1 for Doctor, 2 for Banker ")
    if role == '1':
      role = 'Doctor'
      health = 25
      money = 100
      break
    elif role == '2':
      role = 'Banker'
      health = 20
      money = 150
      break
    else:
      print('Please enter something valid')
  print(f"Health: {health}, Money: {money}")
  return role, health, money

def setPace():
  while True:
    paceInput = input("How fast would you like to go? 1 for Fast, 2 for slow ")
    if int(paceInput) == 1:
      pace = 10
      return pace
    elif int(paceInput) == 2:
      pace = 3
      return pace
    else:
      print("Please enter something valid")

def hunt():
  global food
  huntedFood = random.randint(1, 200)
  food += huntedFood
  print('Hunting')
  return food

def rest():
  global health
  while True:
    days = input('How many days? ')
    if days.isdigit():
      health = health + (int(days) * 3)
      print('Resting ', health)
      return health
    else:
      print('Enter a positive integer')

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

def travel(name, distance, pace, destination, health, food):
  print(distance, health, food)
  while distance > 0 and health > 0 and food > 0:
    print(f"{distance} miles to go")
    print(f"Health: {health}")
    time.sleep(1)
    event()
    food -= 5
    lowFood()
    health -= 10
    lowHealth()
    distance -= 3 * pace
    if distance <= 0:  
      return print(f"{name} arrived at {destination}")
  return health, food

def event():
  global food
  something = random.randint(1, 4)
  if something == 1:
    rest()
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
      rest()
    else:
      print("Health: " + str(health))

def checklife(health, food):
  if health <= 0 or food <= 0:
    print("you died")

def game(health, money):
  global food
  name = getName()
  role,health,money = setRole()
  pace = setPace()
  while health > 0:
    health,food = travel(name, durham.miles, pace, durham.name, health, food)
    print(health)
    checklife(health, food)
    health,food = travel(name, charlotte.miles, pace, charlotte.name, health, food)
    print(health)
    checklife(health, food)
    print('You made it')
    break
  print('You died')

# name = getName()
# print(f"Welcome, {name}, to the adventure!")

# (role, health, money) = setRole()
# print(f"Role: {role}, Health: {health}, Money: {money}")

game(health, money)
