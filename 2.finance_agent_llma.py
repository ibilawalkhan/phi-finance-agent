from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol of a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol of the company.
    """

    symbols = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Google": "GOOGL",
        "Amazon": "AMZN",
        "Facebook": "META",
        "Tesla": "TSLA",
        "NVIDIA": "NVDA",
        "Netflix": "NFLX",
        "Adobe": "ADBE",
        "Intel": "INTC",
    }
    return symbols.get(company, "Unknown")

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    instructions=[
        "Use tables to display data.",
        "If you need to find the symbol for a company, use the get_company_symbol tool.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and MSFT. Show in tables.", stream=True
)