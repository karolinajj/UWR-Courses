import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class Osoba implements Serializable
{
    private String imie;
    private String nazwisko;
    private int wiek;

    public Osoba(String imie, String nazwisko, int wiek) 
    {
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.wiek = wiek;
    }

    public String getImie() 
    {
        return imie;
    }

    public void setImie(String imie) 
    {
        this.imie = imie;
    }

    public String getNazwisko() 
    {
        return nazwisko;
    }

    public void setNazwisko(String nazwisko) 
    {
        this.nazwisko = nazwisko;
    }

    public int getWiek() 
    {
        return wiek;
    }

    public void setWiek(int wiek) 
    {
        this.wiek = wiek;
    }

    @Override
    public String toString() 
    {
        return "Osoba: " + imie + " " + nazwisko + ", " + wiek;
    }

    public void zapiszDoPliku(String nazwaPliku) 
    {
        try 
        {
            FileOutputStream f = new FileOutputStream(new File(nazwaPliku));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(this);
            o.close();
            f.close();
        } 
        catch (IOException e) 
        {
            System.out.println("Error initializing stream");
        } 
    }

    public static Osoba odczytajZPliku(String nazwaPliku)
    {
        try 
        {
            FileInputStream fi = new FileInputStream(new File(nazwaPliku));
            ObjectInputStream oi = new ObjectInputStream(fi);

            // Read objects
            Osoba osoba = (Osoba) oi.readObject();

            oi.close();
            fi.close();

            return osoba;
        } 
        catch (IOException e) 
        {
            System.out.println("Error initializing stream");
            return new Osoba("", "", 10);
        } 
        catch (ClassNotFoundException e) 
        {
            e.printStackTrace();
            return new Osoba("", "", 10);
        }        
    }
}


