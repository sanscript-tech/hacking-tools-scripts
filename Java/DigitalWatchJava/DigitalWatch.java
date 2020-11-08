import java.io.*;
import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.text.*;

class DigitalWatch implements Runnable {
	// Initialise all the components of the application window 
	JFrame f;
	Thread t = null;
	int hours = 0, minutes = 0, seconds = 0;
	String timeString = "";
	String timePeriod = "";
	JButton b;

	DigitalWatch() {
		// frame for outliner
		f = new JFrame();
		//thread to execute time change
		t = new Thread(this);
		t.start();
		// Display of time on a button for better UI
		b = new JButton();
		b.setBounds(100, 100, 100, 50);

		f.add(b);
		f.setSize(300, 300);
		f.setLayout(null);
		f.setVisible(true);
	}

	public void run() {
		try {
			while (true) {
				// hours is checked if > 12 to change the time-period of the day(AM/PM)
				Calendar cal = Calendar.getInstance();
				hours = cal.get(Calendar.HOUR_OF_DAY);
				if (hours > 12) {
					hours -= 12;
					timePeriod = "PM";
				}
				else{
					timePeriod = "AM";
				}
				minutes = cal.get(Calendar.MINUTE);
				seconds = cal.get(Calendar.SECOND);
				// SimpleDateFormat used to get customized time format
				SimpleDateFormat formatter = new SimpleDateFormat("hh:mm:ss");
				Date date = cal.getTime();
				//Time-period is appended with the time
				timeString = formatter.format(date) +" "+ timePeriod;
				printTime();
				// interval given in milliseconds(1 sec = 1000 ms)
				t.sleep(1000); 
			}
		} catch (Exception e) {
		}
	}

	public void printTime() {
		b.setText(timeString);
	}

	public static void main(String[] args) throws Exception {
		// Watch initialized
		new DigitalWatch();
	}
}
