import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm_factory import get_llm

PROMPT = """
A shipment to Mumbai is delayed by 12 hours.
Available carriers:
1. FedEx - ETA 18 hrs - Cost 150
2. DHL - ETA 24 hrs - Cost 120
3. Delhivery - ETA 30 hrs - Cost 90

Select the best carrier and explain why.
"""

MODELS = [
    ("Llama 3.3 (Groq)", "groq"),
    ("Gemini", "gemini"),
]

for model_name, provider in MODELS:
    print("=" * 60)
    print(f"Model: {model_name}")

    try:
        llm = get_llm(provider)
        response = llm.invoke(PROMPT)
        print(response.content)
    except Exception as e:
        print(f"Comparison could not be completed: {e}")