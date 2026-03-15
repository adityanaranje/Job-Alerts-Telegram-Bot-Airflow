import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

SERP_API_KEY = os.getenv("SERP_API_KEY")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")


llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini",
    api_key = OPENAI_API_KEY
)