import javax.swing.*;
import java.awt.*;


public class OsobaEditor extends JComponent implements Editor<Osoba> 
{

    private JTextField imieField;
    private JTextField nazwiskoField;
    private JSpinner wiekSpinner;
    protected Osoba osoba;
    
    public OsobaEditor(Osoba osoba) {
        this.osoba = osoba;

        // pola tekstowe
        imieField = new JTextField(20);
        imieField.setText(osoba.getImie());

        nazwiskoField = new JTextField(20);
        nazwiskoField.setText(osoba.getNazwisko());

        // spinner z wiekiem
        SpinnerModel spinnerModel = new SpinnerNumberModel(osoba.getWiek(), 0, 120, 1);
        wiekSpinner = new JSpinner(spinnerModel);

        setLayout(new GridLayout(3, 2));
        add(new JLabel("Imie:"));
        add(imieField);
        add(new JLabel("Nazwisko:"));
        add(nazwiskoField);
        add(new JLabel("Wiek:"));
        add(wiekSpinner);
    }

    @Override
    public Osoba getEditedObject() {
        // aktualizacja pól osoby na podstawie wartości w polach edycji
        osoba.setImie(imieField.getText());
        osoba.setNazwisko(nazwiskoField.getText());
        osoba.setWiek((int) wiekSpinner.getValue());
        return osoba;
    }

    public JTextField getImieField() {
        return imieField;
    }

    public void setImieField(JTextField imieField) {
        this.imieField = imieField;
    }

    public JTextField getNazwiskoField() {
        return nazwiskoField;
    }

    public void setNazwiskoField(JTextField nazwiskoField) {
        this.nazwiskoField = nazwiskoField;
    }

    public JSpinner getWiekSpinner() {
        return wiekSpinner;
    }

    public void setWiekSpinner(JSpinner wiekSpinner) {
        this.wiekSpinner = wiekSpinner;
    }

    public Osoba getOsoba() {
        return osoba;
    }

    public void setOsoba(Osoba osoba) {
        this.osoba = osoba;
    }
}
