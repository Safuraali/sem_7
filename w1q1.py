##readings = list(map(float, input("Enter temperatures in Celsius separated by spaces: ").split()))
readings = [22.5, 23.1, 20.9, 24.0, 21.5, 19.8, 26.2, 23.5]
fahrenheit_readings = [c * 9/5 + 32 for c in readings]

hot_days = [c for c in readings if c > 23.0]

print("Fahrenheit readings:", fahrenheit_readings)
print("Hot days:", hot_days)
