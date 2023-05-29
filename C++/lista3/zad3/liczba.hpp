#ifndef LICZBA_HPP
#define LICZBA_HPP

#include <stdexcept> //do wyjątków
#include <iostream>

using namespace std;

#define MAX_COUNT = 3

class Liczba
{
    private:
        double zmienna;
        int maks = 3;
        double* historia = nullptr;
        int ostatni;
        int rozmiar;
    public:
        Liczba();
        Liczba(double n);
        Liczba(const Liczba&);
        Liczba(Liczba&&);

        Liczba& operator=(const Liczba&);
        Liczba& operator=(Liczba&&);
        ~Liczba();

        void set(double n);
        double wypisz(int indeks);
        void przywroc(int indeks);
        double get();

        friend std::ostream& operator<<(std::ostream& out, const Liczba& A);
};
#endif