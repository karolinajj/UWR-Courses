#include "calculations.hpp"
#include <iostream>
#include <vector>
using namespace std;

namespace calculations
{
    int Rational::GCD(int a, int b) noexcept
    {
        if (b != 0) return GCD(b, a%b);
        return a;
    }

    void Rational::normalize() noexcept
    {
        int n = this->numerator;
        int d = this->denominator;
        int gcd = GCD(abs(n), abs(d));

        n /= gcd;
        d /= gcd;

        if (denominator < 0)
        {
            n *= -1;
            d *= -1;
        }

        this->numerator = n;
        this->denominator = d;
    }

    //constructors-----------------------------------

    Rational::Rational() noexcept
    {
        this->numerator = 0;
        this->denominator = 1;
    }

    Rational::Rational(int n, int d)
    {
        if(d == 0) throw DenominatorIsZeroException();
        this->numerator = n;
        this->denominator = d;
        normalize();
    }

    Rational::Rational(const Rational& other) noexcept
    {
        this->numerator = other.numerator;
        this->denominator = other.denominator;
    }

    Rational& Rational::operator=(const Rational& other) noexcept
    {
        if (this != &other) 
        {
            this->numerator = other.numerator;
            this->denominator = other.denominator;
        }
        return *this;
    }

    //gettery,settery---------------------------------
    
    const int Rational::get_n() const noexcept
    {
        return this->numerator;
    }

    const int Rational::get_d() const noexcept
    {
        return this->denominator;
    }

    void Rational::set_n(int n) noexcept
    {
        this->numerator = n;
    }

    void Rational::set_d(int d)
    {
        if(d == 0)
        {
            throw DenominatorIsZeroException();
        }
        else
        {
            this->denominator = d;
            normalize();
        }
    }
    

    //operators---------------------------------------

    Rational operator + (const Rational &a, const Rational &b)
    {
        long long tmp_n, tmp_d;
        tmp_n = a.numerator * b.denominator + b.numerator * a.denominator;
        tmp_d = a.denominator * b.denominator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }

        Rational result(tmp_n, tmp_d);
        return result;
    }

    Rational operator - (const Rational &a, const Rational &b)
    {
        long long tmp_n, tmp_d;
        tmp_n = a.numerator * b.denominator - b.numerator * a.denominator;
        tmp_d = a.denominator * b.denominator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }

        Rational result(tmp_n, tmp_d);
        return result;
    }

    Rational operator * (const Rational &a, const Rational &b)
    {
        long long tmp_n, tmp_d;
        tmp_n = a.numerator * b.numerator;
        tmp_d = a.denominator * b.denominator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }

        Rational result(tmp_n, tmp_d);
        return result;
    }

    Rational operator / (const Rational &a, const Rational &b)
    {
        if (b.numerator == 0)
        {
            throw DenominatorIsZeroException();
        }

        long long tmp_n, tmp_d;
        tmp_n = a.numerator * b.denominator;
        tmp_d = a.denominator * b.numerator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }

        Rational result(tmp_n, tmp_d);
        return result;
    }

    Rational operator - (const Rational &a)
    {
        Rational result(a.numerator * (-1), a.denominator);
        return result;
    }

    Rational operator ! (const Rational &a)
    {
        int tmp_n = a.numerator;
        int tmp_d = a.denominator;

        if(a.numerator < 0) //switches numerators and denominators signs
        {
            tmp_d *= (-1);
            tmp_n *= (-1);
        }
        Rational result(tmp_d, tmp_n); //if division by 0 occurs, constructor will throw an error
        return result;
    }

    Rational& Rational::operator += (const Rational &x)
    {
        long long tmp_n = this->numerator * x.denominator + x.numerator * this->denominator;
        long long tmp_d = this->denominator * x.denominator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }
        else
        {
            this->numerator = tmp_n;
            this->denominator = tmp_d;
        }

        return *this;
    }

    Rational& Rational::operator -= (const Rational &x)
    {
        long long tmp_n = this->numerator * x.denominator - x.numerator * this->denominator;
        long long tmp_d = this->denominator * x.denominator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }
        else
        {
            this->numerator = tmp_n;
            this->denominator = tmp_d;
        }

        return *this;
    }

    Rational& Rational::operator *= (const Rational &x)
    {
        long long tmp_n = this->numerator * x.numerator;
        long long tmp_d = this->denominator * x.denominator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }
        else
        {
            this->numerator = tmp_n;
            this->denominator = tmp_d;
        }

        return *this;
    }

    Rational& Rational::operator /= (const Rational &x)
    {
        long long tmp_n = this->numerator * x.denominator;
        long long tmp_d = this->denominator * x.numerator;

        if (tmp_n > INT_MAX || tmp_n < INT_MIN || tmp_d > INT_MAX || tmp_d < INT_MIN)
        {
            throw OverflowException();
        }
        else
        {
            this->numerator = tmp_n;
            this->denominator = tmp_d;
        }

        return *this;
    }

    //double,int--------------------------------------  

    Rational::operator double() noexcept
    {
        return (double) this->numerator / this->denominator;
    }

    Rational::operator int() noexcept
    {
        return this->numerator / this->denominator;
    }

    //out---------------------------------------------

    std::ostream& operator << (std::ostream &output, const calculations::Rational &x) noexcept
    {
        vector <int> remainders;
        vector <int> results;

        unsigned int i, j;
        int remainder, num;
        num = x.numerator;

        if(num < 0)
        {
            num = -num;
            output << "-";
        }

        remainder = num % x.denominator;
        if (remainder == 0)
        {
            output << num / x.denominator;
            return output;
        }

        remainders.push_back (remainder);
        
        output << num / x.denominator;

        while(true)
        {
            results.push_back (remainder * 10 / x.denominator);
            remainder = remainder * 10 % x.denominator;
            
            if (remainder == 0)
            {
                output << ".";
                for (i = 0; i < results.size(); i++)
                    output << results[i];
                return output;
            }

            for (j = 0; j < remainders.size(); j++)
            {
                if (remainder == remainders[j])
                {
                    output << ".";
                    for (i = 0; i < j; i++)
                        output << results[i];

                    output << "(";
                    for (i = j; i < results.size(); i++)
                        output << results[i];
                    output << ")";

                    return output;
                }
            }
            remainders.push_back (remainder);
        }
    } 


}