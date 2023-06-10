public class Person
{
    public int id;
    public string name;
    public string surname;

    public BrithDate bithdate;
    public int age;
    public List<Pass>passes = new List<Pass>();

    public Person(int id, string name, string surname, BrithDate birthdate)
    {
        this.id = id;
        this.name = string.Empty;
        this.surname = string.Empty;
        this.bithdate = birthdate;
        this.age = birthdate.GetAge();
    }
}