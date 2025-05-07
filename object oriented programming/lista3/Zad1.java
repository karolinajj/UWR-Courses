import java.util.ArrayList;
import java.util.List;

class Order {
    private List<OrderItem> items = new ArrayList<>();

    // Creator: Order tworzy OrderItem, ponieważ używa go i ma potrzebne dane do jego inicjalizacji
    
    public void addItem(String productName, int quantity, double price) {
        items.add(new OrderItem(productName, quantity, price));
    }

    // Information Expert: Order posiada informacje o OrderItem, więc oblicza łączną wartość zamówienia
    
    public double getTotalPrice() {
        double total = 0;
        for (OrderItem item : items) {
            total += item.getTotalPrice();
        }
        return total;
    }
}

class OrderItem {
    private String productName;
    private int quantity;
    private double pricePerUnit;

    public OrderItem(String productName, int quantity, double pricePerUnit) {
        this.productName = productName;
        this.quantity = quantity;
        this.pricePerUnit = pricePerUnit;
    }

    public double getTotalPrice() {
        return quantity * pricePerUnit;
    }
}

public class Zad1 {
    public static void main(String[] args) {
        Order order = new Order();
        
        order.addItem("A", 1, 10.00);
        order.addItem("B", 2, 2.99);
        order.addItem("C", 1, 11.00);
        System.out.println("Total order price: $" + order.getTotalPrice());
    }
}


