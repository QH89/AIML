import pymysql
import pandas as pd

# 数据库连接信息
host = "localhost"
port = 3306
user = "root"
passwd = "123456"
db_name = "Ai_Data"

# 表名
table_names = [
    "Ai_Data_DirectionalPDP3",  # 用于DirectionalPDP数据的表名
    "Ai_Data_OmniPDP_Snap3",  # 用于OmniPDP_Snap数据的表名
    "OmniPDP"  # 第三个表的名字
]

# 建立数据库连接
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db_name)

# 创建一个空列表以存储所有的DataFrame
data_frames = []

for table_name in table_names:
    # 构造SQL查询
    sql = f"SELECT * FROM {db_name}.{table_name}"
    # 读取表并转换为DataFrame
    df = pd.read_sql(sql, conn)
    # 将DataFrame添加到列表中
    data_frames.append(df)

# 现在，data_frames列表包含了三个表的DataFrame
# 你可以通过data_frames[0], data_frames[1], data_frames[2]来访问它们

# 关闭数据库连接
conn.close()

# 如果你想打印出来看看
for df in data_frames:
    print(df.head())  # 打印每个DataFrame的前几行
