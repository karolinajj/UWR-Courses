using System;
using System.Text;
using System.Collections.Generic;



namespace zad4
{
    class Wektor
    {
        int size;
        public List<float> values;

        public Wektor(int n, List<float>V)
        {
            if(V.Count != n) Console.WriteLine("Zmień rozmiar wektora");
            this.size = n;
            values = new List<float>(n);

            for(int i = 0; i < this.size; i++)
            {
                values.Add(V[i]);
            }

        }
        public static Wektor operator +(Wektor w1,Wektor w2) //dodawanie wektorów
        {
            
            if( w1.size != w2.size) //nie można dodać wektorów
            {
                Console.WriteLine("Nie można dodawać wektorów");
            }
            
            var values = new List<float>();
            for(int i = 0; i < w1.size; i++)
            {
                values.Add(w1.values[i] + w2.values[i]);
            }
            return new Wektor(w1.size, values);
        }

        public static float operator *(Wektor w1,Wektor w2) //mnożenie dwóch wektorów
        {
            if( w1.size != w2.size) //nie można dodać wektorów
            {
                Console.WriteLine("Nie można dodawać wektorów");
            }

            float wynik = 0.0F;
            for(int i = 0; i < w1.size; i++)
            {
                wynik += w1.values[i] * w2.values[i];
            }
            return wynik;
        }
        public static Wektor operator *(Wektor w,int s) //mnożenie przez skalar
        {
            var values = new List<float>();
            for(int i = 0; i < w.size; i++)
            {
                values.Add(w.values[i] * s);
            }
            return new Wektor(w.size, values);
        }

        public static float norma(Wektor w) // korzystam ze wzoru |a| = sqrt(a*a)
        {
            return MathF.Sqrt(w*w);
        }

        public void Show() //Dodatkowa metoda wypisująca współrzędne wektora
        {
            Console.Write("(");
            for(int i = 0; i < this.size - 1; i++)
            {
                Console.Write(values[i] + ",");
            }
            Console.Write(values[this.size - 1] + ")");
            Console.WriteLine();
        }
    }
}

