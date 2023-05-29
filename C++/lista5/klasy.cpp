#include "klasy.hpp"
#include <iostream>
using namespace std;

kolor::kolor()
{
    R = 0;
    G = 0;
    B = 0;
}

kolor::kolor( unsigned char r, unsigned char g, unsigned char b)
{
    if( r > 255 || g > 255 || b > 255 ||r < 0 || g < 0 || b < 0 )
    {
        throw invalid_argument("Niepoprawna reprezentacja koloru, podaj wartosci z zakresu 0-255");
    }

    R = r;
    G = g;
    B = b;
}

int kolor::get_R()
{
    return (int)R;
}

int kolor::get_G()
{
    return (int)G;
}

int kolor::get_B()
{
    return (int)B;
}

void kolor::set_R(unsigned char a)
{
    if(a>255 || a<0)
    {
        throw invalid_argument("Niepoprawna reprezentacja koloru, podaj liczbe z zakresu 0-255");
    }
    R = a;
}

void kolor::set_G(unsigned char a)
{
    if(a>255 || a<0)
    {
        throw invalid_argument("Niepoprawna reprezentacja koloru, podaj liczbe z zakresu 0-255");
    }
    G = a;
}

void kolor::set_B(unsigned char a)
{
    if(a>255 || a<0)
    {
        throw invalid_argument("Niepoprawna reprezentacja koloru, podaj liczbe z zakresu 0-255");
    }
    B = a;
}

void kolor::przyciemnij(float b)
{
    if(b < 0)
    {
        this->rozjasnij(-1*b);
        return;
    }
    else if(b>1)
    {
        throw invalid_argument("Niepoprawna wartosc, podaj liczbe z zakresu 0-1");
    }

    R -= R*b;
    G -= G*b ;
    B -= B*b;
}

void kolor::rozjasnij(float b)
{
    if(b<0)
    {
        this->przyciemnij(-1*b);
    }
    else if (b>1)
    {
        throw invalid_argument("Niepoprawna wartosc, podaj liczbe z zakresu 0-1");
    }
    else
    {
        R += (R+1)*b;
        G += (G+1)*b ;
        B += (B+1)*b;

        if(R>255)
        {
            R = 255;
        }
        if(G>255)
        {
            G = 255;
        }
        if(B>255)
        {
            B = 255;
        }

    }

}

kolor kolor::polacz(kolor a, kolor b)
{

    return kolor((a.R+b.R)/2,(a.G+b.G)/2,(a.B+b.B)/2 );
}

int kolortransparentny::get_alfa()
{
    return (int)alfa;
}

void kolortransparentny::set_alfa( unsigned char a)
{
    if(a>255 || a<0)
    {
        throw invalid_argument("Niepoprawna wartosc, podaj liczbe z zakresu 0-255");
    }
    alfa = a;
}

kolortransparentny::kolortransparentny()
{
    alfa = 0;
}

kolortransparentny::kolortransparentny(unsigned char r, unsigned char g, unsigned char b, unsigned char d):kolor(r,g,b)
{
    if(d > 255 || d < 0)
    {
        throw invalid_argument("Niepoprawna wartosc dla alfy, podaj liczbe z zakresu 0-255");
    }

    alfa = d;
}

string kolornazwany::get_nazwa()
{
    return nazwa;
}

void kolornazwany::set_nazwa(string a)
{
    for(unsigned char i = 0; i < a.size(); i++)
    {
        if(a[i] >= 'a' && a[i] <= 'z')
        {
            nazwa+= a[i];
        }
        else
        {
            throw invalid_argument ("Niepoprawna nazwa, uzyj malych liter alfabetu angielskiego");
        }
    }

}

kolornazwany:: kolornazwany (unsigned char r, unsigned char g, unsigned char b, string d) :kolor(r,g,b)
{
    this->set_nazwa(d);
}

kolornt::kolornt(unsigned char r, unsigned char g, unsigned char b, unsigned char d, string e):kolor(r,g,b), kolortransparentny(r,g,b,d), kolornazwany(r,g,b,e)
{
    set_alfa(d);
    set_nazwa(e);
}

//--------------------------------------------------------------------

std::ostream& operator<<(std::ostream& out, kolor& a)
{
    string wyn = "";
    wyn += "(" + to_string((int)(a.R)) + ", " + to_string((int)(a.G)) + ", " + to_string((int)(a.B)) + ")"; 

    return out << wyn;
}