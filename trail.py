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


name = getName()
print(f"Welcome, {name}, to the adventure!")
