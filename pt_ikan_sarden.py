# REQUIREMENTS
# 1. python 3
# 2. pip 
# 3. install sympy library using pip

# HOW TO RUN
# py pt_ikan_sarden.py
# or
# python pt_ikan_sarden.py

from sympy import symbols, Eq, solve

print('------------------------------------------------------')
print('------------------- PT IKAN SARDEN -------------------')
print('------------------------------------------------------')

#inisialisasi permintaan, persediaan, dan produksi
permintaan_tertinggi = 64000
permintaan_terkecil = 4166
persediaan_terbesar = 10000
persediaan_terkecil = 5000
produksi_maksimum = 120000
produksi_minimum = 25000

#jumlah permintaan hari ini & persediaan yang masih tersisa
print('Permintaan Tertinggi: ' + str(permintaan_tertinggi) + ' pack')
print('Permintaan Terkecil: ' + str(permintaan_terkecil) + ' pack')
print('Persediaan Terbesar: ' + str(persediaan_terbesar) + ' pack')
print('Persediaan Terkecil: ' + str(persediaan_terkecil) + ' pack')
print('Produksi Maksimum: ' + str(produksi_maksimum) + ' pack')
print('Produksi Minimum: ' + str(produksi_minimum) + ' pack')
print('------------------------------------------------------')
permintaan = int(input("Masukan jumlah permintaan produksi hari ini: "))
persediaan = int(input('Masukan jumlah persediaan yang tersisa: '))

# 1 FUZZIFIKASI
pmtTurun = (permintaan_tertinggi - permintaan) / (permintaan_tertinggi - permintaan_terkecil)
pmtNaik = 1 - pmtTurun

psdSedikit = (persediaan_terbesar - persediaan) / (persediaan_terbesar - persediaan_terkecil)
psdBanyak = 1 - psdSedikit

# 2 INFERENSI
z = symbols('z')

predikat_1 = min(pmtTurun, psdBanyak)
z1 = solve(Eq((produksi_maksimum - z) / (produksi_maksimum - produksi_minimum), predikat_1))[0]

predikat_2 = min(pmtTurun, psdSedikit)
z2 = solve(Eq((produksi_maksimum - z) / (produksi_maksimum - produksi_minimum), predikat_2))[0]

predikat_3 = min(pmtNaik, psdBanyak)
z3 = solve(Eq((z - produksi_minimum) / (produksi_maksimum - produksi_minimum), predikat_3))[0]

predikat_4 = min(pmtNaik, psdSedikit)
z4 = solve(Eq((z - produksi_minimum) / (produksi_maksimum - produksi_minimum), predikat_4))[0]

# 3 DEFUZZIFIKASI
Z = ((predikat_1 * z1) + (predikat_2 * z2) + (predikat_3 * z3) + (predikat_4 * z4)) / (predikat_1 + predikat_2 + predikat_3 + predikat_4)

print('------------------------------------------------------')
print('Ikan Sarden yang harus diproduksi hari ini:')
print(str(round(Z)) + ' pack')