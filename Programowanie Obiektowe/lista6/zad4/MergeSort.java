/*
 * Karolina Jędraszek
 * lista 6 zad 4
 * Windows vs code, openjdk version 17.0.6
 */

public class MergeSort<T extends Comparable<T>> implements Runnable 
{
    private T[] array;
    private int left; //lewa część tablicy
    private int right; //prawa część tablicy

    public MergeSort(T[] array, int left, int right) 
    {
        this.array = array;
        this.left = left;
        this.right = right;
    }

    private void merge(int middle) 
    {
        int i = left;
        int j = middle + 1;
        int k = 0;

        @SuppressWarnings("unchecked") //wiemy, że el tablicy implemetują interfejs Comparable
        T[] tmp = (T[]) new Comparable[right - left + 1];

        while (i <= middle && j <= right) 
        {
            if (array[i].compareTo(array[j]) <= 0) //compareTo zwraca liczbę, będącą wzajemnym "położeniem" porównywanych el. tablicy
            {
                tmp[k] = array[i];
                i++;
            } else 
                {
                    tmp[k] = array[j];
                    j++;
                }
            k++;
        }

        while (i <= middle) 
        {
            tmp[k] = array[i];
            i++;
            k++;
        }

        while (j <= right) 
        {
            tmp[k] = array[j];
            j++;
            k++;
        }

        for (k = 0; k < tmp.length; k++)  //przepisujemy wartości do tablicy array
        {
            array[left + k] = tmp[k];
        }
    }

    @Override
    public void run()
    {
        if (left < right) //czy tablica ma więcej niż jeden el
        {
            int middle = (left + right) / 2;

            MergeSort<T> left_sort = new MergeSort<>(array, left, middle);
            MergeSort<T> right_sort = new MergeSort<>(array, middle + 1, right);

            Thread left_thread = new Thread(left_sort); //pierwszy wątek
            Thread right_thread = new Thread(right_sort); //drugi wątek
            left_thread.start();
            right_thread.start();

            try
            {
                left_thread.join(); 
                right_thread.join();
            } 
            catch (InterruptedException e) 
            {
                e.printStackTrace();
            }
            merge(middle);
        }
    }

}
