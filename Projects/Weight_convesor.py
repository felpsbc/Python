weight = float(input("Enter your weight:"))
unit = input("Kilograms or Pounds? Enter (K) for kilograms or (L) for Pounds:  ")

if unit == "K":
    print(f"Your weight in Pounds is {weight*2.20462}")
else:
    print(f"Your weight in Kilograms is {weight/2.20462}")



