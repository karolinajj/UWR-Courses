#include "tabbit.hpp"

#include <bits/stdc++.h>

const int tab_bit::rozmiarSlowa = sizeof(uint64_t)*8;

//-----------------------------------------------------------------------------------

tab_bit::tab_bit(int rozm) //konstruktor
{
    if (rozm <= 0)
        throw invalid_argument("Nie mozna utworzyc tablicy o podanym rozmiarze");

    dl = rozm;
    int ile_slow = ceil ((double) rozm / rozmiarSlowa);
    
    tab = new slowo[ile_slow]; //tablica o rozm ile_slow

    for (int i = 0; i < ile_slow; i++)
    {
        tab[i] = 0;
    }
}

tab_bit::tab_bit(std::initializer_list<bool> list)
{
    dl = list.size();
    int ile_slow = ceil((double) dl / rozmiarSlowa);
    tab = new slowo[ile_slow];
    int i = 0;

    for(auto it = list.begin(); it != list.end(); it++)
    {
        pisz(i, *it);
        i++;
    }
}

tab_bit::tab_bit(const tab_bit& tb) //konstruktor kopiujący
{
    int ile_slow = ceil ((double) tb.dl / rozmiarSlowa);
    this->dl = tb.dl;
    this->tab = new slowo[ile_slow];
    for (int i = 0; i < ile_slow; i++)
    {
        this->tab[i] = tb.tab[i];
    }
}

tab_bit::tab_bit(tab_bit&& tb) // konstruktor przenoszący
{
    if(tb.tab == nullptr) throw "Nie mozna przeniec";
    this->dl = tb.dl;
    this->tab = tb.tab;
    tb.dl = 0;
    tb.tab = nullptr;
}

tab_bit& tab_bit::operator=(const tab_bit& tb)
{
    if (this == &tb) 
        return *this;

    delete[] tab;
    dl = tb.dl;
    int ile_slow = ceil ((double) tb.dl / rozmiarSlowa);
    tab = new slowo[ile_slow];

    for (int i = 0; i < ile_slow; i++)
    {
        tab[i] = tb.tab[i];
    }
    return *this;
}


tab_bit& tab_bit::operator=(tab_bit&& tb)
{
    if (this == &tb) return *this; 
    delete[] tab;

    dl = tb.dl;
    tab = tb.tab;
    tb.tab = nullptr;
    tb.dl = 0;
    
    return *this;
}


tab_bit::~tab_bit()
{
    if(tab != nullptr)
        delete[] tab;
}


istream & operator >> (istream &we, tab_bit &tb)
{
    string wejscie;
    we >> wejscie;

    delete[] tb.tab;

    tb.dl = wejscie.size();
    int ilosc_slow = ceil((double)wejscie.size() / tab_bit::rozmiarSlowa);
    tb.tab = new tab_bit::slowo[ilosc_slow];

    int i = 0;
    bool wartosc;
    for (auto& bit : wejscie)
    {
        if (bit != '0' and bit != '1')
        {
            throw std::invalid_argument("Podano niepoprawny napis, podaj napis zawierający jedynie cyfry 0 i 1");
        }

        wartosc = (bool)(bit - '0');
        tb[i++] = wartosc;
    }

    return we;
}

ostream & operator << (ostream &wy, const tab_bit &tb)
{
    for (int i = 0; i < tb.dl; i++)
        wy << tb[i];

    return wy;
}

inline int tab_bit::rozmiar() const 
{
    return this->dl;
}


//-----------------------------------------------------------------------------------


bool tab_bit::czytaj(int i) const
{
    return (tab[i / rozmiarSlowa] & (1ull << (i % rozmiarSlowa))) != 0; //sprawdza czy na i-tej pozycji jest 1 czy 0, tworząc maskę bitową
}

bool tab_bit::pisz(int i, bool b) //zwracam true jeśli uda się ustawić, false wpp
{
    int slowo_nr = i / rozmiarSlowa; // obliczenie numeru slowa
    int indeks = i % rozmiarSlowa; // indeks bitu w slowie

    if(i > dl) return false;

    if (b)
        tab[slowo_nr] |= (1ull << indeks);
    else 
        tab[slowo_nr] &= ~(1ull << indeks);

    return true;
}

//-----------------------------------------------------------------------------------

tab_bit::ref tab_bit::operator[] (int i)
{
    return tab_bit::ref(*this, i / this->rozmiarSlowa, i % this->rozmiarSlowa );
}

bool tab_bit::operator[] (int i) const
{
    return this->czytaj(i);
}

auto operator|(tab_bit& tb1, const tab_bit& tb2) -> tab_bit
{
    if (tb1.rozmiar() != tb2.rozmiar()) 
    {
        throw invalid_argument("nie mozna wykonac operacji, rozmiary tab_bit są rozne");
    }

    tab_bit wynik(tb1);
    
    for (int i = 0; i < tb1.rozmiar(); i++) 
    {
        wynik[i] = wynik[i] | tb2[i];
    }
    return wynik;
}

auto operator|=(tab_bit& tb1, const tab_bit& tb2) -> tab_bit&
{
    if (tb1.rozmiar() != tb2.rozmiar()) 
    {
        throw invalid_argument("nie mozna wykonac operacji, rozmiary tab_bit są rozne");
    }
    
    for (int i = 0; i < tb1.rozmiar(); i++) 
    {
        tb1[i] = tb1[i] | tb2[i];
    }
    return tb1;
}

auto operator&(tab_bit& tb1, const tab_bit& tb2) -> tab_bit
{
    if (tb1.rozmiar() != tb2.rozmiar()) 
    {
        throw invalid_argument("nie mozna wykonac operacji, rozmiary tab_bit są rozne");
    }

    tab_bit wynik(tb1);
    
    for (int i = 0; i < tb1.rozmiar(); i++) 
    {
        wynik[i] = wynik[i] & tb2[i];
    }
    return wynik;
}

auto operator&=(tab_bit& tb1, const tab_bit& tb2) -> tab_bit&
{
    if (tb1.rozmiar() != tb2.rozmiar()) 
    {
        throw invalid_argument("nie mozna wykonac operacji, rozmiary tab_bit są rozne");
    }
    
    for (int i = 0; i < tb1.rozmiar(); i++) 
    {
        tb1[i] = tb1[i] & tb2[i];
    }
    return tb1;
}

auto operator^(tab_bit& tb1, const tab_bit& tb2) -> tab_bit
{
    if (tb1.rozmiar() != tb2.rozmiar()) 
    {
        throw invalid_argument("nie mozna wykonac operacji, rozmiary tab_bit są rozne");
    }

    tab_bit wynik(tb1);
    
    for (int i = 0; i < tb1.rozmiar(); i++) 
    {
        wynik[i] = wynik[i] & tb2[i];
    }
    return wynik;
}

auto operator^=(tab_bit& tb1, const tab_bit& tb2) -> tab_bit&
{
    if (tb1.rozmiar() != tb2.rozmiar()) 
    {
        throw invalid_argument("nie mozna wykonac operacji, rozmiary tab_bit są rozne");
    }
    
    for (int i = 0; i < tb1.rozmiar(); i++) 
    {
        tb1[i] = tb1[i] & tb2[i];
    }
    return tb1;
}

auto operator!(tab_bit& tb1) -> tab_bit
{   
    for (int i = 0; i < tb1.rozmiar(); i++) 
    {
        tb1[i] = ~tb1[i];
    }
    return tb1;
}

