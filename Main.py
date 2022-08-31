# ----------------------------<<< import External File >>>--------------------------


FoodList = "Pizza" , "Salad"
DrinkList = "Cola" , "Sprite"


# ----------------------------<<< Select Food >>>-----------------------------------


print ("Type Your Food Name : ")
print (FoodList)

InputFood = input()

if InputFood == FoodList :
    print("you select this" + InputFood)


print ("--------------------------------")

print ("Now Type Your Drink Name : ")
print (DrinkList)

InputDrink = input()

if InputDrink == DrinkList :
    print("you select this" + InputDrink)