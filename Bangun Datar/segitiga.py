# input sisi-sisi segitiga
sisi1 = float(input("Masukkan sisi 1: "))
sisi2 = float(input("Masukkan sisi 2: "))
sisi3 = float(input("Masukkan sisi 3: "))

# menghitung keliling segitiga
keliling = sisi1 + sisi2 + sisi3

# menghitung setengah dari keliling segitiga
s = keliling / 2

# menghitung luas segitiga dengan rumus Heron
luas = (s * (s - sisi1) * (s - sisi2) * (s - sisi3)) ** 0.5

# menampilkan hasil perhitungan
print("Keliling segitiga = ", keliling)
print("Luas segitiga = ", luas)
