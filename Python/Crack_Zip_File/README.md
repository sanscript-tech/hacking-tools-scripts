## Crack a Zip file Password using tqdm (Brute Force)
The aim of the program is to crack a zip file's password using simple brute force approach from a given words list.

### Library Used:
* Python [**tqdm**](https://pypi.org/project/tqdm/) - Instantly shows a smart progress meter for loops.

### Prerequisites:
Can be installed using pip/pip3

`>> pip3 install tqdm`

### Usage:
`>> python crack_zip.py`

### I/O:
```
Enter Words list filename: $(wordlist)

Enter zip filename: $(zipfile)

Total passwords to test: $(total_number_of_words_being_checked)

Password found: $(password)
```
**OR**
```
Password not found, try other wordlist.
```
***NOTE: Example words list can be downloaded from this [link](https://drive.google.com/file/d/19vpcd907W9MnlG93F1ovIRv8H1YKCJhk/view?usp=sharing) along with sample zip file attached with the code file(secret.zip).***