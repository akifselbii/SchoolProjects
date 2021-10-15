#Mehmet Akif SELBİ

sentences_list =[]
input_list =[]
histogram_list=[]

def read_file():
    for i in range(1,11):
        s_file = open("data_files/"+str(i)+".txt")
        s_file = s_file.readlines()
        for j in s_file:
            if(j!="\n"):
                j=j.replace("\n","")
                sentences_list.append(j)

def read_input_file():
    i_file = open("input.txt")
    i_file = i_file.readlines()
    for i in i_file:
        if(i!="\n"):
            i=i.replace("\n","")
            input_list.append(i)

def write_output_file(i):
    o_file.write(i)
    o_file.write("\n")

def my_h(list_1):
    dict_1=dict()
    for i in list_1:
        if i in dict_1:
            dict_1[i]+=1
        else:
            dict_1[i]=1
    return dict_1

def max_value(dict_1):
    max ,key= 0,""
    for i in dict_1:
        if dict_1[i]>max:
            key = i
            max = dict_1[i]
    return key

def split_mtd(i,j):
    list_1 = j.split(i)
    for k in range(1,len(list_1)):
        list_2=list_1[k].split()
        if(len(list_2)>0):
            list_2[0] = list_2[0].replace(",","")
            histogram_list.append(list_2[0])

def process_1():
    for i in input_list:
        if(check_input(i)):
            process_2(i)
            write_output_file(i+"+"+str(max_value(my_h(histogram_list))))
        else:
            write_output_file(i+" ==> "+"5 kelimeden fazla")

def process_2(i):
    histogram_list.clear()
    i=i.lower()
    for j in sentences_list:
        j=j.lower()
        if i in j:
            split_mtd(i,j)

def check_input(i):
    if(len(i.split())<=5):
        return 1
    return 0

o_file = open("output.txt", "w")
read_file()
read_input_file()
process_1()
o_file.close()
