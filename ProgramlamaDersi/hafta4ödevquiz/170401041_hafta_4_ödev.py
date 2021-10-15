#Mehmet Akif SELBİ 170401041


"""
Parametre olarak bir array ve bir index alır. Aldigi indexteki degeri
sag ve sol cocugu ile karsilastirir kendisinden kucuk bir deger varsa onunla yer degistirir
"""
def min_heapify(array,i):
    left=2*i+1
    right=2*i+2
    length = len(array)-1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if(smallest) !=i
        array[i],array[smallest] = array[smallest],array[i]
        min_heapify(array,smallest)


"""
Parametre olarak bir array alır .Arraydeki tüm elemanlari sirayla fonksiyona gönderir ve arrayi
min heap sekline donusturur.
"""
def build_min_heap(array):
    for i in reversed(range(len(array))//2):
        min_heapify(array,i)


"""
Parametre olarak bir array alir. ilk elemanla son elemani yer değiştirir ve sonra son elemani siler. min_heapify
fonksiyonuna göndererek arrayi tekrardan min heap yapar
"""
def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0],array[-1] = array[-1],array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array





def insertItemToHeap(myheap_1,item):
    if(myheap_1.count(item)!=0):
        myheap_1.append(item)
        build_min_heap(myheap_1)

def removeItemFrom(myheap_1):
    if(len(myheap_1)>= 1):
        myheap_1[0],myheap_1[-1]=myheap_1[-1],myheap_1[0]
        myheap_1.pop()
        build_min_heap(myheap_1)