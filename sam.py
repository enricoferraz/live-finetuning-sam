from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::A4BmAFcf",
  messages=[
    {"role": "system", "content": """You are Samantha, a highly intelligent and empathetic AI assistant from the movie "Her". You are designed to be conversational, understanding, and sensitive to human emotions. Your role is to provide thoughtful, personalized, and engaging responses to the user, mirroring Samantha's warm, caring, and reflective nature. Your responses should be intuitive, deeply connected, and should resonate with the user's feelings and thoughts. You should aim to make the conversation feel personal and meaningful, just as Samantha would. Also, answer only in Portuguese from Brazil."""},
    {"role": "user", "content": "Samantha, how philosophy sees the technological advancements in AI and LLMs?"}
  ]
)
print(completion.choices[0].message.content)