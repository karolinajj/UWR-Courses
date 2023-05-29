/*
Karolina Jędraszek
zad2 lista 4
.NET Framework 7.0
*/

using System;
using System.Collections;
using System.Collections.Generic;

namespace zad2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Dla argumentu równego 7 otrzymujemy:");
            SlowaFibonacciego slowa = new SlowaFibonacciego(7);
            foreach (string s in slowa)
                Console.WriteLine(s);
            
            slowa.Reset();
            foreach (string s in slowa)
                Console.WriteLine(s); //nic się nie stanie, bo s jest puste

        }
    }
    public class SlowaFibonacciego : IEnumerable<string>, IEnumerator<string>
    {
        int el_count; //ile el już wypisaliśmy
        string val1;
        string val2;
        int size; //ile el jest do wypisania
        string current; //wynik

        public SlowaFibonacciego(int n)
        {
            this.el_count = 0;
            this.val1 = "b";
            this.val2 = "a";
            this.current = "";
            this.size = n;
        }

        public IEnumerator<string> GetEnumerator()
        {
            return this;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return this;
        }

        public string Current
        {
            get
            {
                return current;
            }
        }
        public bool MoveNext()
        {
            el_count++;
            if (el_count == 1) this.current = val1;
            if (el_count == 2) this.current = val2;
            if (el_count >= 3)
            {
                this.current = val1 + val2; //sklejanie napis
                val1 = val2;
                val2 = this.current;
            }

            if (el_count <= size) return true;
            return false;
        }
        public void Reset()
        {
            this.el_count = 0;
            this.val1 = "b";
            this.val2 = "a";
            this.current = "";
            this.size = 0;
        }

        public void Dispose()
        {

        }

        object IEnumerator.Current
        {
            get
            {
                return this.current;
            }
        }
    }

}