/*
Karolina Jędraszek
zad 4 lista 3 
.NET Framework 7.0
vs code windows

mcs -t:library nazwa.cs
*/


using System;
using zad2;

/* 
UWAGI: Jeśli wywołamy dict.Add(klucz1, wartosc), a podany klucz (klucz1) znajduje się już w słowniku,
to nic się nie stanie. Aby zmienić wartość klucza1 najleży najpierw go usunąć (dict.Delete()).
*/
class Program
{
    static void Main(string[] args)
    {
       MyDictionary<string, string> dict = new MyDictionary<string, string>();
       Console.WriteLine("Dodajmy do słownika pol-ang następujące tłumaczenia: \npies - dog, kot - cat");
       dict.Add("pies", "dog");
       dict.Add("kot", "cat");
       Console.WriteLine("Wyświetlmy zawartość słownika: ");
       dict.Show();
       Console.WriteLine("Wyszukajmy tłumaczenie dla słowa 'kot'");
       Console.WriteLine(dict.Search("kot"));
       Console.WriteLine("Usuńmy tłumaczenie pies - dog");
       dict.Delete("pies");
       Console.WriteLine("Wyświetlmy zawartość słownika: ");
       dict.Show();

    }
}


