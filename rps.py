again = 'y' 

while (again == 'y'):
    p1 = input("player 1 --> Rock, Paper, or Scissors?")
    p1 = p1.lower()

    print()

    p2 = input("player 2 --> Rock, Paper, or Scissors?")
    p2 = p2.lower() 

    print()

    if (p1 == "rock"):
        if (p2 == "rock"):
            print("Its a tie...")
        elif (p2 == "paper"):
            print("player 2 wins")
        elif (p2 == "scissors"):
            print("player 1 wins")
    elif (p1 == "paper"):
        if (p2 == "rock"):
            print("player 1 wins")
        elif (p2 == "paper"):
            print("It is a tie....")
        elif (p2 == "scissors"):
            print("Player 2 wins")
    if (p1 == "scissors"):
        if (p2 == "rock"):
            print("player 2 wins")
        elif (p2 == "paper"):
            print("player 1 wins")
        elif (p2 == "scissors"):
            print("It is a tie....")
    else:
        print()
    again = input("Type y to play again or n to stop")
    print()                                                
