import pymysql
import os

# Database connection information
host = "localhost"
port = 3306
user = "root"
passwd = "123456"
db_name = "Ai_Data"
# Tables
table_name_directional = "Ai_Data_DirectionalPDP3"
table_name_omni = "Ai_Data_OmniPDP_Snap3"
table_name_OmniPDPInfo = "OmniPDP"

# Establish database connection
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db_name)
cursor = conn.cursor()

# Table creation logic for different tables
tables = {
    table_name_directional: "(col1 FLOAT, col2 FLOAT, col3 FLOAT, col4 FLOAT, col5 FLOAT, col6 FLOAT, col7 FLOAT)",
    table_name_omni: "(col1 FLOAT, col2 FLOAT, col3 FLOAT, col4 FLOAT, col5 FLOAT, col6 FLOAT, col7 FLOAT)",
    table_name_OmniPDPInfo: "(col1 VARCHAR(255), col2 VARCHAR(255), col3 VARCHAR(255), col4 VARCHAR(255), col5 VARCHAR(255))"
}

# Check and create tables if not exists
for table_name, cols in tables.items():
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    if not cursor.fetchone():
        create_table_sql = f"CREATE TABLE {table_name} {cols}"
        cursor.execute(create_table_sql)
        print(f"Table {table_name} created.")

# Specify the directory containing data files
directory_path = "/Users/yanzewu/Desktop/Matlab_WorkSpace/Data"

# Iterate over all files in the specified directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # Determine the table based on filename
    if "DirectionalPDP" in filename and filename.endswith(".txt"):
        table_name = table_name_directional
        col_count = 7
    elif "OmniPDP_Snap" in filename and filename.endswith(".txt"):
        table_name = table_name_omni
        col_count = 7
    elif "OmniPDPInfo" in filename and filename.endswith(".txt"):
        table_name = table_name_OmniPDPInfo
        col_count = 5
    else:
        continue

    print(f"Processing {filename}...")

    with open(file_path, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip("\n").split('\t')
            param = line[:col_count] + [None] * (col_count - len(line))
            placeholders = ', '.join(['%s'] * col_count)
            sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(sql, param)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("All files have been processed.")
