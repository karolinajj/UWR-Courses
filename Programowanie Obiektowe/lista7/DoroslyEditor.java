import javax.swing.*;
import java.awt.*;

public class DoroslyEditor extends OsobaEditor 
{

    private JTextField zawodField;
    
    public DoroslyEditor(Dorosly Dorosly) {
        super(Dorosly);

        zawodField = new JTextField(20);
        zawodField.setText(Dorosly.getZawod());

        setLayout(new GridLayout(4, 2));
        add(new JLabel("Zawod:"));
        add(zawodField);
    }

    @Override
    public Osoba getEditedObject() {

        super.getEditedObject();
        ((Dorosly) osoba).setZawod(zawodField.getText());
        return osoba;
    }
}
