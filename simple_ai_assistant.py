from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() #by default looks for .env file in the current directory

client = OpenAI(
    base_url = os.getenv("BASE_URL"), 
    api_key = os.getenv("API_KEY")
)
messages=[]
while True:
    user_input = input("\nUser:")

    if user_input in ["exit","quit","bye"]:
        break
    messages.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    messages.append(
        {
            "role":"assistant",
            "content":response.choices[0].message.content
        }
        )
    print("LLM Response:")
    print(response.choices[0].message.content) #response from qwen3:4b
