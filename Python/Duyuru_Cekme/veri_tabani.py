#Mehmet Akif SELBİ

import sqlite3

def vt_mail(veriler):
    #mailleri kaydetmek için
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,sinif)""")

        try:
            im.execute("""INSERT INTO mailler VALUES (?,?,?)""",veriler)
        except:
            print("Kayıtlı Kullanıcı")
        
        vt.commit()

def vt_link(veriler):
    #linkeri kaydetmek için
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS linkler (link PRIMARY KEY)""")

        try:
            im.execute("""INSERT INTO linkler VALUES (?)""",veriler)
        except:
            print("")
        
        vt.commit()

def vt_link_cekme():
    #Veri tabanından link çekme
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS linkler (link PRIMARY KEY)""")
        im.execute("""SELECT link FROM linkler""")
        
        return im

def vt_link_silme(link):
    #Veri tabanından link silme
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS linkler (link PRIMARY KEY)""")
        try:
            im.execute("DELETE FROM linkler WHERE link = ?",(link,))
        except:
            print("")
        vt.commit()

def vt_veri_cekme():
    #Veri tabanındaki mail tablosundaki tüm mailleri çekme
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,sinif)""")
        im.execute("""SELECT * FROM mailler""")

        return im
    
def vt_mail_cekme():
    #Veri tabanından mail çekme
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,sinif)""")
        im.execute("""SELECT mail FROM mailler""")
        
        return im
    
def vt_mail_silme(mail):
    #Veri tabanından mail silme
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,sinif)""")
        try:
            im.execute("DELETE FROM mailler WHERE mail = ?",(mail,))
        except:
            print("Böyle bir mail yok")
        vt.commit()


