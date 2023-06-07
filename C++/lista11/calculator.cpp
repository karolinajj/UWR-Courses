#include "calculator.hpp"

std::unordered_set<std::string> commands; //all resereved names
std::map<std::string, int> con_match; //for constants
std::map<std::string, int> func_match; //for functions


void calculator::make_dict()
{
    commands.insert("exit");
    commands.insert("set");
    commands.insert("clear");
    commands.insert("to");
    commands.insert("print");
    commands.insert("symbol");
    commands.insert("variable");
    commands.insert("addition");
    commands.insert("subtraction");
    commands.insert("multiplication");
    commands.insert("division");
    commands.insert("number");
    commands.insert("constant");
    commands.insert("sin");
    commands.insert("cos");
    commands.insert("atan");
    commands.insert("acot");
    commands.insert("sgn");
    commands.insert("abs");
    commands.insert("ceil");
    commands.insert("floor");
    commands.insert("frac");
    commands.insert("ln");
    commands.insert("exp");
    commands.insert("modulo");
    commands.insert("min");
    commands.insert("max");
    commands.insert("log");
    commands.insert("pow");
    commands.insert("e");
    commands.insert("pi");
    commands.insert("fi");

    con_match.insert({"e", 0});
    con_match.insert({"pi", 1});
    con_match.insert({"fi", 1});

    func_match.insert({"+", 0});
    func_match.insert({"-", 1});
    func_match.insert({"*", 2});
    func_match.insert({"/", 3});
    func_match.insert({"%", 4});
    func_match.insert({"min", 5});
    func_match.insert({"max", 6});
    func_match.insert({"log", 7});
    func_match.insert({"pow", 8});
    func_match.insert({"abs", 9});
    func_match.insert({"sgn", 10});
    func_match.insert({"floor", 11});
    func_match.insert({"ceil", 12});
    func_match.insert({"frac", 13});
    func_match.insert({"sin", 14});
    func_match.insert({"cos", 15});
    func_match.insert({"atan", 16});
    func_match.insert({"acot", 17});
    func_match.insert({"ln", 18});
    func_match.insert({"exp", 19});
}

void calculator::update_vars(std::string name, double value) //updates or adds a variable
{
    if (variable::var_list.find(name) != variable::var_list.end())
    {
        variable::var_list.insert(std::make_pair(name, value));
    }
    else
        variable::var_list[name] = value;
}


void calculator::func_parser(std::string sexp, int code, std::queue<calculator::symbol*> &queue_todo) //parser for functions
{
    switch(code)
    {
        case 0:
            queue_todo.push(new addition());
            break;
        case 1:
            queue_todo.push(new subtraction());
            break;
        case 2:
            queue_todo.push(new multiplication());
            break;
        case 3:
            queue_todo.push(new division());
            break;
        case 4:
            queue_todo.push(new modulo());
            break;
        case 5:
            queue_todo.push(new min());
            break;
        case 6:
            queue_todo.push(new max());
            break;
        case 7:
            queue_todo.push(new log());
            break;
        case 8:
            queue_todo.push(new pow());
            break;
        case 9:
            queue_todo.push(new abs());
            break;
        case 10:
            queue_todo.push(new sgn());
            break;
        case 11:
            queue_todo.push(new floor());
            break;
        case 12:
            queue_todo.push(new ceil());
            break;
        case 13:
            queue_todo.push(new frac());
            break;
        case 14:
            queue_todo.push(new sin());
            break;
        case 15:
            queue_todo.push(new cos());
            break;
        case 16:
            queue_todo.push(new atan());
            break;
        case 17:
            queue_todo.push(new acot());
            break;
        case 18:
            queue_todo.push(new ln());
            break;
        case 19:
            queue_todo.push(new exp());
            break;
    }
}


void calculator::con_parser(std::string sexp, int code, std::queue<calculator::symbol*> &queue_todo) //parser for constants
{
    switch(code)
    {
        case 0:
            queue_todo.push(new e());
            break;
        case 1:
            queue_todo.push(new pi());
            break;
        case 2:
            queue_todo.push(new fi());
            break;
    }
}


bool calculator::is_number (std::string s)
{
    for(int i = 0; i < s.size(); i++)
    {
        if(s[i] < '0' || s[i] > '9')
        {
            if(s[i] != '.' && s[i] != ',' && s[i] != '-')
            {
                return false;
            }
        }
    }
    return true;
}


bool calculator::parser(std::string expression, int it, std::queue<symbol*> &queue_todo)
{
    std::string sexp = ""; //s-expression
    expression += ' ';

    while (it != expression.length())
    {
        if (expression[it] == ' ')
        {
            if (func_match.find(sexp) != func_match.end()) // operators and functions
            {
                func_parser(sexp, func_match[sexp], queue_todo);
            }
            else if (con_match.find(sexp) != con_match.end()) // constants
            {
                con_parser(sexp, con_match[sexp], queue_todo);
            }
            else if (is_number(sexp)) // numbers
            {
                queue_todo.push(new number(std::stod(sexp)));
            }
            else // variables
            {
                auto zit = variable::var_list.find(sexp);
                if (zit == variable::var_list.end())
                {
                    std::clog<< "ERROR! Unknown variable\n";
                    return false;
                }

                queue_todo.push(new variable(zit->first, zit->second));
            }

            sexp = "";
        }
        else
        {
            sexp += expression[it];
        }

        it++;
    }

    return true;
}


double calculator::evaluator(std::queue<symbol*> &expression)
{
    std::stack<double> stos;
    bool error = false;
    double result;

    while (!expression.empty() && !error)
    {
        auto sit = expression.front();
        expression.pop();

        try
        {
            sit->eval(stos);
        }
        catch (std::invalid_argument e)
        {
            std::clog<< "ERROR! Evaluation\n";
            result = 0;
            error = true;
        }
    }

    if (!error)
    {
        try
        {
            if (stos.size() != 1)
            {
                throw std::invalid_argument("variable");
            }

            result = stos.top();
        }
        catch(std::exception& e)
        {
            std::clog<< "ERROR! Evaluation\n";
            result = 0.0;
        }
    }

    return result;
}

void calculator::make_actions()
{
    bool tmp = true;
    bool variables = false;
    double result;
    std::string input = "";
    std::string todo = "";
    std::string var = "";
    int it = 0;

    make_dict();

    while (tmp)
    {
        input = "";
        todo = "";
        var = "";
        std::queue<symbol*> queue_todo;

        std::cout<< "Type a command:\n";
        getline(std::cin, input);
        it = 0;

        while(queue_todo.size() > 0) //clears the queue
        {
           queue_todo.pop();
        }

        while(it != input.length() && input[it] != ' ')
        {
            todo += input[it];
            it++;
        }

        try
        {
            if (todo == "exit")
            {
                tmp = false;
            }
            else if (todo == "clear")
            {
                variable::var_list.clear();
            }
            else if (todo == "print")
            {
                it++;
                try
                {
                    if (!parser(input, it, queue_todo))
                    {
                        throw std::invalid_argument("parser");
                    }

                    result = evaluator(queue_todo);
                    std::cout<< result << "\n";
                }
                catch (std::invalid_argument e)
                {
                    std::clog<< "ERROR! Parser\n";
                    continue;
                }
            }
            else if (todo == "set")
            {
                it++;
                while(it != input.length() && input[it] != ' ') // getting the name of an variable
                {
                    var += input[it];
                    it++;
                }

                try
                {
                    if (var.length() > 7)
                    {
                        throw std::invalid_argument("variable");
                    }

                    if (commands.find(var) != commands.end())
                    {
                        throw std::invalid_argument("variable");
                    }
                }
                catch (std::invalid_argument e)
                {
                    std::clog<< "ERROR! Inccorect name of the variable\n";
                    continue;
                }

                it++;
                todo = "";
                while(it != input.length() && input[it] != ' ') // wyciagniecie "to"
                {
                    todo += input[it];
                    it++;
                }

                try
                {
                    if (todo != "to")
                    {
                        throw std::invalid_argument("command");
                    }
                }
                catch (std::invalid_argument e)
                {
                    std::clog << "ERROR! Incorrect command\n";
                    continue;
                }

                it++;
                try
                {
                    if (!parser(input, it, queue_todo))
                    {
                        throw std::invalid_argument("parser");
                    }

                    result = evaluator(queue_todo);
                    update_vars(var, result);
                    std::cout<< result << "\n";
                }
                catch (std::invalid_argument e)
                {
                    std::clog<< "ERROR! Parser\n";
                    continue;
                }
            }
            else
            {
                throw std::invalid_argument("variable");
            }
        }
        catch (std::invalid_argument e)
        {
            std::clog<< "ERROR! Unknown variable\n";
        }
    }
}