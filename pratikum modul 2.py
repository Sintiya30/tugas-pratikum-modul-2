import math 

Lintang1 = math.radians(float(input("Lintang Kota 1;")))
Bujur1 = math.radians(float(input("Bujur Kota 1;")))
Lintang2 = math.radians(float(input("Lintang kota 2;")))
Bujur2 = math.radians(float(input("Bujur kota 2;")))

R = 6371
Lat = Lintang2 - Lintang1
Long = Bujur2 - Bujur1

a = math.sin(Lat/2)**2 + math.cos(Lintang1) * math.cos(Lintang2) * math.sin(Long/2)**2
C3 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = R * C3


print("jarak antara dua titik tersebut adalah ", d, "kilometer")


import math
nilai_A = float(input("Masukkan Bilangan 1 ="))
nilai_B= float(input("Masukan Bilangan 2= "))
jumlah = nilai_A + nilai_B
hasil_selisih = nilai_A - nilai_B
hasil_kali= nilai_A * nilai_B
hasil_modulus = nilai_A % nilai_B
hasil_bagi= nilai_A / nilai_B
hasil_logA= math.log(nilai_A)
hasil_pangkat = nilai_A ** nilai_B
print(f"hasil dari jumlah nilai_A + nilai_A adalah {jumlah}")
print(f"hasil dari selisih nilai_A - nilai_A adalah {hasil_selisih}")
print(f"hasil dari kali nilai_A * nilai_Aadalah {hasil_kali}")
print(f"hasil dari modulud nilai_A % nilai_A adalah {hasil_modulus}")
print(f"hasil dari bagi nilai_A / nilai_A adalah {hasil_bagi}")
print(f"hasil dari logA adalah {hasil_logA}")
print(f"hasil dari A pangkat B adalah {hasil_pangkat}")



