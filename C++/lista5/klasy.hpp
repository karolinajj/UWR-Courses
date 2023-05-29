#ifndef KLASY_HPP
#define KLASY_HPP
#include <iostream>
using namespace std;

class kolor
{
    protected:
        unsigned char R;
        unsigned char G;
        unsigned char B;
    public:
        kolor();
        kolor(unsigned char r, unsigned char g, unsigned char b);
        int get_R();
        int get_G();
        int get_B();
        void set_R(unsigned char a);
        void set_G(unsigned char a);
        void set_B(unsigned char a);
        void przyciemnij(float b);
        void rozjasnij(float b);
        static kolor polacz(kolor a, kolor b);

    friend std::ostream& operator<<(std::ostream& out, kolor& A);
};

class kolortransparentny : public virtual kolor
{

protected:
    unsigned char alfa;
public:
    kolortransparentny();
    kolortransparentny(unsigned char r, unsigned char g, unsigned char b, unsigned char d);
    int get_alfa();
    void set_alfa(unsigned char a);

};

class kolornazwany : public virtual kolor
{

protected:
    string nazwa = "";
public:
    kolornazwany() = default;
    kolornazwany(unsigned char r, unsigned char g, unsigned char b, string d);
    string get_nazwa();
    void set_nazwa(string a);

};

class kolornt : public kolortransparentny, public kolornazwany
{

public:
    kolornt() = default;
    kolornt(unsigned char r, unsigned char g, unsigned char b, unsigned char d, string e);
};


#endif
