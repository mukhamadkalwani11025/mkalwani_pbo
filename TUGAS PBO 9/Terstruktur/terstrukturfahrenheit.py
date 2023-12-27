print("Konversi Suhu Fahrenheit")

def get_celsius(suhu):
    C = (5/9) * (float(suhu) - 32)
    return C

def get_reamur(suhu):
    R = (4/9) * (float(suhu) - 32)
    return R

def get_kelvin(suhu):
    K = (5/9) * (float(suhu) - 32) + 273.15
    return K

# Input
suhu_fahrenheit = input("Masukkan suhu dalam Fahrenheit:")

# Konversi ke Celsius
celsius = get_celsius(suhu_fahrenheit)

# Konversi ke Reamur
reamur = get_reamur(suhu_fahrenheit)

# Konversi ke Kelvin
kelvin = get_kelvin(suhu_fahrenheit)

# Output
print(f"{suhu_fahrenheit} Fahrenheit sama dengan ")
print(f"{celsius:.2f} Celsius")
print(f"{reamur:.2f} Reamur")
print(f"{kelvin:.2f} Kelvin")
