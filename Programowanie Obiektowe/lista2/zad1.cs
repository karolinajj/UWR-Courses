/*
Karolina Jędraszek
zad1 lista 2
.NET Framework 7.0
*/

using System;

/*
UWAGI:
Jeśli z powodu ograniczonego rozmiaru int'a nie można wywołać metody next(),
program zwróci -1.
*/

namespace zad1
{
    class Program
    {
        static void Main(string[] args)
        {
            IntStream intstream = new IntStream();
            PrimeStream primestream = new PrimeStream();
            RandomStream randomstream = new RandomStream();
            RandomWordStream randomwordstream = new RandomWordStream();

            Console.WriteLine("Prezentacja IntStream: \n");
            Console.WriteLine("Pierwsze wywołanie intstream.next(): " + intstream.next());
            Console.WriteLine("Drugie wywołanie intstream.next(): " + intstream.next());
            Console.WriteLine("Trzecie wywołanie intstream.next(): " + intstream.next());
            Console.WriteLine("Sprawdźmy wartość intstream.eos(): " + intstream.eos());
            Console.WriteLine("Zresetujmy klasę korzystając z intstream.reset()");
            intstream.reset();
            Console.WriteLine("Pierwsze (po reset) wywołanie intstream.next(): " + intstream.next());

            Console.WriteLine();
            Console.WriteLine("Prezentacja PrimeStream: \n");
            Console.WriteLine("Pierwsze wywołanie primestream.next(): " + primestream.next());
            Console.WriteLine("Drugie wywołanie primestream.next(): " + primestream.next());
            Console.WriteLine("Trzecie wywołanie primestream.next(): " + primestream.next());
            Console.WriteLine("Sprawdźmy wartość primestream.eos(): " + primestream.eos());
            Console.WriteLine("Zresetujmy klasę korzystając z primestream.reset()");
            primestream.reset();
            Console.WriteLine("Pierwsze (po reset) wywołanie primestream.next(): " + primestream.next());

            Console.WriteLine();
            Console.WriteLine("Prezentacja RandomStream: \n");
            Console.WriteLine("Pierwsze wywołanie randomstream.next(): " + randomstream.next());
            Console.WriteLine("Drugie wywołanie randomstream.next(): " + randomstream.next());
            Console.WriteLine("Trzecie wywołanie randomstream.next(): " + randomstream.next());
            Console.WriteLine("Sprawdźmy wartość randomstream.eos(): " + randomstream.eos());

            Console.WriteLine();
            Console.WriteLine("Prezentacja RandomWordStream: \n");
            Console.Write("Pierwsze pięć wywołań randomwordstream.next(): ");
            for(int i = 0; i < 5; i++)
            {
                Console.Write(randomwordstream.next() + " ");
            }
            Console.WriteLine("\nZresetujmy klasę korzystając z primewordstream.reset()");
            randomwordstream.reset();

            Console.WriteLine("Pierwsze wywołanie randomwordstream.next() (po reset): " + randomwordstream.next());   
            
        }
    }
}

class IntStream
{
    int wartosc;
    public IntStream()
    {
        this.wartosc = -2;
    }

    public virtual int next()
    {
        if(this.wartosc == -2)
        {
            this.wartosc = 0;
            return 0;
        }
        if(this.wartosc >= 0 && this.wartosc < int.MaxValue) //sprawdzam czy mogę zwrócić next
        {
            this.wartosc += 1;
            return this.wartosc;
        }
        return -1; //zwracam -1, jeśli rozmiar strumienia został przekroczony
        
    }

    public virtual bool eos()
    {
        if(this.wartosc >= 0 && this.wartosc < int.MaxValue) //sprawdzam czy jestem na końcu strumienia
        {
            return false;
        }
        return true; 
    }

    public virtual void reset()
    {
        this.wartosc = -2;
    }

}

class PrimeStream:IntStream
{
    public bool IsPrime(int n) //funcja sprawdza czy podana liczba jest pierwsza
    {
        if(n == 2) return true;
        if(n % 2 == 0) return false;
        int i = 3;
        while( i*i > 0 && i * i <= n) //i*i > 0, żeby nie wyjść poza zakres
        {
            if(n % i == 0) 
            {
                return false;
            }

            i += 2;
        }
        return true;

    }

    int wartosc;
    public PrimeStream()
    {
        this.wartosc = 1;    
    }

    public override int next()
    {
        int nowa_wartosc = 1;

        if(this.wartosc == int.MaxValue || this.wartosc < 0) // int.MaxVaule = 2,147,483,647  (liczba pierwsza)
        {
            return -1; //zwracam -1, jeśli rozmiar strumienia został przekroczony
        }

        for(int i = this.wartosc+1; i <= int.MaxValue; i++) //szukam następnej liczby pierwszej
        {
            if(IsPrime(i))
            {
                nowa_wartosc = i;
                break;
            }
        }

        this.wartosc = nowa_wartosc;
        return nowa_wartosc;
    }

    public override bool eos()
    {

        if(this.wartosc >= int.MaxValue || this.wartosc < 0) //nie jest możliwe obliczenie kolejnej liczby pierwszej
        {
            return true;
        }
        return false;
    }

    public override void reset()
    {
        this.wartosc = 1;
    }

}

class RandomStream:IntStream
{
    int wartosc;
    public RandomStream()
    {
        Random rnd = new Random();
        this.wartosc = rnd.Next();
    }

    public override int next()
    {
        Random rnd = new Random();
        return rnd.Next();
    }

    public override bool eos()
    {
        return false;
    }
}

class RandomWordStream
{
    int dlugosc;
    string napis;
    PrimeStream dl_primestream = new PrimeStream();
    RandomStream n_randomstream = new RandomStream();
    

    public RandomWordStream()
    {
        this.dlugosc = 0;
        this.napis = "";
    }

    public string next()
    {
        this.dlugosc = dl_primestream.next();

        if(this.dlugosc < 0) return "-1"; //chcemy stworzyć za długi napis
        this.napis = n_randomstream.next().ToString();

        while(this.napis.Length != this.dlugosc)
        {
            if(this.napis.Length < this.dlugosc) //wylosowany napis jest za krótki, więc musimy dokleić kolejny fragment
            {
                this.napis += n_randomstream.next().ToString();
            }
            else
            {
                this.napis = this.napis.Substring(0,this.dlugosc); //przycinamy za długi napis
            }
        }
        return this.napis;
    }
    public bool eos()
    {
        return dl_primestream.eos();
    }

    public void reset()
    {
        this.dlugosc = 0;
        this.napis = "";
        dl_primestream.reset();
    }
}
