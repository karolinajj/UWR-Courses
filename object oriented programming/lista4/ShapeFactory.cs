using System;
using System.Collections.Generic;

public interface IShape
{
    void Description();
}

public class Square : IShape
{
    private int _sideLength;
    public Square(int sideLength)
    {
        _sideLength = sideLength;
    }

    public void Description()
    {
        Console.WriteLine($"A square with side length {_sideLength}");
    }
}

public class Rectangle : IShape
{
    private int _width;
    private int _height;
    public Rectangle(int width, int height)
    {
        _width = width;
        _height = height;
    }

    public void Description()
    {
        Console.WriteLine($"A rectangle with width {_width} and height {_height}");
    }
}

public interface IShapeFactoryWorker // shape factory interface
{
    bool CanCreateShape(string shapeName);
    IShape CreateShape(params object[] parameters);
}

public class SquareFactoryWorker : IShapeFactoryWorker // factory to create squares
{
    public bool CanCreateShape(string shapeName)
    {
        return shapeName.Equals("Square", StringComparison.OrdinalIgnoreCase);
    }

    public IShape CreateShape(params object[] parameters)
    {
        if (parameters.Length != 1 || !(parameters[0] is int sideLength) || sideLength <= 0)
            throw new ArgumentException("Square requires one parameter of type int, greater than 0.");
        
        return new Square(sideLength);
    }
}
public class RectangleFactoryWorker : IShapeFactoryWorker // factory to create rectangles
{
    public bool CanCreateShape(string shapeName)
    {
        return shapeName.Equals("Rectangle", StringComparison.OrdinalIgnoreCase);
    }

    public IShape CreateShape(params object[] parameters)
    {
        //(int(parameters[0]) <= 0)) // why is it not working??
        if (parameters.Length != 2 || !(parameters[0] is int width) || !(parameters[1] is int height) || (width <= 0) || (height <= 0))
            throw new ArgumentException("Rectangle requires two parameters of type int, greater than 0");
        
        return new Rectangle(width, height);
    }
}

public class ShapeFactory // factory to create shapes
{
    private List<IShapeFactoryWorker> _workers = new List<IShapeFactoryWorker>();

    public void RegisterWorker(IShapeFactoryWorker worker)
    {
        _workers.Add(worker);
    }

    public IShape CreateShape(string shapeName, params object[] parameters)
    {
        foreach (var worker in _workers)
        {
            if (worker.CanCreateShape(shapeName))
            {
                return worker.CreateShape(parameters);
            }
        }

        throw new ArgumentException($"No worker registered to create shape '{shapeName}'");
    }
}