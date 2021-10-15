#Mehmet Akif SELBİ

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from db import *

def kontrol(veri,psw):
    for student in Students.query.all():
        if(str(veri) == str(student.no)):
            if(str(psw) == str(student.password)):
                return 1
    return 0

def kontrolT(veri,psw):
    for teachers in Teachers.query.all():
        if(str(veri) == str(teachers.no)):
            if(str(psw) == str(teachers.password)):
                return 1
    return 0
    
@app.route('/', methods = ['GET', 'POST'])
def login():
    login = request.form.get('name')
    password = request.form.get('password')
    
    if login == 'admin' and password == 'admin':
        return redirect(url_for('admin'))
    elif(kontrol(login,password)):
        return redirect(url_for('ogrenci_giris'))
    elif(kontrolT(login,password)):
        return redirect(url_for('ogretmen_giris'))
    return render_template('index.html')
    
@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    return render_template('admin.html')

@app.route('/ogrenci_kayit', methods = ['GET', 'POST'])
def ogrenci_kayit():
    if request.method == 'POST':
        no = request.form.get('no')
        fname = request.form.get('fname')
        lname =request.form.get('lname')
        grade =request.form.get('grade')
        password =request.form.get('password')
    
        data = Students(no=no,fname=fname, lname=lname, grade=grade, password=password)
        
        for lecture in Lecture.query.all():
            if request.form.getlist(lecture.name):
                data.lectures.append(lecture)
                
        db.session.add(data)
        db.session.commit()
        #return redirect(url_for('ogrenci_kayit'))
    return render_template('ogrenci_kayit.html',Lecture = Lecture.query.all(),Students = Students.query.all())

@app.route('/ogretmen_kayit', methods = ['GET', 'POST'])
def ogretmen_kayit():
    if request.method == 'POST':
        no = request.form.get('no')
        fname = request.form.get('fname')
        lname =request.form.get('lname')
        password =request.form.get('password')
        
        data = Teachers(no=no ,fname=fname, lname=lname, password=password) 
        
        for lecture in Lecture.query.all():
            if request.form.getlist(lecture.name):
                data.lecture = lecture
                
        db.session.add(data)
        db.session.commit()
        #return redirect(url_for('ogrenci_kayit'))
    return render_template('ogretmen_kayit.html',Lecture = Lecture.query.all(),Teachers = Teachers.query.all())

@app.route('/ders_kayit', methods = ['GET', 'POST'])
def ders_kayit():
    if request.method == 'POST':
        name = request.form.get('name')
        no = request.form.get('no')
        akts = request.form.get('akts')
        kredi = request.form.get('kredi')
        
        data = Lecture(name=name,no=no,akts=akts,kredi=kredi) 
        for book in Book.query.all():
            if request.form.getlist(book.name):
                data.book = book
        db.session.add(data)
        db.session.commit()
        #return redirect(url_for('ogrenci_kayit'))
    return render_template('ders_kayit.html',Book = Book.query.all(),Lecture = Lecture.query.all())

@app.route('/kitap_kayit', methods = ['GET', 'POST'])
def kitap_kayit():
    if request.method == 'POST':
        no = request.form.get('no')
        name = request.form.get('name')
        author =request.form.get('author')
        sayfa =request.form.get('sayfa')
    
        data = Book(no=no ,name=name, author=author, sayfa=sayfa) 
        db.session.add(data)
        db.session.commit()
        #return redirect(url_for('ogrenci_kayit'))
    return render_template('kitap_kayit.html',Book = Book.query.all())

@app.route('/delete/<cls>/<id>/', methods=['GET','POST'])
def delete(id, cls):
    if cls == 'Students':
        data = Students.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return(redirect(url_for('ogrenci_kayit')))
    elif cls == 'Teachers':
        data = Teachers.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return(redirect(url_for('ogretmen_kayit')))
    elif cls == 'Lecture':
        data = Lecture.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return(redirect(url_for('ders_kayit')))
    else:
        data = Book.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return(redirect(url_for('kitap_kayit')))


def delete_2(id,cls):
    if cls == 'Students':
        data = Students.query.get(id)
        db.session.delete(data)
        db.session.commit()
    elif cls == 'Teachers':
        data = Teachers.query.get(id)
        db.session.delete(data)
        db.session.commit()
    elif cls == 'Lecture':
        data = Lecture.query.get(id)
        db.session.delete(data)
        db.session.commit()
    else:
        data = Book.query.get(id)
        db.session.delete(data)
        db.session.commit()
        
@app.route('/edit/<cls>/<id>/', methods=['GET','POST'])
def edit(id, cls):
    if cls == 'Students':
        if request.method == 'POST':
            no = request.form.get('no')
            fname = request.form.get('fname')
            lname =request.form.get('lname')
            grade =request.form.get('grade')
            password =request.form.get('password')
        
            data = Students(no=no,fname=fname, lname=lname, grade=grade, password=password)
            
            for lecture in Lecture.query.all():
                if request.form.getlist(lecture.name):
                    data.lectures.append(lecture)
                    
            if(Students.query.get(id)):
                delete_2(id, cls)
            
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('ogrenci_kayit'))
        return render_template('edit.html',student=Students.query.get(id),Lecture = Lecture.query.all())
    if cls == 'Teachers':
        if request.method == 'POST':
            no = request.form.get('no')
            fname = request.form.get('fname')
            lname =request.form.get('lname')
            password =request.form.get('password')
            
            data = Teachers(no=no ,fname=fname, lname=lname, password=password)
            
            for lecture in Lecture.query.all():
                if request.form.getlist(lecture.name):
                    data.lecture = lecture
                    
            if(Teachers.query.get(id)):
                delete_2(id, cls)
            
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('ogretmen_kayit'))
        return render_template('edit2.html',teacher=Teachers.query.get(id),Lecture = Lecture.query.all())
    if cls == 'Lecture':
        if request.method == 'POST':
            name = request.form.get('name')
            no = request.form.get('no')
            akts = request.form.get('akts')
            kredi = request.form.get('kredi')
            
            data = Lecture(name=name,no=no,akts=akts,kredi=kredi) 
            
            for book in Book.query.all():
                if request.form.getlist(book.name):
                    data.book = book
                    
            if(Lecture.query.get(id)):
                delete_2(id, cls)
            
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('ders_kayit'))
        return render_template('edit3.html',lecture=Lecture.query.get(id),Book = Book.query.all())
    if cls == 'Book':
        if request.method == 'POST':
            no = request.form.get('no')
            name = request.form.get('name')
            author =request.form.get('author')
            sayfa =request.form.get('sayfa')
        
            data = Book(no=no ,name=name, author=author, sayfa=sayfa) 
                    
            if(Book.query.get(id)):
                delete_2(id, cls)
            
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('kitap_kayit'))
        return render_template('edit4.html',book=Book.query.get(id))













@app.route('/ogrenci_giris', methods = ['GET', 'POST'])
def ogrenci_giris():
    return render_template('ogrenci_giris.html',Lecture = Lecture.query.all())

@app.route('/ogretmen_giris', methods = ['GET', 'POST'])
def ogretmen_giris():
    return render_template('ogretmen_giris.html',Lecture = Lecture.query.all())


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)    