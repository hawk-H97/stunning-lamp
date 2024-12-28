from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Give me the list of top 10 tool name for WAPT and no explanation"},
    ],
    max_completion_tokens= 60,
    stop="6"
    #n=6,
)

message = response.choices[0].message.content

print(message)