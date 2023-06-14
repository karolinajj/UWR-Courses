using System;
using System.IO;
using System.Text.Json;
using System.Text.Json.Serialization;

/// <summary>
/// Class representing an item.
/// </summary>
public class Item
{
    /// <summary>
    /// Name of the item.
    /// </summary>
    public string name { get; set; }

    /// <summary>
    /// Price of the item.
    /// </summary>
    public double price { get; set; }

    /// <summary>
    /// Checks the validity of the price format.
    /// </summary>
    /// <param name="sprice">Price as text.</param>
    /// <returns>True if the price is in the correct format; otherwise, false.</returns>
    static public bool isCorrect(string sprice)
    {
        bool dot = false;
        foreach (char c in sprice)
        {
            if ((!char.IsDigit(c) && c != ',') || (c == ',' && dot == true))
            {
                throw new ArgumentOutOfRangeException("Incorrect format! Use only numbers and a comma.");
            }
            if (c == ',') dot = true;
        }

        double price = Math.Round(Double.Parse(sprice), 2);

        if (price <= 0.0)
        {
            throw new ArgumentOutOfRangeException("Price must be greater than zero.");
        }
        return true;
    }

    /// <summary>
    /// Initializes a new instance of the Item class.
    /// </summary>
    /// <param name="name">Name of the item.</param>
    /// <param name="price">Price of the item.</param>
    public Item(string name, double price)
    {
        this.name = name;
        if (isCorrect(price.ToString())) this.price = price;
    }

    /// <summary>
    /// Saves the item to a file.
    /// </summary>
    /// <param name="fileName">File name.</param>
    public void SaveToFile(string fileName)
    {
        string jsonString = JsonSerializer.Serialize(this);

        using (StreamWriter writer = new StreamWriter(fileName, true))
        {
            writer.WriteLine(jsonString);
        }
    }

    /// <summary>
    /// Saves a collection of items to a file.
    /// </summary>
    /// <param name="fileName">File name.</param>
    public static void SaveItems(string fileName)
    {
        Console.WriteLine("How many items do you want to add to the database?");
        int n = 0;
        while (true)
        {
            string input = Console.ReadLine();
            n = int.Parse(input);
            if (n > 0) break;
            else
            {
                Console.WriteLine("Error! Please enter a positive number.");
            }
        }

        for (int i = 0; i < n; i++)
        {
            Console.WriteLine("Enter item's name: ");
            string name = Console.ReadLine();

            bool error = true;
            while (error)
            {
                Console.WriteLine("Enter item's price (e.g., 9.99): ");
                string sprice = Console.ReadLine();
                try
                {
                    Item.isCorrect(sprice);
                    Item item = new Item(name, Double.Parse(sprice));
                    item.SaveToFile(fileName);
                    Console.WriteLine("Item successfully added.");
                    error = false;

                }
                catch (ArgumentOutOfRangeException e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }

    /// <summary>
    /// Retrieves a collection of items from a file.
    /// </summary>
    /// <param name="fileName">File name.</param>
    /// <returns>Collection of items.</returns>
    public static List<Item> getItems(string fileName)
    {
        List<Item> items = new List<Item>();
        string fileContent = File.ReadAllText(fileName);
        string[] tab = fileContent.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string itemJson in tab)
        {
            Item item = JsonSerializer.Deserialize<Item>(itemJson);
            items.Add(item);
        }
        return items;
    }
}
