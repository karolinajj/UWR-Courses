import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Okno
	extends JFrame
	implements ActionListener {

	private Container c;
    private JButton sub;
    private OsobaEditor osobaEitor;
    private String nazwaPliku;    

	public Okno(OsobaEditor editor, String nazwaPliku)
	{
        this.nazwaPliku = nazwaPliku;

		setTitle("Edytor obiektow");
		setBounds(300, 90, 900, 600);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setResizable(false);

		c = getContentPane();
		c.setLayout(null);

        osobaEitor = editor;
        osobaEitor.setFont(new Font("Arial", Font.PLAIN, 15));
        osobaEitor.setSize(200, 200);
        osobaEitor.setLocation(10, 100);
        c.add(osobaEitor);

		sub = new JButton("Submit");
		sub.setFont(new Font("Arial", Font.PLAIN, 15));
		sub.setSize(100, 20);
		sub.setLocation(150, 450);
		sub.addActionListener(this);
		c.add(sub);

		setVisible(true);
	}

	public void actionPerformed(ActionEvent e)
	{
		if (e.getSource() == sub) {
            Osoba osoba = osobaEitor.getEditedObject();
            System.out.println(osoba);
            osoba.zapiszDoPliku(nazwaPliku);
		}
	}
}