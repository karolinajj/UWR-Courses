#ifndef TABBIT_HPP
#define TABBIT_HPP

#include <iostream>
#include <stdint.h> //uint64
using namespace std;

class tab_bit
{
    typedef uint64_t slowo; // komorka w tablicy
    static const int rozmiarSlowa; // rozmiar slowa w bitach

    class ref; // klasa pomocnicza do adresowania bitów
    
    protected:
    int dl; // liczba bitów
    slowo *tab; // tablica bitów
    
    public:
    explicit tab_bit (int rozm); // wyzerowana tablica bitow [0...rozm]
    explicit tab_bit (std::initializer_list<bool> list); // tablica bitów [0...rozmiarSlowa]
    // zainicjalizowana wzorcem
    tab_bit (const tab_bit &tb); // konstruktor kopiujący
    tab_bit (tab_bit &&tb); // konstruktor przenoszący
    tab_bit & operator = (const tab_bit &tb); // przypisanie kopiujące
    tab_bit & operator = (tab_bit &&tb); // przypisanie przenoszące
    ~tab_bit (); // destruktor
    
    private:
    bool czytaj (int i) const; // metoda pomocnicza do odczytu bitu
    bool pisz (int i, bool b); // metoda pomocnicza do zapisu bitu

    public:
    bool operator[] (int i) const; // indeksowanie dla stałych tablic bitowych
    ref operator[] (int i); // indeksowanie dla zwykłych tablic bitowych
    inline int rozmiar () const; // rozmiar tablicy w bitach
    
    public:
    friend tab_bit operator|(tab_bit& tb1, const tab_bit& tb2);
    friend tab_bit& operator|=(tab_bit& tb1, const tab_bit& tb2);
    friend tab_bit operator&(tab_bit& tb1, const tab_bit& tb2);
    friend tab_bit& operator&=(tab_bit& tb1, const tab_bit& tb2);
    friend tab_bit operator^(tab_bit& tb1, const tab_bit& tb2);
    friend tab_bit& operator^=(tab_bit& tb1, const tab_bit& tb2);
    friend tab_bit operator!(tab_bit& tb1);
    
    public:
    friend istream & operator >> (istream &we, tab_bit &tb);
    friend ostream & operator << (ostream &wy, const tab_bit &tb);
};

class tab_bit::ref
{
    friend class tab_bit;
    tab_bit& tablica;
    int indeks_slowa, indeks_bitu;

    ref (tab_bit& t, int i_slowa, int i_bitu) : tablica(t), indeks_slowa(i_slowa), indeks_bitu(i_bitu) {}

    public:
    operator bool() const { return tablica.czytaj(indeks_slowa * tablica.rozmiarSlowa + indeks_bitu); }
    ref& operator= (bool b) { tablica.pisz(indeks_slowa * tablica.rozmiarSlowa + indeks_bitu, b); return *this; }
    ref& operator= (const ref& r) { return operator=(bool(r)); }
    bool operator~() const { return !operator bool(); }
};

#endif