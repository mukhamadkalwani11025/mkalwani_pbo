print("Konversi Suhu Fahrenheit")

# Input
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit:"))

# Rumus konversi
celsius = (5/9) * (fahrenheit - 32)
reamur = (4/9) * (fahrenheit - 32)
kelvin = (5/9) * (fahrenheit - 32) + 273.15

# Output
print(f"{fahrenheit} Fahrenheit sama dengan ")
print(f"{celsius:.2f} Celsius")
print(f"{reamur:.2f} Reamur")
print(f"{kelvin:.2f} Kelvin")

