def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

print("Temperature Converter")
print("1. Celsius to Fahrenheit and Kelvin")
print("2. Fahrenheit to Celsius")
print("3. Kelvin to Celsius")

option = input("Choose an option (1/2/3): ")

if option == "1":
    celsius = float(input("Enter the temperature in Celsius: "))
    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    print(f"{celsius}°C = {celsius_to_kelvin(celsius):.2f}K")

elif option == "2":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")

elif option == "3":
    kelvin = float(input("Enter the temperature in Kelvin: "))
    print(f"{kelvin}K = {kelvin_to_celsius(kelvin):.2f}°C")

else:
    print("Invalid option!")
