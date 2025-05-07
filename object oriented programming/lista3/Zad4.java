public class Zad4 {

    public interface IShape {
        int calculateArea();
    }

    public static class Rectangle implements IShape {
        private int width;
        private int height;

        public Rectangle(int width, int height) {
            this.width = width;
            this.height = height;
        }

        public int getWidth() {
            return width;
        }

        public int getHeight() {
            return height;
        }

        @Override
        public int calculateArea() {
            return width * height;
        }
    }

    public static class Square implements IShape {
        private int side;

        public Square(int side) {
            this.side = side;
        }

        public int getSide() {
            return side;
        }

        @Override
        public int calculateArea() {
            return side * side;
        }
    }

    public static class AreaCalculator {
        public int calculateArea(IShape shape) {
            return shape.calculateArea();
        }
    }
    public static void main(String[] args) {
        IShape rectangle = new Rectangle(5, 10);
        IShape square = new Square(4);
        AreaCalculator areaCalculator = new AreaCalculator();

        System.out.println("Area of Rectangle: " + areaCalculator.calculateArea(rectangle));
        System.out.println("Area of Square: " + areaCalculator.calculateArea(square));
    }
}
