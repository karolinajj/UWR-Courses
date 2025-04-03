using System;
using System.Collections.Generic;
using System.Linq;
public class ObjectPool
{
    int _capacity;
    List<Reusable> _pool = new List<Reusable>(); //realeased - objects that are not currently in use
    List<Reusable> _acquired = new List<Reusable>(); //reused - currently in use
    public ObjectPool(int capacity)
    {
        if (capacity <= 0)
        {
            throw new ArgumentException();
        }
        this._capacity = capacity;
    }
    public Reusable AcqureReusable()
    {
        if (_acquired.Count() >= this._capacity) //max capacity
        {
            throw new ArgumentException();
        }
        if (_pool.Count() == 0) //creating an element if pool is empty
        {
            var reusable = new Reusable();
            _pool.Add(reusable);
        }
        var element = _pool[0];
        _pool.Remove(element);
        _acquired.Add(element);
        return element;
    }
    public void ReleaseReusable(Reusable reusable)
    {
        if (!_acquired.Contains(reusable))
        {
            throw new ArgumentException();
        }
        _acquired.Remove(reusable);
        _pool.Add(reusable);
    }
}

public class BetterReusable
{
    private static readonly ObjectPool _pool = new ObjectPool(10); //all BetterReusable objects use the same pool
    
    private Reusable _reusable;
    private bool _released; //if an object was released

    public BetterReusable()
    {
        _reusable = _pool.AcqureReusable();
        _released = false;
    }

    public void Release()
    {
        if (_released)
        {
            throw new InvalidOperationException("Resource has already been released.");
        }
        _pool.ReleaseReusable(_reusable);
        _released = true;
    }
    public void DoWork()
    {
        if (_released)
        {
            throw new InvalidOperationException("Operation on a released resource is not allowed.");
        }
        _reusable.DoWork();
    }
}

public partial class Reusable
{
    public void DoWork()
    {
        Console.WriteLine("I am working...");
    }
}