/*
 * Karolina Jędraszek
 * lista 7
 * Windows vs code, openjdk version 17.0.6
 */
// UWAGI:
// Aby uruchomić program z terminala należy wpisać kolejno następujące komendy:
// javac *.java //to polecenie skompiluje klasy i powstaną obiekty z rozszerzeniem .class
// java Main nazwa_pliku.txt nazwa_klasy //(nazwy dostępnych klas: Osoba, Dorosly, Dziecko)
// (przy starszych wersjach javy: java Main.css nazwa_pliku.txt nazwa_klasy )

//Aby edytować obiekt ponownie uruchom go poleceniem: java Main nazwa_pliku.txt nazwa_klasy
//następnie dokonaj zmian i kliknij "submit"

public class Main {
    public static void main(String[] args) {
        Osoba osoba = null;
        String klasa = args[1];

        if (klasa.equals("Osoba"))
        {            
            osoba = Osoba.odczytajZPliku(args[0]);
            Okno okno = new Okno(new OsobaEditor(osoba), args[0]);
        }
        else if (klasa.equals("Dziecko")) 
        {
            osoba = Dziecko.odczytajZPliku(args[0]);
            Okno okno = new Okno(new DzieckoEditor((Dziecko)osoba), args[0]);
        }
        else if (klasa.equals("Dorosly")) 
        {
            osoba = Dorosly.odczytajZPliku(args[0]);
            Okno okno = new Okno(new DoroslyEditor((Dorosly)osoba), args[0]);
        }
    }    
}
