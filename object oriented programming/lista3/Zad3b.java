import java.util.*;

public class Zad3b {
    interface TaxCalculator {
        double calculateTax(double price);
    }

    static class StandardTaxCalculator implements TaxCalculator {
        @Override
        public double calculateTax(double price) {
            return price * 0.22;
        }
    }

    static class ReducedTaxCalculator implements TaxCalculator {
        @Override
        public double calculateTax(double price) {
            return price * 0.08;
        }
    }

    static class ZeroTaxCalculator implements TaxCalculator {
        @Override
        public double calculateTax(double price) {
            return 0.0;
        }
    }

    static class Item {
        private double price;
        private String name;
        private String category;

        public Item(String name, double price, String category) {
            this.name = name;
            this.price = price;
            this.category = category;
        }

        public double getPrice() {
            return price;
        }

        public String getName() {
            return name;
        }

        public String getCategory() {
            return category;
        }
    }

    interface IItemSortingStrategy {
        List<Item> sort(List<Item> items);
    }

    static class AlphabeticalSortingStrategy implements IItemSortingStrategy {
        @Override
        public List<Item> sort(List<Item> items) {
            items.sort(Comparator.comparing(Item::getName));
            return items;
        }
    }

    static class PriceSortingStrategy implements IItemSortingStrategy {
        @Override
        public List<Item> sort(List<Item> items) {
            items.sort(Comparator.comparingDouble(Item::getPrice));
            return items;
        }
    }

    static class CashRegister {
        private final TaxCalculator taxCalculator;
        private final IItemSortingStrategy sortingStrategy;

        public CashRegister(TaxCalculator taxCalculator, IItemSortingStrategy sortingStrategy) {
            this.taxCalculator = taxCalculator;
            this.sortingStrategy = sortingStrategy;
        }

        public double calculateTotalPrice(List<Item> items) {
            return items.stream()
                    .mapToDouble(item -> item.getPrice() + taxCalculator.calculateTax(item.getPrice()))
                    .sum();
        }

        public void printBill(List<Item> items) {
            List<Item> sortedItems = sortingStrategy.sort(items);
            for (Item item : sortedItems) {
                System.out.printf("Item: %s, Price: %.2f, Tax: %.2f%n",
                        item.getName(), item.getPrice(), taxCalculator.calculateTax(item.getPrice()));
            }
        }
    }

    public static void main(String[] args) {

        List<Item> items = new ArrayList<>();
        items.add(new Item("Apple", 1.0, "Fruit"));
        items.add(new Item("Banana", 2.0, "Fruit"));
        items.add(new Item("Shampoo", 5.0, "Cosmetics"));

        CashRegister register = new CashRegister(new StandardTaxCalculator(), new AlphabeticalSortingStrategy());
        register.printBill(items);
        System.out.println("Total Price: " + register.calculateTotalPrice(items));

        register = new CashRegister(new StandardTaxCalculator(), new PriceSortingStrategy());
        register.printBill(items);
        System.out.println("Total Price: " + register.calculateTotalPrice(items));
    }
}
