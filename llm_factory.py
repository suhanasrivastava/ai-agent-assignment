from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GROQ_API_KEY, GEMINI_API_KEY


def get_llm(provider="groq"):

    if provider == "groq":
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=GROQ_API_KEY,
            temperature=0
        )

    elif provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=GEMINI_API_KEY,
            temperature=0
        )

    else:
        raise ValueError("Unknown provider")