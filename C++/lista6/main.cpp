#include <iostream>
#include <vector>
#include "expressions.hpp"
#include "binary.hpp"
#include "unary.hpp"

using namespace std;

int main()
{ 

    Expr *e1 = new Div(new Mul(new Sub(new Variable("x"), new Number(1)),new Variable("x")),new Number(2));
    Expr *e2 = new Div(new Add(new Number(3), new Number(5)), new Add(new Number(2), new Mul(new Variable("x"), new Number(7))));
    Expr *e3 = new Sub(new Add(new Number(2),new Mul(new Variable("x"),new Number(7))), new Add(new Mul(new Variable ("y"),new Number(3)),new Number(5)));
    Expr *e4 = new Div(new Cos(new Mul(new Add(new Variable("x"), new Number(1)),new pi())),new Pow(new Pow(new e(), new Variable("x")), new Number(2)));
    Expr *e5 = new Sub(new pi(),new Add(new Number(2),new Mul(new Variable("x"),new Number(7))));

    double i, j;
    i = 0;
    j = 0;
    cout << "\nx = " << i << " ";
    Variable::addVariable("x", i);
    cout << "\ny = " << j << "\n";
    Variable::addVariable("y", j);
    cout << e1->description() << " = " << e1->eval() << endl;
    cout << e2->description() << " = " << e2->eval() << endl;
    cout << e3->description() << " = " << e3->eval() << endl;
    cout << e4->description() << " = " << e4->eval() << endl;
    cout << e5->description() << " = " << e5->eval() << endl;
    Variable::removeVariable("x");
    Variable::removeVariable("y");

    i = 0;
    j = 0.5;
    cout << "\nx = " << i << " ";
    Variable::addVariable("x", i);
    cout << "\ny = " << j << "\n";
    Variable::addVariable("y", j);
    cout << e1->description() << " = " << e1->eval() << endl;
    cout << e2->description() << " = " << e2->eval() << endl;
    cout << e3->description() << " = " << e3->eval() << endl;
    cout << e4->description() << " = " << e4->eval() << endl;
    cout << e5->description() << " = " << e5->eval() << endl;
    Variable::removeVariable("x");
    Variable::removeVariable("y");

    i = 0.5;
    j = 0;
    cout << "\nx = " << i << " ";
    Variable::addVariable("x", i);
    cout << "\ny = " << j << "\n";
    Variable::addVariable("y", j);
    cout << e1->description() << " = " << e1->eval() << endl;
    cout << e2->description() << " = " << e2->eval() << endl;
    cout << e3->description() << " = " << e3->eval() << endl;
    cout << e4->description() << " = " << e4->eval() << endl;
    cout << e5->description() << " = " << e5->eval() << endl;
    Variable::removeVariable("x");
    Variable::removeVariable("y");

    i = 0.5;
    j = 0.5;
    cout << "\nx = " << i << " ";
    Variable::addVariable("x", i);
    cout << "\ny = " << j << "\n";
    Variable::addVariable("y", j);
    cout << e1->description() << " = " << e1->eval() << endl;
    cout << e2->description() << " = " << e2->eval() << endl;
    cout << e3->description() << " = " << e3->eval() << endl;
    cout << e4->description() << " = " << e4->eval() << endl;
    cout << e5->description() << " = " << e5->eval() << endl;
    Variable::removeVariable("x");
    Variable::removeVariable("y");

    i = 1;
    j = 1;
    cout << "\nx = " << i << " ";
    Variable::addVariable("x", i);
    cout << "\ny = " << j << "\n";
    Variable::addVariable("y", j);
    cout << e1->description() << " = " << e1->eval() << endl;
    cout << e2->description() << " = " << e2->eval() << endl;
    cout << e3->description() << " = " << e3->eval() << endl;
    cout << e4->description() << " = " << e4->eval() << endl;
    cout << e5->description() << " = " << e5->eval() << endl;
    Variable::removeVariable("x");
    Variable::removeVariable("y");

    return 0;
}