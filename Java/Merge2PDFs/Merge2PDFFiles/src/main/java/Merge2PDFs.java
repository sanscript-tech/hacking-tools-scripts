import java.io.*;
import org.apache.pdfbox.multipdf.PDFMergerUtility;


class Merge2PDFs {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //Loading PDF1 document from user
        System.out.print("Enter first pdf name(without extension): ");
        String pdf1 = System.getProperty("user.dir") + "/" + br.readLine() + ".pdf";
        File file1 = new File(pdf1);

        //Loading PDF2 document from user
        System.out.print("Enter second pdf name(without extension): ");
        String pdf2 = System.getProperty("user.dir") + "/" + br.readLine() + ".pdf";
        File file2 = new File(pdf2);

        //Instantiating PDFMergerUtility class
        PDFMergerUtility PDFmerger = new PDFMergerUtility();

        //Setting the destination fileName
        System.out.print("Enter destination fileName(without extension): ");
        String merged = System.getProperty("user.dir") + "/" + br.readLine() + ".pdf";
        PDFmerger.setDestinationFileName(merged);

        //adding the source files to PDFmerger
        PDFmerger.addSource(file1);
        PDFmerger.addSource(file2);

        //Merging the two documents
        try {
            PDFmerger.mergeDocuments();
            System.out.println("Documents Successfully Merged!");
        } catch (Exception e) {
            System.out.println("Something went wrong!");
        }
    }
}
