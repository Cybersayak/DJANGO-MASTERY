shop_name = "DADA BOUDI Biriyani"

menu = ["Hyderabadi Biriyani", "Muradabadi Biriyani"]

Customer_Demand = input("Enter which biriyani do you want? - ")

if Customer_Demand in menu:
    print(f"Yes, {Customer_Demand} is available")
else:
    print("Sorry, Dish is not Available")

     