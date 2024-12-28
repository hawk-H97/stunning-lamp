from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "what do you think 5 + 56 is ?"}],
)

message = response.choices[0].message.content

#print(response)
print(message)