print("Konversi Suhu Reamur")

def get_celsius(suhu):
    C = (5/4) * float(suhu)
    return C

def get_fahrenheit(suhu):
    F = (9/4) * float(suhu) + 32
    return F

def get_kelvin(suhu):
    K = (5/4) * float(suhu) + 273.15
    return K

# Input
suhu_reamur = input("Masukkan suhu dalam Reamur:")

# Konversi ke Celsius
celsius = get_celsius(suhu_reamur)

# Konversi ke Fahrenheit
fahrenheit = get_fahrenheit(suhu_reamur)

# Konversi ke Kelvin
kelvin = get_kelvin(suhu_reamur)

# Output
print(f"{suhu_reamur} Reamur sama dengan ")
print(f"{celsius:.2f} Celsius")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{kelvin:.2f} Kelvin")
