#ifndef PIKSEL_HPP
#define PIKSEL_HPP
#include "klasy.hpp"

class piksel
{
    friend int odleglosc(const piksel &p, const piksel &q);
    friend int odleglosc(const piksel *p, const piksel *q);

    protected:
        static const int max_x = 800;
        static const int max_y = 600;
        int x;
        int y;
    public:
        piksel(int a, int b);
        int gora();
        int dol();
        int lewa();
        int prawa();

    friend std::ostream& operator<<(std::ostream& out, piksel& A);
};

class pikselkolorowy: public piksel
{
    public:
        kolortransparentny kolor;
    public:
        pikselkolorowy(int a, int b, kolortransparentny c);
        void przesun(int a, int b);
};

#endif
