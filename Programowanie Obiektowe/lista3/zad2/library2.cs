using System;


namespace zad2
{
    class MyDictionary<K,V>
    {
        K [] keys; //tablica kluczy typu K
        V [] values; //tablica wartosci typu V
        int size; //aktualnie zarezerwowane miejsce w pamięci
        int indeks; //rozmiar słownika

        public MyDictionary()
        {
            size = 5; //na początku rezerwuję miejsce w pamięci
            keys = new K[size];
            values = new V[size];
            indeks = 0;
        }

        public void Add(K key, V value)
        {
            for(int i = 0; i < indeks; i++)
            {
                if(keys[i].Equals(key)) //podany klucz znajduje się już w słowniku
                {
                    return;
                }
            }
            if(indeks >= size) //musimy dodać więcej miejsca w pamięci
            {
                size += 5;
                Array.Resize(ref keys, keys.Length + size);
                Array.Resize(ref values, values.Length + size);
            }
            keys[indeks] = key;
            values[indeks] = value;
            indeks++;
        }

        public V Search(K key)
        {
            for(int i = 0; i < indeks; i++)
            {
                if (keys[i].Equals(key))
                    return values[i];
            }
            return default(V); //zwracam wartość domyślną dla typu V, bo w słowniku nie ma podanego klucza
        }

        public void Delete(K key)
        {
            int delete_indeks = -1;
            for(int i = 0; i < indeks; i++)
            {
                if (keys[i].Equals(key)) //znaleziono klucz
                {
                    delete_indeks = i; //zapamiętuję indeks do usunięcia
                    break;
                }
            }
            if(delete_indeks == -1) return; //w słowniku nie ma podanego klucza, więc nic nie usuwam

            K[] new_keys = new K[indeks - 1];
            V[] new_values = new V[indeks - 1];

            Array.Copy(keys, 0, new_keys, 0, delete_indeks);  //kopiujemy klucze do wystąpienia klucza do usunięcia
            Array.Copy(keys, delete_indeks + 1, new_keys, delete_indeks, indeks - delete_indeks - 1); //dołączamy pozostałe klucze
            Array.Copy(values, 0, new_values, 0, delete_indeks); //kopiujemy wartości do wystąpienia wartości z kluczem do usunięcia
            Array.Copy(values, delete_indeks + 1, new_values, delete_indeks, indeks - delete_indeks - 1); //dołączamy pozostałe wartości

            keys = new_keys; //zastępuję tablicę kluczy jej kopią bez el. do usunięcia
            values = new_values; //zastępuję tablicę wartości jej kopią bez el. do usunięcia
            indeks--;
        }
        public void Show() //metoda wyświetlająca zawartość słownika
        {
            for(int i = 0; i < indeks; i++)
            {
                Console.WriteLine("klucz: " + keys[i] + " wartość: " + values[i]);
            }
        }

    }
}


