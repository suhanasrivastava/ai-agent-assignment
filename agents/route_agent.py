from pydantic import BaseModel, Field
from typing import List
from config import GROQ_API_KEY
from tools.route_tool import get_alternative_routes
from llm_factory import get_llm


class RouteSelection(BaseModel):
    selected_carriers: List[str] = Field(
        description="List of carriers suitable for rerouting"
    )
llm = get_llm("groq")
#llm = get_llm("gemini")

structured_llm = llm.with_structured_output(RouteSelection)


def route_agent(state):

    destination = state["telemetry"]["destination"]

    routes = get_alternative_routes(destination)

    prompt = f"""You are a logistics routing assistant.

Available routes:

{routes}

Select the TWO best carrier options for a delayed shipment.

Consider:
- ETA
- Cost
- Reliability

Return only the carrier names."""

    result = structured_llm.invoke(prompt)

    selected_routes = []

    for carrier in result.selected_carriers:
        for route in routes:
            if route["carrier"] == carrier:
                selected_routes.append(route)

    state["route_options"] = selected_routes

    return state