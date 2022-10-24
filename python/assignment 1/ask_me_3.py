# Asks for the name
name = str(input("Please enter your name: "))
# if the name is jack or jackie, it greets with the name and says bye.
if (name == "Jackie"):
    print("Hello", name,", hope you are doing great.")
    print("bye", name,", Hope to see you soon!!")
elif (name == "Jack"):
    print("Hello", name,", hope you are doing great.")
    print("bye", name,", Hope to see you soon!!")
# Or else it will call you friend and get to ask more questions like your age and inform you of what you should be doing at said age
else: 
    print("Hello Friend!!!")
    age = int(input("How old are you? "))
    if age < 18 :
        print("YOU are below the working age.")
    elif 18 < age < 25 :
        print("You are of age, look for a JOB!!!") 
    elif 25 < age < 30 :
        print("you should be working already")
    elif 30 < age < 60 :
        print("Think about your family dude!")
    elif 60 <= age < 90:
        print("Please Retire")
    else :
        print("Goodbye",name,"who is",age,"years old, you my friend are an Alien")