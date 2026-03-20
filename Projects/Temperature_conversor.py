temp = float(input("Enter the temperature:  "))
unit = input("Type ( C ) for Celsius , ( F ) for Fahrenheit and ( K ) for Kelvin ")


if unit == "C":
    print(f"Celsius for Fahrenheit {temp*1.8+32}")
    print(f"Celsius for Kelvin {temp+273.15}")
elif unit == "K":
    print(f"Kelvin for Fahrenheit {(temp-273.15)*1.8+32}")
    print(f"Kelvin for Celsius {temp-273.15}")
elif unit == "F":
    print(f"Fahrenheit for Celsius {temp-32/1.8}")
    print(f"Fahrenheit for Kelvin {(temp-32)*1.8+273.15}")
else:
    print("Please enter the correct letter")