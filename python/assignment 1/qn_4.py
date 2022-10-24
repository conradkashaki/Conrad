#A program that asks for the hours and rate, calculates them and outputs the gross pay
hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = float(hours * rate)

print("Pay: ", pay)