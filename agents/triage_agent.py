from pydantic import BaseModel, Field
from config import GROQ_API_KEY
from llm_factory import get_llm

# -------------------------------
# Define Structured Output
# -------------------------------

class TriageResult(BaseModel):
    severity: str = Field(description="Severity of the shipment issue")
    action: str = Field(description="Recommended action")
    priority: str = Field(description="Priority level")


# -------------------------------
# Initialize LLM
# -------------------------------

llm = get_llm("groq")
#llm = get_llm("gemini")

structured_llm = llm.with_structured_output(TriageResult)


# -------------------------------
# Agent Function
# -------------------------------

def triage_agent(state):

    telemetry = state["telemetry"]

    prompt = f"""
You are an AI logistics triage agent.

Your job is to determine whether a delayed shipment should be rerouted automatically.

Return:

- severity: Low, Medium or High
- action: monitor, investigate or reroute
- priority: Normal, Urgent or Immediate

Rules:

- Delay less than 4 hours → Low
- Delay between 4 and 8 hours → Medium
- Delay greater than 8 hours → High

If the delay is greater than 8 hours, recommend "reroute".

Shipment Details:

{telemetry}
"""

    result = structured_llm.invoke(prompt)

    state["triage_result"] = result.model_dump()

    return state