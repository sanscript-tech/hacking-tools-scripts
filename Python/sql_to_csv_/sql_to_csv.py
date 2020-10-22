import sqlite3
import pandas as pd

# Open the file
f = open('output.csv', 'w')

# Create a connection and get a cursor
connection = sqlite3.connect('mydata.sql')
cursor = connection.cursor()

# inserting sample data into table if haven't already
cursor.execute('''CREATE TABLE CLIENT([Client_Name] text, [Country_ID] text)''')
cursor.execute(''' INSERT INTO CLIENT(Client_Name,Country_ID)
              VALUES("Tania","1") ''')
cursor.execute(''' INSERT INTO CLIENT(Client_Name,Country_ID)
              VALUES("Ananya","2") ''')
cursor.execute(''' INSERT INTO CLIENT(Client_Name,Country_ID)
              VALUES("Sakshi","3") ''')
cursor.execute(''' INSERT INTO CLIENT(Client_Name,Country_ID)
              VALUES("Harry","4") ''')


# Execute the query
cursor.execute('select * from CLIENT')
# Get data in batches
while True:
    # Read the data
    df = pd.DataFrame(cursor.fetchmany(1000))
    # We are done if there are no data
    if len(df) == 0:
        break
    # Let's write to the file
    else:
        df.to_csv(f, header=False)

# Clean up
f.close()
cursor.close()
connection.close()
