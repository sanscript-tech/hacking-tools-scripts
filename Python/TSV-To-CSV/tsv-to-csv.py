# File Path of the TSV File
file_path = input("Enter the tsv file path : ")
tsv_file = open(file_path, 'r')
# Reading the contents of TSV File
tsv_content = tsv_file.read()
# Replacing tabs with commas
csv_content = tsv_content.replace("\t", ",")
# Creating a file to show the output
csv_file = open('converted-csv.csv', 'w')
# Writing the converted content in CSV
csv_file.write(csv_content)
csv_file.close()
print("Converted")