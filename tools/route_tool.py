def get_alternative_routes(destination):
    """
    Mock route database.
    In a real system, this would query a logistics API.
    """

    routes = [
        {
            "carrier": "FedEx",
            "eta_hours": 18,
            "cost": 150
        },
        {
            "carrier": "DHL",
            "eta_hours": 24,
            "cost": 120
        },
        {
            "carrier": "Delhivery",
            "eta_hours": 30,
            "cost": 90
        }
    ]

    return routes