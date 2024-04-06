import pymysql
import pandas as pd

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

#读取Mysql的表并储存为dataframe (现在只能读Ai.Ai_Data_DirectionalPDP1这一个表）
sql = "Select * from Ai.Ai_Data_DirectionalPDP1"
df = pd.read_sql(sql, conn)
dataFrame = pd.DataFrame(df)

#把每一列储存为pandas.core.series.Series，把所有Seris存到list里
list = []
for i in range(dataFrame.shape[1]):
    dataColSeries = dataFrame.iloc[:, i]
    list.append(dataColSeries)
print(list)


