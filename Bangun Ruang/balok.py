# input panjang, lebar, dan tinggi balok
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

# hitung luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# hitung keliling balok
keliling = 4 * (panjang + lebar + tinggi)

# hitung volume balok
volume = panjang * lebar * tinggi

# tampilkan hasil
print("Luas permukaan balok = ", luas_permukaan)
print("Keliling balok = ", keliling)
print("Volume balok = ", volume)
