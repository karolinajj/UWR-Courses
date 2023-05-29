#include <stdexcept>
#include <iostream>
#include "liczba.hpp"

using namespace std;


int main()
{
    cout << "Bedziemy nadawali zmiennej kolejne wartosci: 1.0, 2.0, 3.0" << endl;
    Liczba n = Liczba(1.0);
    n.set(2.0);
    n.set(3.0);
    cout << "Sprawdzmy jaka byla historia wartosci zmiennej (od najpozniejszej do najwczesniejszej):" << endl;
    cout << n.wypisz(1) << endl;
    cout << n.wypisz(2) << endl;
    cout << n.wypisz(3) << endl;
    cout << "Zmienmy teraz wartosc zmiennej na 4.0 i ponownie wypiszmy historie (od najpozniejszej do najwczesniejszej):" << endl;
    n.set(4.0);
    cout << n.wypisz(1) << endl;
    cout << n.wypisz(2) << endl;
    cout << n.wypisz(3) << endl;
    cout << "Przywrocmy teraz wartosc zmiennej na ostatnia:" << endl;
    n.przywroc(2);
    cout << "(zmienna ma teraz wartosc " << n.get()  << ")"<< endl;
    cout << "Ponownie wypiszmy historie:" << endl;
    cout << n.wypisz(1) << endl;
    cout << n.wypisz(2) << endl;
    cout << n.wypisz(3) << endl;

    cout << "Dodatkowe testy konstruktorow\n";
    //dodatkowe testy konstruktorow
    Liczba m1 = n;
    cout << m1 << endl;
    Liczba m2(3.0);
    Liczba m3(move(m2));
    cout << m3 << endl;
    cout << m3.wypisz(2);
}
