sayi= 1000
toplam_deger = 0

for i in range (1,sayi):
    if (i % 3) == 0 :
        toplam_deger = toplam_deger + i
    if (i % 5) == 0:
        toplam_deger = toplam_deger + i
    if (i % 15) == 0:
        toplam_deger = toplam_deger - i
print(toplam_deger)