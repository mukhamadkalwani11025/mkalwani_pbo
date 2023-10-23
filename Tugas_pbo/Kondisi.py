# kondisi

# Input data pemain
usia = 20
tinggi = 175  # dalam cm
kecepatan = 30  # dalam km/jam

# Kriteria seleksi
batas_usia = 25
batas_tinggi = 180
batas_kecepatan = 25

# Seleksi pemain
if usia <= batas_usia and tinggi >= batas_tinggi and kecepatan >= batas_kecepatan:
    status = "LOLOS"
else:
    status = "TIDAK LOLOS"

# Output hasil seleksi
print(f"Usia: {usia} tahun")
print(f"Tinggi: {tinggi} cm")
print(f"Kecepatan: {kecepatan} km/jam")
print(f"Status: {status}")