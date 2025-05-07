class TaxCalculator {
    public double calculateTax(double price) {
        return price * 0.22;
    }
}

class Item {
    private double price;
    private String name;

    public Item(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public double getPrice() {
        return price;
    }

    public String getName() {
        return name;
    }
}


class CashRegister {
    private TaxCalculator taxCalc = new TaxCalculator();

    public double calculatePrice(Item[] items) {
        double totalPrice = 0;
        for (Item item : items) {
            totalPrice += item.getPrice() + taxCalc.calculateTax(item.getPrice());
        }
        return totalPrice;
    }

    public void printBill(Item[] items) {
        for (Item item : items) {
            System.out.printf("Item: %s, Price: %.2f, Tax: %.2f%n", 
                item.getName(), item.getPrice(), taxCalc.calculateTax(item.getPrice()));
        }
    }
}

public class Zad3a {
    public static void main(String[] args) {
        Item[] items = new Item[] {
            new Item("Apple", 1.0),
            new Item("Banana", 2.0),
            new Item("Orange", 3.0)
        };

        CashRegister register = new CashRegister();
        register.printBill(items);
        System.out.println("Total Price: " + register.calculatePrice(items));
    }
}
