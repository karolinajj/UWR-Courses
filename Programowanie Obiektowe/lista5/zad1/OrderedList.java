/*
 * Karolina Jędraszek
 * lista 5 zad 1
 * Windows vs code, openjdk version 17.0.6
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class OrderedList
{
    List <Ordered> ordered_list;

    OrderedList()
    {
        ordered_list = new ArrayList<Ordered>();
    }

    void Add(Ordered element)
    {
        ordered_list.add(element);
        Collections.sort(ordered_list);
    }

    Ordered get_first()
    {
        try
        {
            return ordered_list.get(0);
        }
        catch(IndexOutOfBoundsException e)
        {
            System.out.println("This list is empty");
        }
        return null;
    }

    public String toString()
    {
        String elements = "";

        int i = 0;
        for (Ordered element : ordered_list) 
        {
            if(i == 0) elements += element;
            else
            {
                elements += " " + element;
            }
            i++;        
        }
        return elements;
    }
}