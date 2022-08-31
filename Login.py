#this is login page for our app

# ----------------------------<<< set User And Pass >>>-----------------------------

U_Name = "Tony Smith"
UserName = "Tony"
PassWord = "T0NY"


# ----------------------------<<< Check User And Pass >>>----------------------------

print ("Enter Your User Name")

UserInput = input()

if UserInput == UserName :
    print ("Enter Your Password")
    PassInput = input()
    if PassInput == PassWord :
        print ("You Logedin")
        print (f"Welcome" , U_Name )
    else :
        print ("Your Password is not Correct")        
else :
    print ("Your User Name is not Correct")
