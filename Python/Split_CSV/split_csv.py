import os

def split(filename, delimiter=',', row_limit=10000): 
    import csv
    output_name_template='output_%s.csv'
    output_path='.'
    keep_headers=True
    output_name_template = filename + output_name_template
    filehandler = open(filename+".csv",'r')
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
         output_path,
         output_name_template  % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.next()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
               output_path,
               output_name_template  % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)

def main():
    file_name = raw_input("Enter name of the csv file(csv file should be present in the pwd):")
    num_of_rows = raw_input("Enter number of rows each split should contain:")
    try:
	split(str(file_name),row_limit = int(num_of_rows))
	print("Output files successfully saved!")

    except Exception as e:
	print("Something went wrong in importing given file...Check below:\n")
	print(e)
	
if __name__ == "__main__":
    main()
