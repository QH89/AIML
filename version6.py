import pymysql
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

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
    # 移除非数值列
    df = df.select_dtypes(include=[np.number])
    # 将DataFrame添加到列表中
    data_frames.append(df)

# 关闭数据库连接
conn.close()

# 数据正则化
optimized_frames = []
scaler = MinMaxScaler(feature_range=(0, 1))
for df in data_frames:
    # 检查DataFrame是否为空
    if not df.empty:
        # 仅对数值型数据进行正则化
        normalized = scaler.fit_transform(df)
        # 转换回DataFrame以保留列名
        df_normalized = pd.DataFrame(normalized, columns=df.columns)
        optimized_frames.append(df_normalized)

# 打印正则化后的数据
for df in optimized_frames:
    print(df.head())

















