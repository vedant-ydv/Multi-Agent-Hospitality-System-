import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# LLM setup (reduced tokens to avoid rate limits)
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0.5,
    max_tokens=300
)

# -------- Agents -------- #

research_agent = Agent(
    role="Travel Researcher",
    goal="Find key attractions and food in the destination",
    backstory="Travel expert",
    llm=llm,
    verbose=True
)

planner_agent = Agent(
    role="Travel Planner",
    goal="Create day wise itinerary",
    backstory="Trip planner",
    llm=llm,
    verbose=True
)

budget_agent = Agent(
    role="Budget Estimator",
    goal="Estimate travel cost",
    backstory="Travel finance expert",
    llm=llm,
    verbose=True
)

writer_agent = Agent(
    role="Travel Writer",
    goal="Create structured itinerary",
    backstory="Travel guide writer",
    llm=llm,
    verbose=True
)

review_agent = Agent(
    role="Travel Reviewer",
    goal="Improve itinerary clarity",
    backstory="Content editor",
    llm=llm,
    verbose=True
)