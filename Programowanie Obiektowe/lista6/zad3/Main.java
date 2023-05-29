/*
 * Karolina Jędraszek
 * lista 6 zad 3
 * Windows vs code, openjdk version 17.0.6
 */

public class Main
{
    public static void main(String[] args)
    {
        int capacity = 5; //maksymalna wielkość bufora
        Buffer buffer = new Buffer(capacity);
        int N = 7; //ile napisów chcemy wyprodukować


        Thread producer = new Thread(() ->
        {
            for(int i = 1; i <= N; i++)
            {
                try
                {
                    System.out.println("producent wyprodukował: " + i);
                    buffer.insert("napis nr " + String.valueOf(i));
                }
                catch (InterruptedException e){e.printStackTrace();}
            }
        });

        Thread consumer = new Thread(() ->
        {
            for(int i = 0; i < N; i++)
            {
                try
                {
                    System.out.println("konsumer zjadł: " + buffer.consume());
                }
            catch (InterruptedException e){e.printStackTrace();}
            }
        });

        //wątki działają równocześnie 
        producer.start();
        consumer.start();
    }
}