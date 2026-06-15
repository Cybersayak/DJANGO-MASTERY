restaurant= "Udupi Hotel"
print("Welcome to", restaurant)

print("Please select your order from the menu")

print("1. Dosa-INR 80")
print("2. Idli-INR 50")
print("3. Vada-INR 60")
print("4. Pongal-INR 70")

order = int(input("Enter what you like to eat : "))

if order == 1:
    print("You have ordered Dosa , it will be ready in 10 minutes")
elif order == Idli:
    print("You have ordered Idli , it will be ready in 5 minutes")
elif order == Vada:
    print("You have ordered Vada , it will be ready in 7 minutes")
elif order == Pongal:
    print("You have ordered Pongal , it will be ready in 12 minutes")
else:
    print("Sorry we don't have that item in our menu")

instructions = input("Please enter the instructions for your order : ")
instructions = instructions.lower()

if "extra chutney" in instructions:
    print("Your order will be extra chutney")
if "less oil" in instructions:
    print("Your order will be with less oil")
if "no onion" in instructions:
    print("Your order will be without onion")
if "no garlic" in instructions:
    print("Your order will be without garlic")
else :
    print("Your order will be prepared as per the standard recipe")

