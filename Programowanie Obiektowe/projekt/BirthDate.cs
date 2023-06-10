using System;
public class BrithDate
{
    public int day;
    public int month;
    public int year;

    public BrithDate(int day, int month, int year)
    {
        DateTime tmp = new DateTime(year,month,day);
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public int GetAge()
    {
        int currentYear = DateTime.Now.Year;
        int currentMonth = DateTime.Now.Month;
        int currentDay = DateTime.Now.Day;

        int result = currentYear - this.year; //year of age
        if((currentMonth < month) || (currentMonth == month && currentDay < day))
        {
            result--; //did not have birthday yet
        }
        return result;
    }
}