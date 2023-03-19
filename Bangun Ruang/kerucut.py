jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))

pi = 3.14

garis_pelukis = (jari_jari**2 + tinggi**2)**0.5
luas_permukaan = pi * jari_jari * (jari_jari + garis_pelukis)
volume = 1/3 * pi * jari_jari ** 2 * tinggi

print("Luas permukaan kerucut adalah:", luas_permukaan)
print("Volume kerucut adalah:", volume)
