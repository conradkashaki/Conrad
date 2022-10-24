#A program that prompts the user for their name, and greets them with their name.
# If the name ain't mentioned, it goes ahead to call them stranger.
name=str(input("Hey please enter your name: "))
if name:
    print("Hello", name,", how you doing")
else:    
    print("Hello, stranger")