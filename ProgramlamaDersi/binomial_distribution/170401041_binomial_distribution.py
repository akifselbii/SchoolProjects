#170401041 Mehmet Akif SELBİ
from sympy import Symbol, pprint,factorial,plot
import matplotlib.pyplot


p=Symbol('p')#istenilen durumu başarma olasılığı
x=Symbol('x')#istenilen durum sayısı
n=Symbol('n')#deneme sayısı

#binomial distribution
#Değişkenin sadece iki değer alacağı durumlarda kullanılır, gerçekleşecek durumun olasılığını hesaplar


#b(x) = nCx * (P**x) * (1-P)**(n-x)

nCx = factorial(n)/(factorial(x)*factorial(n-x))
Px = p**x
Nx = (1-p)**(n-x)

bx = nCx*Px*Nx
pprint(bx)

#sympy
plot(bx.subs({p:0.5,n:30}),(x,0,30))




x_1=[]
y_1=[]
for i in range(1,30):
    z = bx.subs({p:0.5,n:30,x:i})
    x_1.append(i)
    y_1.append(z)

#matplotlib.pyplot
matplotlib.pyplot.plot(x_1,y_1)
matplotlib.pyplot.show()