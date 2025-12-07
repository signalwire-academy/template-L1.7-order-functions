#!/usr/bin/env python3
"""Order status agent with lookup functions.

Lab 1.7 Deliverable: Agent with three SWAIG functions for order management:
- get_order_status: Look up order by order number
- find_orders_by_email: Find orders by customer email
- cancel_order: Cancel an order if not shipped

Environment variables:
    SWML_BASIC_AUTH_USER: Basic auth username (auto-detected by SDK)
    SWML_BASIC_AUTH_PASSWORD: Basic auth password (auto-detected by SDK)
"""

from signalwire_agents import AgentBase, SwaigFunctionResult

agent = AgentBase(
    name="order-agent",
    route="/orders"
)

# Prompt configuration
agent.prompt_add_section(
    "Role",
    "You are an order status assistant. Help customers check "
    "and manage their orders."
)

agent.prompt_add_section(
    "Process",
    bullets=[
        "Greet the customer warmly",
        "Ask if they have an order number, or ask for their email",
        "Use the appropriate function to find or check their order",
        "Tell them the status clearly",
        "Ask if there's anything else"
    ]
)

# Voice configuration
agent.add_language("English", "en-US", "rime.spore")

# Mock databases
ORDERS = {
    "12345": {"status": "shipped", "date": "Monday", "carrier": "FedEx"},
    "67890": {"status": "processing", "date": "tomorrow", "carrier": "UPS"},
    "11111": {"status": "delivered", "date": "last Friday", "carrier": "USPS"},
}

CUSTOMERS = {
    "john@example.com": ["12345", "67890"],
    "jane@example.com": ["11111"],
}


@agent.tool(
    description="Look up an order by order number",
    fillers=["Looking that up now...", "One moment please..."],
    parameters={
        "type": "object",
        "properties": {
            "order_number": {
                "type": "string",
                "description": "The order number to look up"
            }
        },
        "required": ["order_number"]
    }
)
def get_order_status(args: dict, raw_data: dict = None) -> SwaigFunctionResult:
    """Look up order status by order number."""
    order_number = args.get("order_number", "").strip()

    if order_number in ORDERS:
        order = ORDERS[order_number]
        return SwaigFunctionResult(
            f"Order {order_number} status is {order['status']}. "
            f"Shipped via {order['carrier']}, "
            f"{'delivered' if order['status'] == 'delivered' else 'expected'} "
            f"{order['date']}."
        )
    return SwaigFunctionResult(f"Order {order_number} not found.")


@agent.tool(
    description="Find orders for a customer by email",
    fillers=["Searching for your orders..."],
    parameters={
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The customer's email address"
            }
        },
        "required": ["email"]
    }
)
def find_orders_by_email(args: dict, raw_data: dict = None) -> SwaigFunctionResult:
    """Find orders by customer email address."""
    email = args.get("email", "").lower().strip()

    if email in CUSTOMERS:
        orders = CUSTOMERS[email]
        return SwaigFunctionResult(
            f"Found {len(orders)} order(s) for {email}: {', '.join(orders)}."
        )
    return SwaigFunctionResult(f"No orders found for {email}.")


@agent.tool(
    description="Cancel an order if it hasn't shipped yet",
    parameters={
        "type": "object",
        "properties": {
            "order_number": {
                "type": "string",
                "description": "The order number to cancel"
            }
        },
        "required": ["order_number"]
    }
)
def cancel_order(args: dict, raw_data: dict = None) -> SwaigFunctionResult:
    """Cancel an order if status is still processing."""
    order_number = args.get("order_number", "").strip()

    if order_number not in ORDERS:
        return SwaigFunctionResult(f"Order {order_number} not found.")

    order = ORDERS[order_number]

    if order["status"] == "processing":
        return SwaigFunctionResult(
            f"Order {order_number} has been cancelled. "
            "You'll receive a confirmation email."
        )
    elif order["status"] == "shipped":
        return SwaigFunctionResult(
            f"Order {order_number} has already shipped and cannot be cancelled. "
            "Would you like information about returns instead?"
        )
    else:
        return SwaigFunctionResult(
            f"Order {order_number} has already been delivered."
        )


if __name__ == "__main__":
    agent.run()
