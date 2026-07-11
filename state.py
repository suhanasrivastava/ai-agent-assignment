from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    telemetry: Dict[str, Any]
    triage_result: Dict[str, Any]
    route_options: List[Dict[str, Any]]
    final_decision: Dict[str, Any]
    notification: str