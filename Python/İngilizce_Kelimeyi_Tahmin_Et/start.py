#Ekrana gelen ingilizce cümledeki eksik kelimeyi bul
#https://www.limasollunaci.com/ingilizce-cumleler
#Mehmet Akif SELBİ

import random
class İngilizce:

    def __init__(self):
        self.dosya = open("cumleler.txt")
        self.cumleler = self.dosya.readlines()
        self.cumle = self.cumleler[random.randint(0,len(self.cumleler)-1)]
        self.tahmin_hakki = 3
        self.isim = ""

    def secim(self):
        while(1):
            index_1 = random.randint(0,len(self.cumle)-1)
            isim = self.cumle[index_1]
            
            if(isim == self.cumle[-1] or isim.isupper() == True):
                continue
            index_2 = index_1+1
            harf = self.cumle[index_2]

            if(self.cumle[index_1-1] == " "):
                while(1):
                    isim+=harf
                    if(harf == self.cumle[-1]):
                        break
                    index_2+=1
                    harf = self.cumle[index_2]
                    if(harf == " " or harf == "\n"):
                        break
                print(self.cumle[0:index_1],"....",self.cumle[index_2:-1])
                return isim

    def ekrana_yaz(self):
        self.isim = self.secim()
        print(len(self.isim),"harfli bir kelime\n")
    
    def tahmin(self):
        tahmin = input("Tahmin = ")
        if(tahmin == self.isim):
            return 1
        else:
            self.tahmin_hakki -= 1
            return 0

    def basla(self):
        self.ekrana_yaz()
        while(1):
            if(self.tahmin()):
                print("Doğru Tahmin")
                break
            elif(self.tahmin_hakki != 0):
                print("Yanlış Tahmin","Tahmin Hakkı =",self.tahmin_hakki)
            else:
                print("Yanlış Tahmin Tahmin Hakkı =",self.tahmin_hakki,"\n",self.cumle)
                break


if __name__ == '__main__':
    ing = İngilizce()
    ing.basla()
