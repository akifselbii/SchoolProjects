#Mehmet Akif SELBİ

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from sqlalchemy.orm import relationship

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db.db"))

app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




student_lecture = db.Table('StudentLecture',
        db.Column('student_no', db.Integer, db.ForeignKey('students.id')),
        db.Column('lecture_no', db.Integer, db.ForeignKey('lecture.id'))
)
        
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Integer)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
      
    lectures = db.relationship('Lecture', secondary=student_lecture, lazy='dynamic', backref=db.backref('students', lazy='dynamic'))

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Integer)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    
    lecture = db.relationship('Lecture',back_populates='teachers',uselist=False)


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    no = db.Column(db.Integer)
    akts = db.Column(db.Integer)
    kredi = db.Column(db.Integer)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    
    teachers = db.relationship('Teachers',back_populates='lecture',uselist=False)
    
    book = db.relationship('Book',back_populates='lecture',uselist=False)
    #book = db.relationship('Book', backref='lecturename', lazy='dynamic')              

class Book(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    no = db.Column(db.Integer)
    name = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200))
    sayfa = db.Column(db.Integer)
    lecture = db.relationship('Lecture',back_populates='book',uselist=False)
    #lecture = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    
db.create_all()
