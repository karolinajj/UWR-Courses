public class Pass : Item
{
    bool isMonthly;
    int entries;

    public Pass(string name, int price, bool isMonthly, int entries=4) : base(name,price)
    {
        this.isMonthly = isMonthly;
        this.entries = entries;
    }
}