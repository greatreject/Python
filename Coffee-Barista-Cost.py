#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!
#Let's build robot Barista!!



print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!!!!!!")

name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino"

price = 8

order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

quantity = input("How many coffee's would you like?\n")

total = price * int(quantity)

print("Thank you, your total is £" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order+"'s" + " ready in a moment.")