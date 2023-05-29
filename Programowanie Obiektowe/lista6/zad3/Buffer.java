import java.util.ArrayList;

/*
 * Karolina Jędraszek
 * lista 6 zad 3
 * Windows vs code, openjdk version 17.0.6
 */

public class Buffer
{
    ArrayList<String> buffer;
    int counter; //aktualny rozmiar
    public int capacity; //maksymalny rozmiar

    public Buffer(int capacity)
    {
        this.capacity = capacity;
        this.buffer = new ArrayList<String>(capacity);
        counter = 0;
    }

    public boolean isEmpty()
    {
        if (counter == 0)
            return true;
        else
            return false;
    }

    public boolean isFull()
    {
        if (counter == capacity)
            return true;
        else
            return false;
    }

    public synchronized void insert (String elem) throws InterruptedException
    {
        while (this.isFull()) //czekamy aż zwoli się miejsce
        {
            wait();
        }
        buffer.add(elem);
        counter++;
        notify();
        return;
    }

    public synchronized String consume () throws InterruptedException
    {
        while (this.isEmpty()) //należy coś dodać
        {
            wait();
        }
        counter--;
        notify();
        String result = buffer.get(0);
        buffer.remove(0);
        return result;

    }
}