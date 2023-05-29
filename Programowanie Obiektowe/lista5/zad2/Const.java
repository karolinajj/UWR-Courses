/*
 * Karolina Jędraszek
 * lista 5 zad 2
 * Windows vs code, openjdk version 17.0.6
 */

public class Const extends Expression
{
    int value;
    public Const(int n)
    {
        this.value = n;
    }

    public int evaluate()
    {
        return value;
    }

    public String toString()
    {
        return String.valueOf(value);
    } 
}


