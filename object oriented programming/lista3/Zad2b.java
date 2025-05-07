class ReportDataProvider {
    public String getData() {
        return "Dane raportu";
    }
}

class ReportFormatter {
    public String formatDocument(String data) {
        return "Sformatowany raport: " + data;
    }
}

class ReportPrinter1 {
    public void printReport(String formattedData) {
        System.out.println("Drukowanie: " + formattedData);
    }
}

public class Zad2b {
    public static void main(String[] args) {
        ReportDataProvider dataProvider = new ReportDataProvider();
        ReportFormatter formatter = new ReportFormatter();
        ReportPrinter1 printer = new ReportPrinter1();

        String data = dataProvider.getData();
        String formatted = formatter.formatDocument(data);
        printer.printReport(formatted);
    }
}
