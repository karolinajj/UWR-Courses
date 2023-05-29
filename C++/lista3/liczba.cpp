#include"liczba.hpp"

Liczba::Liczba()
{
    Liczba(0.0);
}

Liczba::Liczba(const double n)
{
    zmienna = n;
    historia = new double[maks];
    ostatni = 0;
    rozmiar = 1;
    historia[0] = n;
    rozmiar = 1;
}

Liczba::Liczba(const Liczba& x)
{
    maks = x.maks;
    ostatni = 0;
    rozmiar = 1;
    historia = new double[maks];
    zmienna = x.zmienna;
    historia[0] = x.zmienna;
}

Liczba::Liczba(Liczba&& x)
{
    maks = x.maks;
    zmienna = x.zmienna;
    ostatni = x.ostatni;
    rozmiar = x.rozmiar;
    historia = x.historia;
    x.historia = nullptr;
}

Liczba & Liczba::operator=(const Liczba& x)
{   
    zmienna = x.zmienna;
    ostatni = x.ostatni;
    maks = x.maks;
    rozmiar = x.rozmiar;
    historia = new double[maks];
    
    for (int i = 0; i < x.maks; i++)
    {
        historia[i] = x.historia[i];
    }

    return *this;
}

Liczba& Liczba::operator=(Liczba&& x)
{
    if (this != &x) // uniknięcie samoprzypisania
    {
        delete [] historia;
        maks = x.maks;
        rozmiar = x.rozmiar;
        historia = x.historia;
        zmienna = x.zmienna;
        x.historia = nullptr;
    }

    return *this;
}

Liczba::~Liczba()
{
    if(historia != nullptr)
        delete [] historia;
}

//--------------------------------------------------------------------

void Liczba::set(double nowa)
{
    double n = zmienna;
    zmienna = nowa;

    if(rozmiar < maks)
    {
        historia[rozmiar] = n;
        ostatni = rozmiar;
        rozmiar++;
    }
    else
    {
        rozmiar = maks;
        historia[(ostatni + 1) % maks] = n;
        ostatni++;
    }
}
double Liczba::wypisz(int indeks) //zakładamy, że indeks = 1 oznacza atualną wartość zmiennej, indeks = 2 przedostatnią itd.
{
    if(indeks == 1 || indeks > rozmiar) return zmienna;
    else
    {
        int i; //początek
        if(rozmiar < maks)
            i = 0;
        else 
            i = (ostatni + 1) % maks;
        return historia[(i + rozmiar + 1 - indeks) % maks];
    }
}

void Liczba::przywroc(int indeks) //zakładamy, że indeks = 1 oznacza aktualną wartość zmiennej, indeks = 2 przedostatnią itd.
{
    int id_do_zmiany;

    if(indeks + 1 > rozmiar || indeks == 1)
    {
        id_do_zmiany = ostatni;
    }
    else
    {
        int i = (ostatni + 1) % maks;
        id_do_zmiany = (i + rozmiar + 1 - indeks) % maks;
    }

    double tmp = zmienna;
    zmienna = historia[id_do_zmiany];
    historia[id_do_zmiany] = tmp;

}

double Liczba::get()
{
    return zmienna;
}

//--------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, const Liczba& x)
{
    return out << x.zmienna;
}

