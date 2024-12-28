from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a language translater "},
        {"role": "user", "content": "Translate English to arabic: Security and also give the pronunciation"},
    ],
)

message = response.choices[0].message.content

print(message)
#print(response)