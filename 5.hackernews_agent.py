from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.hackernews import HackerNewsTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[HackerNewsTools()],
    markdown=True,
)
agent.print_response("Summarize the top 5 stories on hackernews", stream=True)