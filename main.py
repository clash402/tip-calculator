# MAIN
bill = float(input("What is the total bill? $"))
tip = float(input("What percentage tip would you like to give: 10, 15, 20? ")) / 100
split = int(input("How many people to split the bill? "))

total = bill * tip + bill
total_split = total / split
total_rounded = round(total_split, 2)
total_rounded = "{:.2f}".format(total_split)

print(f"Each person pays {total_rounded}")
