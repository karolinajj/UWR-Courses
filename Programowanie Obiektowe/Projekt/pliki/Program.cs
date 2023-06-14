using System;
using System.Text.Json;
using System.IO;
using System.Collections.Generic;

/// <summary>
/// Main program class.
/// </summary>
class Program
{
    public static string filePeople = "people.txt";
    public static string fileCoaches = "coaches.txt";
    public static string fileClasses = "classes.txt";
    public static string fileItems = "items.txt";
    public static string filePasses = "passes.txt";

    public static int peopleCount = Person.getPeople(filePeople).Count;
    public static int coachesCount = Coach.getPeople(fileCoaches).Count;
    
    /// <summary>
    /// Updates the count of people.
    /// </summary>
    public static void UpdatePeopleCount()
    {
        peopleCount = Person.getPeople(filePeople).Count;
    }
    
    /// <summary>
    /// Updates the count of coaches.
    /// </summary>
    public static void UpdateCoachesCount()
    {
        peopleCount = Person.getPeople(filePeople).Count;
    }
    static void Main()
    {
        while (true)
        {
            UpdatePeopleCount();
            UpdateCoachesCount();

            Console.WriteLine("Choose an option:");
            Console.WriteLine("1. Add classes");
            Console.WriteLine("2. Add people");
            Console.WriteLine("3. Add coaches");
            Console.WriteLine("4. Add items");
            Console.WriteLine("5. Add passes");
            Console.WriteLine("6. Get user information");

            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    if(coachesCount == 0 || peopleCount == 0)
                    {
                        Console.WriteLine("Error! To create a class you need to create at least one coach and one person.");
                    }
                    else
                    {
                        Class.SaveClass();
                    }
                    break;
                case "2":
                    Person.SavePeople(Program.peopleCount, Program.filePeople);
                    UpdatePeopleCount();
                    break;
                case "3":
                    Coach.SavePeople(Program.coachesCount, Program.fileCoaches);
                    UpdateCoachesCount();
                    break;
                case "4":
                    Item.SaveItems(fileItems);
                    break;
                case "5":
                    Pass.SaveItems(filePasses);
                    break;
                case "6":
                    Person.userGetInfo();
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }

            Console.WriteLine("Press any key to continue or 'q' to quit.");
            string input = Console.ReadLine();
            if (input == "q")
                break;
        }
    }
}


