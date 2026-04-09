class Temperature:
    # Convert Celsius to Fahrenheit
    def convert_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    # Convert Fahrenheit to Celsius
    def convert_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

# Main program
t = Temperature()

print("Temperature Conversion Menu")
print("1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C = {t.convert_fahrenheit(c):.2f}°F")
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F = {t.convert_celsius(f):.2f}°C")
else:
    print("Invalid choice!")
