# Oyuncu, anlamı ekranda gözüken ismi tahmin etmeye çalışır. 3 hakkı vardır.
#https://onedio.com/haber/en-cok-kullanilan-kiz-isimleri-ve-anlamlari-a-dan-z-ye-kiz-isimleri-listesi-822036

#Mehmet Akif SELBİ
import random

class İsimTahmini:
    
    def __init__(self):
        self.liste=["A","B","C","Ç","D","E","F","G","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
        self.rand = random.randint(0,len(self.liste)-1)
        self.dosya = open("İsimler/"+self.liste[self.rand]+".txt")
        self.isimler = self.dosya.readlines()
        self.kelime = self.isimler[random.randint(0,len(self.isimler)-1)]
        self.isim = self.isim_ayir()
        self.anlam = self.anlam_ayir()
        self.tahmin_hakki = 3

    def isim_ayir(self):
        isim=""
        for i in self.kelime:
            if(i == ":"):
                break
            isim+=i
        return isim

    def anlam_ayir(self):
        anlam,j="",0
        for i in self.kelime:
            if(i == ":"):
                j=1
            elif(j==1):
                anlam+=i
        return anlam

    def ekrana_yaz(self):
       print(self.anlam)
       for i in self.isim:
           print("_",end=" ")
       print("")

    def tahmin(self):
        while(self.tahmin_hakki != 0):
            tahmin = input("Tahmin = ")
            if(tahmin == self.isim):
                print("Doğru Tahmin")
                return 1
            else:
                self.tahmin_hakki -=1
                print("Yanlış Tahmin, Tahmin Hakkı = ",self.tahmin_hakki)
        return 0

    def oyuna_basla(self):
        self.ekrana_yaz()
        while(1):
            if(self.tahmin()):
                break
            elif(self.tahmin_hakki == 0):
                print("Doğru Cevap = ",self.isim)
                break


if __name__=='__main__':
    oyuncu_1 = İsimTahmini()
    oyuncu_1.oyuna_basla()

