#include<bits/stdc++.h>
using namespace std;

const vector<pair<int, string>> rzym =
{
    {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4,"IV"},{1, "I"}
};


string bin2rzym(int x)
{

    int val;
    string res = "";

    for(int i = 0; i < rzym.size(); i++)
    {
        val = rzym[i].first;
        while((x > 0) && (x - val >= 0))
        {
            x -= val;
            res += rzym[i].second;
        }
    }

    return res;
}

/*
bool all_numbers(string x) //sprawdzenie czy podany ciag znakow jest liczba
{
    for(int i = 0; i < x.size(); i++)
    {
        if((x[i] < '0') || (x[i] > '9'))
        {
            return 0;
        }
    }
    return 1;
}
*/

bool all_numbers(string x) //sprawdzenie czy podany ciag znakow jest liczba
{
    for(int i = 0; i < x.size(); i++)
    {
        if(!isdigit(x[i])) return 0;
    }
    return 1;
}

void change(string n)
{
int binary;

    try
    {
        if(n[0] == '-' && all_numbers(n.substr(1, n.size()))) //sprawdzenie czy n jest liczba ujemna
        {
            throw out_of_range("");
        }
        else if(!all_numbers(n))
        {
            throw invalid_argument("");
        }

        binary = stoi(n);

        if((binary < 1) || (binary > 3999)) //sprawdzenie czy liczba jest w odpowiednim zakresie
        {

            throw out_of_range("");
        }
        else
        {
            cout << bin2rzym(binary) << endl;
        }
    }
    catch (invalid_argument)
    {
        clog << "Podany argument nie jest liczba" << endl;
    }
    catch (out_of_range)
    {
        clog << "Podano niepoprawny zakres" << endl;
    }
}

int main(int argc, char *argv[])
{
    for(int i = 1; i < argc; i++)
    {
        change(argv[i]);
    }
    return 0;
}
