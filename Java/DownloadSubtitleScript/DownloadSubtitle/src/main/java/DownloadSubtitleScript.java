/*
 * Author : Haripriya Baskaran
 * Date : 13th Nov 2020
 * Source : http://thesubdb.com/api/
 * */

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class DownloadSubtitleScript {
    // This hash function receives the name of the file and returns the hash code
    public static String getHash(String fileName) throws IOException {
        // Execute the hash algorithm in python file
        Process p = Runtime.getRuntime().exec("python get_hash.py " + fileName);
        BufferedReader output = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String s = output.readLine();
        if (!s.equals("0")) {
            return s; // return the calculated hash value
        }
        return null;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // Video file taken from user input
        System.out.print("Enter file name with extension: ");
        String fileName = br.readLine();
        String hashCode = getHash(fileName); // Hash value calculated
        // The api endpoint is declared
        String endPoint = "http://api.thesubdb.com/?action=download&hash=" + hashCode + "&language=en";
        URL url = new URL(endPoint);
        // HTTP connect request made
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        // User agent credentials taken from user
        System.out.print("Enter client name: ");
        String clientName = br.readLine();
        System.out.print("Enter client version: ");
        String clientVersion = br.readLine();
        System.out.print("Enter client URL: ");
        String clientURL = br.readLine();
        // User Agent set as header property
        connection.setRequestProperty("User-Agent", "SubDB/1.0 (" + clientName + "/" + clientVersion + "; " + clientURL + ")");
        int response = connection.getResponseCode();
        // Response code is fetched
        if (response == HttpURLConnection.HTTP_OK) {
            BufferedReader responseOutput = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String readResponse;
            try {
                FileWriter myWriter = new FileWriter(fileName+".srt");
                // Save the response in a .srt file
                while ((readResponse = responseOutput.readLine()) != null) {
                    myWriter.write(readResponse);
                    myWriter.write("\n");
                }
                myWriter.close();
                responseOutput.close();
                System.out.println("Subtitles saved in "+fileName+".srt file");
                connection.disconnect();
                //Connect disconnected
            } catch (Exception e) {
                System.out.println("Subtitle cannot be downloaded...");
            }

        } else {
            System.out.println("Couldn't fetch anything!");
        }
    }
}


