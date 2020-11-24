package FileCounter;
import java.io.File;
import java.util.*;
// The time and space complexity is O(n) as we will be iterating through all files recursively
public class filecounter {
public static int countDirectory=0;
// function which counts number of file and sub-directory in the given directory
    public static int countFilesInDirectory(File directory){
     int countFile=0;
     // iterate over all files
     for (File file : directory.listFiles()) {
        // if it is file increment countFile
         if (file.isFile()) {
             countFile++;
         }
         // else increment countDirectory
         if (file.isDirectory()) {
        	 countDirectory++;
             countFile += countFilesInDirectory(file);
         }
     }
     return countFile;
 }
    public static void main(String args[]) {
	    Scanner s = new Scanner(System.in);
      // Take input as the path for directory
	    System.out.println("Enter the Path of your directory : ");
	    String path = s.next();
      // Make a file object and pass the entered path as an argument
  	 	File file = new File(path);
  		int countFile = filecounter.countFilesInDirectory(file);
  		System.out.println("The No of Files in entered Directory are : "+countFile);
  		System.out.println("The No of Sub-Directory in entered Directory are : "+countDirectory);
    }
}
