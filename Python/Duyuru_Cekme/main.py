#http://ce.muhendislik.comu.edu.tr/arsiv/duyurular duyuruları çeker ve kayıtlı maillere duyuruları mail atar
#mail_gonder.py dosyasına email atacak mail adresini ve şifresini girin
#Mehmet Akif SELBİ

import time
import arayuz as ar
import veri_tabani as vt
import duyurular as dy
import mail_gonder as mg

zaman,sayi = 1,1 #varsayılan değerler

def komutlar():
    print("""
        help    ---> Komut Penceresini Açar
        arayuz  ---> Mail Kayıt Arayüzünü Açar
        mail    ---> Komut Penceresinde mail işlemleri için
        duyuru  ---> Duyuruları listeler
        time    ---> Duyuru kontrol zamanını ayarlama(varsayılan 1dk)
        start   ---> Programı Başlatır (Atılmış mail bir daha atılmaz)
        start2  ---> Programı Başlatır (Atılmış mail bir daha atılabilir)
        exit    ---> Program sonlanır
        
    """)
    
def start():
    print("Program başladığında aynı anda kaç mail atılıcağını giriniz")
    try:
        sayi = int(input("Sayi Girin : "))
    except:
        print("Doğal sayı giriniz")
        start()
        
    while(True):
            if(sayi>15):
                sayi = 15
            elif(sayi<1):
                sayi = 1
                
            linkler = dy.linkler()
            link = vt.vt_link_cekme()
            for i in link:
                for j in i:
                    link = j
                
            liste = []
            for i in linkler:
                if(i!= link):
                    liste.append(i)
                else:
                    break
            if(len(liste)>0):
                try:
                    liste = liste[:sayi]
                except:
                    print("hata")
                    
                duyuru = dy.basliklar()
                flag = 1
                konu=[]
                for i in duyuru:
                    if(flag==2):konu.append(i)
                    if(flag==4):flag=0
                    flag +=1
                konu = konu[:len(liste)]
                yazilar = dy.yazilar(liste)
                mailler = vt.vt_mail_cekme()
                for i in mailler:
                    for k in i:
                        for j in range(len(liste)):
                            mg.mail(konu[j],yazilar[j],k)
                
                vt.vt_link_silme(link)
                liste = [liste[0]]
                vt.vt_link(liste)
            else:
                print("Yeni Duyuru Yok")
            time.sleep(60*zaman)

def linksil():
    link = vt.vt_link_cekme()
    for i in link:
            for j in i:
                link = j
    vt.vt_link_silme(link)

def mail_getir():
    im = vt.vt_veri_cekme()
    for i in im:
        print(i)
            
def mail_kaydet():
    isim = input("İsim : ")
    mail = input("Mail : ")
    sinif = input("Sınıf : ")
    liste = [mail,isim,sinif]
    vt.vt_mail(liste)
        
def mail_sil():
    maill = input("Kayıtlı Kişinin Maili : ")
    vt.vt_mail_silme(maill)

def main():       
    while(True):
        secim = input("==> ")
        if(secim == "help"):
            komutlar()
            
        elif(secim == "arayuz"):
            ar.calistir()
            
        elif(secim == "mail"):
            print("""
                kaydet   ---> Terminalden mail ve kişi kaydetmek için
                sil      ---> Kayitli kişileri silmek için
                listele  ---> Kayıtlı kişileri listelemek için
                exit     ---> Komut Penceresine dönmek için
                        """)
            while(True):
                secim_2 = input("m=: ")
                
                if(secim_2 == "kaydet"):
                    mail_kaydet()

                elif(secim_2 == "sil"):
                    mail_sil()
                
                elif(secim_2 == "listele"):
                    mail_getir()
                    
                elif(secim_2 == "exit"):
                    break
                    main()
                else:
                    print("Lütfen komutlardan birini giriniz")
                
        elif(secim == "duyuru"):
            duyuru = dy.basliklar()
            flag = 1
            for i in duyuru:
                if(flag==2):print(i)
                if(flag==4):flag=0
                flag +=1
                
        elif(secim == "time"):
            try:
                zaman = int(input("Dakika Giriniz : "))
            except:
                print("Tam sayı giriniz")
                
        elif(secim == "start"):
            start()

        elif(secim == "start2"):
            linksil()
            start()

        elif(secim == "exit"):
            break

        else:
            print("Lütfen komutlardan birini giriniz")

komutlar()       
main()

