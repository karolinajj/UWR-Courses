using System.Threading;
using NUnit.Framework;
using Singleton;
using System;


namespace UnitTestProject
{
    [TestFixture]
    public class SingletonTests
    {
        [Test]
        public void ProcessSingletonTest1()
        {
            ProcessSingleton ps1 = ProcessSingleton.Instance();
            ProcessSingleton ps2 = ProcessSingleton.Instance();
            Assert.AreEqual(ps1,ps2, "Instances should be the same.");
        }

        [Test]
        public void ProcessSingletonTest2()
        {
            ProcessSingleton instance1 = null;
            ProcessSingleton instance2 = null;

            var thread1 = new Thread(() =>
            {
                instance1 = ProcessSingleton.Instance();
            });

            var thread2 = new Thread(() =>
            {
                instance2 = ProcessSingleton.Instance();
            });

            thread1.Start();
            thread2.Start();
            thread1.Join();
            thread2.Join();
            Assert.AreEqual(instance1, instance2, "Threads should have the sameinstances.");
        }

        [Test]
        public void ThreadSingletonTest()
        {
            ThreadSingleton instance1 = null;
            ThreadSingleton instance2 = null;

            var thread1 = new Thread(() =>
            {
                instance1 = ThreadSingleton.Instance;
            });

            var thread2 = new Thread(() =>
            {
                instance2 = ThreadSingleton.Instance;
            });

            thread1.Start();
            thread2.Start();
            thread1.Join();
            thread2.Join();
            Assert.AreNotEqual(instance1, instance2, "Threads should have different instances.");
        }

        [Test]
        public void TimeLimitedSingletonTest1()
        {
            var instance1 = TimeLimitedSingleton.Instance;
            Thread.Sleep(6000);
            var instance2 = TimeLimitedSingleton.Instance;

            Assert.AreNotEqual(instance1, instance2, "Instances should be different.");
        }

        [Test]
        public void TimeLimitedSingletonTest2()
        {
            var instance1 = TimeLimitedSingleton.Instance;
            var instance2 = TimeLimitedSingleton.Instance;

            Assert.AreEqual(instance1, instance2, "Instances should be the same.");
        }
    
    }
}
