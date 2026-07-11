def notification_agent(state):
    decision = state["final_decision"]
    telemetry = state["telemetry"]

    message = (
        f"""
========== NOTIFICATION ==========

Shipment ID : {telemetry['shipment_id']}

Destination : {telemetry['destination']}

Selected Carrier : {decision['selected_carrier']}

Reason :
{decision['reason']}

==================================
"""
    )

    state["notification"] = message

    return state