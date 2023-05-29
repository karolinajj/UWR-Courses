#pragma once
#include <iostream>
#include <stdexcept>
#include "exception.hpp"
using namespace std;

namespace calculations 
{
    class Rational
    {
        private:
            int numerator;
            int denominator;
            int GCD(int a, int b) noexcept;
            void normalize() noexcept;

        public:
            Rational() noexcept;
            Rational(int numerator, int denominator);
            Rational(const Rational& other) noexcept;
            Rational& operator=(const Rational& other) noexcept;

            const int get_n() const noexcept;
            const int get_d() const noexcept;
            void set_n(int n) noexcept;
            void set_d(int d);
				            
			friend Rational operator + (const Rational &a, const Rational &b);
			friend Rational operator - (const Rational &a, const Rational &b);
			friend Rational operator * (const Rational &a, const Rational &b);
			friend Rational operator / (const Rational &a, const Rational &b);
            friend Rational operator - (const Rational &a);				            
			friend Rational operator ! (const Rational &a);

            Rational& operator += (const Rational &x);
			Rational& operator -= (const Rational &x);
			Rational& operator *= (const Rational &x);
			Rational& operator /= (const Rational &x);

            operator double() noexcept;
			operator int() noexcept;

            friend std::ostream& operator << (std::ostream &output, const Rational &x) noexcept;

    };

} 