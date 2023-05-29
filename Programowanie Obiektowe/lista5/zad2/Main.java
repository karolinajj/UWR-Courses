public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Let's create a new variable:");
        Variable x = new Variable("x");
        x.setValue(2);
        System.out.println(x.toString() + " = " + x.evaluate());

        System.out.println("Let's add x + 7 and create a variable with 'y' with the result:");
        Expression res1 = new Addition(x, new Const(7));
        Variable y = new Variable("y");
        y.setValue(res1.evaluate());
        System.out.println(res1.toString() + " = " + y.evaluate());

        System.out.println("Let's now muliply x and y:");
        Expression res2 = new Multiplication(x, y);
        System.out.println(res2.toString() + " = " + res2.evaluate());
    }
}