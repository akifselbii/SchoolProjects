//İkili arama agacında kokten yapraga en kısa yol uzunlugu

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
}

int en_kisa_yol(struct dugum *root){
	if(root == NULL)
		return 0;
	if( en_kisa_yol(root->sol) < en_kisa_yol(root->sag) )
		return 1+en_kisa_yol(root->sol);
	else
		return 1+en_kisa_yol(root->sag);
}

int main(){
	return 0;
}
