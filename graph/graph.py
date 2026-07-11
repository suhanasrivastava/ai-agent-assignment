from langgraph.graph import StateGraph, END
from state import AgentState
from agents.triage_agent import triage_agent
from agents.route_agent import route_agent
from agents.decision_agent import decision_agent
from agents.notification_agent import notification_agent


workflow = StateGraph(AgentState)

def route_after_triage(state):
    severity = state["triage_result"]["severity"].lower()

    if severity == "low":
        return "end"

    return "route"

# Nodes
workflow.add_node("triage", triage_agent)
workflow.add_node("route", route_agent)
workflow.add_node("decision", decision_agent)
workflow.add_node("notification", notification_agent)

# Flow
workflow.set_entry_point("triage")

workflow.add_conditional_edges(
    "triage",
    route_after_triage,
    {
        "route": "route",
        "end": END
    }
)
workflow.add_edge("route", "decision")
workflow.add_edge("decision", "notification")
workflow.add_edge("notification", END)

graph = workflow.compile()