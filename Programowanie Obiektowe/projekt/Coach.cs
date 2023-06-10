public class Coach : Person
{
    int type; //0-bouldering, 1-rope climbing 2-both

    public Coach(int id, string name, string surname, BrithDate birthdate, int type) 
    : base(id,name,surname,birthdate) //from class Person
    {
        this.type = type;
    }
}