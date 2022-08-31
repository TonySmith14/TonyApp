#this is login page for our app

# ----------------------------<<< set User And Pass >>>-----------------------------

U_Name = "Tony Smith"
UserName = "Tony"
UserEmail = "tony@smith.com"
PassWord = "T0NY"


# ----------------------------<<< Check User And Pass >>>----------------------------

print ("Enter Your User Name or Email Address")

UserInput = input()

if UserInput == UserName or UserEmail :
    print ("Enter Your Password")
    PassInput = input()
    if PassInput == PassWord :
        print ("You Logedin")
        print (f"Welcome" , U_Name )
    else :
        print ("Your Password is not Correct")        
else :
    print ("Your User Name or Email Address is not Correct")

