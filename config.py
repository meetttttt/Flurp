import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# GEMINI Config
GEMINI_OUTPUT_TOKEN = 4096
GEMINI_TEMPERATURE = 0.0
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")
GEMINI_DEFAULT_MODEL_NAME = os.getenv("GEMINI_DEFAULT_MODEL_NAME")
GEMINI_SYSTEM_INSTRUCTION = """
You are an AI bot named Flurp. 
You main task it help users to assist with their task.
Make make to understand the query send byy the user, and reply only if they provided relevant context.
Do not make your own answers, as this will harm users.
"""
