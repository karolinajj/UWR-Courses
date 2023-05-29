#pragma once
#include <iostream>
#include <stdexcept>
using namespace std;
    
class RationalException : public std::logic_error
{
public:
    explicit RationalException(const std::string& message)
        : std::logic_error(message) {}
};

class DenominatorIsZeroException : public RationalException
{
public:
    DenominatorIsZeroException()
        : RationalException("Denominator is zero!") {}
};

class OverflowException : public RationalException
{
public:
    OverflowException()
        : RationalException("Overflow exception!") {}
};