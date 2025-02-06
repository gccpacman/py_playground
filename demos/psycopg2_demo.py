import os
import psycopg2

# 设置 PostgreSQL 连接参数
db_name = os.getenv('POSTGRES_NAME')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

connection = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

try:
    # 打开游标
    cursor = connection.cursor()

    # 执行简单查询
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("PostgreSQL version:", db_version)

except psycopg2.Error as e:
    # 捕捉数据库相关错误
    print("Error while connecting to PostgreSQL:", e)

finally:
    # 确保连接关闭
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")