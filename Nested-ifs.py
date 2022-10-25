#Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation.

if name == "Ben":
  evil_status = input("Are you evil?\n")
  if evil_status == "Yes":
    print("You're not welcome here Ben!! Get out!!")
    exit()
  else:
    print("Oh you are a good Ben, come on in!")
else:
  print("Hello " + name + ", thank you so much for coming in today.\n\n\n")