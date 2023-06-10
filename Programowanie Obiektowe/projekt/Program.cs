// See https://aka.ms/new-console-template for more information

using System;
using System.Windows.Forms;

Person p1 = new Person(1,"Karolina", "Jędraszek", new BrithDate(20,2,2003));
//Console.WriteLine(p1.age);

Application.EnableVisualStyles();
Application.SetCompatibleTextRenderingDefault(false);
MainForm mainForm = new MainForm();
Application.Run(mainForm);



