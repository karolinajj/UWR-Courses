/*
Karolina Jędraszek
zad1 lista 4
.NET Framework 7.0
*/

using System;
using System.Collections;

/*
UWAGI:
Korzystam z zaprogramowanych wcześniej strumieni IntStream oraz PrimeStream (lista 2, zad1).
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

            Console.WriteLine("IEnumerable, ToString(), dostęp indeksowany i Length() dla intstream:");
            Console.WriteLine("(Dostęp indeksowany) Dla indeksu = 20 mamy " + intstream[20]);
            Console.WriteLine("Przekonwertujmy wartość intstream[20] do string'a: " + intstream[20].ToString());
            Console.WriteLine("Sprawdźmy czy to na pewno string, wykorzystując GetType(): " + (intstream[20].ToString()).GetType());
            
            Console.WriteLine("Wykorzystajmy foreach do wypisywania pierwszych 10 wartości intstream: " + (intstream[20].ToString()).GetType());
            int i = 0;
            foreach(int s in intstream)
            {
                Console.WriteLine(s);
                i++;
                if(i == 10) break;
            }

            intstream.Reset(); //resetujemy strumień
            Console.WriteLine("Teraz kolejnym foreach'em wypiszemy pierwsze 5 wartości intstream: " + (intstream[20].ToString()).GetType());
            i = 0;
            foreach(int s in intstream)
            {
                Console.WriteLine(s);
                i++;
                if(i == 5) break;
            }
        }
    }

    interface IStream
    {
        int next();
        bool eos();
        void reset();
    }

    class IntStream : IStream, IEnumerable<int>, IEnumerator<int>
    {
        int wartosc;
        public IntStream()
        {
            this.wartosc = -2;
        }

        public int next()
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

        public bool eos()
        {
            if(this.wartosc >= 0 && this.wartosc < int.MaxValue) //sprawdzam czy jestem na końcu strumienia
            {
                return false;
            }
            return true; 
        }

        public void reset()
        {
            this.wartosc = -2;
        }

        public int Length
        {
            get
            {
                if(this.wartosc == -1) return -1; //rozmiar strumienia został przekroczony 
                if(this.wartosc < 0) return 0;
                return this.wartosc + 1;
            }
        }

        public override string ToString()
        {
            if (this.wartosc >= 0) return this.wartosc.ToString();
            return "";
        }

        public IEnumerator<int> GetEnumerator()
        {
            return this;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return this;
        }

        public int Current
        {
            get
            {
                return this.wartosc;
            }
        }

        public bool MoveNext()
        {
            next();
            return !(eos());
        }

        public void Reset()
        {
            reset();
        }

        public void Dispose()
        {

        }

        object IEnumerator.Current
        {
            get
            {
                return this.wartosc;
            }
        }

        public int this[int indeks] //dostęp indeksowany
        {
            get
            {
                if(indeks < 0 || indeks > int.MaxValue) //poza zakresem
                {
                    return -1;
                }
                return indeks;
            }
        }
    }

    class PrimeStream: IStream
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

        public int next()
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

        public bool eos()
        {

            if(this.wartosc >= int.MaxValue || this.wartosc < 0) //nie jest możliwe obliczenie kolejnej liczby pierwszej
            {
                return true;
            }
            return false;
        }

        public void reset()
        {
            this.wartosc = 1;
        }
    }
}