#include <iostream>
#include "calculations.hpp"
using namespace std;
using namespace calculations;

int main()
{
    // Create rational numbers
    Rational r1(1, 2);
    Rational r2(1, 3);
    Rational r3(5, 2);
    Rational r4 = r1;
    Rational r5(r1);

    cout << "Rational Numbers:" << endl;
    cout << "r1: " << r1 << endl;
    cout << "r2: " << r2 << endl;
    cout << "r3: " << r3 << endl;
    cout << "r4: " << r4 << endl;
    cout << "r5: " << r5 << endl << endl;

    //get,set
    cout << "r5 = " << r5.get_n() << " / " << r5.get_d();
    r5.set_n(3);
    r5.set_d(-7);
    cout << r5 << endl << endl;

    // Test arithmetic operators
    Rational sum = r1 + r2;
    cout << "r1 + r2 = " << sum << endl;
    Rational difference = r1 - r2;
    cout << "r1 - r2 = " << difference << endl;
    Rational product = r1 * r2;
    cout << "r1 * r2 = " << product << endl;
    Rational quotient = r1 / r2;
    cout << "r1 / r2 = " << quotient << endl;
    cout << "-r1 = " << -r1 << endl;
    cout << "1/r1 = " << !r1 << endl << endl;

    // Test compound assignment operators
    Rational compoundSum = r1;
    compoundSum += r2;
    cout << "r1 += r2: " << compoundSum << endl;
    Rational compoundDifference = r1;
    compoundDifference -= r2;
    cout << "r1 -= r2: " << compoundDifference << endl;
    Rational compoundProduct = r1;
    compoundProduct *= r2;
    cout << "r1 *= r2: " << compoundProduct << endl;
    Rational compoundQuotient = r1;
    compoundQuotient /= r2;
    cout << "r1 /= r2: " << compoundQuotient << endl << endl;

    // Test conversion operators
    double decimalValue = static_cast<double>(r2);
    cout << "(double) r2 = " << decimalValue << endl;
    int integerValue = static_cast<int>(r1);
    cout << "(int) r1 = " << integerValue << endl;

    return 0;
}
