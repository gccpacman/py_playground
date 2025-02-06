import os

from psycopg2 import sql
from icecream import ic
from openai import OpenAI

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
