print("Konversi Suhu Kelvin")

# Input
kelvin = float(input("Masukkan suhu dalam Kelvin:"))

# Rumus konversi
reamur = (4/5) * (kelvin - 273.15)
fahrenheit = (9/5) * (kelvin - 273.15) + 32
celsius = kelvin - 273.15

# Output
print(f"{kelvin} Kelvin sama dengan ")
print(f"{reamur:.2f} Reamur")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{celsius:.2f} Celsius")