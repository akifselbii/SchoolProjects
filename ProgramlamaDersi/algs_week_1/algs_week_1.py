
import random

def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers

def my_frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1
    return frequency_dict

my_list = get_n_random_numbers(10,-8,8)
sorted(my_list)
my_f=my_frequency_with_dict(my_list)
print(my_list)
print(my_f)


def my_frequency_with_list_of_tuples(list_1):
    frequency_list = []
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list

result_1 = my_frequency_with_dict(my_list)
result_2 = my_frequency_with_list_of_tuples(my_list)
print(result_1,result_2)





# mode of a list with histogram

def my_mode_with_dict(my_hist_d):
    frequency_max = -1
    mode = -1
    for key in my_hist_d.keys():
        print(key,my_hist_d[key])
        if(my_hist_d[key]>frequency_max):
            frequency_max = my_hist_d[key]
            mode=key
    return mode,frequency_max

my_list_1 = get_n_random_numbers(10)
my_hist_d = my_frequency_with_dict(my_list_1)
my_hist_l=my_frequency_with_list_of_tuples(my_list_1)

print(my_mode_with_dict(my_hist_d))





# mode of a list with histogram (a list of tuples)

def my_mode_with_list(my_hist_list):
    frequency_max = -1
    mode = -1
    for item,frequency in my_hist_list:
        print(item,frequency)
        if(frequency>frequency_max):
            frequency_max = frequency
            mode=item
    return mode,frequency_max

my_list_100 = get_n_random_numbers(20,-4,4)
my_hist_l=my_frequency_with_list_of_tuples(my_hist_l)
print(my_mode_with_list(my_hist_l))




#linear search on list

def my_linear_searh(my_list,item_search):
    found=(-1,-1)
    n=len(my_list)
    for indis in range(n):
        if my_list[indis] == item_search:
            found=(my_list[indis],indis)
    return found

my_list = get_n_random_numbers(10,-5,5)
print(my_linear_searh(my_list,10))


#mean of list

def my_mean():
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean_ = t/s
    return mean_

my_list = get_n_random_numbers(4,-5,5)
print(my_mean(my_list))




#sort the list

def my_bubble_sort(my_list):
    n=len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list

my_list = get_n_random_numbers(4,-5,5)
print(my_bubble_sort(my_list))




#binary search on a sorted list

def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)-1

    while(low <= high):
        mid =(low+hig)

        if(my_list[mid]==item_search):
            return my_list[mid],mid
        elif(my_list[mid]>item_search):
            high = mid-1
        else:
            low=mid+1
    return found



#median of a list

size=input("dizi boyutunu giriniz")
size=int(size)
my_list_1=get_n_random_numbers(size)

print("liste ",my_list_1)

def my_median(my_list):
    my_list_2 = my_bubble_sort(my_hist_l)
    #print(my_list_2)
    n=len(my_list_2)
    if(n%2==1):
        middle=int(n/2)+1
        median = my_list_2[middle-1]
        #print(median)

    else:
        middle_1= int(n/2)
        middle_2= middle_1+1
        median= (my_list_2[middle_1]+my_list_2[middle_2])/2
        #print(median)
    return median

my_list_2 = get_n_random_numbers(5,-10,10)
print(my_median(my_list_2))





