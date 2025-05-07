// The ComparisonComparer<T> class allows a Comparison<T> to be used where an IComparer<T> is expected.

using System;
using System.Collections.Generic;

// adapter to convert Comparison<T> to IComparer<T>
public class ComparisonComparer<T> : IComparer<T>
{
    private readonly Comparison<T> _comparison;
    
    public ComparisonComparer(Comparison<T> comparison)
    {
        _comparison = comparison ?? throw new ArgumentNullException(nameof(comparison));
    }
    
    public int Compare(T x, T y)
    {
        return _comparison(x, y);
    }
}

// adapter to convert IComparer<T> to Comparison<T>
public static class ComparerExtensions
{
    public static Comparison<T> ToComparison<T>(this IComparer<T> comparer)
    {
        if (comparer == null) throw new ArgumentNullException(nameof(comparer));
        return (x, y) => comparer.Compare(x, y);
    }
}

// IComparer<int> comparer = Comparer<int>.Default;
// Comparison<int> comparison = comparer.ToComparison();
// int result = comparison(1, 3);


