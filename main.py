print("Welcome to the tip calculator!")

bill = float(input("What is the total bill? "))
tip_percentage = float(input("What percentage of tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip = tip_percentage/100
total_tip = bill + (bill * tip)

final_bill = round((total_tip / people),2)

print(f"Each person should pay Rs.{final_bill}")


