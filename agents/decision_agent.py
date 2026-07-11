from pydantic import BaseModel, Field
from config import GROQ_API_KEY
from llm_factory import get_llm


# -------------------------------
# Structured Output
# -------------------------------

class DecisionResult(BaseModel):
    selected_carrier: str = Field(description="Best carrier for rerouting")
    reason: str = Field(description="Reason for selecting this carrier")


# -------------------------------
# LLM
# -------------------------------
llm = get_llm("groq")
#llm = get_llm("gemini")

structured_llm = llm.with_structured_output(DecisionResult)


# -------------------------------
# Decision Agent
# -------------------------------

def decision_agent(state):

    telemetry = state["telemetry"]
    triage = state["triage_result"]
    routes = state["route_options"]

    prompt = f"""
You are a logistics decision agent.

Shipment Details:
{telemetry}

Triage Result:
{triage}

Available Routes:
{routes}

Choose the BEST carrier.

Consider:
- Faster ETA is better
- Lower cost is preferred if ETA is similar
- High priority shipments should prioritize speed

Return:
- selected_carrier
- reason
"""

    result = structured_llm.invoke(prompt)

    state["final_decision"] = result.model_dump()

    return state