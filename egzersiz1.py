#mastermind
import random

tutulan=str(random.randint(10,99))
print(tutulan)

tahmin=input("10 ile 98 arasında bir sayı girin: ")
#bilgisayarın tuttuğu sayının rakamları aynı ise
while tutulan[0]==tutulan[1]:
    tutulan=str(random.randint(10,99))
#kullanıcı geçersiz bir sayı girdiyse
while int(tahmin)<10 or int(tahmin)>98 or tahmin[0]==tahmin[1]:
    tahmin=input("Geçerli bir sayı girin: ")

while tutulan!=tahmin:
    dogru_yer=0
    yanlis_yer=0
    if tutulan[0]==tahmin[0] or tutulan[1]==tahmin[1]:
        dogru_yer=dogru_yer+1
    if tutulan[0]==tahmin[1]:
        yanlis_yer=yanlis_yer-1
    if tutulan[1]==tahmin[0]:
        yanlis_yer=yanlis_yer-1

    print("Doğru yer: ", dogru_yer)
    print("Yanlış yer: ", yanlis_yer)
    tahmin=input("Bilemediniz! Başka bir sayı girin: ")

    while int(tahmin)<10 or int(tahmin)>98 or tahmin[0]==tahmin[1]:
        tahmin=input("Geçerli bir sayı girin: ")    



if tutulan==tahmin:
    print("Tebrikler kazandınız!")
    
