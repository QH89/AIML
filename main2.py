
import pymysql
from decimal import Decimal

# Establish connection to the database
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="Qiaohui0319", db="Ai")
cursor = conn.cursor()

fileopen = "DirectionalPDP_Snap1.txt"
''' 
    创造一个value 找到每次nyu sim 跑的数据
    omni 40 个txt数据一个表
'''
# Open and read the file
with open(fileopen, 'r', encoding="UTF-8") as file:
    lines = file.readlines()

    for line in lines:
        print(line)
        line = line.strip("\n").split('\t')

        # Convert string values to Decimal, handle missing values appropriately
        param = [Decimal(str(value)) if value.strip() else None for value in line]

        # Ensure the parameter list is of length 8
        while len(param) < 8:
            param.append(None)

        # SQL query for insertion
        sql = "INSERT INTO Ai.Data1 (idData1, col1, col2, col3, col4, col5, col6, col7) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        # Execute the query with the parameters
        cursor.execute(sql, param)

# Commit changes and close connections
conn.commit()
cursor.close()
conn.close()
