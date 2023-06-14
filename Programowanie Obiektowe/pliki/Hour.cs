using System.Text.Json;
using System.Text.Json.Serialization;

/// <summary>
/// Class representing the time in HH:MM format.
/// </summary>
public class Hour
{
    /// <summary>
    /// Represents the hours.
    /// </summary>
    public int hours { get; set; }

    /// <summary>
    /// Represents the minutes.
    /// </summary>
    public int minutes { get; set; }

    /// <summary>
    /// Checks if the given hours and minutes are in the correct format.
    /// </summary>
    /// <param name="hours">The hours.</param>
    /// <param name="minutes">The minutes.</param>
    /// <returns>True if the format is correct, otherwise False.</returns>
    bool IsCorrect(int hours, int minutes)
    {
        if (hours < 0 || hours > 23 || minutes < 0 || minutes > 59)
        {
            throw new ArgumentOutOfRangeException("Incorrect format! Hours must be between 00:00 and 23:59");
        }
        return true;
    }

    /// <summary>
    /// Initializes a new instance of the Hour class with the specified hours and minutes.
    /// </summary>
    /// <param name="hours">The hours.</param>
    /// <param name="minutes">The minutes.</param>
    public Hour(int hours, int minutes)
    {
        this.hours = hours;
        this.minutes = minutes;
    }

    /// <summary>
    /// Returns a string that represents the current Hour object in HH:MM format.
    /// </summary>
    /// <returns>A string representation of the current Hour object.</returns>
    public override string ToString()
    {
        string zero = this.hours < 10 ? "0" : "";
        return zero + this.hours.ToString() + ":" + this.minutes.ToString("D2");
    }

    /// <summary>
    /// Prompts the user to enter the hour in HH:MM format and returns the corresponding Hour object.
    /// </summary>
    /// <returns>The Hour object based on user input.</returns>
    public static Hour UserGetHour()
    {
        while (true)
        {
            Console.WriteLine("Enter the hour in the HH:MM format");
            string input = Console.ReadLine();

            try
            {
                int hours = int.Parse(input.Substring(0, 2));
                int minutes = int.Parse(input.Substring(3, 2));

                Hour hour = new Hour(hours, minutes);
                return hour;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }
    }
}
