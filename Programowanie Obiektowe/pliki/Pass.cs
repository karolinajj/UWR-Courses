using System;
using System.IO;
using System.Text.Json;

/// <summary>
/// Class representing a pass.
/// </summary>
public class Pass : Item
{
    /// <summary>
    /// Gets or sets a value indicating whether the pass is for a class.
    /// </summary>
    public bool isForClass { get; set; }

    /// <summary>
    /// Gets or sets a value indicating whether the pass is reduced.
    /// </summary>
    public bool isReduced { get; set; }

    /// <summary>
    /// Initializes a new instance of the Pass class with the specified name, price, and pass type.
    /// </summary>
    /// <param name="name">The name of the pass.</param>
    /// <param name="price">The price of the pass.</param>
    /// <param name="isForClass">A value indicating whether the pass is for a class.</param>
    /// <param name="isReduced">A value indicating whether the pass is reduced.</param>
    public Pass(string name, double price, bool isForClass, bool isReduced = false) : base(name, price)
    {
        this.isForClass = isForClass;
        this.isReduced = isReduced;
    }

    /// <summary>
    /// Saves the pass to a file in JSON format.
    /// </summary>
    /// <param name="fileName">The name of the file.</param>
    public new void SaveToFile(string fileName)
    {
        string jsonString = JsonSerializer.Serialize(this);

        using (StreamWriter writer = new StreamWriter(fileName, true))
        {
            writer.WriteLine(jsonString);
        }
    }

    /// <summary>
    /// Retrieves one-entry passes from the file, filtered by whether reduced passes can be used.
    /// </summary>
    /// <param name="canUseReduced">A value indicating whether reduced passes can be used.</param>
    /// <returns>A list of one-entry passes.</returns>
    public new static List<Pass> getOneEntryPasses(bool canUseReduced)
    {
        List<Pass> passes = Pass.getItems(Program.filePasses);
        List<Pass> result = new List<Pass>();
        foreach (Pass pass in passes)
        {
            if (pass.isForClass == true || (pass.isReduced == true && canUseReduced == false))
            {
                continue;
            }
            else
            {
                result.Add(pass);
            }
        }
        return result;
    }

    /// <summary>
    /// Returns the price of the cheapest class pass.
    /// </summary>
    /// <returns>The price of the cheapest class pass.</returns>
    public new static double BuyClassPass()
    {
        List<Pass> passes = Pass.getItems(Program.filePasses);
        double result = 0.0;
        if (passes.Count > 0)
        {
            result = passes[0].price;
        }
        else
        {
            return 0.0;
        }

        foreach (Pass pass in passes)
        {
            if (pass.isForClass == true)
            {
                result = Math.Min(pass.price, result);
            }
        }
        return result;
    }

    /// <summary>
    /// Prompts the user to enter passes and saves them to a file.
    /// </summary>
    /// <param name="fileName">The name of the file.</param>
    public new static void SaveItems(string fileName)
    {
        Console.WriteLine("How many passes do you want to add to the database?");
        int n = 0;
        bool isReduced = false;
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
            string name = "Pass";

            bool error = true;
            while (error)
            {
                Console.WriteLine("Enter item's price (e.g., 9,99): ");
                string sprice = Console.ReadLine();
                try
                {
                    Console.WriteLine("If it's a class-pass, please type 1 (otherwise, a one-entry pass will be created):");
                    bool tmp = false;
                    if (Console.ReadLine() == "1")
                    {
                        tmp = true;
                    }
                    else
                    {
                        Console.WriteLine("Do you want this pass to be a reduced one (only for kids)? If yes, enter 'y'; otherwise, it will not be reduced:");
                        string answer = Console.ReadLine();
                        if (answer == "y")
                        {
                            isReduced = true;
                        }

                    }

                    Item.isCorrect(sprice);
                    Pass pass = new Pass(name, Double.Parse(sprice), tmp, isReduced);
                    pass.SaveToFile(fileName);
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
    /// Retrieves passes from the file.
    /// </summary>
    /// <param name="fileName">The name of the file.</param>
    /// <returns>A list of passes.</returns>
    public new static List<Pass> getItems(string fileName)
    {
        List<Pass> items = new List<Pass>();
        string fileContent = File.ReadAllText(fileName);
        string[] tab = fileContent.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string itemJson in tab)
        {
            Pass item = JsonSerializer.Deserialize<Pass>(itemJson);
            items.Add(item);
        }
        return items;
    }
}
