from graph.graph import graph
from tools.telemetry import get_telemetry_alert

state = {
    "telemetry": get_telemetry_alert(),
    "triage_result": {},
    "route_options": [],
    "final_decision": {},
    "notification": ""
}
print(type(graph))
print(graph)
result = graph.invoke(state)

print("\nTelemetry")
print(result["telemetry"])

print("\nTriage")
print(result["triage_result"])

print("\nRoutes")
print(result["route_options"])

print("\nDecision")
print(result["final_decision"])

print(result["notification"])