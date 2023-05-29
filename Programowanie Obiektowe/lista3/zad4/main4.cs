/*
Karolina Jędraszek
zad 4 lista 3 
.NET Framework 7.0
vs code windows

mcs -t:library nazwa.cs
*/

using System;
using System.Collections.Generic;
using zad4;


class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Tworzymy wektor w1 = (4, 5, 2)");
        List<float> values1 = new List<float> { 4.0F, 5.0F, 2.0F };
        Wektor w1 = new Wektor(3, values1);
    

        Console.WriteLine("Tworzymy wektor w2 = (2, 9, 1)");
        List<float> values2 = new List<float> { 2.0F, 9.0F, 1.0F };
        Wektor w2 = new Wektor(3, values2);


        Console.WriteLine("Dodajemy wektory: w1 + w2:");
        (w1+w2).Show();

        Console.WriteLine("Obliczamy iloczyn skalarny wektorów: w1 * w2:");
        Console.WriteLine(w1*w2);

        Console.WriteLine("Wynik pomnożenia w1 przez 3 (w1 * 3) wynosi: "); //w1 pozostaje niezmienione
        (w1*3).Show();

        Console.WriteLine("Obliczamy długość wektora w1: ");
        Console.WriteLine(Wektor.norma(w1));

    }
}

