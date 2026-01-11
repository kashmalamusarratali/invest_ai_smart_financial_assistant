import json
from llm.client import client
from llm.tools import tools
from services.stocks import fetch_stock_price

SYSTEM_PROMPT = """
You are InvestAI, a financial assistant.
Use tools for stock data.
No financial advice.
"""

def handle_tool_calls(message):
    responses = []

    for call in message.tool_calls:
        if call.function.name == "get_stock_price":
            args = json.loads(call.function.arguments)
            stock = fetch_stock_price(args["symbol"])

            if stock:
                content = f"{stock['symbol']} is trading at ${stock['price']:.2f}"
            else:
                content = "Stock not found"

            responses.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": content
            })
    return responses

def chat_with_agent(messages, model):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools
    )

    while response.choices[0].finish_reason == "tool_calls":
        msg = response.choices[0].message
        messages.append(msg)

        tool_responses = handle_tool_calls(msg)
        for r in tool_responses:
            messages.append(r)

        response = client.chat.completions.create(
            model=model,
            messages=messages
        )

    return response.choices[0].message.content
