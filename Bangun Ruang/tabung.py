jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

pi = 3.14

luas_permukaan = 2 * pi * jari_jari * (jari_jari + tinggi)
volume = pi * jari_jari ** 2 * tinggi

print("Luas permukaan tabung adalah:", luas_permukaan)
print("Volume tabung adalah:", volume)
