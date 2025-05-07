class ReportPrinter {
    public String getData() {
        return "Dane raportu";
    }

    public String formatDocument(String data) {
        return "Sformatowany raport: " + data;
    }

    public void printReport(String formattedData) {
        System.out.println("Drukowanie: " + formattedData);
    }
}

public class Zad2a{
    public static void main(String[] args) {
        ReportPrinter printer = new ReportPrinter();
        String data = printer.getData();
        String formatted = printer.formatDocument(data);
        printer.printReport(formatted);
    }
}

