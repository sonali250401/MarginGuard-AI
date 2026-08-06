def leakage_detector(order):

    margin = (
        order["order_value"] -
        order["cost_to_serve"]
    ) / order["order_value"]

    if margin < 0.10:
        return "HIGH"

    return "LOW"


def optimizer_agent(order):

    if order["cost_to_serve"] > 700:
        return "Switch Carrier"

    return "Proceed Normally"


def finance_agent(order):

    margin = (
        (
            order["order_value"] -
            order["cost_to_serve"]
        ) /
        order["order_value"]
    ) * 100

    return {
        "margin_percentage": round(margin, 2),
        "expected_savings": 180
    }