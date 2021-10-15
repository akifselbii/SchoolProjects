#Mehmet Akif SELBİ
#Liste içindeki verilerin alt dizilerinde toplamı maks olan değer kaçtır?
def my_f_1(list_1 = [4,-3,5,-2,-1,2,6,-2]):
    maxSum = 0
    n = len(list_1)
    for i in range(n):
        for j in range(i,n):
            t = 0
            for k in range(i,j):
                t+=list_1[k]
            if t>maxSum:
                maxSum = t
    return maxSum
