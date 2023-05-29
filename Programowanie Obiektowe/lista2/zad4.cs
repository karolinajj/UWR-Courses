/*
Karolina Jędraszek
zad 4 lista 2
.NET 7.0
*/

using System;
using System.Collections.Generic; //Listy


/*
UWAGI: 
Listy LazyIntList indeksuję od zera, tj. lista.element(0) doda zero na pozycję zerową i zwróci 0.
Wtedy wielkość listy lista.size() = 1 (bo zawiera jeden element).
Listy LazyPrimeList indeksuję od jedynki, tj. lista.element(0) zwróci -1.
Jeśli wywołamy element(a), gdzie a < 0 program zwróci -1.
*/

namespace zad1
{
    class Program
    {
        static void Main(string[] args)
        {
            LazyIntList list = new LazyIntList();
            LazyPrimeList list_prime = new LazyPrimeList();

            Console.WriteLine("Prezentacja LazyIntList:");
            Console.WriteLine("Wywołanie list.element(0): " + list.element(0));
            Console.WriteLine("Wywołanie list.size(): " + list.size());
            Console.WriteLine("Wywołanie list.element(20): " + list.element(20));
            Console.WriteLine("Wywołanie list.size(): " + list.size() + " (liczby 0,1,..,20)");
            Console.WriteLine("Wywołanie list.element(-3): " + list.element(-1) + " (nie ma elementu -3)");
            Console.WriteLine();
            Console.WriteLine("Prezentacja LazyPrimeList:");
            Console.WriteLine("Wywołanie list.element(0): " + list_prime.element(0) + " (numeruję liczby pierwsze od 1, więc nie ma elementu zerowego)");
            Console.WriteLine("Wywołanie list.element(3): " + list_prime.element(3));
            Console.WriteLine("Wywołanie list.size(): " + list_prime.size() + " (liczby 2,3,5)");
            Console.WriteLine("Wywołanie list.element(5): " + list_prime.element(5));
            Console.WriteLine("Wywołanie list.size(): " + list_prime.size() + " (liczby 2,3,5,7,11)");
        }
    }
}


class LazyIntList 
{
    List<int> lista; 
    protected int el_count; //ile elementów ma lista

    public LazyIntList()
    {
        this.el_count = 0;
        this.lista = new List<int>();
    }

    public virtual int element(int indeks)
    {
        if(indeks < 0) return -1; //na liście nie ma elementów ujemnych
        if(this.el_count == 0 && indeks == 0) 
        {
            this.lista.Add(0);
            this.el_count = 1;
        }
        else if (this.el_count < indeks) //do listy trzeba dopisać brakujące elementy
        {
            for(int i = el_count; i <= indeks;i++)
            {
                this.lista.Add(i);
            }
            this.el_count = indeks+1; //zwiększa się licza elementów na liście
        }
        return this.lista[indeks];
    }
    public virtual int size()
    {
        return this.el_count;
    }

}

class LazyPrimeList:LazyIntList
{
    List<int> lista_prime;
   //ile el ma lista

    public bool IsPrime(int n) //sprawdzenie czy n jest liczbą pierwszą
    {
        if(n == 2) return true;
        if(n % 2 == 0) return false;
        for(int i = 3; i*i <= n; i+=2)
        {
            if(n % i == 0) return false;
        }
        return true;

    }

    public LazyPrimeList()
    {
        this.el_count = 0;
        this.lista_prime = new List<int>();
    }

    public override int element(int indeks)
    {

        if(indeks <= 0) return -1; //numeruję liczby pierwsze od 1, stąd nie ma zerowej liczby pierwszej
        if(this.el_count == 0)
        {
            this.lista_prime.Add(2);
            el_count += 1;

        }
        int tmp = indeks - el_count; //ile liczb pierwszych należy dodać
        for(int i = lista_prime[el_count - 1] + 1; tmp > 0; i++)
        {
            if(IsPrime(i)) //szukam kolejnych liczb pierwszych i dodaję je do listy
            {
                this.lista_prime.Add(i);
                tmp -= 1;
            }
        }
        el_count = Math.Max(indeks,el_count); //aktualizuję liczbę elementów na liście
        
        return this.lista_prime[indeks - 1];
    }

    public override int size()
    {
        return el_count;
    }
}