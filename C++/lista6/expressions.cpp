#include "expressions.hpp"
using namespace std;

vector<pair<string, double>> Variable::variables;

Number::Number(double value)
{
    this->value = value;
}

string Number::description()
{
    string str = to_string(value);
    int offset = 1;
    
    if (str.find_last_not_of('0') == str.find('.')) // handles cases where the string ends with one or more zeros after the decimal point
        offset = 0;
    
    str.erase(str.find_last_not_of('0') + offset, string::npos); //removes all trailing zeros from the string

    return str;
}

double Number::eval()
{
    return value;
}

Variable::Variable(string var)
{
    this->Variable_name = var;
}

string Variable::description()
{
    return Variable_name;
}

double Variable::eval()
{
    try
    {
        int counter = Variable::variables.size();
        for (int i = 0; i < counter; i++)
        {
            if (Variable::variables[i].first == Variable_name)
            {
                return Variable::variables[i].second;
            }
        }

        string error = "Error, variable was not found.";
        throw error;
    }
    catch(string error_msg)
    {
        cerr << "Error in static variables: " << error_msg << " while executing eval.\n";
        return -1; //If there is an error, -1 will be returned
    }
}

//-----------------------------------------------------------------------

void Variable::addVariable(string var, double val)
{
    int counter = Variable::variables.size();

    for (int i = 0; i < counter; i++)
    {
        if (Variable::variables[i].first == var)
        {
            cout << "Warning! Variable " << var << " already exists.";
            return;
        }
    }

    Variable::variables.push_back(make_pair(var, val));
}

void Variable::removeVariable(string var)
{
    try
    {
        int counter = Variable::variables.size();
        for (int i = 0; i < counter; i++)
        {
            if (Variable::variables[i].first == var)
            {
                Variable::variables.erase(Variable::variables.begin() + i);
                return;
            }
        }
        string error = "Variable was not found.";
        throw error;
    }
    catch (string error)
    {
        cout << "Error in static variables: " << error << endl;
        cout << "The Array of variables has not been changed." << endl;
    }
}

void Variable::printVariables()
{
    int counter = Variable::variables.size();

    cout << "Variables: " << endl;
    for (int i = 0; i < counter; i++)
        std::cout << Variable::variables[i].first << "\t" << Variable::variables[i].second << endl;
}

//-----------------------------------------------------------------------

pi::pi()
{
    value = 3.141592;
}

std::string pi::description()
{
    return "pi";
}

double pi::eval()
{
    return value;
}

//-----------------------------------------------------------------------

e::e()
{
    value = 2.718281;
}

string e::description()
{
    return "e";
}

double e::eval()
{
    return value;
}

//-----------------------------------------------------------------------

fi::fi()
{
    value = 3.141592;
}

string fi::description()
{
    return "fi";
}

double fi::eval()
{
    return value;
}
