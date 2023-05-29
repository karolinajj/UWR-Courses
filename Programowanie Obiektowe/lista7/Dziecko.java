import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class Dziecko extends Osoba
{
    private String imie_matki;
    
    public Dziecko (String imie, String nazwisko, int wiek, String imie_matki) 
    {
        super(imie, nazwisko, wiek); //wywołanie konstruktora klasy bazowej (Osoba)
        this.imie_matki = imie_matki;
    }

    public String getImieMatki()
    {
        return imie_matki;
    }

    public void setImieMatki(String imieMatki)
    {
        imie_matki = imieMatki;
    }
    
    @Override
    public String toString() 
    {
        return super.toString() + ", imie matki:" + imie_matki;
    }

    public static Dziecko odczytajZPliku(String nazwaPliku)
    {
        try 
        {
            FileInputStream fi = new FileInputStream(new File(nazwaPliku));
            ObjectInputStream oi = new ObjectInputStream(fi);

            Dziecko osoba = (Dziecko) oi.readObject();

            oi.close();
            fi.close();

            return osoba;
        } 
        catch (IOException e) 
        {
            System.out.println("Error initializing stream");
            return new Dziecko("", "", 10, "");
        } 
        catch (ClassNotFoundException e) 
        {
            e.printStackTrace();
            return new Dziecko("", "", 10, "");
        }        
    }
}
