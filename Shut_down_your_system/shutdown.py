'''
Python Script to Shutdown/Restart your computer
'''

import os;
print("1. Shutdown Computer\n2. Restart Computer\n3. Exit");
choice = int(input("\nEnter your choice: "));
if choice == 1:
    os.system("shutdown /s /t 1");
elif choice==2:
    os.system("shutdown /r /t 1");
elif choice==3:
    exit();
else:
    print('Invalid choice')