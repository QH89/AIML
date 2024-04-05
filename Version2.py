import pymysql
from decimal import Decimal
import os
'''
版本更新2
这个版本的代码不但可以从一个directory里面识别所有文件，还可以自动生成table{详细类型为FLOAT}
下一版本尝试过滤png读取所有的txt

'''
# 数据库连接信息
host = "localhost"
port = 3306
user = "root"
passwd = "123456"
db_name = "Ai_Data"
table_name = "Ai_Data3"

# 建立数据库连接
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db_name)
cursor = conn.cursor()

# 检查表是否存在，如果不存在则创建
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
        col7 FLOAT,
        col8 FLOAT
    )
    """
    cursor.execute(create_table_sql)
    print(f"Table {table_name} created.")


# 指定包含数据文件的目录
directory_path = "/Users/yanzewu/Desktop/Matlab_WorkSpace/PDP_Data"

# 遍历指定目录下的所有文件
for filename in os.listdir(directory_path):
    # 构造完整的文件路径
    file_path = os.path.join(directory_path, filename)

    if filename.endswith(".txt"):
        print(f"Processing {filename}...")

        with open(file_path, 'r', encoding="UTF-8") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip("\n").split('\t')
                param = [Decimal(str(value)) if value.strip() else None for value in line]
                while len(param) < 8:
                    param.append(None)

                sql = f"INSERT INTO {table_name} (col1, col2, col3, col4, col5, col6, col7, col8) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, param)

conn.commit()
cursor.close()
conn.close()

print("All files have been processed.")
