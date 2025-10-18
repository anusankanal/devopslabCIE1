

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

if celsius < 15:
    category = "Cold"
elif 15 <= celsius <= 30:
    category = "Normal"
else:
    category = "Hot"

print(f"Temperature: {celsius}°C")
print(f"temperature:{fahrenheit:.2f}°F — It's {category}.")
