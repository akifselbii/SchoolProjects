#Mehmet Akif SELBİ

from tkinter import *
import duyurular as dy
import veri_tabani as vt

def label(window,yazi,x,y,w,h,boyut,bg):
    lbl = Label(window, text =yazi, fg="black", bg=bg, font=("verdana", boyut, "bold"))
    lbl.place(x=x, y=y, width= w, height=h)
    return lbl

def text_box(window,x,y,w,h):
    tb = Text(window, height= h, width= w)
    tb.config(font =("Courier", 14), state=DISABLED)
    tb.place(x=x, y=y)
    return tb

def buton(window,yazi,x,y,w,h,komut):
    btn = Button(window, font=("Verdana",12,"bold"), text= yazi, width=w, height="5",bd=0, bg="#00007f", activebackground="#3c9d9b", fg='#ffffff', command= komut)
    btn.place(x=x, y=y, height=h)
    return btn

def girdi(window,x,y,w,h):
    box = Text(window, bd=0, bg="white",width="1", height="1", font="Arial")
    box.place(x=x, y=y, height=h, width=w)
    
    return box

def scroll_bar(window,x,y,w,h,komut):
    scrollbar = Scrollbar(window, command=komut.yview)
    scrollbar.place(x=x,y=y, height=h, width=w)
    return scrollbar

def boyut(window,w,h):
    #Pencere boyutunu ayarlama
    app_width = w
    app_height = h

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        
def calistir():
    def ekle():
        #mail ekle butonu fonksiyonu
        isim = entbx.get("1.0",'end-1c').strip()
        entbx.delete("0.0",END)
        mail = entbx_1.get("1.0",'end-1c').strip()
        entbx_1.delete("0.0",END)
        sinif = entbx_2.get("1.0",'end-1c').strip()
        entbx_2.delete("0.0",END)
        
        veri = [mail,isim,sinif]

        vt.vt_mail(veri)
        yenilee()

    def sil():
        #mail sil butonu fonksiyonu
        mail = entbx_1.get("1.0",'end-1c').strip()
        entbx_1.delete("0.0",END)
        entbx.delete("0.0",END)
        entbx_2.delete("0.0",END)
        vt.vt_mail_silme(mail)
        yenilee()
    
    def yenile():
        #yenile butonu fonksiyonu
        im = vt.vt_veri_cekme()
        box1.configure(state = "normal")
        box1.delete("0.0",END)
        
        for i in im:
            box1.insert(END, str(i))
            box1.insert(END, "\n")
        box1.configure(state = "disabled")

    def yenilee():
        #mail eklendiğinde veya silindiğinde yenileme
        im = vt.vt_veri_cekme()
        box1.configure(state = "normal")
        box1.delete("0.0",END)
        
        for i in im:
            box1.insert(END, str(i))
            box1.insert(END, "\n")
        box1.configure(state = "disabled")
        
    def duyuru_yenile():
        #Duyuru yenile butonu fonksiyonu
        duyuru = dy.basliklar()
        box2.configure(state = "normal")
        box2.delete("0.0",END)
        flag=1
        for i in duyuru:
            if(flag==2):
                box2.insert(END, str(i))
                box2.insert(END,"\n\n")
            if(flag==4):flag=0
            flag +=1
        box2.configure(state = "disabled")

    
    window = Tk()
    window.title("Mail Kayıt")
    boyut(window,821,540)
    window.resizable(0,0)

    arka_plan = label(window,"",0,0,821,600,0,"#cccccc")

    mail_listesi = label(window,"Mail Listesi",0,0,400,50,20,"#56ffff")
    duyurular = label(window,"Duyurular",420,0,400,50,20,"#56ffff")
    isim = label(window,"İsim",50,415,50,20,10,"#56ffff")
    mail = label(window,"Mail Ekleme ve Silme Alanı",310,415,200,20,10,"#56ffff")
    sinif = label(window,"Sınıf",570,415,50,20,10,"#56ffff")


    box1 = text_box(window,0,50,34,15)
    box2 = text_box(window,420,50,34,15)

    entbx = girdi(window,50,435,200,48)
    entbx_1 = girdi(window,310,435,200,48)
    entbx_2 = girdi(window,570,435,200,48)

    ekle = buton(window,"Ekle",215,500,8,25,ekle)
    sil = buton(window,"Sil",510,500,8,25,sil)
    yenile = buton(window,"Yenile",0,370,34,25,yenile)
    yenile2 = buton(window,"Yenile",420,370,34,25,duyuru_yenile)

    scrollbar = scroll_bar(window,377,50,24,320,box1)
    scrollbar2 = scroll_bar(window,798,50,24,320,box2)

    box1['yscrollcommand'] = scrollbar.set
    box2['yscrollcommand'] = scrollbar2.set

    window.mainloop()
