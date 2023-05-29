/*
 * Karolina Jędraszek
 * lista 5 zad 2
 * Windows vs code, openjdk version 17.0.6
 */

public class Variable extends Expression
{
    String name;
    int value;

    public Variable(String n)
    {
        this.name = n;
        this.value = 0; //wartość domyślna zmiennej to 0
    }

    public void setValue(int n) //ustawianie wartości zmiennej
    { 
        this.value = n; 
    }

    public int evaluate() 
    {
        return this.value;
    }

    public String toString()
    {
        return name;
    }
}