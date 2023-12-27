print("Konversi Suhu Reamur")

# Input
reamur = float(input("Masukkan suhu dalam Reamur:"))

# Rumus konversi
celsius = (5/4) * reamur
fahrenheit = (9/4) * reamur + 32
kelvin = (5/4) * reamur + 273.15

# Output
print(f"{reamur} Reamur sama dengan ")
print(f"{celsius:.2f} Celsius")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{kelvin:.2f} Kelvin")
