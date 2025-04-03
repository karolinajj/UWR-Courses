using NUnit.Framework;
using System;

namespace UnitTestProject
{
    [TestFixture]
    public class ObjectPoolTests
    {
        [Test]
        public void InvalidSize()
        {
            Assert.Throws<ArgumentException>(
            () =>
            {
                var pool = new ObjectPool(0);
            });
        }
        [Test]
        public void ValidSize()
        {
            var pool = new ObjectPool(1);
            var reusable = pool.AcqureReusable();
            Assert.IsNotNull(reusable);
        }
        [Test]
        public void CapacityDepleted()
        {
            var pool = new ObjectPool(1);
            var reusable = pool.AcqureReusable();
            Assert.Throws<ArgumentException>(
            () =>
            {
                var reusable2 = pool.AcqureReusable();
            });
        }
        [Test]
        public void ReusedInstance()
        {
            var pool = new ObjectPool(1);
            var reusable = pool.AcqureReusable();
            pool.ReleaseReusable(reusable);
            var reusable2 = pool.AcqureReusable();
            Assert.That(reusable2, Is.EqualTo(reusable));
        }
        [Test]
        public void ReleaseInvalidInstance()
        {
            var pool = new ObjectPool(1);
            var reusable = new Reusable();
            Assert.Throws<ArgumentException>(
            () =>
            {
                pool.ReleaseReusable(reusable);
            });
        }
    }

    
    [TestFixture]
    public class ObjectPoolTestsBetter
    {
        [Test]
        public void DoWorkBeforeRelease()
        {
            var betterReusable = new BetterReusable();
            Assert.DoesNotThrow(() => betterReusable.DoWork());
        }

        [Test]
        public void DoWorkAfterReleaseException()
        {
            var betterReusable = new BetterReusable();
            betterReusable.Release();
            Assert.Throws<InvalidOperationException>(() => betterReusable.DoWork());
        }

        [Test]
        public void DoubleReleaseException()
        {
            var betterReusable = new BetterReusable();
            betterReusable.Release();
            Assert.Throws<InvalidOperationException>(() => betterReusable.Release());
        }
    }
}