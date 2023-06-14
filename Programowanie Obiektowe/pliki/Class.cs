using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Text.Json.Serialization;

/// <summary>
/// Class representing a class.
/// </summary>
public class Class
{
    public Coach coach { get; set; }
    
    [JsonInclude]
    public List<Person> participants { get; set; }
    public DayOfWeek day { get; set; }
    public Hour hour { get; set; }

    /// <summary>
    /// Initializes a new instance of the <see cref="Class"/> class.
    /// </summary>
    /// <param name="coach">The coach of the class.</param>
    /// <param name="participants">The list of participants.</param>
    /// <param name="day">The day of the class.</param>
    /// <param name="hour">The hour of the class.</param>
    public Class(Coach coach, List<Person> participants, DayOfWeek day, Hour hour)
    {
        this.coach = coach;
        this.participants = participants;
        this.day = day;
        this.hour = hour;
    }

    /// <summary>
    /// Saves the class to a file.
    /// </summary>
    /// <param name="fileName">The name of the file.</param>
    public void SaveToFile(string fileName)
    {
        JsonSerializerOptions options = new JsonSerializerOptions
        {
            IncludeFields = true
        };

        string jsonString = JsonSerializer.Serialize(this, options);

        using (StreamWriter writer = new StreamWriter(fileName, true))
        {
            writer.WriteLine(jsonString);
        }
    }

    /// <summary>
    /// Gets a list of classes from a file.
    /// </summary>
    /// <param name="fileName">The name of the file.</param>
    /// <returns>The list of classes.</returns>
    public static List<Class> getClasses(string fileName)
    {
        List<Class> classes = new List<Class>();
        string fileContent = File.ReadAllText(fileName);
        string[] tab = fileContent.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string ClassJson in tab)
        {
            Class Class = JsonSerializer.Deserialize<Class>(ClassJson);
            classes.Add(Class);
        }
        return classes;
    }

    /// <summary>
    /// Prompts the user to enter the day of the week.
    /// </summary>
    /// <returns>The selected day of the week.</returns>
    public static DayOfWeek userGetDayOfWeek()
    {
        while (true)
        {
            Console.WriteLine("Enter the day of the week (e.g., Monday, Tuesday, etc.):");
            string input = Console.ReadLine();

            if (Enum.TryParse(input, out DayOfWeek dayOfWeek))
            {
                return dayOfWeek;
            }

            Console.WriteLine("Invalid input. Please enter a valid day of the week.");
        }
    }

    /// <summary>
    /// Gets the classes for the current day.
    /// </summary>
    /// <param name="classes">The list of all classes.</param>
    /// <returns>The classes for the current day.</returns>
    public static List<Class> getTodaysClasses(List<Class> classes)
    {
        List<Class> result = new List<Class>();

        foreach (Class c in classes)
        {
            if (c.day == DateTime.Now.DayOfWeek)
            {
                result.Add(c);
            }

        }
        return result;
    }

    /// <summary>
    /// Prompts the user to enter class details and creates a new class.
    /// </summary>
    /// <returns>The new class.</returns>
    public static Class userGetClass()
    {
        Console.WriteLine("Enter class details:");

        Console.WriteLine("Enter coach details:");
        Coach coach = Coach.userGetCoach();
        Console.WriteLine();

        Console.WriteLine("Enter participant details:");
        List<Person> participants = Person.userGetParticipants();
        Console.WriteLine();

        DayOfWeek day = userGetDayOfWeek();
        Console.WriteLine();

        Console.WriteLine("Enter the class hour:");
        Hour hour = Hour.UserGetHour();
        Console.WriteLine();

        Class newClass = new Class(coach, participants, day, hour);
        return newClass;
    }

    /// <summary>
    /// Saves a class entered by the user.
    /// </summary>
    public static void SaveClass()
    {
        Class class_ = userGetClass();
        class_.SaveToFile(Program.fileClasses);
        Console.WriteLine("Class successfully added.");
    }
}
