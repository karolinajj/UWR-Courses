/*
 * Karolina Jędraszek
 * lista 5 zad 2
 * Windows vs code, openjdk version 17.0.6
 */

public class Multiplication extends Expression 
{
    Expression left;
    Expression right;

    public Multiplication(Expression l, Expression r) 
    {
        this.left = l;
        this.right = r;
    }
    public int evaluate() 
    {
        return left.evaluate() * right.evaluate();
    }
    public String toString() 
    {
        return "(" + left.toString() + " * " + right.toString() + ")";
    }
}
