import javax.swing.*;
import java.awt.*;

public class DzieckoEditor extends OsobaEditor 
{

    private JTextField imieMatkiField;
    
    public DzieckoEditor(Dziecko dziecko) {
        super(dziecko);

        imieMatkiField = new JTextField(20);
        imieMatkiField.setText(dziecko.getImieMatki());

        setLayout(new GridLayout(4, 2));
        add(new JLabel("Imie matki:"));
        add(imieMatkiField);
    }

    @Override
    public Osoba getEditedObject() {

        super.getEditedObject();
        ((Dziecko) osoba).setImieMatki(imieMatkiField.getText());
        return osoba;
    }
}
