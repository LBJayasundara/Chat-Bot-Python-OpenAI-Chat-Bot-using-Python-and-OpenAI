from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY
)

while True:

    question = input("user:")

    if(question!="bye"):

        response=client.chat.completions.create(
            model="tngtech/deepseek-r1t-chimera:free",
            messages=[
                {"role": "user", "content": question},
            ]

        )

        for choice in response.choices:
            print(f"AI :{choice.message.content}")
    else:
        print("AI :bye")
        break   




