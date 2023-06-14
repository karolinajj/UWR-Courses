using System;

/// <summary>
/// Class representing a day of birth.
/// </summary>
public class BirthDate
{
    /// <summary>
    /// Gets or sets the day of the birth date.
    /// </summary>
    public int day { get; set; }

    /// <summary>
    /// Gets or sets the month of the birth date.
    /// </summary>
    public int month { get; set; }

    /// <summary>
    /// Gets or sets the year of the birth date.
    /// </summary>
    public int year { get; set; }

    /// <summary>
    /// Initializes a new instance of the BirthDate class with the specified day, month, and year.
    /// </summary>
    /// <param name="day">The day of the birth date.</param>
    /// <param name="month">The month of the birth date.</param>
    /// <param name="year">The year of the birth date.</param>
    public BirthDate(int day, int month, int year)
    {
        DateTime tmp = new DateTime(year, month, day);

        this.day = day;
        this.month = month;
        this.year = year;
    }

    /// <summary>
    /// Calculates and returns the age based on the birth date and the current date.
    /// </summary>
    /// <returns>The age in years.</returns>
    public int GetAge()
    {
        int currentYear = DateTime.Now.Year;
        int currentMonth = DateTime.Now.Month;
        int currentDay = DateTime.Now.Day;

        int result = currentYear - this.year; // year of age
        if ((currentMonth < month) || (currentMonth == month && currentDay < day))
        {
            result--; // did not have birthday yet
        }
        return result;
    }

    /// <summary>
    /// Returns a string representation of the BirthDate object in the format "dd.mm.yyyy".
    /// </summary>
    /// <returns>A string representation of the BirthDate object.</returns>
    public override string ToString()
    {
        string sday = this.day < 10 ? "0" + this.day.ToString() : this.day.ToString();
        string smonth = this.month < 10 ? "0" + this.month.ToString() : this.month.ToString();

        return sday + "." + smonth + "." + year.ToString();
    }

    /// <summary>
    /// Prompts the user to enter a birth date and returns the corresponding BirthDate object.
    /// </summary>
    /// <returns>The BirthDate object based on user input.</returns>
    public static BirthDate userGetBirthDate()
    {
        while (true)
        {
            Console.WriteLine("Enter day of birth (e.g., 07): ");
            int day = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter month of birth (e.g., 07): ");
            int month = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter year of birth (e.g., 2007): ");
            int year = int.Parse(Console.ReadLine());

            try
            {
                BirthDate result = new BirthDate(day, month, year);
                return result;
            }
            catch
            {
                Console.WriteLine("Error: wrong date format!");
            }
        }
    }
}
