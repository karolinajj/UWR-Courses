using System;
using System.Collections.Generic;
public class Classes
{
    public Coach coach;
    List<Person> participants;

    Classes(Coach coach, List<Person> participants)
    {
        this.coach = coach;
        this.participants = participants;
    }
}