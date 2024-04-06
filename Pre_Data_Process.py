import pymysql
from decimal import Decimal
import os

'''
无敌是多么太寂寞
'''


# 数据库连接信息
host = "localhost"
port = 3306
user = "root"
passwd = "Qiaohui0319"
db_name = "Ai"
table_name_directional = "Ai_Data_DirectionalPDP1"  # 用于DirectionalPDP数据的表名, 注意要改每个表的名字
table_name_omni = "Ai_Data_OmniPDP_Snap1"  # 用于OmniPDP_Snap数据的表名

# 建立数据库连接
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db_name)
cursor = conn.cursor()

# 检查表是否存在，如果不存在则创建
for table_name in [table_name_directional, table_name_omni]:
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()
    if not result:
        # 如果表不存在，创建表
        create_table_sql = f"""
        CREATE TABLE {table_name} (
            col1 FLOAT,
            col2 FLOAT,
            col3 FLOAT,
            col4 FLOAT,
            col5 FLOAT,
            col6 FLOAT,
            col7 FLOAT
        )
        """
        cursor.execute(create_table_sql)
        print(f"Table {table_name} created.")

# 指定包含数据文件的目录
directory_path = "/Users/qh89/Desktop/AIML/Data"

# 遍历指定目录下的所有文件
for filename in os.listdir(directory_path):
    # 构造完整的文件路径
    file_path = os.path.join(directory_path, filename)

    # 根据文件名决定使用的表名
    if "DirectionalPDP" in filename and filename.endswith(".txt"):
        table_name = table_name_directional
    elif "OmniPDP_Snap" in filename and filename.endswith(".txt"):
        table_name = table_name_omni
    else:
        continue  # 如果文件不匹配任何模式，则跳过此文件

    print(f"Processing {filename}...")

    with open(file_path, 'r', encoding="UTF-8") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip("\n").split('\t')
            param = [Decimal(str(value)) if value.strip() else None for value in line]

            sql = f"INSERT INTO {table_name} (col1, col2, col3, col4, col5, col6, col7) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, param)

conn.commit()
cursor.close()
conn.close()

print("All files have been processed.")
