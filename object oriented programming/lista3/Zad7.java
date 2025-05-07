public class Zad7 {

    public interface IReportDataProvider {
        String getData();
    }

    public interface IReportFormatter {
        String formatDocument(String data);
    }

    public interface IReportPrinter {
        void printReport(String formattedData);
    }

    public static class ReportDataProvider implements IReportDataProvider {
        @Override
        public String getData() {
            return "Dane raportu";
        }
    }

    public static class ReportFormatter implements IReportFormatter {
        @Override
        public String formatDocument(String data) {
            return "Sformatowany raport: " + data;
        }
    }

    public static class ReportPrinter implements IReportPrinter {
        @Override
        public void printReport(String formattedData) {
            System.out.println("Drukowanie: " + formattedData);
        }
    }

    public static class ReportComposer {
        private final IReportDataProvider dataProvider;
        private final IReportFormatter formatter;
        private final IReportPrinter printer;

        public ReportComposer(IReportDataProvider dataProvider, IReportFormatter formatter, IReportPrinter printer) {
            this.dataProvider = dataProvider;
            this.formatter = formatter;
            this.printer = printer;
        }

        public void generateReport() {
            String data = dataProvider.getData();
            String formattedData = formatter.formatDocument(data);
            printer.printReport(formattedData);
        }
    }

    public static void main(String[] args) {
        IReportDataProvider dataProvider = new ReportDataProvider();
        IReportFormatter formatter = new ReportFormatter();
        IReportPrinter printer = new ReportPrinter();
        ReportComposer reportComposer = new ReportComposer(dataProvider, formatter, printer);
        reportComposer.generateReport();
    }
}

