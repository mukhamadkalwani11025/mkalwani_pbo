print("Konversi Suhu Kelvin")

def get_reamur(suhu):
    R = (4/5) * (float(suhu) - 273.15)
    return R

def get_fahrenheit(suhu):
    F = (9/5) * (float(suhu) - 273.15) + 32
    return F

def get_celsius(suhu):
    C = float(suhu) - 273.15
    return C

# Input
suhu_kelvin = input("Masukkan suhu dalam Kelvin:")

# Konversi ke Reamur
reamur = get_reamur(suhu_kelvin)

# Konversi ke Fahrenheit
fahrenheit = get_fahrenheit(suhu_kelvin)

# Konversi ke Celsius
celsius = get_celsius(suhu_kelvin)

# Output
print(f"{suhu_kelvin} Kelvin sama dengan ")
print(f"{reamur:.2f} Reamur")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{celsius:.2f} Celsius")

