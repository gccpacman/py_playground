import os
import psycopg2
from psycopg2 import sql
from icecream import ic
from openai import OpenAI


# 设置 PostgreSQL 连接参数
db_name = os.getenv('POSTGRES_NAME')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

# connection = psycopg2.connect(
#     dbname=db_name,
#     user=db_user,
#     password=db_password,
#     host=db_host,
#     port=db_port
# )

# try:
#     # 打开游标
#     cursor = connection.cursor()

#     # 执行简单查询
#     cursor.execute("SELECT version();")
#     db_version = cursor.fetchone()
#     print("PostgreSQL version:", db_version)

# except psycopg2.Error as e:
#     # 捕捉数据库相关错误
#     print("Error while connecting to PostgreSQL:", e)

# finally:
#     # 确保连接关闭
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed.")

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
    base_url = os.environ.get("OPENAI_API_BASE_URL")
)


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

# print(completion.choices[0].message)
ic(completion.choices[0].message)
