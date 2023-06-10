public class Item
{
    public string name;
    public double price;

    bool isCorrect(double price)
    {
        if(price <= 0.0)
        {
            throw new ArgumentOutOfRangeException("Price must be greater than zero");
        }

        double fractionalPart = price % 1.0;
        if(fractionalPart*100 % 1.0 == 0)
        {
            return true;
        }
        else
        {
            throw new ArgumentOutOfRangeException("Incorrect format! To many decimal places (use maximum two).");
        }
        
    }

    public Item(string name, double price)
    {
        this.name = name;
        if(isCorrect(price)) this.price = price;
    }

}