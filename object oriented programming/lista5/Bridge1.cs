//PersonRegistry is responsible for getting a list of people and sending notifications
// If we wanted to add a new notification type or data source 
// we would have to modify the class.
public class Person
{
    public string Name { get; set; }
    public string Contact { get; set; }
    public override string ToString() => $"{Name} ({Contact})";
}
public interface IPersonSource
{
    List<Person> GetPersons();
}
public class XmlPersonSource : IPersonSource
{
    public List<Person> GetPersons() =>
        new List<Person> {
            new Person { Name = "A", Contact = "a@example.com" },
            new Person { Name = "B", Contact = "B@example.com" }
        };
}
public class DbPersonSource : IPersonSource
{
    public List<Person> GetPersons() =>
        new List<Person> {
            new Person { Name = "C", Contact = "c@ex.com" },
            new Person { Name = "D", Contact = "d@ex.com" }
        };
}
//PersonRegistry is responsible for getting a list of people and sending notifications
public abstract class PersonRegistry 
{
    protected IPersonSource _source;
    protected PersonRegistry(IPersonSource source){
        _source = source;
    }
    public abstract void NotifyPersons();
}

public class EmailRegistry : PersonRegistry
{
    public EmailRegistry(IPersonSource source) : base(source) { }
    public override void NotifyPersons()
    {
        foreach (var person in _source.GetPersons())
        {
            Console.WriteLine($"email sent to {person.Name}, {person.Contact}");
        }
    }
}

public class SmsRegistry : PersonRegistry
{
    public SmsRegistry(IPersonSource source) : base(source) { }

    public override void NotifyPersons()
    {
        foreach (var person in _source.GetPersons())
        {
            Console.WriteLine($"sms sent to {person.Name}, {person.Contact}");
        }
    }
}
