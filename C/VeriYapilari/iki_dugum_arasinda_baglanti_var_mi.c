//Eğer iki düğüm birbirine baglantılı yolda ise bağlı olduğu düğüm sayısını eğer bağlı değil ise -1 döndürür

//Mehmet Akif SELBİ

#include <stdio.h>
#include <stdlib.h>

struct dugum {
    int icerik;
    struct dugum *sol;
    struct dugum *sag;
};

struct ikili_arama_agaci{
    struct dugum *kok;
};

int baglimi(struct dugum *root ,int a ,int b){
        static int bulun_ma = 0, kontrol = 1;
	if(root == NULL)
		return -1*kontrol;
        if(bulun_ma == 0){
                if((a<root->icerik && b>root->icerik) || (a>root->icerik && b<root->icerik))
                        return -1;
        }
        if(root->icerik == b){
                if(bulun_ma == 1) return 0;
                else
                        bulun_ma += 1;
        }
	if(root->icerik == a){
                if(bulun_ma == 1) return 0;
                else{
                        a=b;
                        bulun_ma += 1;
                }
        }
        if(a<root->icerik){
                if(bulun_ma == 1) {
			kontrol += 1;
			return 1+baglimi(root->sol,a,b);
		}
		else
                        return 0+baglimi(root->sol,a,b);
        }
        else{

                if(bulun_ma == 1){ 
			kontrol +=1;
			return 1+baglimi(root->sag,a,b);
		}
		else
                        return 0+baglimi(root->sag,a,b);
        }
}

int main(){
	return 0;
}
