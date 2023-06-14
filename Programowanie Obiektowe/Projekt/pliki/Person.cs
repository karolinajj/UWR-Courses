using System;
using System.Collections.Generic;
using System.Text.Json;
using System.IO;

/// <summary>
/// Class representing a person.
/// </summary>
public class Person
{

    /// <summary>
    /// Represents the ID of the person.
    /// </summary>
    public int id { get; set; }

    /// <summary>
    /// Represents the name of the person.
    /// </summary>
    public string name { get; set; }

    /// <summary>
    /// Represents the surname of the person.
    /// </summary>
    public string surname { get; set; }

    /// <summary>
    /// Represents the birthdate of the person.
    /// </summary>
    public BirthDate birthdate { get; set; }

    /// <summary>
    /// Represents the age of the person.
    /// </summary>
    public int age;

    /// <summary>
    /// Initializes a new instance of the Person class.
    /// </summary>
    /// <param name="id">The ID of the person.</param>
    /// <param name="name">The name of the person.</param>
    /// <param name="surname">The surname of the person.</param>
    /// <param name="birthdate">The birthdate of the person.</param>
    public Person(int id, string name, string surname, BirthDate birthdate)
    {
        this.id = id;
        this.name = name;
        this.surname = surname;
        this.birthdate = birthdate;
        this.age = birthdate.GetAge();
    }

    /// <summary>
    /// Saves the person object to a JSON file.
    /// </summary>
    /// <param name="fileName">The name of the file.</param>
    public void SaveToFile(string fileName)
    {
        string jsonString = JsonSerializer.Serialize(this);

        using (StreamWriter writer = new StreamWriter(fileName, true))
        {
            writer.WriteLine(jsonString);
        }
    }

    /// <summary>
    /// Saves multiple people to the database.
    /// </summary>
    /// <param name="id">The ID of the first person.</param>
    /// <param name="fileName">The name of the file.</param>
    public static void SavePeople(int id, string fileName)
    {
        Console.WriteLine("How many people do you want to add to the database?");
        int n = 0;
        while(true)
        {
            string input = Console.ReadLine();
            n = int.Parse(input);
            if(n > 0) break;
            else
            {
                Console.WriteLine("Error! Please Enter a positive number.");
            }
        }

        for (int i = 0; i < n; i++)
        {
            Console.WriteLine("Enter name: ");
            string name = Console.ReadLine();

            Console.WriteLine("Enter surname: ");
            string surname = Console.ReadLine();

            BirthDate birthdate = BirthDate.userGetBirthDate();

            Person person = new Person(id + i, name, surname, birthdate);
            person.SaveToFile(fileName);
            Console.WriteLine("Person successfully added.");
        }
    }

    /// <summary>
    /// Retrieves a list of people from a JSON file.
    /// </summary>
    /// <param name="fileName">The name of the file.</param>
    /// <returns>A list of Person objects.</returns>
    public static List<Person> getPeople(string fileName)
    {
        List<Person> people = new List<Person>();
        string fileContent = File.ReadAllText(fileName);
        string[] tab = fileContent.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string personJson in tab)
        {
            Person person = JsonSerializer.Deserialize<Person>(personJson);
            people.Add(person);
        }
        return people;
    }

    /// <summary>
    /// Retrieves a list of person IDs.
    /// </summary>
    /// <returns>A sorted list of person IDs.</returns>
   public static List<int> personIds()
    {
        List<Person> people = getPeople(Program.filePeople);
        List<int> ids = new List<int>();

        foreach (Person person in people)
        {
            ids.Add(person.id);
        }
        ids.Sort();

        return ids;
    }

    /// <summary>
    /// Looks up a person by their ID.
    /// </summary>
    /// <param name="people">The list of people.</param>
    /// <param name="id">The ID to look up.</param>
    /// <returns>The person with the specified ID, or null if not found.</returns>
    static Person lookUpId(List<Person> people, int id)
    {
        foreach (Person person in people)
        {
            if (person.id == id)
            {
                return person;
            }
        }
        return null;
    }

    /// <summary>
    /// Prompts the user to select participants from the available people.
    /// </summary>
    /// <returns>A list of selected people.</returns>
    public static List<Person> userGetParticipants() // returns list of chosen people
    {
        Console.WriteLine("Podaj id osób, dostępne id to:");
        List<int> ids = personIds();
        List<Person> people = getPeople(Program.filePeople);

        foreach (Person person in people)
        {
            Console.WriteLine(person.id.ToString() + " (" + person.name + " " + person.surname + ")");
        }
        Console.WriteLine("Wpisz id osoby (po jednym na linii), wpisz 'q' aby zakończyć:");

        HashSet<int> setIds = new HashSet<int>(ids);
        List<Person> selectedPeople = new List<Person>();
        string input;

        while (true)
        {
            input = Console.ReadLine();
            if(input == "q")
            {
                break;
            }
            else
            {
                if (int.TryParse(input, out int personId) && setIds.Contains(personId))
                {
                    //Console.WriteLine("Id: " + personId.ToString());
                    Person selectedPerson = lookUpId(people, personId);
                    selectedPeople.Add(selectedPerson);
                }
                else
                {
                    Console.WriteLine("Podano nieprawidłowe id osoby, dostępne id to:");
                    foreach (Person person in people)
                    {
                        Console.WriteLine(person.id.ToString() + " (" + person.name + " " + person.surname + ")");
                    }
                }
            }
        }

        return selectedPeople.Distinct().ToList();
    }

    /// <summary>
    /// Retrieves a list of classes attended by a person with the specified ID.
    /// </summary>
    /// <param name="id">The ID of the person.</param>
    /// <returns>A list of classes attended by the person.</returns>

    public static List<Class> personsClasses(int id) //returns a list of classes attended by person with the given id
    {
        List<Class> classes = Class.getClasses(Program.fileClasses);
        List<Class> attendedClasses = new List<Class>();
        foreach(Class c in classes)
        {
            if(lookUpId(c.participants,id) != null) //person with th egiven id is in the classs
            {
                attendedClasses.Add(c);
            }
        }
        return attendedClasses;

    }

    /// <summary>
    /// Prompts the user to purchase a one-entry pass.
    /// </summary>
    /// <param name="id">The ID of the person.</param>
    /// <param name="canUseReduced">Whether the person can use a reduced price pass.</param>
    static void userOneEntry(int id, bool canUseReduced)
    {
        double checkout = 0.0;
        Console.WriteLine("I will check if we have any one-entry passes available for you...");
        Thread.Sleep(3000);
        List<Pass> oneEntryPasses = Pass.getOneEntryPasses(canUseReduced);
        if(oneEntryPasses.Count == 0)
        {
            Console.WriteLine("Unfortunarely there are no available entry passes. Press anything to exit");
            Console.ReadLine();
            return;
        }
        else
        {
            int i = 0;
            foreach(Pass c in oneEntryPasses)
            {
                Console.WriteLine( i+1 + " Pass: " + c.price);
                i++;
            }

            Console.WriteLine("Enter the passes number (ex. 1) to purchase a pass: ");
            while(true)
            {
                string whichpass = Console.ReadLine();
                try
                {
                    int n = int.Parse(whichpass);
                    if(n < 1 || n > oneEntryPasses.Count)
                    {
                        Console.WriteLine("Incorrect number. Please enter the passes number (ex. 1) to purchase a pass: ");
                    }
                    else
                    {
                        checkout += oneEntryPasses[n-1].price;
                        break;
                    }
                }
                catch
                {
                    Console.WriteLine("Incorrect format. Please enter the passes number (ex. 1) to purchase a pass: ");
                }
            }
        }

        checkout += userBuyItem();
        checkout = Math.Round(checkout, 2);
        Console.WriteLine("That would be " + checkout.ToString());
    }

    /// <summary>
    /// Prompts the user to buy an item.
    /// </summary>
    /// <returns>The total price of the purchased items.</returns>
    public static double userBuyItem()
    {
        Console.WriteLine("Do you want to buy an item? Enter 'y' if yes, else press any key.");
        if (Console.ReadLine() != "y")
        {
            return 0.0;
        }

        List<Item> items = Item.getItems(Program.fileItems);
        double totalPrice = 0.0;

        Console.WriteLine("Available items:");
        for (int i = 0; i < items.Count; i++)
        {
            Item item = items[i];
            Console.WriteLine($"{i + 1}. {item.name} - {item.price}");
        }

        Console.WriteLine("Enter the numbers of items you want to purchase (ex. 1 3 4): ");
        string input = Console.ReadLine();
        string[] selectedItems = input.Split(' ');

        foreach (string selectedItem in selectedItems)
        {
            if (int.TryParse(selectedItem, out int itemIndex) && itemIndex >= 1 && itemIndex <= items.Count)
            {
                Item selected = items[itemIndex - 1];
                totalPrice += selected.price;
                Console.WriteLine($"Added {selected.name}.");
            }
            else
            {
                Console.WriteLine($"Invalid item number: {selectedItem}");
            }
        }
        totalPrice = Math.Round(totalPrice, 2);
        return totalPrice;
    }

    /// <summary>
    /// Retrieves information from the user, checks if a person can attend a class or use a single-entry pass.
    /// </summary>

    public static void userGetInfo()
    {
        int id;
        double itemsprice = 0.0;
        double checkout = 0.0; //price at checkout

        while(true)
        {
            Console.WriteLine("Please enter your id: ");
            {
                id = int.Parse(Console.ReadLine());
                if(id > Program.peopleCount)
                {
                    Console.WriteLine("Entered id is incorrect (it should be less than " + Program.peopleCount +" )");
                }
                else
                {
                    break;
                }
            }
        }

        bool canUseReduced = false;
        Person person = lookUpId(getPeople(Program.filePeople),id);
        if(person.age < 18)
        {
            canUseReduced = true;
        }
        
        Console.WriteLine("Hello! Do you want to attend a class? Enter 'y' if yes (else press any key).");
        string answer = Console.ReadLine();
        if(answer == "y")
        {
            List<Class> classes = personsClasses(id);
            if(classes.Count == 0)
            {
                Console.WriteLine("Unfortunately you are not signed to any class.");
                userOneEntry(id,canUseReduced);
                return;

            }
            else
            {
                Console.WriteLine("You are signed to the following classes:");
                int i = 0;
                foreach(Class c in classes)
                {
                    Console.WriteLine( i+1 + " Class with " + c.coach.name + " " + c.coach.surname + " on " + c.day + " at " + c.hour);
                    i++;
                }
                List<Class> todaysClasses = Class.getTodaysClasses(classes);
                Console.WriteLine("However, on the current day of the week you can only attend " + todaysClasses.Count.ToString() + " classes");
                if(todaysClasses.Count == 0)
                {
                    Person.userOneEntry(id, canUseReduced);
                    return;
                }
                i = 0;
                foreach(Class c in todaysClasses)
                {
                    Console.WriteLine( i+1 + " Class with " + c.coach.name + " " + c.coach.surname + " at " + c.hour);
                    i++;
                }


                Console.WriteLine("Which class do you want to attend today? Enter the number (ex. 1)");
                while(true)
                {
                    string whichclass = Console.ReadLine();
                    try
                    {
                        int n = int.Parse(whichclass);
                        if(n < 1 || n > todaysClasses.Count)
                        {
                            Console.WriteLine("Incorrect number. Please enter the passes number (ex. 1) to purchase a pass: ");
                        }
                        else
                        {
                            checkout += Pass.BuyClassPass();
                            itemsprice = userBuyItem();
                            break;
                        }
                    }
                    catch
                    {
                        Console.WriteLine("Incorrect format. Please enter the passes number (ex. 1) to purchase a pass: ");
                    }
                }

            }
        }
        else
        {
            userOneEntry(id, canUseReduced);
            return;
        }
        
        double total = checkout + itemsprice;
        Math.Round(total, 2);
        
        Console.WriteLine("That would be " + (total).ToString());

    }
}