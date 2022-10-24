#A program that tells you your grade.
score = float(input("Enter your score: "))
if 0.9 <= score <= 1.0:
    print("A")

elif 0.8 <= score < 0.9:
    print("B")

elif 0.7 <= score < 0.8:
    print("C")

elif 0.6 <= score < 0.7:
    print("D")

elif 0.0 <= score < 0.6:
    print("F")

else:
    print("Bad score!!")