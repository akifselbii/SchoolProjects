#Mehmet Akif SELBİ

import sys

def kontrol():
    if (len(sys.argv) != 3):
        print('Girdi "python numaranız_hw_2.py input_dir_name output_dir_name" şeklinde olmalıdır')
        return 0
    else:
        if not("input_hw_2" in sys.argv[1]):
            sys.argv[1] += "input_hw_2.csv"
        if not("170401041_hw_2_output" in sys.argv[2]):
            sys.argv[2] += "170401041_hw_2_output.txt"
        return 1

def dosya_oku():
    list_=[]
    dosya = open(sys.argv[1])
    dosya = dosya.readlines()
    for i in dosya:
        j = i.split("-")
        list_.append(j[3])
    return list_

def dosya_yaz(ort,median):
    dosya = open(sys.argv[2],"w")
    dosya.write("Medyan "+str(median))
    dosya.write("\nOrtalama "+str(ort))
    dosya.close()

def bubble_sort(my_list):
    n=len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list

def histogram(list_):
    dict_={}
    for i in list_:
        if i in dict_:
            dict_[i]+=1
        else:
            dict_[i]=1
    for i in dict_:
        print(i," ",dict_[i])
    return dict_

def ortalama(dict_):
    toplam = 0
    for i in dict_:
        toplam += dict_[i]
    return toplam/float(len(dict_))

def medyan(dict_):
    liste =[]
    for i in dict_:
        liste.append(dict_[i])

    liste = bubble_sort(liste)
    if(len(liste)%2==1):
        middle = int(len(liste)/2)+1
        median = liste[middle-1]
    else:
        middle_1 = int(len(liste)/2)
        middle_2 = middle_1+1
        median = (liste[middle_1]+liste[middle_2])/2
    return median

if(kontrol()):
    dict_ = histogram(dosya_oku())
    dosya_yaz(ortalama(dict_),medyan(dict_))


