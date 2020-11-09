#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// Add a global variable to skip the first line of shell output in windows.
int first_skip = 1;

// Function to format shell output.
char* formatLog(char *buffer)
{
    // Check which OS the script is currently running on.
    #ifdef __linux__

        // Tokenize the script using `:` as a delimiter.
        char *token_1 = strtok(buffer, ":");
        char *token_2 = strtok(NULL, ":");

        // Extract the password tokenizing through `=`.
        char *ssid_part = strrchr(token_1, '/');
        char *psk = strrchr(token_2, '=');

        // Extract the ssid.
        char *ssid = strtok(ssid_part+1, ".");

        // Some formatting to make it more readable.
        psk += 1;
        strcat(ssid, ":");
        strcat(ssid, psk);

        return ssid;

    #elif _WIN32

        #include<ctype.h>

        // Skip the first line of shell output.
        if(first_skip == 1)
        {   first_skip = 0;
            return "";
        }

        // Extract ssid by tokenizing through `:`.
        char *ssid = strtok(buffer, ":");
        ssid = strtok(NULL, ": ");

        // Trim trailing whitespaces.
        char *end;
        end = ssid + strlen(ssid) - 1;
        while(end > ssid && isspace((unsigned char)*end)) end--;
        end[1] = '\0';

        // Create a file pointer to access a different shell.
        FILE *shell_ptr;

        // Format the shell command to extract the password.
        char psk_command[1024];
        sprintf(psk_command, "netsh wlan show profile %s key=clear | findstr \"Key Content\"", ssid);
        shell_ptr = popen(psk_command, "r");

        // Create a buffer to read the data.
        char psk_temp[1024];
        fgets(psk_temp, sizeof(psk_temp), shell_ptr);

        // Extract the password.
        char *psk = strtok(psk_temp, ":");
        psk = strtok(NULL, ": ");

        // Ignore passwords which are null.
        if((psk != NULL) && (psk[0] == '\0') && (strcmp(psk, "1") != 0))
        {
            end = psk + strlen(psk) - 1;
            while(end > psk && isspace((unsigned char)*end)) end--;
            end[1] = '\0';
        }

        // Set open networks as [Open Network]
        if(strlen(psk) == 2)
            psk = "[Open Network]";

        // Close unused shell pointer.
        pclose(shell_ptr);

        // Format output for better readability.
        strcat(ssid, ":");
        strcat(ssid, psk);
        return ssid;

    #endif
}

int main()
{
    /*
    Create file pointers for:
    - Reading information from shell.
    - Writing to a Text File.

    Also create a buffer to read the shell output, line by line.
    */
    FILE *shell_op, *fptr;
    char buffer[3096];

    // Check which OS the program is currently being run on.
    #ifdef _WIN32

        char *command = "netsh wlan show profile | findstr \":\"";

    #elif __linux__

        char *command = "sudo grep -r '^psk=' /etc/NetworkManager/system-connections/";

    #endif

    // Open a text file for writing.
    fptr = fopen("wifi_password.txt", "w");

    // Check if file was created or not.
    if(fptr == NULL)
    {
        puts("Error creating file...");
        exit(1);
    }

    // Spawn a shell process to communitcate with OS.
    shell_op = popen(command, "r");
    if(shell_op == NULL)
    {
        puts("Failed to communicate with shell.");
        exit(1);
    }

    // Read shell output line by line.
    while (fgets(buffer, sizeof(buffer), shell_op) != NULL)
    {
        // Format shell output for better readability.
        char *formattedLog = formatLog(buffer);

        // Write the formated information to the file.
        fprintf(fptr, "%s", formattedLog);
    }


    // Close all file pointers and free up memory space.
    pclose(shell_op);
    fclose(fptr);

    // Time Complexity = O(n); n = No. of saved wifi networks.
    // Space Complexity = O(1);

    return 0;
}
