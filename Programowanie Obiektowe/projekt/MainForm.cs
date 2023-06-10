using System;
using System.Collections.Generic;
using System.Windows.Forms;

public class MainForm : Form
{
    private TextBox textBoxImie;
    private TextBox textBoxNazwisko;
    private Button buttonDodaj;
    private ListBox listBoxOsoby;

    private List<Person> listaOsob;

public MainForm()
{
    InitializeComponents();
    listaOsob = new List<Person>();
}

private void InitializeComponents()
{
    this.Text = "Aplikacja Osoby";
    this.Size = new System.Drawing.Size(400, 300);

    Label labelImie = new Label();
    labelImie.Text = "Imię:";
    labelImie.Location = new System.Drawing.Point(20, 20);

    textBoxImie = new TextBox();
    textBoxImie.Location = new System.Drawing.Point(100, 20);

    Label labelNazwisko = new Label();
    labelNazwisko.Text = "Nazwisko:";
    labelNazwisko.Location = new System.Drawing.Point(20, 50);

    textBoxNazwisko = new TextBox();
    textBoxNazwisko.Location = new System.Drawing.Point(100, 50);

    buttonDodaj = new Button();
    buttonDodaj.Text = "Dodaj";
    buttonDodaj.Location = new System.Drawing.Point(20, 80);
    buttonDodaj.Click += ButtonDodaj_Click;

    listBoxOsoby = new ListBox();
    listBoxOsoby.Location = new System.Drawing.Point(20, 120);
    listBoxOsoby.Size = new System.Drawing.Size(200, 150);

    this.Controls.Add(labelImie);
    this.Controls.Add(textBoxImie);
    this.Controls.Add(labelNazwisko);
    this.Controls.Add(textBoxNazwisko);
    this.Controls.Add(buttonDodaj);
    this.Controls.Add(listBoxOsoby);
}

private void ButtonDodaj_Click(object sender, EventArgs e)
{
    string imie = textBoxImie.Text;
    string nazwisko = textBoxNazwisko.Text;

    Person osoba = new Person(1, imie, nazwisko, new BrithDate(1,12,2003));
    listaOsob.Add(osoba);

    listBoxOsoby.Items.Add(osoba);

    textBoxImie.Clear();
    textBoxNazwisko.Clear();
}
}