public class Addition extends Expression 
{
    Expression left;
    Expression right;

    public Addition(Expression l, Expression r) 
    {
        this.left = l;
        this.right = r;
    }
    public int evaluate() 
    {
        return left.evaluate() + right.evaluate();
    }
    public String toString() 
    {
        return "(" + left.toString() + " + " + right.toString() + ")";
    }
}

    

