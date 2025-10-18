# Python program to classify temperature in Celsius and Fahrenheit

# Get temperature input from user in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Classify temperature based on Celsius
if celsius < 15:
    category = "Cold"
elif 15 <= celsius <= 30:
    category = "Normal"
else:
    category = "Hot"

# Display results
print(f"Temperature: {celsius}°C / {fahrenheit:.2f}°F — It's {category}.")