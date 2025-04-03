using System;
using System.Threading;

namespace Singleton
{
    //One instance for the whole process
    public class ProcessSingleton
    {
        private static ProcessSingleton _instance;
        private static object _lock = new object();
        public static ProcessSingleton Instance(){
            if(_instance == null)
            {
                lock(_lock)
                {
                    if(_instance == null)
                    {
                        _instance = new ProcessSingleton();
                    }
                }
            }
            return _instance;
            
        }
    }

    //Each thread has a different instance
    public class ThreadSingleton
    {
        private static readonly ThreadLocal<ThreadSingleton> _instance = new ThreadLocal<ThreadSingleton>(() => new ThreadSingleton());
        private ThreadSingleton() { }
        public static ThreadSingleton Instance => _instance.Value;
    }

    //New instance can be created every 5 seconds

    public class TimeLimitedSingleton
    {
        private static TimeLimitedSingleton _instance;
        private static DateTime _createdAt;
        private static readonly object _lock = new object();

        private TimeLimitedSingleton() // private constructor
        {
            _createdAt = DateTime.Now;
        }
        public static TimeLimitedSingleton Instance //getter
        {
            get
            {
                lock (_lock)
                {
                    if (_instance == null || DateTime.Now - _createdAt > TimeSpan.FromSeconds(5))
                    {
                        _instance = new TimeLimitedSingleton();
                    }

                    return _instance;
                }
            }
        }
    }

}
