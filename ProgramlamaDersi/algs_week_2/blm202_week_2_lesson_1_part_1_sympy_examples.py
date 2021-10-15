
from sympy import Symbol,factor,expand,pprint

x = Symbol("x")
y = Symbol("y")

p=x*(x+x)
print(p)

p = (x+2)*(x+3)
print(p)

expr = x**2 - y**2
factors = factor(expr)#ifadeyi çarpanlarına ayırır
print(factors)

expand = expand(factors)
print(expand)

expr = x**3+3*x**2*y+3*x*y**2+y**3

factors = factor(expr)
pprint(factors)#ifadeyi matematiksel yazar

x = Symbol('x')
series = x
n=5
for i in range(2,n+1):
    series = series + (x**i)/i
    pprint(series)
    
expr = x*x + x*y +x*y + y*y
res = expr.subs({x:1,y:2})#fonksiyonel ifadeye verilen değerleri yazar
pprint(res)

r=expr.subs({x:1-y})#x i yok etme işlemi
pprint(r)


x = Symbol('x')
series = x
n=5
x_value = 10
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)
series_value = series.subs({x:x_value})


