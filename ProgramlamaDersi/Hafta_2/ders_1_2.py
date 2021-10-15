#Mehmet Akif SELBİ
#Liste içindeki verilerin alt dizilerinde toplamı maksimum olan değer kaçtır?
def my_f_2(list_1 = [4,-3,5,-2,-1,2,6,-2]):
    maxSum = 0
    n = len(list_1)
    for i in range(n):
        t = 0
        for j in range(i,n):
            t+=list_1[j]
            if t>maxSum:
                maxSum = t
    return(maxSum)

print(my_f_2())
