# gemini_llm.py
import os
from crewai import LLM

gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    provider="google",
    api_key=os.getenv("GEMINI_API_KEY")
)
