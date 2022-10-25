#lets learn about lists


supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows", "tent"]


camp_site = ["Crystal Lake", 404, 95.5, 10, False]


supplies.extend(["toilet paper", "bidet"])

#supplies.remove("tent")
#supplies.pop(0)
print("This item was deleted: " + supplies.pop(0))

print(supplies)