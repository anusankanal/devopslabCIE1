
temperature = float(input("Enter temperature in Celsius: "))

if temperature < 15:
    print("It's Cold.")
elif 15 <= temperature <= 30:
    print("It's Normal.")
else:
    print("It's Hot.")