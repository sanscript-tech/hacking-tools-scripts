#include <stdio.h> 
#include <dirent.h> 

int main(void) 
{ 
	struct dirent *de;  // Pointer for directory 
    int ctr = 0;        // variable to store size
	DIR *dr = opendir(".");  

	if (dr == NULL)  //if directory not exist
	{ 
		printf("Can't open current directory" ); 
		return 0; 
	} 
 
	while ((de = readdir(dr)) != NULL)    //if directory exists and till the end of directory
    {
         FILE* fp = fopen(de->d_name, "r");
        fseek(fp, 0L, SEEK_END); 
        ctr = ctr + ftell(fp);    // calculating the size of each file in folder
        fclose(fp);     
    }		
      
    printf("Directory Size : %d bytes", ctr);
    closedir(dr);	 
	return 0; 
} 
