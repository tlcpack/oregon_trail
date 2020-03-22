import random, time, sys

health = 100
money = 0
food = 0
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


name = getName()
print(f"Welcome, {name}, to the adventure!")

(role, health, money) = setRole()
print(f"Role: {role}, Health: {health}, Money: {money}")