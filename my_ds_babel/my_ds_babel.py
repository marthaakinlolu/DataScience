import sqlite3
import csv

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Execute a SELECT query on the specified table
    c.execute(f"SELECT * FROM {table_name}")
    data = c.fetchall()

    # Get the column names of the table
    c.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in c.fetchall()]

    # Format the data as a CSV string
    csv_string = ",".join(columns) + "\n"
    for row in data:
        csv_string += ",".join(str(x) for x in row) + "\n"

    # Close the database connection
    conn.close()

    return csv_string[:-1]

print(sql_to_csv('all_fault_line.db','fault_lines'))

def csv_to_sql(csv_content, database, table_name):
    # Connect to the database
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Create the table with columns matching the CSV
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
                ("Volcano Name" TEXT,
                "Country" TEXT,
                "Type" TEXT,
                "Latitude (dd)" REAL,
                "Longitude (dd)" REAL,
                "Elevation (m)" INTEGER)
    ''')

    data = csv_content.getvalue()
    data_split = data.split("\n")

    # Insert the data into the table
    for line, row in enumerate(data_split):
        if line > 0:
            values = row.split(',')
            if len(values) > 1:
                vol_data = [values[0], values[1], values[2], values[3], values[4], values[5]]
                c.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?,?,?)", vol_data)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# with open ("list_volcano.csv") as file:
#     csv_content = file.read()

# csv_to_sql(StringIO(csv_content), 'list_volcanos.db','volcanos')

# conn = sqlite3.connect("list_volcanos.db")
# c = conn.cursor()
# c.execute(f"SELECT * FROM volcanos LIMIT 20")
# query = c.fetchall()
# for i in query:
#     print(i)