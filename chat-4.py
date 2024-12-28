from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

user_input = input("I'm at your service! Anything you want?")

response_message = "****** of course, Master! Let me fetch that for you. *******"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": user_input},
    ],
    max_completion_tokens= 60,
    stop="6"
    #n=6,
)

message = response.choices[0].message.content

print(response_message) ; sleep(1)


print(message) 