/*
 * Karolina Jędraszek
 * lista 6 zad 4
 * Windows vs code, openjdk version 17.0.6
 */

import java.util.Arrays;
public class Main
{
    public static void main(String[] args) 
    {
        System.out.println("Posortujemy następującą tablicę intów: 2, 1, 7 ,-2, 1");
        Integer[] array1 = {2,1,7,-2, 1};

        MergeSort<Integer> test1 = new MergeSort<>(array1, 0, array1.length - 1);
        Thread thread = new Thread(test1);
        thread.start();
        try 
        {
            thread.join();
        } catch (InterruptedException e) 
        {
            e.printStackTrace();
        }
        System.out.println(Arrays.toString(array1));

        System.out.println("A teraz tablicę podanych słów: ala, kot, akacje, pies ");
        String[] array2 = {"ala", "kot", "akacje", "pies"};
        MergeSort<String> test2 = new MergeSort<>(array2, 0, array2.length - 1);
        
        Thread thread2 = new Thread(test2);
        thread2.start();
        try 
        {
            thread2.join();
        } catch (InterruptedException e) 
        {
            e.printStackTrace();
        }
        System.out.println(Arrays.toString(array2));
    }
        
}