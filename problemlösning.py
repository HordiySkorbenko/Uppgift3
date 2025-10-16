def celsius_convertion(choice, temperature):
    if choice == "1" :
        fahrenheit = (temperature * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == "2" :
        celsius = (temperature - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == "3" :
        celsius = temperature - 273.15
        print(f"{kelvin}K is equal to {celsius}°C")
    elif choice == "4" :    
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {kelvin}K")

print(celsius_convertion())