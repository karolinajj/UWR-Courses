using System.Threading;
using NUnit.Framework;
using Singleton;
using System;

    
namespace UnitTestProject
{    
    [TestFixture]
    public class ShapeFactoryTests
    {
        [Test]
        public void SquareFactoryWorkerTest1() //should create square
        {
            var squareFactory = new SquareFactoryWorker();
            int sideLength = 5;

            var shape = squareFactory.CreateShape(sideLength);
            Assert.IsInstanceOf<Square>(shape);
        }

        [Test]
        public void SquareFactoryWorkerTest2() //invalid input for square
        {
            var squareFactory = new SquareFactoryWorker();
            Assert.Throws<ArgumentException>(() => squareFactory.CreateShape("invalid"));
            Assert.Throws<ArgumentException>(() => squareFactory.CreateShape(5, 5));
        }

        [Test]
        public void RectangleFactoryWorkerTest1() //creates rectangle
        {
            var rectangleFactory = new RectangleFactoryWorker();
            int width = 4, height = 7;

            var shape = rectangleFactory.CreateShape(width, height);
            Assert.IsInstanceOf<Rectangle>(shape);
        }

        [Test]
        public void RectangleFactoryWorkerTest2() //invalid rectangle
        {
            var rectangleFactory = new RectangleFactoryWorker();
            Assert.Throws<ArgumentException>(() => rectangleFactory.CreateShape(4)); // only 1 parameter
            Assert.Throws<ArgumentException>(() => rectangleFactory.CreateShape("invalid", 7)); // invalid type
        }

        [Test]
        public void ShapeFactoryTest1() // creates a square
        {
            var shapeFactory = new ShapeFactory();
            shapeFactory.RegisterWorker(new SquareFactoryWorker());
            int sideLength = 5;

            var shape = shapeFactory.CreateShape("Square", sideLength);
            Assert.IsInstanceOf<Square>(shape);
        }

        [Test]
        public void ShapeFactoryTest2() // creates a rectangle
        {
            var shapeFactory = new ShapeFactory();
            shapeFactory.RegisterWorker(new RectangleFactoryWorker());
            int width = 4, height = 7;

            var shape = shapeFactory.CreateShape("Rectangle", width, height);
            Assert.IsInstanceOf<Rectangle>(shape);
        }

        //data for the last test
        public class AnotherShape : IShape
        {
            public void Description()
            {
                Console.WriteLine("Another shape's description.");
            }
        }

        public class AnotherShapeFactoryWorker: IShapeFactoryWorker
        {
            public bool CanCreateShape(string shapeName)
            {
                return shapeName.Equals("AnotherShape", StringComparison.OrdinalIgnoreCase);
            }
            public IShape CreateShape(params object[] parameters)
            {
                return new AnotherShape();
            }
        }

        [Test]
        public void ShapeFactoryTest3() // creates a new shape
        {
            var shapeFactory = new ShapeFactory();
            shapeFactory.RegisterWorker(new AnotherShapeFactoryWorker());
            IShape shape = shapeFactory.CreateShape("AnotherShape");
            Assert.IsNotNull(shape);
        }
    }
}
