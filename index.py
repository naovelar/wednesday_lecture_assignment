#Build a Shopping Cart
#You can use either lists or dictionaries. The program should have the following capabilities:

#1) Takes in input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, print out all items in the user's list

cart = []

def addItem(item):
  cart.appent(item)
def removeItem(item):
  cart.remove(item)
def showCart():
  print("This is what is in your cart...")
  for item in cart:
    print(item)
    
def clearCart():
  print("Your cart is now empty")
  cart.clear()
  
def shoppingCart():
  while True:
  response = input("Would you like to: add, remove, show or clear cart?")
  if response.lower() == "quit":
    print("Thank you for shopping!")
    showCart()
    break
  elif response.lower() == "add":
    item = input("What would you like to add to your cart?")
    addItem(item)
  elif response.lower() == "remove"
    item = input("What would you like to remove from your cart?")
    removeItem(item)
  elif response.lower() == "show"
    showCart()
  elif response.lower() == "clear"
    clearCart()
    
 shoppingCart()
 print(shoppingCart)
 
 #Create a Module in VS Code and Import It into jupyter notebook
Module should have the following capabilities:

#1) Has a function to calculate the square footage of a house
Reminder of Formula: Length X Width == Area

#2) Has a function to calculate the circumference of a circle

def area():

    shape = input ("Enter the shape you want to calculate the area of: ")
    
    area = 0
    pi = 3.14
    
    if shape == "square":
        side = int(input("Enter the value of side: "))
        area = area + (side ** 2)
    elif shape == "Circle":
        radius = int(input("Enter the value of radius: "))
        area = area + (2 * pi * radius)
    else:
        break
    
    shape()
    print(shape)
