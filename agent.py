from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

#Step 1: Initiate the API Keys

GROQ_APIKEY = os.getenv('GROQ_APIKEY')
SERPER_APIKEY = os.getenv("SERPER_APIKEY")

from groq import Groq

client = Groq(api_key=GROQ_APIKEY)

completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[],
    temperature=0.6,
    max_completion_tokens=4096,
    top_p=0.95,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")