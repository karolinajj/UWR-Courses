using System.Text.Json;
using System.Text.Json.Serialization;

/// <summary>
/// Class representing a coach.
/// </summary>
public class Coach : Person
{
    /// <summary>
    /// Gets or sets the type of the coach.
    /// 0 - bouldering
    /// 1 - rope climbing
    /// 2 - both
    /// </summary>
    public int type { get; set; } //0-bouldering, 1-rope climbing 2-both

    /// <summary>
    /// Initializes a new instance of the <see cref="Coach"/> class.
    /// </summary>
    /// <param name="id">The coach's ID.</param>
    /// <param name="name">The coach's name.</param>
    /// <param name="surname">The coach's surname.</param>
    /// <param name="birthdate">The coach's birthdate.</param>
    /// <param name="type">The type of the coach.</param>
    public Coach(int id, string name, string surname, BirthDate birthdate, int type) 
    : base(id,name,surname,birthdate) //from class Person
    {
        this.type = type;
    }

    /// <summary>
    /// Saves the coach information to a file in JSON format.
    /// </summary>
    /// <param name="fileName">The name of the file to save to.</param>
    new public void SaveToFile(string fileName)
    {
        string jsonString = JsonSerializer.Serialize(this);

        using (StreamWriter writer = new StreamWriter(fileName, true))
        {
            writer.WriteLine(jsonString);
        }
    }

    /// <summary>
    /// Adds coaches to the database and saves their information to a file.
    /// </summary>
    /// <param name="id">The starting ID for the coaches.</param>
    /// <param name="fileName">The name of the file to save to.</param>
    new public static void SavePeople(int id, string fileName)
    {
        Console.WriteLine("How many coaches do you want to add to the database?");
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

            Console.WriteLine("Enter: 0 (if this coach teaches only bouldering)" + "\n" + "1 (if this coach teaches only rope climing)" + "\n" +"2 (if this coach teaches both)");
            int type = int.Parse(Console.ReadLine());

            Coach coach = new Coach(id + i, name, surname, birthdate,type);

            coach.SaveToFile(fileName);
            
            Console.WriteLine("Coach successfully added.");
        }
    }

    /// <summary>
    /// Gets a list of coaches from the specified file.
    /// </summary>
    /// <param name="fileName">The name of the file to read from.</param>
    /// <returns>A list of coaches.</returns>
    new public static List<Coach> getPeople(string fileName)
    {
        List<Coach> people = new List<Coach>();
        string fileContent = File.ReadAllText(fileName);
        string[] tab = fileContent.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string personJson in tab)
        {
            Coach person = JsonSerializer.Deserialize<Coach>(personJson);
            people.Add(person);
        }
        return people;
    }

    
    /// <summary>
    /// Gets a list of coach IDs.
    /// </summary>
    /// <returns>A list of coach IDs.</returns>
    public static List<int> coachIds()
    {
        List<Coach> coaches = getPeople(Program.fileCoaches);
        List<int> ids = new List<int>();

        foreach (Coach coach in coaches)
        {
            ids.Add(coach.id);
        }
        ids.Sort();
        
        return ids;
    }

    /// <summary>
    /// Looks up a coach by ID in the specified list of coaches.
    /// </summary>
    /// <param name="coaches">The list of coaches to search in.</param>
    /// <param name="id">The ID of the coach to look up.</param>
    /// <returns>The coach with the specified ID, or the first coach if not found.</returns>
    static Coach lookUpId(List<Coach> coaches, int id)
    {   
        foreach(Coach coach in coaches)
        {
            if(coach.id == id)
            {
                return coach;
            }
        }
        return coaches[0];
    }

    /// <summary>
    /// Prompts the user to enter a coach's ID and returns the corresponding coach object.
    /// </summary>
    /// <returns>The selected coach.</returns>
    public static Coach userGetCoach()
    {
        Console.WriteLine("Enter coaches id, aviable ids: ");
        List<int>ids = Coach.coachIds();
        List<Coach> coaches = getPeople(Program.fileCoaches);

        foreach (Coach coach in coaches)
        {
            Console.WriteLine( coach.id.ToString() + " (" + coach.name + " " + coach.surname + ")");
        }
        Console.WriteLine("Enter id: ");

        HashSet<int> setIds = new HashSet<int>(ids);
        int coachid;
        
        while(true)
        {
            if(int.TryParse(Console.ReadLine(),out coachid) == true && setIds.Contains(coachid))
            {
                break;
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter one of the following ids:");

                foreach (Coach coach in coaches)
                {
                    Console.WriteLine( coach.id.ToString() + " (" + coach.name + " " + coach.surname + ")");
                    

                }
                Console.WriteLine("Enter id: ");
            }
        }
        return lookUpId(coaches, coachid);
    }

}