import random

def zar():
    min_zar = 1
    max_zar = 6
    zar = random.randint(min_zar,max_zar)
    return  zar

print("Zar Oyununa hoşgeldiniz 1 atana kadar istediğiniz gibi devam edebilirsiniz ama 1 atarsanız toplam puanınız sıfırlanır.")
max_puan = 50
basla = input("Oyuna Başlamak ister misiniz ? e/h")
oyuncular = 2
oyuncu_puan = [0 for _ in range(oyuncular)]

while max(oyuncu_puan) < max_puan:
    for oyuncuid in range(oyuncular):
        print("Şimdi sırada ", oyuncuid +1,". oyuncu var")
        print("Senin toplam skorun : ", oyuncu_puan[oyuncuid])
        simdiki_puan = 0
        while True:
            dur_devam = input("Zar Atmak İster misin ? (e)")
            if dur_devam != "e":
                break
            cikanzar = zar()
            if cikanzar == 1:
              print("Zar attın maalesef çıkan zar :", cikanzar)
              print("Senin sıran bitti.")
              simdiki_puan = 0
              break
            else:
                print("Zar attın çıkan zar :", cikanzar)
                simdiki_puan += cikanzar

            print("Senin turdaki skorun : ", simdiki_puan )
        oyuncu_puan[oyuncuid] += simdiki_puan
        print("Senin Toplam skorun :" ,oyuncu_puan[oyuncuid])
        print("------------------------------------------------------")

max_puan = max(oyuncu_puan)
kazananoyuncu = oyuncu_puan.index(max_puan) + 1
print(max_puan ,"ile kazanan oyuncu :" ,"Oyuncu",kazananoyuncu)



