#Coffee menu

#Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation.

#if name == "Ben":
#  evil_status = input("Are you evil?\n")
#  if evil_status == "Yes":
#    print("You're not welcome here Ben!! Get out!!")
#    exit()
#  else:
#    print("Oh you are a good Ben, come on in!")
#else:
#  print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

#Ask the customer what they would like from the menu and store it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

#Set the price for coffee

if order == "Frappuccino":
  price = 13
elif order == "Black Coffee":
  price = 3
elif order == "Espresso":
  price = 4
elif order == "Latte":
  price = 5
elif order == "Cappucino":
  price = 6
else:
  print("We don't have that here...")
  price = 0

print(price)