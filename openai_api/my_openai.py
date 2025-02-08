import os
from openai import OpenAI

# 替换为你的 OpenAI API Key
OPENAI_API_KEY = "your-api-key-here"

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
    base_url = os.environ.get("OPENAI_API_BASE_URL")
)


def chat_with_agent(messages, model="gpt-4o-mini", temperature=0.7):
    """与 OpenAI API 交互的简单聊天代理"""
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

messages = [{"role": "system", "content": "You are a helpful AI assistant."}]


# 交互式聊天
if __name__ == "__main__":
    print("欢迎使用 AI Agent! 输入 'exit' 退出。")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("再见！")
            break
        messages.append({"role": "user", "content": user_input})
        response = chat_with_agent(messages=messages)
        messages.append({"role": "assistant", "content": response})
        print(f"AI: {response}")


"""
输出 （支持记住上下文)

欢迎使用 AI Agent! 输入 'exit' 退出。
You: hi, I'm pacman
AI: Hi Pacman! How can I assist you today?
You: what's my name
AI: Your name is Pacman! How can I help you today?
"""