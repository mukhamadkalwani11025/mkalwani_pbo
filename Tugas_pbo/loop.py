# loop

angka_rahasia = 44
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-100): "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")

print("Selamat, Anda menebak angka yang benar:", angka_rahasia)
