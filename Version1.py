import pymysql
from decimal import Decimal
import os  # 导入os库以访问文件系统
'''
版本更新1
这个版本的代码只能识别directory所有的文件，并且得自己手动创mysql的table 
下一版本尝试自己创建Table

'''
# 数据库连接信息
host = "localhost"
port = 3306
user = "root"
passwd = "123456"
db_name = "Ai_Data"

# 指定包含数据文件的目录
directory_path = "/Users/yanzewu/Desktop/Matlab_WorkSpace/PDP_Data"

# 建立数据库连接
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db_name)
cursor = conn.cursor()

# 遍历指定目录下的所有文件
for filename in os.listdir(directory_path):
    # 构造完整的文件路径
    file_path = os.path.join(directory_path, filename)

    # 检查是否为文本文件
    if filename.endswith(".txt"):
        print(f"Processing {filename}...")

        # 读取并处理文件
        with open(file_path, 'r', encoding="UTF-8") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip("\n").split('\t')

                # 转换字符串值为Decimal，处理空值
                param = [Decimal(str(value)) if value.strip() else None for value in line]

                # 确保参数列表长度为8
                while len(param) < 8:
                    param.append(None)

                # SQL 插入语句
                sql = "INSERT INTO Ai_Data.Ai_Data2 (col1, col2, col3, col4, col5, col6, col7, col8) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                # 执行SQL语句
                cursor.execute(sql, param)

# 提交更改并关闭连接
conn.commit()
cursor.close()
conn.close()

print("All files have been processed.")
