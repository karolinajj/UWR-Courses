#include <stdexcept>
#include <iostream>
#include "tabbit.hpp"

using namespace std;


int main()
{
    cout << "Konstruktor: \n";
    tab_bit t1(4); //konstruktor
    cout << "t1: " << t1 << endl;
    tab_bit t2(100); //konstruktor
    cout << "t2: " << t2 << endl;
    cout << "Po zmianie bitu w t1 mamy:\n";
    t1[0] = 1;
    cout << "t1: " << t1 << endl;

    t1[3] = 1;
    tab_bit t5(4);
    t5[3] = 1;
    cout << "t1: " << t1 << " t5: " << t5<< endl;
    tab_bit w1 = t1|t5;
    tab_bit w2 = t1&t5;
    tab_bit w3 = t1^t5;
    tab_bit w4 = !t1;
    cout << "t1|t5 = " << w1 << endl;
    cout << "t1&t5 = " << w2 << endl;
    cout << "t1^t5 = " << w3 << endl;
    cout << "!t1 = " << w4 << endl;

    cout << "Przypisanie kopiujace:\n";
    tab_bit t7(4);
    tab_bit t6(4);
    t7[1] = 1;
    t6 = t7;
    cout << t6 << endl;

    cout << "Przypisanie przenoszace:\n";
    tab_bit t8(4);
    tab_bit t9(4);
    t9[2] = 1;
    t8 = move(t9);
    cout << t8 << endl;

    cout << "Konstruktor kopiujacy:\n";
    tab_bit t11(4);
    tab_bit t10(t11);
    cout << t10 << endl;

    cout << "Konstruktor ze wzorcem:\n";
    tab_bit t12({1, 0, 1, 1, 0, 0, 0, 1});
    cout << t12 << endl;

    cout << "Konstruktor przenoszacy:\n";
    tab_bit t13(4);
    t13[3] = 1;
    tab_bit t14(move(t13));
    cout << t14 << endl;

    tab_bit t(46); // tablica 46-bitowa (zainicjalizowana zerami)
    tab_bit u(45ull); // tablica 64-bitowa (sizeof(uint64_t)*8)
    tab_bit v(t); // tablica 46-bitowa (skopiowana z t)
    tab_bit w({1, 0, 1, 1, 0, 0, 0, 1}); // tablica 8-bitowa (przeniesiona)
    v[0] = 1; // ustawienie bitu 0-go bitu na 1
    t[45] = true; // ustawienie bitu 45-go bitu na 1
    bool b = v[1]; // odczytanie bitu 1-go
    u[45] = u[46] = u[63]; // przepisanie bitu 63-go do bitow 45-go i 46-go
    cout<<t<<endl; // wysietlenie zawartości tablicy bitów na ekranie

}
