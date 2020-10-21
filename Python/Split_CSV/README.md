# Split a CSV file in to multiple smaller files
### Description:
The aim of this program is to take a large csv file as input and break it in to multiple smaller files based on the number of rows per file given by the user.

### Library used: 
* Python CSV

### Parameters used and their Significance:
* `row_limit`: The number of rows you want in each output file. 10,000 by default.
* `filename`: The raw input csv file name.

### Usage:
**`>> python split_csv.py`**

#### I/O:
```
* Enter name of the csv file(csv file should be present in the pwd): $(file_name)

* Enter number of rows each split should contain:($num_of_rows)

* Output files successfully saved!
```
***The output files are stored in the present working directory(pwd) itself. A sample dataset.csv for example can be found [HERE](https://drive.google.com/file/d/1Q5dpNYAhfA3f_MTJE49sutBOH-pYVyEQ/view?usp=sharing).***