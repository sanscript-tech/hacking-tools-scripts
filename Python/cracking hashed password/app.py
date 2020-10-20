# Importing libraries
import xlrd
import hashlib

# Dehash function
def dehash(rows,cols):

    #Taking hash from user
    inp=input("Enter hash to decrypt it :")
    opt=None

    # If length is 64 then calling sha256 function to search hash
    if(len(inp)==64):
        print("Searching data in database")
        # Calling function
        opt=sha256(rows,cols,inp)
        print(opt)
        if(opt==None):
            print("Hash not found in database")

    # If length is 32 then it will call md5 function to search hash
    elif(len(inp)==32):
        print("Searching data in database")
        #  Calling md5 function to search
        opt=md5(rows,cols,inp)
        print(opt)
        if(opt==None):
            print("Hash not found in database")
    else:
        print("Invalid hash format")

# SHA256 function to search for hash in excel sheet
def sha256(rows,cols,inp):
    for col in range(1,cols,4):
        for row in range(0,rows):
            # Iterating through excel sheet to search data
            if(inp==sheet.cell_value(row,col)):
                print("Found data in database.It's SHA256 hash:")
                # It will return decoded hash 
                return(sheet.cell_value(row,col-1))
                break

# MD5 function to search for hash in excel sheet
def md5(rows,cols,inp):
    for col in range(2,cols,4):
        for row in range(0,rows):
            # Iterating through excel sheet to search data
            if(inp==sheet.cell_value(row,col)):
                print("Found data in database.It's MD5 hash:")
                # It will return decoded hash 
                return(sheet.cell_value(row,col-2))
                break


if __name__ == '__main__':
    try:
        # Openning excel sheet and reading it
        file='hash.xls'
        wb=xlrd.open_workbook(file)
        #  Reading first sheet
        sheet = wb.sheet_by_index(0)
        # Taking number of rows
        rows=sheet.nrows
        # Taking number of columns
        cols=sheet.ncols
        # Calling dehash function and with rows and columns as argurments
        dehash(rows,cols)
    except:
        print("File missing")
