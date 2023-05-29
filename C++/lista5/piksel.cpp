#include "piksel.hpp"
#include "klasy.hpp"
#include <cmath>

piksel::piksel(int a, int b)
{
    if(a < 0 || a >= max_x || b < 0 || b >= max_y )
    {
        throw out_of_range("Podaj inne wspolrzedne, chcesz utworzyc piksel poza ekranem");
    }
    x = a;
    y = b;
}

int piksel::gora()
{
    return y;
}

int piksel::dol()
{
    return max_y-y;
}

int piksel::lewa()
{
    return max_x-x;
}

int piksel::prawa()
{
    return x;
}

pikselkolorowy::pikselkolorowy(int a, int b, kolortransparentny c):piksel(a,b)
{
    kolor = c;
}

void pikselkolorowy::przesun(int a, int b)
{
    if(x + a >= max_x || x + a < 0 || y + b >= max_y || y + b < 0)
    {
        throw out_of_range("Podano niepoprawny wektor przesuniecia, piksel znajduje sie poza ekranem");
    }
    x+=a;
    y+=b;
}

int odleglosc(const piksel &p, const piksel &q)
{
    return sqrt(pow(q.x - p.x, 2) + pow(q.y - p.y, 2));
}

int odleglosc(const piksel *p, const piksel *q)
{
    return sqrt(pow(q->x - p->x, 2) + pow(q->y - p->y, 2));
}

//--------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, piksel& a)
{
    string wyn = "";
    wyn += "(" + to_string(a.prawa()) + ", " + to_string(a.gora()) + ")"; 

    return out << wyn;
}
