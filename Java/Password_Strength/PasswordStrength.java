package password;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PasswordStrength {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the password:");
        String password = sc.next();
        check(password);
	}

	public static void check(String password) {
		// TODO Auto-generated method stub
		// ^ represents the starting of the string.
		// (?=.*[a-z]) represent at least one lowercase character.
		// (?=.*[A-Z]) represents at least one uppercase character.
		// (?=.*\\d) represents at least one numeric value.
		// (?=.*[-+_!@#$%^&*., ?]) represents at least one special character.
		// . represents any character except line break.
		// + represents one or more times.
		String regex = "^(?=.*[a-z])(?=."+ "*[A-Z])(?=.*\\d)"+ "(?=.*[-+_!@#$%^&*., ?]).+$";

		// Compile the ReGex
        Pattern pattern = Pattern.compile(regex);

        // if the string entered is null then the output will be password invalid
        if (password == null) {
            System.out.println("Password Invalid.");
            return;
        }

        // Find match between given string & regular expression
        Matcher matcher = pattern.matcher(password);

        if (matcher.matches())
            System.out.println("Password Valid and Strong.");
        else
            System.out.println("Weak Password.");
    }

	}
