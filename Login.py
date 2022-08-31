#this is login page for our app


# ----------------------------<<< import External File >>>--------------------------


FoodList = "Pizza" , "Salad"
DrinkList = "Cola" , "Sprite"



# ----------------------------<<< user Information >>>------------------------------


U_Name = "Tony Smith"
UserName = "Tony"
UserEmail = "tony@smith.com"
PassWord = "T0NY"



# ----------------------------<<< User Login >>>------------------------------------

print ("Enter Your User Name or Email Address")

UserInput = input()

if UserInput == UserName or UserEmail :
    print ("Enter Your Password")
    PassInput = input()
    if PassInput == PassWord :
        print ("--------------------------------")
        print ("You Logedin")
        print (f"Welcome" , U_Name )

    else :
        print ("Your Password is not Correct")        
else :
    print ("Your User Name or Email Address is not Correct")

print ("--------------------------------")


# ----------------------------<<< Select Food >>>-----------------------------------


print ("Type Your Food Name : ")
print (FoodList)

InputFood = input()

if InputFood == FoodList :
    print("you select this" + InputFood)


print ("---------------------------------------------------------")

print ("Now Type Your Drink Name : ")
print (DrinkList)

InputDrink = input()

if InputDrink == DrinkList :
    print("you select this" + InputDrink)