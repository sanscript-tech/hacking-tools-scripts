import html2markdown
import sys


def convert_me_to_markdown(input_html, output_md):
    """This function take an HTML file as input and
       converts it into a markdown file. The name of
       the markdown file is set according to the
       output_md string.

    Args:
        input_html (string): The input HTML file
        output_md (string): The name of the output markdown file
    """

    # Used context manger to open the input and output files.
    with open(input_html, 'r') as input_file:
        with open(output_md, 'w') as output_file:
            for data in input_file:
                # Writing the conveted data to the output file.
                output_file.write(html2markdown.convert(data))


def main():

    # The html file which undergoes conversion
    input_html = input("Enter your html file please: ")

    # To make sure the user inputs only html files
    # HMTL files can end with .html or .htm
    if any(input_html.endswith(s) for s in ['.html', '.htm']):
        # To have a matching file name for the output file
        output_md = input_html.split('.')[0] + ".md"
        convert_me_to_markdown(input_html, output_md)
    else:
        sys.exit("Bruh this script takes html files only")


if __name__ == "__main__":
    main()
    print("Your HTML file has been converted to Markdown successfully!!")
