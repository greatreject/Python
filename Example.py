print("Welcome to our shop")
name = input("What is your name?")
mood = input("Hello " + name + " how are you today?")
print("I am " + mood + " today")
purchase = input("Is there anything you are interested in?")

if purchase == "yes":
    print("Take a look around and see if you find something you like")
elif purchase == "no":
    print("Stop wasting my time! Lol only joking!")
else:
    print("I am sorry I didn't understand that")