import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class Dorosly extends Osoba
{
    private String zawod;
        
    public Dorosly (String imie, String nazwisko, int wiek, String zawod) 
    {
        super(imie, nazwisko, wiek); //wywołanie konstruktora klasy bazowej (Osoba)
        this.zawod = zawod;
    }

    public String getZawod()
    {
        return zawod;
    }

    public void setZawod(String z)
    {
        zawod = z;
    }
    
    @Override
    public String toString() 
    {
        return super.toString() + ", zawod:" + zawod;
    }

    public static Dorosly odczytajZPliku(String nazwaPliku)
    {
        try 
        {
            FileInputStream fi = new FileInputStream(new File(nazwaPliku));
            ObjectInputStream oi = new ObjectInputStream(fi);

            Dorosly osoba = (Dorosly) oi.readObject();

            oi.close();
            fi.close();

            return osoba;
        } 
        catch (IOException e) 
        {
            System.out.println("Error initializing stream");
            return new Dorosly("", "", 10, "");
        } 
        catch (ClassNotFoundException e) 
        {
            e.printStackTrace();
            return new Dorosly("", "", 10, "");
        }        
    }
}
