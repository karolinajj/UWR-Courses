/*
 * Karolina Jędraszek
 * lista 5 zad 1
 * Windows vs code, openjdk version 17.0.6
 */
public class Main 
{
    public static void main (String[] args)
    {
        OrderedList o1 = new OrderedList();
        o1.Add(new Major());
        o1.Add(new Private());
        o1.Add(new Sergeant());
        o1.Add(new Specialist());

        System.out.println("Lista wszystkich stopni: " + o1.toString());
        
        Ordered o2 = o1.get_first();
        System.out.println("Pierwszy stopień: " + o2.toString());
        
    }
}
