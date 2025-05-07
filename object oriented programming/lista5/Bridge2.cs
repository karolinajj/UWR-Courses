// PersonRegistry is only getting a list of people
// IPersonNotifier hendles the notifications
public class Person
{
    public string Name { get; set; }
    public string Contact { get; set; }
    public override string ToString() => $"{Name} ({Contact})";
}
public interface IPersonNotifier
{
    void Notify(Person person);
}
public class EmailNotifier : IPersonNotifier
{
    public void Notify(Person person)
    {
        Console.WriteLine($"email sent to {person.Name}, {person.Contact}");
    }
}

public class SmsNotifier : IPersonNotifier
{
    public void Notify(Person person)
    {
        Console.WriteLine($"SMS sent to {person.Name}, {person.Contact}");
    }
}

public abstract class PersonRegistry 
{
    protected IPersonNotifier _notifier;

    protected PersonRegistry(IPersonNotifier notifier)
    {
        _notifier = notifier;
    }

    public abstract List<Person> GetPersons();

    public void NotifyPersons()
    {
        foreach (var person in GetPersons())
        {
            _notifier.Notify(person);
        }
    }
}

public class XmlPersonRegistry : PersonRegistry
{
    public XmlPersonRegistry(IPersonNotifier notifier) : base(notifier) { }

    public override List<Person> GetPersons()
    {
        return new List<Person>
        {
            new Person { Name = "A", Contact = "a@example.com" },
            new Person { Name = "B", Contact = "b@example.com" }
        };
    }
}

public class DbPersonRegistry : PersonRegistry
{
    public DbPersonRegistry(IPersonNotifier notifier) : base(notifier) { }

    public override List<Person> GetPersons()
    {
        return new List<Person>
        {
            new Person { Name = "C", Contact = "c@ex.com" },
            new Person { Name = "D", Contact = "d@ex.com" }
        };
    }
}