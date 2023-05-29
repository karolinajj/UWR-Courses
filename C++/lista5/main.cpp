#include <iostream>
#include <cmath>
#include "klasy.hpp"
#include "piksel.hpp"

using namespace std;

int main()
{
    kolor a = kolor(); //konstruktor bezparametrowy
    cout << a << endl;

    kolor b = kolor(100,70,20); //konstruktor z argumentami

    //get i set:
    cout << "\nGettery (dla koloru b):\n";
    cout << b.get_R() << " " << b.get_G() << " " << b.get_B() << endl;
    cout << "Settery (dla koloru a):\n";
    a.set_R(10);
    a.set_G(20);
    a.set_B(30);
    cout << a << endl;
    
    //przyciemnianie, rozjasnianie
    cout << "\nb.przyciemnij(0.2):\n";
    b.przyciemnij(0.2);
    cout << b << endl;
    cout << "b.rozjasnij(0.4):\n";
    b.rozjasnij(0.2);
    cout << b << endl;

    //laczenie kolorow
    cout << "\nLaczenie kolorow a i b:\n";
    kolor c = kolor::polacz(a,b);
    cout << c << endl;

    cout << "\nKolor transparentny:\n";
    kolortransparentny t1 = kolortransparentny(); //konstruktor bezparametrowy
    kolortransparentny t2 = kolortransparentny(10,20,30,100); //konstruktor z parametrami
    cout << "t1: " << t1 << ", alfa = " << t1.get_alfa() << endl;
    cout << "t2: " << t2 << ", alfa = " << t2.get_alfa() << endl;

    cout << "\nKolor nazwany:\n";
    kolornazwany n1 = kolornazwany(); //konstruktor bezparametrowy
    kolornazwany n2 = kolornazwany(13,12,53, "aaa"); //konstruktor z parametrami
    cout << "n1: " << n1 << ", nazwa = " << n1.get_nazwa() << endl;
    n1.set_nazwa("a");
    cout << "Kolor n1 po zmianie nazwy: " << a << endl;
    cout << "n2: " << n2 << ", nazwa = " << n2.get_nazwa() << endl;

    cout << "\nKolornt:\n";
    kolornt nt1 = kolornt(); //konstruktor bezparametrowy
    kolornt nt2 = kolornt(1,2,3,4,"a"); //konstruktor z parametrami
    cout << "nt1: " << nt1 <<  ", alfa = " << nt1.get_alfa() << ", nazwa = " << nt1.get_nazwa() << endl;
    cout << "nt2: " << nt2 <<  ", alfa = " << nt2.get_alfa() << ", nazwa = " << nt2.get_nazwa() << endl;

    cout << "\nPiksel:\n";
    piksel p = piksel(100,200); //konstruktor z parametrami
    cout<< p.gora()<<endl;
    cout<< p.prawa()<<endl;
    cout<< p.dol()<<endl;
    cout<< p.lewa()<<endl;


    pikselkolorowy pk1 = pikselkolorowy(200,400,t2);
    cout << "pk1 = " << pk1 << endl;
    cout << "pk1.przesun(10,20):\n";
    pk1.przesun(10,20);
    cout << pk1 << endl;
    cout << "pk1.kolor = "<< pk1.kolor <<endl;
    cout << "pk1.kolor.get_alfa() = "<< pk1.kolor.get_alfa() <<endl;

    cout << "\nOdlegosc pikseli:\n";
    cout << "pk1 od p: " << odleglosc(pk1,p) << endl;
    cout << "pk1 od p: " << odleglosc(&pk1,&p) << endl;
    return 0;
}
